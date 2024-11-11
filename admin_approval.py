from flask import Flask, jsonify, request

app = Flask(__name__)

# Route to approve or reject the request based on unique key
@app.route('/approve_request', methods=['POST'])
def approve_request():
    approval_data = request.json
    key = approval_data.get("key")
    
    if key == "EXPECTED_KEY":  # Replace EXPECTED_KEY with actual unique key logic
        return jsonify({"message": "Approval accepted", "status": "approved"})
    else:
        return jsonify({"message": "Approval rejected", "status": "rejected"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
