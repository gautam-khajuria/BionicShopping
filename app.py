from flask import Flask, render_template, request, url_for, redirect, flash
from datetime import datetime
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.secret_key = b'3_)(*@udjsfbbsHSKJHDA)'

# 
signed_in = False

@app.route("/")
def index():
  if not signed_in:
    # redirect if not logged
    return redirect(url_for("login"))
  else:
    return render_template("home.html")

@app.route("/home")
def home(): 
    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template("login.html")
  elif request.method == 'POST':
    if request.form["email-input"] == os.environ.get("EMAIL") and request.form["password-input"] == os.environ.get("PASSWORD"):
      signed_in = True
      return redirect(url_for("index"))
    else:
      flash("Incorrect email address or password!")
      return redirect(url_for("login"))
    
# API #

@app.route("/api/welcome/<name>")
def welcome(name):
  # API to get the welcome message from name (passed in)
  return f"<p>Hello {name}, it's <b>{datetime.weekday()}</b>. What will you buy?</p>"
  
  
if __name__ == "__main__":
  app.run()
