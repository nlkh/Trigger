from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/hello', methods=["POST", "GET"])
def hello() :
    return jsonify({
        'lastBuild' : 200
    })

@app.route('/hello-second')
def helloSecond() :
    return jsonify({
        'status' : 200,
        'message' : "success2"
    })

if __name__ == '__main__' :
    app.run()