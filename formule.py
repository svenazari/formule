#UPUTE ZA KORIŠTENJE:
#1. Pokrenuti Python3 shell u folderu u kojem se nalazi skripta.
#2. Pokrenuti naredbu 'exec(open('formule.py').read())'.
#3. Upisati 'pomoć ()' za pomoć u korištenju funkcija.
#
#Autor: Sven Azari
#http://www.github.com/svenazari

#import modula
import math
import cmath
import requests
import sys
from os import system, name
import readline

#početni tekst
print ("# FORMULE.py #")
print ("Autor: Sven Azari")
print ("http://www.github.com/svenazari")
print ("Upiši 'pomoć ()' za informacije o naredbama.")

def clear (): #čišćenje zaslona
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#matematika
def linearna (a,b): #pronalaženje x za linearne jednadžbe sa jednom nepoznanicom (jednadžba treba biti u formatu Ax+B=0)
    if a == 0:
        print ("Nema rješenja! To nije jednadžba sa nepoznanicama!")
    else:
        x = str(round(-b / a,3))
        print ("x = " + x)

def kvadratna (a,b,c): #pronalaženje x za kvadratne jednadžbe sa jednom nepoznanicom (jednadžba treba biti u formatu Ax^2+Bx+C=0)
    if a == 0: #računanje linearne jednadžbe ukoliko je a = 0
        linearna (b,c)
    else:
        d = math.pow(b,2) - 4 * a * c #diskriminanta
        if d < 0: #diskriminanta je negativna - rješenja su kompleksni brojevi
            ds = cmath.sqrt(d)
            i = str(round(-b / (2 * a),3)) #realni dio kompleknog broja
            z = str(abs(round((ds.imag) / (2 * a),3))*1j) #imaginarni dio kompleksnog broja (samo pozitivna vrijednost)
            #ispis rješenja
            print("x1 = " + i + "+" + z)
            print("x2 = " + i + "-" + z)
        elif d == 0: # diskriminanta je 0 - samo jedno rješenje
            x = str(round((-1 * b) / (2 * a),3))
            print("x = " + x)
        else: #diskriminanta je pozitivna - dva rješenja
            ds = math.sqrt(d) #korijen diskriminante
            x1 = round((-b + ds) / (2 * a),3)
            x1s = str(x1)
            x2 = round((-b - ds) / (2 * a),3)
            x2s = str(x2)
            #ispis rješenja
            print("x1 = " + x1s)
            print("x2 = " + x2s)

