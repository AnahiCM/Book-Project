from app import app
from flask import render_template, request
from app.models import model, formopener
from app.models.model import littlewpage1
from app.models.matchgirl import matchgirlp1
from app.models.otis import otus
from app.models.littlemermaid import lmermaid
from app.models.littlemermaid import limermaid
from app.models.littlemermaid import lmermaid3
from app.models.littlemermaid import lmermaid4
from app.models.alcestis import alcestis

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
    mAtchgirl=matchgirlp1[1]
    maTchgirl=matchgirlp1[2]
    matChgirl=matchgirlp1[3]
    matcHgirl=matchgirlp1[4]
    matchGirl=matchgirlp1[5]
    matchgIrl=matchgirlp1[6]
    matchgiRl=matchgirlp1[7]
    return render_template("matchgirlpage1.html", matchgirl=matchgirl, mAtchgirl=mAtchgirl, maTchgirl=maTchgirl, matChgirl=matChgirl, matcHgirl=matcHgirl, matchGirl=matchGirl, matchgIrl=matchgIrl, matchgiRl=matchgiRl)
    
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
    meRmaid= limermaid[0]
    merMan= limermaid[1]
    fIsh=limermaid[2]
    lMerman= limermaid[3]
    lfish= limermaid[4]
    meraid= limermaid[5]
    mrmaid= limermaid[6]
    bigFish= limermaid[7]
    lFish= limermaid[8]
    ariel= limermaid[9]
    sea_folk= limermaid[10]
    seafolk= limermaid[11]
    return render_template("littlemermaid2.html", meRmaid=meRmaid, merMan=merMan, fIsh=fIsh, lMerman=lMerman, lfish=lfish, meraid=meraid, mrmaid=mrmaid, bigFish=bigFish, lFish=lFish, ariel=ariel, sea_folk=sea_folk, seafolk=seafolk)
    
@app.route('/littlemermaid3', methods= ["GET", "POST"])
def littleMermaidPage3():
    seaFolk= lmermaid3[0]
    mermAid= lmermaid3[1]
    fiSh=lmermaid3[2]
    lman= lmermaid3[3]
    littlef= lmermaid3[4]
    mermaId= lmermaid3[5]
    memaid= lmermaid3[6]
    bigf= lmermaid3[7]
    littleF= lmermaid3[8]
    Ariel= lmermaid3[9]
    aRiel= lmermaid3[10]
    arIel= lmermaid3[11]
    ariEl= lmermaid3[12]
    arieL= lmermaid3[13]
    ursula= lmermaid3[14]
    Ursula= lmermaid3[15]
    uRsula= lmermaid3[16]
    urSula= lmermaid3[17]
    return render_template("littlemermaid3.html", seaFolk=seaFolk, mermAid=mermAid, fiSh=fiSh,lman=lman, littlef=littlef, mermaId=mermaId, memaid=memaid, bigf=bigf, littleF=littleF, Ariel=Ariel, aRiel=aRiel, arIel=arIel, ariEl=ariEl, arieL=arieL, ursula=ursula, Ursula=Ursula, uRsula=uRsula, urSula=urSula)
    
@app.route('/littlemermaid4', methods= ["GET", "POST"])
def littleMermaidPage4():
    trident=lmermaid4[0]
    Trident=lmermaid4[1]
    tRident=lmermaid4[2]
    trIdent=lmermaid4[3]
    triDent=lmermaid4[4]
    tridEnt=lmermaid4[5]
    trideNt=lmermaid4[6]
    tridenT=lmermaid4[7]
    mermaid1=lmermaid4[8]
    Mermaid1=lmermaid4[9]
    mErmaid1=lmermaid4[10]
    merMaid1=lmermaid4[11]
    mermAid1=lmermaid4[12]
    mermaId1=lmermaid4[13]
    mermaiD1=lmermaid4[14]
    Mermaid2=lmermaid4[15]
    mErmaid2=lmermaid4[16]
    meRmaid2=lmermaid4[17]
    merMaid2=lmermaid4[18]
    mermAid2=lmermaid4[19]
    mermaId2=lmermaid4[20]
    mermaiD2=lmermaid4[21]
    Mermaid3=lmermaid4[22]
    mErmaid3=lmermaid4[23]
    meRmaid3=lmermaid4[24]
    merMaid3=lmermaid4[25]
    mermAid3=lmermaid4[26]
    mermaId3=lmermaid4[27]
    mermaiD3=lmermaid4[28]
    Mermaid4=lmermaid4[29]
    mErmaid4=lmermaid4[30]
    meRmaid4=lmermaid4[31]
    merMaid4=lmermaid4[32]
    mermAid4=lmermaid4[33]
    return render_template("littlemermaid4.html", trident=trident, Trident=Trident, tRident=tRident, trIdent=trIdent, triDent=triDent, tridEnt=tridEnt, trideNt=trideNt, tridenT=tridenT, mermaid1=mermaid1, mErmaid1=mErmaid1, merMaid1=merMaid1, mermAid1=mermAid1, mermaId1=mermaId1, mermaiD1=mermaiD1, Mermaid2=Mermaid2, mErmaid2=mErmaid2, meRmaid2=meRmaid2, merMaid2=merMaid2, mermAid2=mermAid2, mermaId2=mermaId2, mermaiD2=mermaiD2, Mermaid3=Mermaid3, mErmaid3=mErmaid3, meRmaid3=meRmaid3, merMaid3=merMaid3, mermAid3=mermAid3, mermaId3=mermaId3, mermaiD3=mermaiD3, Mermaid4=Mermaid4, mErmaid4=mErmaid4, meRmaid4=meRmaid4, merMaid4=merMaid4, mermAid4=mermAid4)

@app.route('/littlemermaidcontents', methods= ["GET", "POST"])
def MermaidContents():
    return render_template("littlemermaidcontents.html")
    
@app.route('/alcestis', methods= ["GET", "POST"])
def Alcestis():
    return render_template("alcestis.html")
    
@app.route('/alcestispage1', methods= ["GET", "POST"])
def AlcestisPage1():
    Alcestis=alcestis[0]
    aLcestis=alcestis[1]
    alCestis=alcestis[2]
    alcEstis=alcestis[3]
    alceStis=alcestis[4]
    alcesTis=alcestis[5]
    alcestIs=alcestis[6]
    alcestiS=alcestis[7]
    alcestis1=alcestis[8]
    return render_template("alcestispage1.html", Alcestis=Alcestis, aLcestis=aLcestis, alCestis=alCestis, alcEstis=alcEstis, alceStis=alceStis, alcesTis=alcesTis, alcestIs=alcestIs, alcestiS=alcestiS, alcestis1=alcestis1)
    
    