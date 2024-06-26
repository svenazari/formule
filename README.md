# FORMULE.PY
<pre>
UPUTE ZA KORIŠTENJE:
1. Pokrenuti Python3 shell u folderu u kojem se nalazi skripta.
2. Unjeti naredbu 'exec(open('formule.py').read())'.
3. Upisati 'pomoć ()' za pomoć u korištenju funkcija.

Autor: Sven Azari
http://www.github.com/svenazari

FUNKCIJE:

MATEMATIKA:  
  linearna (a,b):  
    Daje rješenja linearne jednadžbe.  
    a i b su koeficjenti linearne jednadžbe u obliku ax+b=0  
    
  kvadratna (a,b,c):  
    Daje rješenja kvadratne jednadžbe.  
    a, b i c su koeficjenti kvadratne jednadžbe u obliku ax^2+bx+c=0  
    
  dnepoz (z1,a1,b1,c1,z2,a2,b2,c2)
    Rješava sustav jednadžbi sa dvije nepoznanice u kojem su jednadžbe formata Zy=Ax^2+Bx+C.
    Sustavi jednadžbi mogu biti dvije kvadratne, kvadratana i linarna ili dvije linearne.
    Ako se traži linearna jednadžba, koeficjenci A1 ili A2 moraju biti 0.
    Ako se traži tješenje sutava kvadratne i linearne jednadžbe, prva jednadžba mora biti kvadratna, a druga linearna (A1 ne smije biti 0, a A2 mora biti 0).
    
  dnepoz2 (a,b,c,d,e,f,g,h,i)
    Rješava sustav jednadžbi sa dvije nepoznanice od kojih je prva jednadžba kvadratna jednadžba u formatu Ax^2+By^2+Cxy+Dx+Ey+F=0, a druga jednadžba je linearna u formatu Gy=Hx+I.
    
  trokut (a,b,alfa)  
    Unosi se vrijednost dvaju stranica i kuta izeđu tih stranica, a funkcija računa vrijednosti treće stranice i preostala dva kuta te ispisuje sve vrijednosti.
    Kutevi se unose u stupnjevima. 
    
  trokut_povrsina (a,b,c)
    Računa površinu trokuta koristeći heronovu formulu.
    a, b i c su stranice trokuta.

FIZIKA
  jpg (v,s,t)
    Rješava formule za jednoliko pravocrtno gibanje
    v - brzina, s - prijeđeni put, t - vremenski period
    Za veličinu koju se traži upisati "?"
    Korisnik sam treba paziti da si vrijednosti koje unosi međusobno odgovaraju po mjernim jedinicama. 
    
  jug (a,v,s,t):  
    Rješava formule za jednoliko ubrzano gibanje po pravcu.  
    a - ubrzanje, v - brzina ili promjena brzine, s - prijeđeni put ili promjena prijeđenog puta, t - vremenski period  
    Za veličinu koju se traži upisati "?", a za veličinu koja je nepoznata ili nije potrebna upisati "/" (navodni znakovi su potrebni). NPR., ako se želi izračunati ubrzanje, a poznate su promjena brzine (npr. 2) i promjena vremena (npr. 4) treba upisati: jug ("?",2,"/",4)  
    Korisnik sam treba paziti da si vrijednosti koje unosi međusobno odgovaraju po mjernim jedinicama.  

  ohm_zakon (I,U,R):
    Rješava formule za Ohmov zakon.
    I - jakost struje, U - napon, R - otpor
    Za vrijednost koju se traži treba upisati "?" (navodni znakovi su potrebi). NPR., ako se želi izračunati napon, potrebno je upisati ohm_zakon (2,"?",5)
    Korisnik sam mora uskladiti mjerne jedinice.

  time_dilitation_vel (t,v):
    Računa relativističo smanjivanje prolaska vremena zbog brzine kretanja.
    t - promjena vremena referentnom sustavu promatrača
    v - brzina kretanja tijela
    Izračunata vrijednost je promjena vremena u referentnom sustavu tijela koje se kreće. Izračunata vrijednost bit će u sekundama (s).
    Formula brzinu svjetlosti iskazuje u m/s te stoga svemenski interval mora biti u s, a brzina kretanja tijela mora biti u m/s.

METEO
  vlaga (tt,td):
    Funkcija računa relativnu vlagu zraka.
    tt - temperatura zraka [°C], td - temperatura rosišta [°C]

  wbtc (TT,UU,bbb):
    Funkcija računa vrijednost mokre temperature i izražava ju u °C.
    TT - temperatura zraka [°C], UU - relativna vlaga zraka [°C], bbb - tlak zraka na razini postaje [hPa]
    Ako je tlak zraka iznad 1000 hPa, mogu se izostaviti znamenke tisućica i stotica.
    
  wbtcx (TT,UU,bbb)
    Verzija wbtc funkcije u kojoj se vrijednosti unose bez decimalne točke.
</pre>
