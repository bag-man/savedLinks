# https://gist.github.com/kemitche/9749639
from flask import Flask, abort, request
from uuid import uuid4
import requests
import requests.auth
import urllib
import praw
CLIENT_ID = "_p3ZcJt2WaZePw"
CLIENT_SECRET = "HrzyQ4Q2f5ovJJGq-JN_9i6basU"
REDIRECT_URI = "http://198.98.119.217/auth"
 
app = Flask(__name__)
@app.route('/')
def homepage():
  text = '<a href="%s">Authenticate with reddit</a>'
  return text % make_authorization_url()
     
def make_authorization_url():
  state = str(uuid4())
  save_created_state(state)
  params = {
    "client_id": CLIENT_ID,
    "response_type": "code",
    "state": state,
    "redirect_uri": REDIRECT_URI,
    "duration": "temporary",
    "scope": "history,identity"
  }
  url = "https://ssl.reddit.com/api/v1/authorize?" + urllib.urlencode(params)
  return url


def save_created_state(state):
  pass
def is_valid_state(state):
  return True

@app.route('/auth')
def auth():
  error = request.args.get('error', '')
  if error:
    return "Error: " + error
  state = request.args.get('state', '')
  if not is_valid_state(state):
    abort(403)
  code = request.args.get('code')
  #access_token = get_token(code)
  access_information = r.get_access_information(code)
  r.set_access_credentials(**access_information)
  return "Your reddit username is: %s" % get_username(access_token)

def get_token(code):
  client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
  post_data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": REDIRECT_URI
  }
  headers =  {"User-Agent": "savedLinks app by /u/Midasx"}
  response = requests.post(
    "https://ssl.reddit.com/api/v1/access_token",
    headers=headers,
    auth=client_auth,
    data=post_data
  )
  token_json = response.json()
  return token_json["access_token"]
    
    
def get_username(access_token):
  headers = {"Authorization": "bearer " + access_token}
  response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
  me_json = response.json()
  return me_json['name']

def get_savedLinks(access_token):
  headers = {"Authorization": "bearer " + access_token}
  response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
  me_json = response.json()
  return me_json['name']



if __name__ == '__main__':     
  app.run(debug=True, host='198.98.119.217', port=80)
