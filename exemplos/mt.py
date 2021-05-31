import random

## Troca 0's por 1's (possui transicao sem movimento)
Q1 = {'q0', 'q1', 'q2'}
S1 = {'0', '1'}
G1 = {'0', '1', 'X', 'Y'}
D1 = {( 'q0', '0'): ('q0', '1', "R"), 
   ( 'q0', '1'): ('q1', '1', "S"),
   ( 'q0', 'B'): ('q2', 'B', "L"),
   ( 'q1', '0'): ('q0', '0', "S"),
   ( 'q1', '1'): ('q1', '0', "R"),
   ( 'q1', 'B'): ('q2', 'B', "L")}
M1 = (Q1, S1, G1, D1, 'q0', 'B', {'q2'})


## Inverte palavra binaria (colocando no começo da fita e apagando a original) (possui transicao sem movimento)
Q2 = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
S2 = {'0', '1'}
G2 = {'0', '1', 'X'}
D2 =  {( 'q0', 'B'): ('q4', 'B', "L"),
   ( 'q0', 'X'): ('q0', 'X', "R"),
   ( 'q0', '0'): ('q1', 'X', "L"),
   ( 'q0', '1'): ('q2', 'X', "L"),
   ( 'q1', 'B'): ('q3', '0', "R"),
   ( 'q1', 'X'): ('q1', 'X', "L"),
   ( 'q1', '0'): ('q1', '0', "L"),
   ( 'q1', '1'): ('q1', '1', "L"),
   ( 'q2', 'B'): ('q3', '1', "R"),
   ( 'q2', 'X'): ('q2', 'X', "L"),
   ( 'q2', '0'): ('q2', '0', "L"),
   ( 'q2', '1'): ('q2', '1', "L"),
   ( 'q3', 'X'): ('q0', 'X', "R"),
   ( 'q3', '0'): ('q3', '0', "R"),
   ( 'q3', '1'): ('q3', '1', "R"),
   ( 'q4', 'X'): ('q4', 'B', "L"),
   ( 'q4', '0'): ('q5', '0', "S"),
   ( 'q4', '1'): ('q5', '1', "S")}
M2 = (Q2, S2, G2, D2, 'q0', 'B', {'q5'})

## Inverte palavra binaria (colocando no fim da fita e depois substituindo por cima da original) (nao possui transicao sem movimento)
Q3 = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7','q8','q9','q10','q11'}
S3 = {'0', '1'}
G3 = {'0', '1', 'X', 'Y'}
D3 = {( 'q0', 'B'): ('q1', 'B', "L"),
 ( 'q0', '0'): ('q0', '0', "R"),
 ( 'q0', '1'): ('q0', '1', "R"),
 ( 'q1', 'B'): ('q5', 'B', "R"),
 ( 'q1', 'X'): ('q1', 'X', "L"),
 ( 'q1', '0'): ('q2', 'X', "R"),
 ( 'q1', '1'): ('q3', 'X', "R"),
 ( 'q2', 'B'): ('q4', '0', "L"),
 ( 'q2', 'X'): ('q2', 'X', "R"),
 ( 'q2', '0'): ('q2', '0', "R"),
 ( 'q2', '1'): ('q2', '1', "R"),
 ( 'q3', 'B'): ('q4', '1', "L"),
 ( 'q3', 'X'): ('q3', 'X', "R"),
 ( 'q3', '0'): ('q3', '0', "R"),
 ( 'q3', '1'): ('q3', '1', "R"),
 ( 'q4', 'X'): ('q1', 'X', "L"),
 ( 'q4', '0'): ('q4', '0', "L"),
 ( 'q4', '1'): ('q4', '1', "L"),
 ( 'q5', 'X'): ('q5', 'X', "R"),
 ( 'q5', 'Y'): ('q5', 'Y', "R"),
 ( 'q5', '0'): ('q6', 'Y', "L"),
 ( 'q5', '1'): ('q7', 'Y', "L"),
 ( 'q5', 'B'): ('q10','B', "L"),
 ( 'q6', 'X'): ('q6', 'X', "L"),
 ( 'q6', 'Y'): ('q6', 'Y', "L"),
 ( 'q6', 'B'): ('q8', 'B', "R"),
 ( 'q6', '0'): ('q8', '0', "R"),
 ( 'q6', '1'): ('q8', '1', "R"),
 ( 'q7', 'X'): ('q7', 'X', "L"),
 ( 'q7', 'Y'): ('q7', 'Y', "L"),
 ( 'q7', 'B'): ('q9', 'B', "R"),
 ( 'q7', '0'): ('q9', '0', "R"),
 ( 'q7', '1'): ('q9', '1', "R"),
 ( 'q8', 'X'): ('q5', '0', "R"),
 ( 'q9', 'X'): ('q5', '1', "R"),
 ( 'q10', 'Y'): ('q10', 'B', "L"),
 ( 'q10', '1'): ('q10', '1', "L"),
 ( 'q10', '0'): ('q10', '0', "L"),
 ( 'q10', 'B'): ('q11', 'B', "R")}
M3 = (Q3, S3, G3, D3, 'q0', 'B', {'q11'})

palavra = '1010110'

