# Intro to Prob

- sample space
  - possible outcomes
- laws
  - axioms
    - rules (e.g., not negative)

## Sample space
- possible outcomes
- describe likelihood of outcomes
- make list/set $\Omega$
  - mutually <hl>exclusive</hl>
    - only 1 outcome
  - collectively <hl>exhaustive</hl>
    - you can definitely point to one outcome
  - "right" <hl>granularity</hl>
    - ignore irrelevant variables

### Example 1
- discrete & finite
- 2 x tetrahedral die
- use a treediagram

### Example 2
- continuous
- dart on a target (x,y) 0 =< x, y =< 1

## Probability axioms

- assign probabilities to subsets of sample space = <hl>Event</hl>
  - P(A) $\in [0,1]$
- axioms
  - nonnegativity: P(A) >=0 (a)
  - normalization: P($\Omega$) = 1 (b)
  - (finite) additivity (c)
    - If A $\cap$ B = $\emptyset$ then P(A $\cup$ B)= P(A) + P(B)

## Consequences of axioms
- P(A) =< 1
- P($\emptyset$) = 0
- P(A) + P($A^c$) = 1
- P(A $\cup$ B $\cup$ C) = P(A) + P(B) + P(C)

$1 = P(\Omega) = P(A \cup A^c) = P(A) + P(A^c)$
$P(A) = 1 - P(A^c) =< 1$


$1 = P(\Omega) + P(\Omega^c) = 1 + P(\emptyset) \implies P(\emptyset) = 0$