def dnepoz (z1,a1,b1,c1,z2,a2,b2,c2): #rješavanje jednandžbi sa dvije nepoznanice (format jednadžbi Zy = Ax^2 + Bx + C)
    if a1 == 0 and a2 == 0: #obje jednadžbe su linearne
        yr = ((b2 * c1) - (b1 * c2)) / ((b2 * z1) - (b1 * z2)) #y rješenje
        xr = ((z1 * yr) - c1) / b1 #x rješenje
        yp = str(round(yr,3))
        xp = str(round(xr,3))
        print ("(" + xp + "," + yp + ")")
    elif a1 != 0 and a2 == 0: #prva jednadžba je kvadratna, a druga je linearna
        #koeficjenti pomoćne jednandžbe
        p = -1 * a1 * z2 #a
        r = b2 * z1 - b1 * z2 #b
        s = c2 * z1 - c1 * z2 #c
        #diskriminanta pomoćne jednadžbe
        q = math.pow(r,2) - 4 * p * s
        if q < 0 : #diskriminanta negativna - nema rješenja
            print ("Ovaj sustav jednadžbi nema rješenja!")
        elif q == 0: #diskriminanta je 0 - postoji samo jedan par rješenja
            x = round((-1 * r) / (2 * p),3) #x rješenje
            xs = str(x)
            y = round(((b2 * x) + c2) / z2,3) #y rješenje
            ys = str(y)
            print ("(" + xs + "," + ys + ")")
        elif q > 0: #diskriminanta je pozitivna - sustav ima dva para rješenja
            qs = math.sqrt(q) #korijen diskriminante
            x1 = round(((-1 * r) + qs) / (2 * p),3) #x1 rješenje
            x2 = round(((-1 * r) - qs) / (2 * p),3) #x2 rješenje
            x1s = str(x1)
            x2s = str(x2)
            y1 = round(((b2 * x1) + c2) / z2,3) #y1 rješenje
            y2 = round(((b2 * x2) + c2) / z2,3) #y2 rješenje
            y1s = str(y1)
            y2s = str(y2)
            print("(" + x1s + "," + y1s + ")")
            print("(" + x2s + "," + y2s + ")")
    else: #obje jednadžbe su kvadratne
        #koeficjenti pomoćne jednadžbe
        p = a1 * z2 - a2 * z1 #a
        r = b1 * z2 - b2 * z1 #b
        s = c1 * z2 - c2 * z1 #c
        #diskriminanta pomoćne jednadžbe
        q = math.pow(r,2) - 4 * p * s
        if q < 0: # diskriminanta je negativna - nema rješenja
            print ("Ovaj sustav jednadžbi nema rješenja!")
        elif q == 0: #diskriminanta je 0 - postoji samo jedan par rješenja
            x = round((-1 * r) / (2 * p),3) #x rješenje
            y = round((a2 * math.pow(x,2) + b2 * x + c2) / z2,3) #y rješenje
            xs = str(x)
            ys = str(y)
            print("(" + xs + "," + ys + ")")
        elif q > 0: #diskriminanta je pozitivna - sustav ima dva para rješenja
            qs = math.sqrt(q) #korijen diskriminante
            x1 = round(((-1 * r) + qs) / (2 * p),3) #x1 rješenje
            x2 = round(((-1 * r) - qs) / (2 * p),3) #x2 rješenje
            x1s = str(x1)
            x2s = str(x2)
            y1 = round((a2 * math.pow(x1,2) + b2 * x1 + c2) / z2,3) #y1 rješenje
            y2 = round((a2 * math.pow(x2,2) + b2 * x2 + c2) / z2,3) #y2 rješenje
            y1s = str(y1)
            y2s = str(y2)
            print("(" + x1s + "," + y1s + ")")
            print("(" + x2s + "," + y2s + ")")

def dnepoz2 (a,b,c,d,e,f,g,h,i): #rješava sustav kvadratne i linearne jednadžbe u formatu Ax^2 + By^2 + Cxy + Dx + Ey + F = 0 i Gy = Hx + I
    if a == 0 and b == 0 and c == 0:
        if d == 0 and e == 0 and f != 0:
            print("To nije sustav jednadžbi!")
        elif d == 0 and e == 0 and f == 0:
            if g != 0:
                print("To nije sustav jednadžbi!")
            else:
                linearna(h,i)
        else:
            dnepoz(e,0,d,f,g,0,h,i)
    elif g == 0:
        print("To nije sustav jednadžbi!") 
    elif h == 0: #ako je u linearnoj jednadžbi h = 0
        if a == 0:
            #definiranje koeficjenata pomoćne jednadžbe
            p = ((c * i) / g) + d #a
            r = (b * math.pow(i / g,2)) + (e * (i / g) + f) #b
            x = str(round((-1 * r) / p,3)) #x rješenje
            y = str (i / g) #y rješenje
            print("(" + x + "," + y + ")")
        else:
            #definiranje koeficjenata pomoćne jednadžbe
            p = a #a
            r = ((c * i) / g) + d #b
            s = (b * math.pow(i / g,2)) + (e * (i / g) + f) #c
            #diskriminanta pomoćne jednadžbe
            q = math.pow(r,2) - 4 * p * s
            if q < 0: #diskriminanta je negativna - nema rješenja
                print ("Ovaj sustav jednadžbi nema rješenja!")
            elif q == 0: #diskriminanta je 0 - postoji samo jedan par rješenja
                x = str(round((-1 * r) / (2 * p),3)) #x rješenje
                y = str(i / f) #y rješenje
                print ("(" + x + "," + y + ")")
            elif q > 0: #diskriminanta je pozitivna - sustav ima dva rješenja
                qs = math.sqrt(q) #korijen diskriminante
                x1 = str(round(((-1 * r) + qs) / (2 * p),3)) #x1 rješenje
                x2 = str(round(((-1 * r) - qs) / (2 * p),3)) #x2 rješenje
                y = str(i / g) #y rješenje
                print("(" + x1 + "," + y + ")")
                print("(" + x2 + "," + y + ")")
    else:
        #definiranje koeficjenata pomoćne jednadžbe
        p = a + (b * math.pow(h / g,2)) + ((c * h) / g) #a
        r = ((2 * b * h * i) / math.pow(g,2)) + ((c * i) / g) + d + ((e * h) / g) #b
        s = (b * math.pow(i / g,2)) + ((e * i) / g) + f #c
        #diskriminanta pomoćne jednadžbe
        q = math.pow(r,2) - 4 * p * s
        if q < 0: #diskriminanta je negativna - nema rješenja
            print ("Ovaj sustav jednadžbi nema rješenja!")
        elif q == 0: #diskriminanta je 0 - postoji samo jedan par rješenja
            x = round((-1 * r) / (2 * p),3) #x rješenje
            y = round(((h / g) * x) + (i / g),3) #y rješenje
            xs = str(x)
            ys = str(y)
            print("(" + xs + "," + ys + ")")
        elif q > 0: #diskriminanta je pozitivna - sustav ima dva para rješenja
            qs = math.sqrt(q) #korijen diskriminante
            x1 = round(((-1 * r) + qs) / (2 * p),3) #x1 rješenje
            x2 = round(((-1 * r) - qs) / (2 * p),3) #x2 rješenje
            x1s = str(x1)
            x2s = str(x2)
            y1 = round(((h / g) * x1) + (i / g),3) #y1 rješenje
            y2 = round(((h / g) * x2) + (i / g),3) #y2 rješenje
            y1s = str(y1)
            y2s = str(y2)
            print("(" + x1s + "," + y1s + ")")
            print("(" + x2s + "," + y2s + ")")

