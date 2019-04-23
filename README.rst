============================
Cyfra kontrolna
============================


Program ten oblicza cyfrę kontrolną Księgi Wieczystej na podstawie kodu sądu oraz
numeru księgi wieczystej.

Program działa ma możliwość pracy w trybie:

- interfejsu graficznego
- wiersza poleceń

W tym pierwszym przypadku księgi są obliczane pojedyńczo, a obliczony numer automatycznie jest kopiowany do schowka
W drugim przypadku program można uruchomić z wiersza poleceń wskazując scieżkę do pliku z numerami kw, program
przeliczy zawartość pliku, plik powinien być z rozszerzeniem .txt i w nazwie zawierać kod sądu, np. WL1A.txt

Sposób użycia z wiersza poleceń::
	
	>>>python3 ck.py ./WL1A.txt
  
Uruchomieni interfejsu graficznego::
  
  >>>python3 ck.py

