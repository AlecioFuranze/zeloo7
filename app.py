import json
from decouple import config
from flask import Flask, render_template, session, redirect, url_for
from authlib.integrations.flask_client import OAuth
from src.py.login_oauth import GET_GOOGLE_OAUTH, GET_FACEBOOK_OAUTH


app = Flask(import_name=__name__, static_folder="src/static/",
            template_folder="src/template/")
oauth = OAuth(app)
app.secret_key = config("APP_SECRET_KEY")
google = GET_GOOGLE_OAUTH(oauth)
facebook = GET_FACEBOOK_OAUTH(oauth)


def UserInfo():
    uimg = "https://lh3.googleusercontent.com/ogw/ADea4I7tl-tUgcEOkDfaivKrFibB4LRQQT48O6klfbmi=s83-c-mo"

    data_str = {
        "uimg": uimg,
        "name": "Alecio Furanze",
        "fName": "Alecio",
        "lName": "Furanze",
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


# google login
@app.route("/login/google/")
def google_login():
    google = oauth.create_client("google")
    redirect_uri = url_for("google_authorize", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


# google login authorize
@app.route("/login/google/authorize/")
def google_authorize():
    google = oauth.create_client("google")
    token = google.authorize_access_token()
    resp = google.get("userinfo")
    user_info = resp.json()
    user = oauth.google.userinfo()
    # using db
    return user


# facebook login
@app.route("/login/facebook/")
def facebook():
    redirect_uri = url_for("facebook_authorize", _external=True)
    return oauth.facebook.authorize_redirect(redirect_uri)


# facebook login authorize
@app.route("/login/facebook/authorize/")
def facebook_authorize():
    token = oauth.facebook.authorize_access_token()
    resp = oauth.facebook.get(
        "https://graph.facebook.com/me?fields=id,name,first_name,last_name,email,picture{url}"
    )
    profile = resp.json()
    print("Facebook User ", profile)
    return profile


if __name__ == "__main__":
    app.run(debug=True)