def trokut (a,b,gama): #kosinusov poučak - a i b su stranica, a gama je kut između te dvije stranice (za pitagorin poučak, za vrijednost kuta upisati 90)
    gamar = gama * math.pi / 180 #pretvaranje stupnjeva u radijane
    c = round(math.sqrt(math.pow(a,2) + math.pow(b,2) - 2 * a * b * math.cos(gamar)),3) #kosinusov poučak - za stranicu nasuprot kutu gama (c stranica)
    cosa = (math.pow(b,2) + math.pow(c,2) - math.pow(a,2)) / (2 * b * c) #kosinus kuta alfa (kut nasuprot a stranici)
    cosb = (math.pow(a,2) + math.pow(c,2) - math.pow(b,2)) / (2 * a * c) #kosinus kuta beta (kut nasuprot b stranici)
    alfar = math.acos(cosa) #kut alfa u radianima
    betar = math.acos(cosb) #kut beta u radianima
    #pretvaranje kuteva u stupnjeve
    alfa = round(alfar * 180 / math.pi,3)
    beta = round(betar * 180 / math.pi,3)
    #string
    ap = str(round(a,3))
    bs = str(round(b,3))
    cs = str(c)
    alfas = str(alfa)
    betas = str(beta)
    gamas = str(gama)
    #ispis
    print ("a = " + ap)
    print ("b = " + bs)
    print ("c = " + cs)
    print ("alfa = " + alfas)
    print ("beta = " + betas)
    print ("gama = " + gamas)

#fizika

def jpg (v,s,t): #jednoliko pravocrtno gibanje (v - brzina, s - put, t - vrijeme)
    if v == "?": #računanje brzine
        v1 = str(round(s / t,3))
        print ("v = " + v1)
    elif s == "?": #računanje prijeđenog puta
        s1 = str(round(v * t,3))
        print ("s = " + s1)
    elif t == "?": #računanje proteklog vremena
        t1 = str(round(s / v, 3))
        print ("t = " + t1)

