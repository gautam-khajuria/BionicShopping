from flask import Flask, render_template, request, url_for, redirect, flash
from datetime import date
import os, requests
from os.path import join, dirname
from dotenv import load_dotenv
from Product import Product
import calendar

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.secret_key = b'3_)(*@udjsfbbsHSKJHDA)'

# SIGNED IN BOOLEAN
signed_in = False
products = {1: Product(name="Gear", 
                       imageLink="https://cdn.glitch.global/d41ba89f-852f-4513-8c71-8d07b82ca711/gear_1.jpeg?v=1679490572576", 
                       description="green. crunch. delicious. Use this for all of your chained needs!", 
                       id=1
                      ),
           2: Product(name="Screwdriver", 
                      imageLink="https://cdn.glitch.global/d41ba89f-852f-4513-8c71-8d07b82ca711/screwdriver_3pack_1.jpg?v=1679492884372", 
                      description="simple. basic. efficent. A #necessity for the modern toolist. Got a problem? SCREWDRIVER!", 
                      id=2
                     )
           }


def format_url(url):
  return url.replace("/", "$")

@app.route("/")
def index():
  global signed_in, products

  if signed_in == False:
    # redirect if not logged
    return redirect(url_for("login"))
  else:
    name = os.environ.get("NAME") # access env variable 
    return render_template("home.html", name=name, products=products.values(), 
                           message=requests.get(f"https://proximal-gorgeous-cheek.glitch.me/api/welcome/{name}").text)

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
  global products, signed_in
  
  if not signed_in:
    return redirect(url_for("login"))
  
  if id in products:
    return render_template("product-page.html", product=products[id], products=products.values())
  
  else :
    index_url = "https://proximal-gorgeous-cheek.glitch.me/"
    return redirect(f"/api/error/{os.environ.get('NAME')}/{format_url(index_url)}") 
  
# API #


@app.route("/api/welcome/")
def welcomeOG():
  # API to get default welcome message
  return f"Hello! It's {calendar.day_name[date.today().weekday()]}. Start shopping for..."

@app.route("/api/welcome/<name>")
def welcome(name):
  # API to get the welcome message from name (passed in)
  return f"Hello {name}, it's {calendar.day_name[date.today().weekday()]}. Start shopping for..."

  
@app.route("/api/error/<name>")
def error_name(name):
  # API to send an error message from name (passed in)
  return f"<p>Sorry {name.toUpperCase()}, looks like that caused an error! Try again later</p>"

# uses the user's name but also provides them with a redirect link to reacces website 
@app.route("/api/error/<name>/<redir_link>/")
def error_name_redir(name, redir_link):
  # API to send an error message from name (passed in) + url (passed in)
  return f"<p>Sorry {name}, looks like that caused an error!</p> <a href= {redir_link.replace('$', '/')}> Take me back :( </a>"
   


if __name__ == "__main__":
  app.run(debug=True)
