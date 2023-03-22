from flask import Flask, render_template, request, url_for, redirect, flash
from datetime import datetime
import os
from os.path import join, dirname
from dotenv import load_dotenv
from Product import Product

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.secret_key = b'3_)(*@udjsfbbsHSKJHDA)'

# SIGNED IN BOOLEAN
signed_in = False
products = {1: Product(name="Gear", imageLink="", description="green. crunch. delicious", id=1),
           2: Product(name="Screwdriver", imageLink="", description="", id=2)}



@app.route("/")
def index():
  global signed_in, products
  
  if signed_in == False:
    # redirect if not logged
    return redirect(url_for("login"))
  else:
    return render_template("home.html", name=os.environ.get("NAME"), products=products.values())

@app.route("/login", methods=['GET', 'POST'])
def login():
  global signed_in

  if signed_in == True:
    return redirect(url_for("index"))
  
  if request.method == 'GET':
    return render_template("login.html")
  
  elif request.method == 'POST':
    
    if request.form["email-input"] == os.environ.get("EMAIL") and request.form["password-input"] == os.environ.get("PASSWORD"):
      signed_in = True
      return redirect(url_for("index"))
    else:
      flash("Incorrect email address or password!")
      return redirect(url_for("login"))
    
@app.route("/products/<int:id>")
def product_page(id):
  global products
  return render_template("product-page.html", product=products[id])
    
# API #

@app.route("/api/welcome/<name>")
def welcome(name):
  # API to get the welcome message from name (passed in)
  return f"<p>Hello {name}, it's <b>{datetime.weekday()}</b>. Welcome to our store!</p>"
  
 
if __name__ == "__main__":
  app.run(debug=True)
