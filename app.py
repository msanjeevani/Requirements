
from flask import Flask, jsonify, render_template

app = Flask(__name__)

SERVICES = [
    {
        "id": 1,
        "name": "Income Certificate Issuance",
        "department": "Revenue Department",
        "description": "Access information about income certificate applications.",
        "icon": "file-text",
        "category": "Certificates",
        "available": True,
    },
    {
        "id": 2,
        "name": "Grievance Redressal Tracking",
        "department": "Public Administration",
        "description": "Learn how to register and track a public grievance.",
        "icon": "message-square",
        "category": "Public Services",
        "available": True,
    },
    {
        "id": 3,
        "name": "Business License Renewal",
        "department": "Commerce & Trade",
        "description": "Access information about business license renewal.",
        "icon": "building-2",
        "category": "Business",
        "available": True,
    },
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/services")
def get_services():
    return jsonify({
        "status": "success",
        "count": len(SERVICES),
        "services": SERVICES,
    })


@app.route("/api/status")
def get_status():
    return jsonify({
        "system": "CitizenConnect Core Gateway",
        "status": "Operational",
        "version": "1.0.0",
        "services_count": len(SERVICES),
    })


@app.route("/api/health")
def health_check():
    return jsonify({
        "status": "healthy",
        "message": "CitizenConnect backend is responding",
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

