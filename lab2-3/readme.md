# IA Lab 2-3

Authors: Barat Narcis Stefan & Gradinariu Florin Marian

## Statement

Pe malul stâng al unui râu sunt n cupluri (soț-soție) și o barcă în care încap maxim două persoane. Găsiți o secvență de mutări, folosind barca, astfel încât toate persoanele să ajungă pe malul drept. 

Știm că:

- Barca nu se poate deplasa de pe un mal pe celălalt decât cu cel puțin o persoană.
        
- Pe nici un mal nu poate fi vreodată o soție fără soțul său, dacă pe acel mal mai există cel puțin un soț. Persoanele din barcă sunt considerate pe malul destinație (transferul este instantaneu). 

## Steps

- &#9745; 1. (0.2) Alegeți o reprezentare a unei stări a problemei. Reprezentarea trebuie să fie suficient de explicită pentru a conține toate informaţiile necesare pentru continuarea găsirii unei soluții dar trebuie să fie și suficient de formalizată pentru a fi ușor de prelucrat/memorat.
- &#9745; 2. (0.2) Identificați stările speciale (inițială și finală) și implementați funcția de inițializare (primește ca parametrii instanța problemei, întoarce starea inițială) și funcția booleană care verifică dacă o stare primită ca parametru este finală.
- &#9745; 3. (0.2) Implementați tranzițiile ca o funcție care primește ca parametri o stare și parametrii tranziției și întoarce starea rezultată în urma aplicării tranziției. Validarea tranziției se face într-o funcție booleană separată, cu aceeași parametrii. 
- &#9745; 4. (0.2) Implementați strategia Backtracking.
- &#9745; 5. (0.2) Implementați strategia BFS.
- &#9744; 6. (0.2) Implementați strategia Hillclimbing.
- &#9745; 7. (0.2) Implementați strategia A*
- &#9745; 8. (0.2) Implementați un meniu care permite, după introducerea instanței, selectarea strategiei care va fi încercată.

The checkbox means that the problem was solved.

### Output
```commandline
Enter the number of couples: 3
How many persons can the boat hold: 2

Strategies:
	(1) Backtracking
	(2) Breadth-First-Search
	(3) Hillclimbing
	(4) A*-Search-Algorithm
Select the search strategy you would like to use: 4
Visited states:  1
Visited states:  2
Visited states:  3
Visited states:  4
Visited states:  5
Visited states:  6
Visited states:  7
Visited states:  8
Visited states:  9
Visited states:  10
Visited states:  11
Visited states:  12
Visited states:  13
Visited states:  14
Visited states:  15
Visited states:  16
Visited states:  17
Visited states:  18
Visited states:  19
Visited states:  20
Visited states:  21
Visited states:  22
Visited states:  23
Visited states:  24
Visited states:  25
Visited states:  26
Visited states:  27
Visited states:  28
Visited states:  29
Visited states:  30
Visited states:  31
Visited states:  32
Visited states:  33
Visited states:  34
Visited states:  35
Visited states:  36
Visited states:  37
Visited states:  38
Visited states:  39
Visited states:  40
Visited states:  41
Visited states:  42
Visited states:  43
Visited states:  44
Visited states:  45
Visited states:  46
Visited states:  47
Visited states:  48
Visited states:  49
Visited states:  50
Visited states:  51
Visited states:  52
Visited states:  53
Visited states:  54
Visited states:  55
Visited states:  56
Visited states:  57

Success:  [1, 1, 1, 1, 1, 1]  reached
Depth:  11
Path:  [[0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 1], [0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1]]

Process finished with exit code 0
```