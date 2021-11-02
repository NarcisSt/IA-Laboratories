# IA Lab 5-6

Authors: Barat Narcis Stefan & Gradinariu Florin Marian

## Mastermind

Jucătorul A are bile de n culori diferite, câte m bile de fiecare culoare. Jucătorul A alege k bile, fără ca alegerea să fie vizibilă pentru jucătorul B. Un pas al jocului constă în:

- Jucătorul B propune o secvență de k  culori. O culoare se poate repeta de cel mult m ori.
- Jucătorul A indică o valoare între 0 și k corespunzătoare numărului de potriviri de culori și poziții între secvența propusă de B și bilele alese la începutul jocului.

Dacă după cel mult 2*n pași jucătorul B a propus secvența de culori corespunzătoare secvenței de k bile alese de jucătorul A, jucătorul B câștigă jocul. Altfel, câștigă jucătorul A.

## Steps

- &#9745; 1. (0.2) Implementați funcția de inițializare (primește ca parametrii n, m și k, întoarce starea inițială) și funcția care verifică dacă o stare primită ca parametru este finală, caz în care întoarce câștigătorul.
- &#9745; 2. (0.2) Implementați o funcție care alege aleator k bile din cele m*n disponibile.
- &#9745; 3. (0.2) Implementați o funcție care compară o secvență de k culori cu secvența generată de funcția anterioară și întoarce o valoare între 0 și k corespunzătoare numărului de potriviri între cele două șiruri.
- &#9745; 4. (0.3) Implementați o interfață pentru jucătorul B uman, cu posibilitatea introducerii unei secvențe de culori, afișarea numărului de potriviri și afișarea câștigătorului jocului.
- &#9744; 5. (0.7) Implementați o strategie pentru jucătorul B folosind algoritmul MINIMAX cu retezarea ALPHA-BETA.

The checkbox means that the problem was solved.

# Output
```bash


1 - RED, 2 - GREEN, 3 - YELLOW, 4 - BLUE, 5 - BLACK, 6 - ORANGE


    |	UNK	UNK	UNK	UNK
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
Number of right colors: 0
Enter the code : 1 2 3 4


1 - RED, 2 - GREEN, 3 - YELLOW, 4 - BLUE, 5 - BLACK, 6 - ORANGE


    |	UNK	UNK	UNK	UNK
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	RED	GRE	YEL	BLU
------------------------------
Number of right colors: 0
Enter the code : 4 3 2 1


1 - RED, 2 - GREEN, 3 - YELLOW, 4 - BLUE, 5 - BLACK, 6 - ORANGE


    |	UNK	UNK	UNK	UNK
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	BLU	YEL	GRE	RED
------------------------------
- - |
- - |	RED	GRE	YEL	BLU
------------------------------
Number of right colors: 0
Enter the code : 1 3 5 2 


1 - RED, 2 - GREEN, 3 - YELLOW, 4 - BLUE, 5 - BLACK, 6 - ORANGE


    |	UNK	UNK	UNK	UNK
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- K |	RED	YEL	BLA	GRE
------------------------------
- - |
- - |	BLU	YEL	GRE	RED
------------------------------
- - |
- - |	RED	GRE	YEL	BLU
------------------------------
Number of right colors: 1
Enter the code : 6 3 2 5


1 - RED, 2 - GREEN, 3 - YELLOW, 4 - BLUE, 5 - BLACK, 6 - ORANGE


    |	UNK	UNK	UNK	UNK
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
K - |
- - |	ORA	YEL	GRE	BLA
------------------------------
- - |
- K |	RED	YEL	BLA	GRE
------------------------------
- - |
- - |	BLU	YEL	GRE	RED
------------------------------
- - |
- - |	RED	GRE	YEL	BLU
------------------------------
Number of right colors: 1
Enter the code : 6 1 5 2


1 - RED, 2 - GREEN, 3 - YELLOW, 4 - BLUE, 5 - BLACK, 6 - ORANGE


    |	UNK	UNK	UNK	UNK
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- K |
K - |	ORA	RED	BLA	GRE
------------------------------
K - |
- - |	ORA	YEL	GRE	BLA
------------------------------
- - |
- K |	RED	YEL	BLA	GRE
------------------------------
- - |
- - |	BLU	YEL	GRE	RED
------------------------------
- - |
- - |	RED	GRE	YEL	BLU
------------------------------
Number of right colors: 2
Enter the code : 6 2 5 1


1 - RED, 2 - GREEN, 3 - YELLOW, 4 - BLUE, 5 - BLACK, 6 - ORANGE


    |	UNK	UNK	UNK	UNK
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
- - |	-	-	-	-
------------------------------
- - |
K - |	ORA	GRE	BLA	RED
------------------------------
- K |
K - |	ORA	RED	BLA	GRE
------------------------------
K - |
- - |	ORA	YEL	GRE	BLA
------------------------------
- - |
- K |	RED	YEL	BLA	GRE
------------------------------
- - |
- - |	BLU	YEL	GRE	RED
------------------------------
- - |
- - |	RED	GRE	YEL	BLU
------------------------------
Number of right colors: 1
Enter the code : 6 5 1 2
    |	ORA	BLA	RED	GRE
------------------------------
- - |
- - |	-	-	-	-
------------------------------
K K |
K K |	ORA	BLA	RED	GRE
------------------------------
- - |
K - |	ORA	GRE	BLA	RED
------------------------------
- K |
K - |	ORA	RED	BLA	GRE
------------------------------
K - |
- - |	ORA	YEL	GRE	BLA
------------------------------
- - |
- K |	RED	YEL	BLA	GRE
------------------------------
- - |
- - |	BLU	YEL	GRE	RED
------------------------------
- - |
- - |	RED	GRE	YEL	BLU
------------------------------
Number of right colors: 4
You win! :)

Process finished with exit code 0
```