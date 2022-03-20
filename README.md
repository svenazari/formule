<pre>
# FORMULE.PY

UPUTE ZA KORIŠTENJE:
1. Pokrenuti Python3 shell u folderu u kojem se nalazi skripta.
2. Unjeti naredbu 'exec(open('formule.py').read())'.
3. Upisati 'pomoć ()' za pomoć u korištenju funkcija.

FUNKCIJE:

MATEMATIKA:  
  linearna (a,b):  
    Daje rješenja linearne jednadžbe.  
    a i b su koeficjenti linearne jednadžbe u obliku ax+b=0  
  kvadratna (a,b,c):  
    Daje rješenja kvadratne jednadžbe.  
    a, b i c su koeficjenti kvadratne jednadžbe u obliku ax^2+bx+c=0  
  trokut (a,b,alfa):  
    Računa vrijednost treće stranice trokuta.  
    a i b su stranice trokuta, a alfa je kut između njih izražen u stupnjevima (°).  

FIZIKA
  jug (a,v,s,t):  
    Rješava formule za jednoliko ubrzano gibanje po pravcu.  
    a - ubrzanje, v - brzina ili promjena brzine, s - prijeđeni put ili promjena prijeđenog puta, t - vremenski period  
    Za veličinu koju se traži upisati "?", a za veličinu koja je nepoznata ili nije potrebna upisati "/" (navodni znakovi su potrebni). NPR., ako se želi izračunati ubrzanje, a poznate su promjena brzine (npr. 2) i promjena vremena (npr. 4) treba upisati: jug ("?",2,"/",4)  
    Korisnik sam treba paziti da si vrijednosti koje unosi međusobno odgovaraju po mjernim jedinicama.  

ohm_zakon (I,U,R):
Rješava formule za Ohmov zakon.
I - jakost struje, U - napon, R - otpor
Za vrijednost koju se traži treba upisati "?" (navodni znakovi su potrebi). NPR., ako se želi izračunati napon, potrebno je upisati ohm_zakon (2,"?",5)
  *Korisnik sam mora uskladiti mjerne jedinice.

METEO
vlaga (tt,td):
Funkcija računa relativnu vlagu zraka.
tt - temperatura zraka [°C], td - temperatura rosišta [°C]

wbtc (TT,UU,bbb):
Funkcija računa vrijednost mokre temperature i izražava ju u °C.
TT - temperatura zraka [°C], UU - relativna vlaga zraka [°C], bbb - tlak zraka na razini postaje [hPa]
Ako je tlak zraka iznad 1000 hPa, mogu se izostaviti znamenke tisućica i stotica.
</pre>
