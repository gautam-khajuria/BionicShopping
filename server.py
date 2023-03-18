from flask import Flask, render_template, request, url_for
from datetime import datetime
import model

app = Flask(__name__)

signed_in = False

@app.route("/api/welcome/<name>"):
def welcome(name):
  # API to get the welcome message from name (passed in)
  
  return f"<p>Hello {name}, it's <b>{datetime.weekday()}</b>. What will you buy?</p>"

@app.route("/")
def home():
  if not signed_in:
    # redirect if not logged
    return redirect(url_for("login"))
  else
    pass

@app.route("/login", methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    
  
if __name__ == "__main__":
  app.run()
