sfrom flask import Flask, render_template, request, url_for, redirect, flash
from datetime import datetime

app = Flask(__name__)

signed_in = False

@app.route("/")
@app.route("/<name>")
def home(name=None):
  if not signed_in:
    # redirect if not logged
    return redirect(url_for("login"))
  else:
    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template("login.html")
  else:
    if request.form["email-address"] == process.env.EMAIL and request.form["password"] == process.env.PASSWORD:
      return redirect(url_for("home"))
    else:
      flash("Incorrect email address or password!")
    
# API #

@app.route("/api/welcome/<name>")
def welcome(name):
  # API to get the welcome message from name (passed in)
  return f"<p>Hello {name}, it's <b>{datetime.weekday()}</b>. What will you buy?</p>"
  
  
if __name__ == "__main__":
  app.run()
