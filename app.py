import json
from flask import Flask, render_template

app = Flask (import_name=__name__, static_folder="src/static/", template_folder="src/template/")

def UserInfo():
    uimg = "https://lh3.googleusercontent.com/ogw/ADea4I7tl-tUgcEOkDfaivKrFibB4LRQQT48O6klfbmi=s83-c-mo"
    
    data_str = {
        "uimg":uimg,
        "name":"Alecio Furanze",
        "fName":"Alecio",
        "lName":"Furanze",
    }

    data_str = json.dumps(data_str)
    data_obj = json.loads(data_str)
    return data_obj


@app.route("/")
def home():
    data_obj = UserInfo()
    return render_template("public/index.html", title="Home", main="main.html", user=data_obj)


@app.route("/login/")
def login():
    data_obj = UserInfo()
    return render_template("public/index.html", title="Login", main="login.html", user=data_obj)



if __name__ == "__main__":
    app.run(debug=True)


