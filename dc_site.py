from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("/Site/home2.html")

@app.route("/sobre")
def sobre():
    return render_template("/Site/sobre.html")

@app.route("/portifolio")
def portifolio():
    return render_template("/Site/portifolio.html")

if __name__ == "__main__":
    app.run(debug=True)


