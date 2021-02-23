from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/hello', methods=["POST", "GET"])
def hello() :
    return jsonify({
    "data": {        "id": 9604521,
        "ownerCode": "J534327",
        "createdAt": "2021-01-11 16:24:36"},
    "meta": {
        "message": "이게 돼?????",
        "code": ""
    }
})

@app.route('/hello-second')
def helloSecond() :
    return jsonify({        "id": "9604521",
        "statusCode": "ACTIVE",
        "typeCode": "NORMAL",
        "loginId": "dlrudgud08**@gmail.com",
        "ownerCode": "J534327",
        "phone": "010-****-0828",
        "createdAt": "2021-01-11 16:24:36"})

if __name__ == '__main__' :
    app.run(debug=True)