#UPUTE ZA KORIŠTENJE:
#1. Pokrenuti Python3 shell u folderu u kojem se nalazi skripta.
#2. Unjeti naredbu 'exec(open('formule.py').read())'.
#3. Upisati 'pomoć ()' za pomoć u korištenju funkcija.

#import modula
import math
import cmath
import requests

print ("Autor: Sven Azari")
print ("Upiši 'pomoć ()' za informacije o naredbama.")

#matematika
def linearna (a,b): #pronalaženje x za linearne jednadžbe sa jednom nepoznanicom (jednadžba treba biti u formatu ax+b=0)
    if a == 0:
        print ("Nema rješenja! To nije jednadžba sa nepoznanicama!")
    else:
        x = str(round(-b / a,3))
        print ("x = " + x)

def kvadratna (a,b,c): #pronalaženje x za kvadratne jednadžbe sa jednom nepoznanicom (jednadžba treba biti u formatu ax^2+bx+c=0)
    if a == 0: #računanje linearne jednadžbe ukoliko je a = 0
        linearna (b,c)
    else:
        d = math.pow(b,2) - 4 * a * c #diskriminanta
        if d < 0: #ako je diskriminanta negativna (rješenja su kompleksni brojevi)
            ds = cmath.sqrt(d)
            i = str(round(-b / (2 * a),3)) #realni dio kompleknog broja
            z = str(abs(round((ds.imag) / (2 * a),3))*1j) #imaginarni dio kompleksnog broja (samo pozitivna vrijednost)
        
            #ispis rješenja
            print("x1 = " + i + "+" + z)
            print("x2 = " + i + "-" + z)
    
        else: #ako je diskriminanta 0 ili pozitivna
            ds = math.sqrt(d)
            x1 = round((-b + ds) / (2 * a),3)
            x1s = str(x1)
            x2 = round((-b - ds) / (2 * a),3)
            x2s = str(x2)

            #ispis rješenja
            print("x1 = " + x1s)
            print("x2 = " + x2s)

def trokut (a,b,alfa):
    alfar = alfa * math.pi / 180 #pretvaranje stupnjeva u radijane
    cx = str(round(math.sqrt(math.pow(a,2) + math.pow(b,2) - 2 * a * b * math.cos(alfar)),3)) #kosinusov poučak
    print ("c = " + cx) #ispis rješenja

#fizika

#def jpg (v,s,t): #jednoliko pravocrtno gibanje

def jug (a,v,s,t): #jednoliko ubrzano gibanje - vrijednost nepoznanica mogu biti ili vrednost veličine ili vrijednost promjene te veličine (DOVRŠITI)
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


def ohm_zakon (I,U,R): #ohmov zakon
    if I == "?":
        Ix = str(round(U / R,3))
        print ("I = " + Ix)
    elif U == "?":
        Ux = str(round(I * R,3))
        print ("U = " + Ux)
    elif R == "?":
        Rx = str(round(U / I,3))
        print ("R = " + Rx)

#meteo
def vlaga (tt,td):
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

def wbtc (TT,UU,bbb):
    if bbb < 70:
        p = (bbb + 1000) / 10
    else:
        p = bbb / 10
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

#pomoć
def pomoć ():
    print ("Za detaljnije upute pročitati procitaj.txt datoteku.")
    print (" ")
    print ("MATEMATIKA")
    print ("linearna (a,b)")
    print ("kvadratna (a,b,c)")
    print ("trokut (a,b,alfa)")
    print (" ")
    print ("* * * ")
    print (" ")
    print ("FIZIKA")
    print ("jug (a,v,s,t)")
    print ("ohm_zakon (I,U,R)")
    print (" ")
    print ("* * * ")
    print (" ")
    print ("METEO")
    print ("vlaga (tt, td)")
    print ("wbtc (TT,UU,bbb)")