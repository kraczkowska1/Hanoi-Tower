import numpy as np
import random

P = 3                   # patyki
K = 4                   # krążki
MD = 2**K          # maks decyzji, kroki
PU = 1                  # początkowe ułożenie
KU = 3                  # końcowe ułożenie

def tworzenie_decyzji(K, MD, P):

    # macierz decyzji
    decyzja = np.zeros((K, MD, P), dtype=int)

    # początkowe ułożenie
    for i in range(K):
        decyzja[i, 0, PU-1] = 1

    for i in range(K):
        decyzja[i, MD-1, KU-1] = 1

    return decyzja

def ilosc_krokow(decyzja):
    return np.sum(decyzja)


def ograniczenia(decyzja):

    l_pomylek = 0

    # zawsze gdzieś leży
    for i in range(K):
        for j in range(MD):
            if np.sum(decyzja[i, j, :]) != 1:
                l_pomylek += 1

    # odpowiedni ruch - jeden na rundę
    for d in range(1, MD):
        if np.sum([abs(decyzja[k, d, p] - decyzja[k, d-1, p]) for k in range(K) for p in range(P)]) > 1:
            l_pomylek += 1

    # nie można kłaść większego na mniejszym
    for i in range(1, K):
        for j in range(1, MD):
            for z in range(P):
                if np.sum(decyzja[:i, j-1, z]) + ((abs(decyzja[i, j, z] - decyzja[i, j-1, z]) - 1) * 10) > 0:
                    l_pomylek += 1

    return l_pomylek

def ilosc_bledow(decyzja):

    l_pomylek = ograniczenia(decyzja)

    return l_pomylek


# Wyżarzanie
H = 1000            # warunek stopu, maks iteracji
h = 0               # licznik iteracji
alpha = 0.7        # współczynnik schładzania
lb_prob = 3         # liczba prób w każdej iteracji
temp_pocz = 100     # temperatura początkowa

temp = temp_pocz

def generuj_nowe(decyzja):

    nowe_ruchy = np.copy(decyzja)

    for d in range(1, MD - 1):
        for k in range(0, K):

            p = random.randint(0, P - 1)
            nowe_ruchy[k, d, p] = 1

    return nowe_ruchy

decyzja = tworzenie_decyzji(K, MD, P)

najlepszy_koszt = MD  # ile krokow do celu

def wyzarzanie(K, MD, P, H, alpha, lb_prob, temp_pocz, funkcja_celu = ilosc_bledow):

    h = 0

    H = H * lb_prob

    temp = temp_pocz

    trzy_ostatnie = []

    najlepszy_koszt = np.inf

    decyzja = tworzenie_decyzji(K, MD, P)

    # wylosuj permutację, która spełnia ograniczenia -  to nie spelnia ograniczen
    nowa_decyzja = generuj_nowe(decyzja)

    najlepsza_decyzja = nowa_decyzja

    # koszt nowego rozwiązania
    najlepszy_koszt = funkcja_celu(nowa_decyzja)

    while h < H:

        # wylosuj permutację, która spełnia ograniczenia -  to nie spelnia ograniczen
        nowa_decyzja = generuj_nowe(decyzja)

        # while nowa_decyzja in trzy_ostatnie:
        #     nowa_decyzja = generuj_nowe(decyzja)

        while any((nowa_decyzja == x).all() for x in trzy_ostatnie):
            nowa_decyzja = generuj_nowe(decyzja)

        # koszt nowego rozwiązania
        nowy_koszt = funkcja_celu(nowa_decyzja)

        # Akceptacja nowego rozwiązania
        if nowy_koszt < najlepszy_koszt or random.uniform(0, 1) < np.exp((najlepszy_koszt - nowy_koszt) / temp):

            decyzja = nowa_decyzja
            # najlepszy_koszt = nowy_koszt

            # Aktualizacja najlepszego rozwiązania
            if nowy_koszt < najlepszy_koszt:
                najlepsza_decyzja = np.copy(nowa_decyzja)
                najlepszy_koszt = nowy_koszt

                print("ok")

                if len(trzy_ostatnie) == 3:
                    trzy_ostatnie.pop(0)

                trzy_ostatnie.append(najlepsza_decyzja)
        # print(trzy_ostatnie)

        # schładzanie
        temp *= alpha

        # następna iteracja
        h += 1

    return najlepszy_koszt, najlepsza_decyzja



wyniki = []

for liczba in range(5):
    najlepszy_koszt, najlepsza_decyzja = wyzarzanie(K, MD, P, H, alpha, lb_prob, temp_pocz)

    print(najlepszy_koszt)
    wyniki.append(najlepsza_decyzja)

    # for decyzje in najlepsza_decyzja:
    #     print(decyzje)
    #     print("\n")
