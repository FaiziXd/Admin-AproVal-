from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# اپروول درخواستوں کو دیکھنے اور مینج کرنے کا پیج
@app.route('/view_requests', methods=['GET'])
def view_requests():
    try:
        with open("approval_requests.txt", "r") as file:
            requests = file.readlines()
    except FileNotFoundError:
        requests = []

    return render_template_string('''
        <h2>Approval Requests</h2>
        <ul>
            {% for key in requests %}
                <li>{{ key }} 
                    <form action="/approve_request" method="post" style="display:inline;">
                        <input type="hidden" name="unique_key" value="{{ key.strip() }}">
                        <button type="submit">Approve</button>
                    </form>
                    <form action="/reject_request" method="post" style="display:inline;">
                        <input type="hidden" name="unique_key" value="{{ key.strip() }}">
                        <button type="submit">Reject</button>
                    </form>
                </li>
            {% endfor %}
        </ul>
    ''', requests=requests)

# اپروول کو منظور کرنے کا API
@app.route('/approve_request', methods=['POST'])
def approve_request():
    unique_key = request.form.get('unique_key')
    
    # اپروول کو مستقل طور پر اسٹور کریں
    with open("approved_requests.txt", "a") as file:
        file.write(f"{unique_key}\n")
    
    return jsonify({"message": "Request approved", "key": unique_key})

# اپروول کو مسترد کرنے کا API
@app.route('/reject_request', methods=['POST'])
def reject_request():
    unique_key = request.form.get('unique_key')
    return jsonify({"message": "Request rejected", "key": unique_key})

if __name__ == '__main__':
    app.run(port=5001)