def jug (a,v,s,t): #jednoliko ubrzano gibanje - vrijednost nepoznanica mogu biti ili vrednost veličine ili vrijednost promjene te veličine (a - ubrzanje, v - brzina, s - put, t - vrijeme)
    if a == "?": #računanje ubrzanja
        if s =="/": #iz promjene brzine i promjene vremena (nepoznat pređeni put)
            a1 = str(round(v / t,3)) #a=v/t
            print ("a = " + a1)
        elif v == "/": #iz pređenog puta i promjene vremena (nepoznata promjena brzine)
            a1 = str(round(2 * s /math.pow(t,2),3)) #a=2s/t^2
            print ("a = " + a1)
    elif v == "?": #računanje brzine
        if s == "/:": #iz promjene brzine i vremena
            v1 = str(round(a * t,3)) #a=v*t
            print ("v = " + v1)
        if t == "/": #promjena brzine iz ubrzanja i pređenog puta (vrijeme nepoznato)
            dv = str(round(math.sqrt(2 * a * s),3)) # dv=(2as)^(1/2)
            print("[delta]v = " + dv)
    elif s == "?": #računanje pređenog puta
        if a == "/": #iz brzine ako je v0 = 0 (nepoznato ubrzanje)
            s1 = str(round(v / 2 * t,3)) #s=(v0+v)/2*t
            print ("s = "+ s1)
        elif v == "/": #iz ubrzanja
            s1 = str(round(a / 2 * math.pow(t,2),3)) #s=a/2*t^2
            print ("s = " + s1)
    elif t == "?": #računanje pređenog vremena
        if s == "/":  #iz ubrzanja i promjene brzine (nepoznati pređeni put)
            t1 = str(round(a / v,3)) #t=a/v
            print ("t = " + t1)
        elif v == "/": #iz pređenog puta i ubrzanja (nepoznata promjena brzine)
            t1 = str(round(math.sqrt(2 * s / a),3)) #t=(2s/a)^(1/2)
            print ("t = " + t1)
        elif a == "/": #iz pređenog puta i brzine ako je v0=0 (nepoznato ubrzanje)
            t1 = str(round(2 * s / v,3)) #t=2s/v
            print ("t = " + t1)


def ohm_zakon (I,U,R): #ohmov zakon (I - jakost struje, U - napon struje, R - električni otpor)
    if I == "?": #računanje jakosti struje
        Ix = str(round(U / R,3))
        print ("I = " + Ix)
    elif U == "?": #računanje napona struje
        Ux = str(round(I * R,3))
        print ("U = " + Ux)
    elif R == "?": #računanje električnog otpora
        Rx = str(round(U / I,3))
        print ("R = " + Rx)

#def ziva (ta,lmm,tb): #računanje visine stupca žive u barometru za drugačiju temperaturu
#    lm = lmm / 1000 #konverzija stupca žive u metre
#    lx = lm * 0.0000604 * (tb - ta) #promjena dužine (u metrima)
#    lx2 = lm + lx #nova visina (u metrima)
#    lmm2 = round(lx2 * 1000,1) #konverzija nove visine u mm
#    lmmp = str(lmm2)
#    print ("Pri novoj temperaturi, visina stupca žive je " + lmmp + " mmHg.")

#meteo
def vlaga (tt,td): #računanje relativne vlage zraka iz temperature zraka i temperature rosišta
    #konstante
    e = 2.718282
    #pozitivna temperatura
    p1 = 6.10780
    p2 = 17.08085
    p3 = 234.175
    #negativna temperatura
    pv1 = 6.10780
    pv2 = 17.84362
    pv3 = 245.425
    if (tt < 0): #koje konstante koristiti za temperaturu zraka
        ctt1 = pv1
        ctt2 = pv2
        ctt3 = pv3
    else:
        ctt1 = p1
        ctt2 = p2
        ctt3 = p3
    if (td < 0): #koje konstante koristiti za temperaturu rosišta
        ctd1 = pv1
        ctd2 = pv2
        ctd3 = pv3
    else:
        ctd1 = p1
        ctd2 = p2
        ctd3 = p3
    #računanje tlaka zasićene vodene pare za temperaturu zraka
    mitt = ctt2 * tt / (ctt3 + tt)
    SVPTT = ctt1 * math.pow(e,mitt)
    #računanje tlaka zasiće vodene pare za temperaturu rosišta
    mitd = ctd2 * td / (ctd3 + td)
    SVPTD = ctd1 * math.pow(e,mitd)
    #računanje relativne vlage zraka
    U = str (round (SVPTD / SVPTT * 100))
    Up = "U = " + U + "%"
    #ispis rezultata
    print (Up)

