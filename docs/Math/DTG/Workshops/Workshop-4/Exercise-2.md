



| P(x) | Q(x) | ¬R(x) | ¬P(x) | Output
|------|------|-------|-------|-------
|  0   |  0   |   0   |   1   |   1   
|  0   |  1   |   0   |   1   |   1   
|  1   |  0   |   0   |   1   |   1   
|  1   |  1   |   1   |   0   |   0 

P isprime

R is2mod5

Q isgcd1

(P(x) ∧ ¬R(x)) ∨ ¬(P(x) ∨ ¬Q(x) ∨ R(x)) ∨ (¬P(x) ∧ ¬Q(x) ∧ R(x))


1:  (P(x) ∧ ¬R(x)) ==(P(x) ∧ ¬R(x) ∧ Q(x)) ∨ (P(x) ∧ ¬R(x) ∧ ¬Q(x))  
2:  ¬(P(x) ∨ ¬Q(x) ∨ R(x)) == (¬P(x) ∧ Q(x) ∧ ¬R(x)) 
3:  (¬P(x) ∧ ¬Q(x) ∧ R(x))  


(P(x) ∧ ¬R(x) ∧ Q(x)) **∨ (P(x) ∧ ¬R(x) ∧ ¬Q(x)) ∨ (¬P(x) ∧ Q(x) ∧ ¬R(x)) ∨ (¬P(x) ∧ ¬Q(x) ∧ R(x))

https://github.com/DeeKahy/UniNotes/edit/master/docs/Math/DTG/Workshops/Workshop-4/Exercise-2.md
https://github.com/DeeKahy/UniNotes/blob/master/docs/Math/DTG/Workshops/Workshop-4/Exercise-1.md
https://github.com/DeeKahy/UniNotes/edit/master/docs/Math/DTG/Workshops/Workshop-4/Exercise-1.md
