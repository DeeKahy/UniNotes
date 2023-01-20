

## 1  Rewrite the condition in (1) into PDNF.

* P isprime
* R is2mod5
* Q isgcd1

Form:

(P(x) ∧ ¬R(x)) ∨ ¬(P(x) ∨ ¬Q(x) ∨ R(x)) ∨ (¬P(x) ∧ ¬Q(x) ∧ R(x))

Into PDNF:

* (P(x) ∧ ¬R(x)) ==(P(x) ∧ ¬R(x) ∧ Q(x)) ∨ (P(x) ∧ ¬R(x) ∧ ¬Q(x))  
*  ¬(P(x) ∨ ¬Q(x) ∨ R(x)) == (¬P(x) ∧ Q(x) ∧ ¬R(x)) 
* (¬P(x) ∧ ¬Q(x) ∧ R(x))  

Solution:
(P(x) ∧ ¬R(x) ∧ Q(x)) ∨ (P(x) ∧ ¬R(x) ∧ ¬Q(x)) ∨ (¬P(x) ∧ Q(x) ∧ ¬R(x)) ∨ (¬P(x) ∧ ¬Q(x) ∧ R(x))

truth table:

| P(x) | R(x) | Q(x) | out |
| ---- | ---- | ---- | --- |
| T    | T    | T    | F   |
| T    | T    | F    | F   |
| T    | F    | T    | T   |
| T    | F    | F    | T   |
| F    | T    | T    | T   |
| F    | T    | F    | F   |
| F    | F    | T    | T   |
| F    | F    | F    | F   |

## 2 How many minterms does the normalform contain? What does this mean for the corresponding truth table?

it has 4 minterms, this means that 4 out of the 8 rows need to be true.