def wbtc (TT,UU,bbb): #računanje vrijednosti temperature mokrog termometra iz temperature zraka, relativne vlage zraka i tlaka zraka na razini postaje
    if bbb == "/":
        bbbx = float(1013.3)
    else:
        bbbx = float(bbb)
    if bbbx < 70:
        p = (bbbx + 1000)
    else:
        p = bbbx
    for HT in range (-5000, 4000):
        HTd = HT / 100
        e = 2.718282 
        c1 = 6.10780 
        c2 = 17.08085
        c3 = 234.175
        expTT = (c2 * TT) / (c3 + TT)
        SVPTT = c1 * pow (e, expTT) 
        expHT = (c2 * HTd) / (c3 + HTd)
        SVPHT = c1 * pow (e, expHT) 
        SVPDT = SVPHT - (0.000660 * (1 + 0.0015 * HTd)) * p * (TT - HTd) 
        U_test = round (SVPDT / SVPTT * 100)
        if U_test == UU:
            break
    if HTd >= 0:
        HTa = round(HT / 100,1)
        HTap = str (HTa)
        print ("HT = " + HTap)
    else:
        for HTl in range (-5000, 4000):
            HTdl = HTl / 100
            e = 2.718282 
            c1 = 6.10780 
            c2 = 17.08085
            c3 = 234.175
            cl1 = 6.10714 
            cl2 = 22.44294
            cl3 = 272.440
            expTTl = (c2 * TT) / (c3 + TT)
            SVPTTl = c1 * pow (e, expTTl) 
            expHTl = (cl2 * HTdl) / (cl3 + HTdl)
            SVPHTl = cl1 * pow (e, expHTl) 
            SVPDTl = SVPHTl - 0.000582 * p * (TT - HTdl) 
            U_test_led = round (SVPDTl / SVPTTl * 100)
            if U_test_led == UU:
                break
        for HTv in range (-5000, 4000):
            HTdv = HTv / 100
            e = 2.718282 
            c1 = 6.10780 
            c2 = 17.08085
            c3 = 234.175
            cv1 = 6.10780
            cv2 = 17.84362
            cv3 = 245.425
            expTTv = (c2 * TT) / (c3 + TT)
            SVPTTv = c1 * pow (e, expTTv) 
            expHTv = (cv2 * HTdv) / (cv3 + HTdv)
            SVPHTv = cv1 * pow (e, expHTv) 
            SVPDTv = SVPHTv - (0.000660 * (1 + 0.0015 * HTd)) * p * (TT - HTd) 
            U_test_voda = round (SVPDTv / SVPTTv * 100)
            if U_test_voda == UU:
                break
        HTal = round (HTl / -100,1)
        HTav = round (HTv / -100,1)
        HTalp = str (HTal)
        HTavp = str (HTav)
        print ("HT = V" + HTavp + " [L" + HTalp + "]")
        print ("V - na krpici mokrog termometra je voda")
        print ("L - na krpici mokrog termometra je led")     

