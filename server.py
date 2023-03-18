from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
import model

app = Flask(__name__)

@app.route("/")
def home():
  
  return

@app.route("/api/welcome/<name>"):
def welcome(name):
  # API to get the welcome message from name (passed in)
  
  return f"<p>Hello {name}, it's a new day, <b>{datetime.weekday()}</b>. What will you do today?</p>"


  
  
if __name__ == "__main__":
  app.run()
