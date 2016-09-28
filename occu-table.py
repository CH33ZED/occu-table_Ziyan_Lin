from flask import Flask, render_template
from utils import occupations
import random

app = Flask(__name__)




@app.route("/")
      
def main():
     ga = occupations.a()
     ea = occupations.stuff()
     return render_template("main.html", listing = ga, pref = ea)
  

if __name__ =="__main__":
    app.debug=True
    app.run()



