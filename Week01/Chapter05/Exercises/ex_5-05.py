# Complete this truth table:

p q r (not (p and q)) or r
F F F -> (not(F and F)) or F -> (not(F)) or F -> (T) or F -> T
F F T -> (not(F and F)) or T -> (not(F)) or T -> (T) or T -> T
F T F -> (not(F and T)) or F -> (not(F)) or F -> (T) or F -> T
F T T -> (not(F and T)) or T -> (not(F)) or T -> (T) or T -> T
T F F -> (not(T and F)) or F -> (not(F)) or F -> (T) or F -> T
T F T -> (not(T and F)) or T -> (not(F)) or T -> (T) or T -> T
T T F -> (not(T and T)) or F -> (not(T)) or F -> (F) or F -> F
T T T -> (not(T and T)) or T -> (not(T)) or T -> (F) or T -> T