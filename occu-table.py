from flask import Flask, render_template
import random

app = Flask(__name__)


def stuff():
  a = open('occupations.csv')
  a.readline()
  name = []
  perc = []
  for line in a:
      b = line.rfind(",")
      name.append(line[0:b])
      perc.append((line.replace("\n",""))[b+1:])
  del name[-1]
  del perc[-1]
  mess = []
  d = 0
  while d < len(name):
      c = float(perc[d]) * 10
      while c > 0:
        c = c - 1
        mess.append(name[d])
      d = d + 1
  e = random.choice(mess)
  return e

def a():
    x = ""
    z = open('occupations.csv')
    z.readline()
    g = {}
    for line in z:
      b = line.rfind(",")
      g[line[0:b]]=((line.replace("\n",""))[b+1:])
    return g


@app.route("/")
      
def main():
     ga = a()
     ea = stuff()
     return render_template("main.html", listing = ga, pref = ea)
  

if __name__ =="__main__":
    app.debug=True
    app.run()


#This doesn't seem to load the main.html template, I have no idea why.
