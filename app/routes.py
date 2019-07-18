from app import app
from flask import render_template, request
from app.models import model, formopener
from app.models.model import littlewpage1
from app.models.matchgirl import matchgirlp1
from app.models.otis import otus
from app.models.littlemermaid import lmermaid

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/matchgirl', methods= ["GET", "POST"])
def Matchgirl():
    return render_template("matchgirl.html")

@app.route('/matchgirlpage1', methods= ["GET", "POST"])
def matchgirlPage1():
    matchgirl= matchgirlp1[0]
    return render_template("matchgirlpage1.html", matchgirl=matchgirl)
    
@app.route('/littlewomen', methods= ["GET", "POST"])
def Little_Women():
    return render_template("LittleWomen.html")

@app.route('/littlewomenpage1', methods= ["GET", "POST"])
def Little_Women_page1():
    littlewomenpage1 = littlewpage1[0]
    return render_template("littlewomenpage1.html", littlewomenpage1 = littlewomenpage1)

@app.route('/aloadae', methods= ["GET", "POST"])
def Aloadae():
    return render_template("aloadae.html")

@app.route('/aloadaepage1', methods= ["GET", "POST"])
def aloadePage1():
    aloade= otus[0]
    aloa= otus[1]
    aloadae= otus[2]
    ephialtes= otus[3]
    ephy= otus[4]
    otis= otus[5]
    return render_template("aloadaepage1.html", aloade=aloade, aloa=aloa, aloadae=aloadae, ephialtes=ephialtes, ephy=ephy, otis=otis)
@app.route('/littlemermaid', methods= ["GET", "POST"])
def littleMermaid():
    return render_template("littlemermaid.html")
    
@app.route('/littlemermaidpage1', methods= ["GET", "POST"])
def littleMermaidPage1():
    mermaid= lmermaid[0]
    merman= lmermaid[1]
    fish=lmermaid[2]
    lmerman= lmermaid[3]
    littlefish= lmermaid[4]
    merMaid= lmermaid[5]
    mErmaid= lmermaid[6]
    bigfish= lmermaid[7]
    littleFish= lmermaid[8]
    return render_template("littlemermaidpage1.html", mermaid=mermaid, merman=merman, fish=fish, lmerman=lmerman, littlefish=littlefish, merMaid=merMaid, mErmaid=mErmaid, bigfish=bigfish, littleFish=littleFish)
    
@app.route('/littlemermaid2', methods= ["GET", "POST"])
def littleMermaidPage2():
    return render_template("littlemermaid2.html")
    
@app.route('/littlemermaid3', methods= ["GET", "POST"])
def littleMermaidPage3():
    return render_template("littlemermaid3.html")