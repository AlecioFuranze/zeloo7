import json
from turtle import st
from flask import Flask, redirect, url_for, render_template, jsonify

app = Flask (import_name=__name__, static_folder="src/static/", template_folder="src/template/")

@app.route("/")
def home():
    uimg = "https://lh3.googleusercontent.com/ogw/ADea4I7tl-tUgcEOkDfaivKrFibB4LRQQT48O6klfbmi=s83-c-mo"
    user_json_str = {
        "uimg":uimg
    }

    user_json_str = json.dumps(user_json_str)

    print("UserJson: ")
    print(user_json_str)
    user_json_obj = json.loads(user_json_str)
    return render_template("public/index.html", title="Home", main="main.html", user=user_json_obj)

if __name__ == "__main__":
    app.run(debug=True)