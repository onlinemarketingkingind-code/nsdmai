import os
import requests
from flask import Flask, request, jsonify
from google.cloud import storage
from datetime import datetime
import json

app = Flask(__name__)

BUCKET_NAME = "nsdmai-audit-reports"

@app.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "Eva API Gateway running",
        "version": "1.0.0",
        "powered_by": "Google Cloud Run",
        "google_services": [
            "Google Cloud Run",
            "Google Cloud Storage",
            "Google Cloud TTS",
            "Google Cloud STT",
            "Google Search Console"
        ]
    })

@app.route("/eva/reports", methods=["GET"])
def list_reports():
    try:
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blobs = list(bucket.list_blobs(prefix="reports/"))
        reports = [
            {
                "name": blob.name,
                "size": blob.size,
                "url": f"https://storage.googleapis.com/{BUCKET_NAME}/{blob.name}"
            }
            for blob in blobs
        ]
        return jsonify({
            "total_reports": len(reports),
            "reports": reports,
            "bucket": BUCKET_NAME
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
