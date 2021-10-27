# IA Lab 5-6

Authors: Barat Narcis Stefan & Gradinariu Florin Marian

## Mastermind

Jucătorul A are bile de n culori diferite, câte m bile de fiecare culoare. Jucătorul A alege k bile, fără ca alegerea să fie vizibilă pentru jucătorul B. Un pas al jocului constă în:

- Jucătorul B propune o secvență de k  culori. O culoare se poate repeta de cel mult m ori.
- Jucătorul A indică o valoare între 0 și k corespunzătoare numărului de potriviri de culori și poziții între secvența propusă de B și bilele alese la începutul jocului.

Dacă după cel mult 2*n pași jucătorul B a propus secvența de culori corespunzătoare secvenței de k bile alese de jucătorul A, jucătorul B câștigă jocul. Altfel, câștigă jucătorul A.

## Steps

- &#9744; 1. (0.2) Implementați funcția de inițializare (primește ca parametrii n, m și k, întoarce starea inițială) și funcția care verifică dacă o stare primită ca parametru este finală, caz în care întoarce câștigătorul.
- &#9744; 2. (0.2) Implementați o funcție care alege aleator k bile din cele m*n disponibile.
- &#9744; 3. (0.2) Implementați o funcție care compară o secvență de k culori cu secvența generată de funcția anterioară și întoarce o valoare între 0 și k corespunzătoare numărului de potriviri între cele două șiruri.
- &#9744; 4. (0.3) Implementați o interfață pentru jucătorul B uman, cu posibilitatea introducerii unei secvențe de culori, afișarea numărului de potriviri și afișarea câștigătorului jocului.
- &#9744; 5. (0.7) Implementați o strategie pentru jucătorul B folosind algoritmul MINIMAX cu retezarea ALPHA-BETA.

The checkbox means that the problem was solved.

# Output
```bash
TBD
```