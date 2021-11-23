# IA Lab 7

Authors: Barat Narcis Stefan & Gradinariu Florin Marian

## Backpropagation

Implementati algoritmul Backpropagation pentru o retea neuronala multistrat (cu un strat ascuns si doi

neuroni in stratul ascuns) cu scopul de a invata functii logice binare. Datele de antrenare vor fi citite dintr-
un fisier. Spre exemplu, fisierul de intrare pentru functia AND poate contine:

0 0 0<br>
0 1 0<br>
1 0 0<br>
1 1 1

Parametrii algoritmului (numarul maxim de epoci de antrenare, rata de invatare, etc) vor fi cititi de la
tastatura.

## Steps

- &#9745; 1. (0.1) citirea datelor
- &#9745; 2. (0.1) functia de activare sigmoida
- &#9745; 3. (0.2) propagarea inainte
- &#9745; 4. (0.3) propagare inapoi
    - &#9745; 4a. calculul gradientilor si corectia ponderilor pentru stratul de iesire
    - &#9745; 4b. calculul gradientilor si corectia ponderilor pentru stratul ascuns
- &#9745; 5. (0.2) actualizarea ponderilor, procedura iterativa de antrenare
- &#9745; 6. (0.1) afisarea rezultatelor

The checkbox means that the problem was solved.

# Output
```commandline
Please enter the number of epochs: 200000

Please enter the learning rate: 10.0

Please enter the maximum error: 0.000001
Boolean function:
0 0 0
0 1 0
1 0 0
1 1 1
Finished training epoch 5000
Finished training epoch 10000
Finished training epoch 15000
Finished training epoch 20000
Finished training epoch 25000
Finished training epoch 30000
Finished training epoch 35000
Finished training epoch 40000
Finished training epoch 45000
Finished training epoch 50000
Finished training epoch 55000
Finished training epoch 60000
Finished training epoch 65000
Finished training epoch 70000
Finished training epoch 75000
Finished training epoch 80000
Finished training epoch 85000
Finished training epoch 90000
Finished training epoch 95000
Finished training epoch 100000
Finished training epoch 105000
Finished training epoch 110000
Finished training epoch 115000
Finished training epoch 120000
Finished training epoch 125000
Finished training epoch 130000
Finished training epoch 135000
Finished training epoch 140000
Finished training epoch 145000
Finished training epoch 150000
Finished training epoch 155000
Finished training epoch 160000
Finished training epoch 165000
Finished training epoch 170000
Finished training epoch 175000
Finished training epoch 180000
Finished training epoch 185000
Finished training epoch 190000
Finished training epoch 195000
Finished training epoch 200000
Enter bellow the values you want to test:
1 1
[[0.90922594]]
Enter bellow the values you want to test:
0 1
[[0.06321065]]
Enter bellow the values you want to test:
1 0
[[0.06264213]]
Enter bellow the values you want to test:
0 0
[[0.00048429]]
Enter bellow the values you want to test:
100 100
[[1.]]
Enter bellow the values you want to test:
10 10
[[1.]]
Enter bellow the values you want to test:
1 1
[[0.90922594]]
Enter bellow the values you want to test:
12 12
[[1.]]
Enter bellow the values you want to test:
2 2
[[0.99999581]]
Enter bellow the values you want to test:
3 3
[[1.]]
```