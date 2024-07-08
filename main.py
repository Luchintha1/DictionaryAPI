from flask import Flask, render_template
import pandas as pd

app = Flask("Weather API")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/<word>")
def display(word):
    df = pd.read_csv("dictionary.csv")
    definition = df.loc[df["word"] == word]["definition"].squeeze()

    return {"word": word,
            "definition": definition}


if __name__ == "__main__":
    app.run(debug=True)