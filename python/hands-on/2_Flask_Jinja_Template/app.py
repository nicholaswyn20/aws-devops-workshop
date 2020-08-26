from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def head():
    return render_template("index.html", number1 = 321)
@app.route("/ikinci")
def second():
    return render_template("secondpage.html", hazirlayan = "nicholas")



if __name__ == "__main__":
    app.run(debug = True)