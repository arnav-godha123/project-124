from flask import Flask,jsonify, request

app = Flask(__name__)

Contact = [
    {
        'id': 1,
        'Name': u'raju',
        'Contact': u'9987644456', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'rahul',
        'contact': u'9876543222', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    data={
    "id":Contact[-1]["id"]+1,
    "Name":request.json["Name"],
    "Contact":request.json.get("Contact",""),
    "done":False
 }
    Contact.append(data)
    return jsonify({
        "status":"success","message":"contact added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : Contact
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)