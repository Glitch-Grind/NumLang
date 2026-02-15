from flask import Flask, request
from numlang import run_code  # your interpreter

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run():
    data = request.get_json()
    code = data.get("code", "")
    try:
        output = run_code(code)  # your numlang.py must have run_code function
        return output
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(port=5000)

