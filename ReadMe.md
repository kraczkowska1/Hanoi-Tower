## README.md

# Wieże Hanoi Optimization

## Opis projektu

Projekt ten ma na celu rozwiązanie klasycznego problemu Wież Hanoi przy użyciu dwóch różnych metod:
1. **Optymalizacja z użyciem programu CPLEX** - Celem jest znalezienie optymalnego rozwiązania, minimalizując liczbę ruchów.
2. **Metaheurystyka w Pythonie** - Porównanie wydajności algorytmu optymalizacyjnego z metaheurystyką (metoda wyżarzania).

### Zasady Wież Hanoi
Wieże Hanoi to matematyczny problem, który polega na przenoszeniu dysków (krążków) między trzema kołkami zgodnie z następującymi zasadami:
1. Można przenosić tylko jeden dysk naraz.
2. Każdy ruch polega na zdjęciu górnego dysku z jednego kołka i umieszczeniu go na innym kołku.
3. Żaden krążek nie może być umieszczony na krążku mniejszym od siebie.

## Struktura projektu

- `metaheurystyka_wieza_hanoi.py` - Skrypt Pythona implementujący metaheurystykę.
- `optymalizacja_wieza_hanoi.mod` - Plik modelu CPLEX definiujący problem Wież Hanoi.
- `requirements.txt` - Lista zależności potrzebnych do uruchomienia skryptu Pythona.
- `Sprawozdanie_KRączkowska_IPaniczek.pdf` - Dokumentacja projektu, zawierająca szczegółowe informacje o założeniach, wynikach i wnioskach.

## Instalacja

1. **Python i zależności**:
    - Upewnij się, że masz zainstalowanego Pythona w wersji 3.x.
    - Zainstaluj wymagane zależności, uruchamiając:
      ```
      pip install -r requirements.txt
      ```

2. **CPLEX**:
    - Zainstaluj IBM ILOG CPLEX Optimization Studio.
    - Upewnij się, że ścieżka do CPLEX jest dodana do zmiennych środowiskowych systemu.

## Uruchamianie

### Optymalizacja CPLEX

1. Otwórz `optymalizacja_wieza_hanoi.mod` w środowisku CPLEX.
2. Uruchom model, aby znaleźć optymalne rozwiązanie problemu Wież Hanoi dla zadanej liczby krążków.
3. Wynikiem będzie macierz decyzji, wskazująca optymalne ruchy.

### Metaheurystyka w Pythonie

1. Uruchom skrypt Pythona:
   ```
   python metaheurystyka_wieza_hanoi.py
   ```
2. Skrypt wygeneruje wyniki dla metaheurystyki, pokazując liczbę błędów dla różnych iteracji.

## Wyniki

### Optymalizacja CPLEX

Przykładowe macierze decyzji dla różnych liczby krążków:

- **2 krążki**:
  ```
  [[1 0 0]   [1 0 0] 
   [0 1 0]   [1 0 0] 
   [0 1 0]   [0 0 1] 
   [0 0 1]]  [0 0 1]]
  ```

- **3 krążki**:
  ```
  [[1 0 0]   [1 0 0]   [1 0 0] 
   [0 0 1]   [1 0 0]   [1 0 0] 
   [0 0 1]   [0 1 0]   [1 0 0] 
   [0 1 0]   [0 1 0]   [1 0 0] 
   [0 1 0]   [0 1 0]   [0 0 1] 
   [1 0 0]   [0 1 0]   [0 0 1] 
   [1 0 0]   [0 0 1]   [0 0 1] 
   [0 0 1]]  [0 0 1]]  [0 0 1]]
  ```

### Metaheurystyka

Wyniki dla różnych liczby krążków i iteracji:

- **2 krążki**: Liczba błędów waha się od 2 do 5.
- **3 krążki**: Liczba błędów waha się od 9 do 18.
- **4 krążki**: Liczba błędów waha się od 33 do 48.

## Wnioski

Program CPLEX okazał się skuteczny w znajdowaniu optymalnych rozwiązań problemu Wież Hanoi, nawet dla większej liczby krążków. Metaheurystyka, mimo iż dawała przybliżone rozwiązania, była mniej precyzyjna, zwłaszcza przy większej liczbie krążków. Sugeruje to, że dla problemów o wyższym stopniu skomplikowania, algorytm optymalizacyjny CPLEX jest bardziej odpowiedni niż metaheurystyka.

## Autorzy

- Iza Paniczek
- Karolina Rączkowska

---

Opracowanie oparte na sprawozdaniu dostępne w pliku `Sprawozdanie_Wieże_Hanoi.pdf`.
