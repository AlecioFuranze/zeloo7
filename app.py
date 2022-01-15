from xml.etree.ElementInclude import include
from flask import Flask, redirect, url_for, render_template

app = Flask (import_name=__name__, static_folder="src/static/", template_folder="src/template/")

@app.route("/")
def home():
    return render_template("public/index.html", title="Home", main="main.html")

if __name__ == "__main__":
    app.run(debug=True)