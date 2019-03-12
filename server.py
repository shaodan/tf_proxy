from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/tf", methods=['POST'])
def post_data():
    j = request.get_json()
    app.logger.info(j)
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
