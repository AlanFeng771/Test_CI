from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/add", methods=["GET"])
def add():
    try:
        a = float(request.args.get("a", ""))
        b = float(request.args.get("b", ""))
    except (TypeError, ValueError):
        return jsonify({"error": "a 和 b 必須是數字"}), 400

    return jsonify({"result": a + b})


if __name__ == "__main__":
    app.run(debug=True)
