from flask import Flask, request
from flask_cors import CORS
from numlang import run_code

app = Flask(__name__)
CORS(app)

@app.route("/run", methods=["POST"])
def run():
    data = request.get_json()
    code = data.get("code", "")

    try:
        return run_code(code)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(port=5000)
