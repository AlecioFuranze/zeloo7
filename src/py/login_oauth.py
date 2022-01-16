from decouple import config
from authlib.integrations.flask_client import OAuth


def GET_GOOGLE_OAUTH(oauth: OAuth):
    CI = config("GOOGLE_CLIENT_ID")
    CS = config("GOOGLE_CLIENT_SECRET")

    str(CI).split()
    str(CS).split()

    google = oauth.register(
        name="google",
        client_id=CI,
        client_secret=CS,
        access_token_url="https://accounts.google.com/o/oauth2/token",
        access_token_params=None,
        authorize_url="https://accounts.google.com/o/oauth2/auth",
        authorize_params=None,
        api_base_url="https://www.googleapis.com/oauth2/v1/",
        # This is only needed if using openId to fetch user info
        userinfo_endpoint="https://openidconnect.googleapis.com/v1/userinfo",
        client_kwargs={"scope": "openid email profile"},
    )

    return google


def GET_TWITTER_OAUTH(oauth: OAuth):
    CI = config("TWITTER_CLIENT_ID")
    CS = config("TWITTER_CLIENT_SECRET")

    str(CI).split()
    str(CS).split()

    twitter = oauth.register(
        name="twitter",
        client_id=CI,
        client_secret=CS,
        request_token_url="https://api.twitter.com/oauth/request_token",
        request_token_params=None,
        access_token_url="https://api.twitter.com/oauth/access_token",
        access_token_params=None,
        authorize_url="https://api.twitter.com/oauth/authenticate",
        authorize_params=None,
        api_base_url="https://api.twitter.com/1.1/",
        client_kwargs=None,
    )

    return twitter


def GET_FACEBOOK_OAUTH(oauth: OAuth):
    CI = config("FACEBOOK_CLIENT_ID")
    CS = config("FACEBOOK_CLIENT_SECRET")

    str(CI).split()
    str(CS).split()

    facebook = oauth.register(
        name="facebook",
        client_id=CI,
        client_secret=CS,
        access_token_url="https://graph.facebook.com/oauth/access_token",
        access_token_params=None,
        authorize_url="https://www.facebook.com/dialog/oauth",
        authorize_params=None,
        api_base_url="https://graph.facebook.com/",
        client_kwargs={"scope": "public_profile, email"},
    )

    return facebook
