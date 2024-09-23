// Ilosc patykow
int P = 3;

// ilosc krazkow
int K = 4;

// Maksymalna ilosc decyzji 2^K
int D = 16;

// poczatkowe ulozenie
int PU = 1;

// koncowe ulozenie
int KU = 3;

// macierz decyzji dla K krążków, D decyzji, P patykow
dvar boolean decyzja[1..K, 1..D, 1..P];

dexpr float rownanie = sum(i in 1..K, j in 1..D, z in 1..P) decyzja[i, j, z];
minimize rownanie;

subject to 
 {
   // Kazdy krazek zawsze gdzies lezy
   cons1:
   forall(i in 1..K, j in 1..D) sum( z in 1..P ) decyzja[i, j, z] == 1;
   
   // Miejsce zakonczenia
   cons2:
   forall (i in 1..K) decyzja[i, D, KU] == 1;
   
   // Miejsce rozpoczecia
   cons3:
   forall (i in 1..K) decyzja[i, 1, PU] == 1;
   
   // Jeden ruch na runde
   cons4:
   forall(j in 2..D) sum(k in 1..K, p in 1..P) abs(decyzja[k, j, p] - decyzja[k, j-1, p]) == 2;
   
   // Najpierw podnosimy mniejszy krazek z piramidy, nie kladziemy wiekszego krazka na mniejszy
    forall(i in 2..K, j in 2..D, z in 1..P) (sum( l in 1..i-1) (decyzja[l, j-1, z]) + ((abs(decyzja[i, j, z] - decyzja[i, j-1, z]) - 1) * 10)) <= 0;

 };