def wbtcx (TTx,UU,bbb): #WBTC, ali se vrijednosti unose bez decimalne točke
    TT = TTx / 10
    if bbb == "/":
        bbbx = float(1013.3)
    else:
        bbbx = float(bbb) / 10
    if bbbx < 70:
        p = (bbbx + 1000)
    else:
        p = bbbx
    for HT in range (-5000, 4000):
        HTd = HT / 100
        e = 2.718282 
        c1 = 6.10780 
        c2 = 17.08085
        c3 = 234.175
        expTT = (c2 * TT) / (c3 + TT)
        SVPTT = c1 * pow (e, expTT) 
        expHT = (c2 * HTd) / (c3 + HTd)
        SVPHT = c1 * pow (e, expHT) 
        SVPDT = SVPHT - (0.000660 * (1 + 0.0015 * HTd)) * p * (TT - HTd) 
        U_test = round (SVPDT / SVPTT * 100)
        if U_test == UU:
            break
    if HTd >= 0:
        HTa = round(HT / 10)
        HTap = str (HTa)
        print ("HT = " + HTap)
    else:
        for HTl in range (-5000, 4000):
            HTdl = HTl / 100
            e = 2.718282 
            c1 = 6.10780 
            c2 = 17.08085
            c3 = 234.175
            cl1 = 6.10714 
            cl2 = 22.44294
            cl3 = 272.440
            expTTl = (c2 * TT) / (c3 + TT)
            SVPTTl = c1 * pow (e, expTTl) 
            expHTl = (cl2 * HTdl) / (cl3 + HTdl)
            SVPHTl = cl1 * pow (e, expHTl) 
            SVPDTl = SVPHTl - 0.000582 * p * (TT - HTdl) 
            U_test_led = round (SVPDTl / SVPTTl * 100)
            if U_test_led == UU:
                break
        for HTv in range (-5000, 4000):
            HTdv = HTv / 100
            e = 2.718282 
            c1 = 6.10780 
            c2 = 17.08085
            c3 = 234.175
            cv1 = 6.10780
            cv2 = 17.84362
            cv3 = 245.425
            expTTv = (c2 * TT) / (c3 + TT)
            SVPTTv = c1 * pow (e, expTTv) 
            expHTv = (cv2 * HTdv) / (cv3 + HTdv)
            SVPHTv = cv1 * pow (e, expHTv) 
            SVPDTv = SVPHTv - (0.000660 * (1 + 0.0015 * HTd)) * p * (TT - HTd) 
            U_test_voda = round (SVPDTv / SVPTTv * 100)
            if U_test_voda == UU:
                break
        HTal = round (HTl / -10)
        HTav = round (HTv / -10)
        HTalp = str (HTal)
        HTavp = str (HTav)
        print ("HT = V" + HTavp + " [L" + HTalp + "]")
        print ("V - na krpici mokrog termometra je voda")
        print ("L - na krpici mokrog termometra je led")  

#pomoć
def pomoć ():
    print ("Za detaljnije upute pročitati procitaj.txt datoteku. Za preuzimanje, upisati preuzmi ()")
    print (" ")
    print ("MATEMATIKA")
    print ("linearna (a,b)")
    print ("kvadratna (a,b,c)")
    print ("dnepoz (z1,a1,b1,c1,z2,a2,b2,c2)")
    print ("dnepoz2 (a,b,c,d,e,f,g,h,i)")
    print ("trokut (a,b,gama)")
    print (" ")
    print ("* * * ")
    print (" ")
    print ("FIZIKA")
    print ("jpg (v,s,t)")
    print ("jug (a,v,s,t)")
    print ("ohm_zakon (I,U,R)")
    print (" ")
    print ("* * * ")
    print (" ")
    print ("METEO")
    print ("vlaga (tt, td)")
    print ("wbtc (TT,UU,bbb)")
    print ("wbtcx (TT,UU,bbb) - wbtc bez decimalne točke")
    print (" ")
    print ("* * * ")
    print (" ")
    print ("clear ()")
    print ("izl ()")

def preuzmi (): #preuzimanje uputa za korištenje
    try:
        url="https://raw.githubusercontent.com/svenazari/formule/main/procitaj.txt"
        r = requests.get(url, allow_redirects=True)
        open('procitaj.txt', 'wb').write(r.content)
    except:
        print("Preuzimanje nije uspjelo!")
    else:
        print("Datoteka je uspješno preuzeta u mapu u kojoj se nalazi skripta.")

def izl (): #izlazna funkcija - briše python povijest za sesiju u kojoj je korištena skripta
    readline.clear_history ()
    exit ()

#DODATI I DORADITI:
#- funkcije za računanje rješenja drugih oblika kvadratnih jednadžbi sa dvije nepoznanice 
#- napraviti da WBTC i WBTCX funkcije pokazuju i drige vrijednosti vezane uz vlagu zraka
#- naći rješenje za funkciju ziva
