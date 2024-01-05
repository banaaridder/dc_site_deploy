from flask import Flask, render_template

app = Flask(__name__)
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return render_template("/site/home2.html")

@app.route("/sobre")
def sobre():
    return render_template("/site/sobre.html")

@app.route("/portifolio")
def portifolio():
    return render_template("/site/portifolio.html")

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku

