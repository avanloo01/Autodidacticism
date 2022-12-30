# Lecture 2
---
## Afine Cipher
$K = (a,b)$
enc: $y \equiv a*x + b\ mod\ 26$

> *IMP*: $use\ noemer^{-1}$

x: $x \equiv a^{-1}(y-b)\ mod\ 26$

### Keyspace
> a's & b's in system

- b: 26
- a: no apparent restriction in y
  - Inverse only exists if gcd(a, 26) = 1
  - e.g., 1, 3, 5, 7, 9, 11
  - #a = 12

> #K = #a * #b = 312

### Attacking
- Fixed encoding ==> letterfrequency
- Brute force

# Lecture 3
---
## Stream ciphers
- a symmetric cipher
- streaming bits
  - one bit after another processed

> it encrypts bits individually

### Motivation
- GSM
  - first use of crypto in consumer products
  - $e_K(x) = y \implies d(y) = x$

### Encryption
$y_i = e(x_i) \equiv x_i + s_i\ mod\ 2$

### Decryption
$x_i = d(y_i) \equiv y_i + s_i\ mod\ 2$

- $x_i, y_i, s_i \in \{0,1\}$

### Questions
- We expect minus in decryption
  - decryption = encryption (operation)

$d(y_i) \equiv y_i + s_i\ mod\ 2$
$\equiv (x_i + s_i) + s_i\ mod\ 2$
$\equiv x_i + 2s_i\ mod\ 2$
$\equiv x_i$

$\implies mod\ 2$ addition & substraction = same operation

### Mod 2 addition

$mod\ 2$ addition is <hl>$\oplus$</hl>

| $x_i$ | $s_i$ | $y_i$ |
|-------|-------|-------|
|0      |0      |0      |
|0      |1      |1      |
|1      |0      |1      |
|1      |1      |0      |

$\implies$ mod 2 addition = XOR operation

- 0 can be encrypted as both 0 & 1
  - can be good if encrypted at <hl>random</hl>
- 1 flips the x & 0 stays the same

### Example of ASCII "A"

> $x_1, x_2, … x_7$ = 10000001

e.g., $s_1, s_2, … s_7$ = 0101101

After mod 2 …
$y_1, y_2, … y_7$ = 1101100
$\implies l$

### Question #2
- generating keystreambits $s_i$
  - related to randomness

## Random nº generators (RNG)
- 3 types
  1. <hl>True</hl> Random Number Generators (TRNG)
      - True random numbers stem from random <hl>physical</hl> processes
      - e.g., coin flipping, lottery, noise (thermal), movement/clicks of mouse, key stroke timing …
      - 'impossible' to recreate
  2. <hl>Pseudo</hl> Random Number Generator (PRNG)
      - computed, i.e., they deterministic
        - not in crypto
        - unless with property …
      - often they = computed w/ the following function:
      $s_0$ = Seed
      $s_{i+1} = f(s_i)$
      - rand( ) in ANSI C
        - fixed seed = 12345
        - $s_{i+1}= 1103515245 s_i + 12345 \bmod 2^{31}$
  3. Cryptographically <hl>Secure</hl> PRNG (CPRNG)
      - PRNGs w/ an additional property:
        - the numbers = <hl>unpredictable</hl>
      - given n output bits
        $s_i, s_{i+1}, …, s_{i+n-1}$
      - computationally infeasible to construct $s_n$
      - full def. see 2.2.1

## One Time Pad (OTP)
- Goal: build a "perfect" cipher  

  > A cipher is "unconditionally secure" (or information theoretically secure) IFF it can not be broken even w/ <hl>infinite</hl> computing resources

- Very easy

  > The One Time Pad (OTP) is a stream cipher where …   
  > 1. the key stream bits $s_i$ stem from a TRNG
  > 1. Each key stream bit is used only once.

- Big drawback
  - key = as long as msg
  - e.g., encr. of 400 MB
    - 8 * 400 MB = 3.2 GB of key

## Linear Congruential Generator (LCG)
- Idea: Use a key stream $s_i$ from a PRNG
- most modern stream ciphers like this

  > $S_0$ = seed
  > $S_{i+1}= A* S_i + B \bmod m\ \ \ A_i, B_i, S_i \in \mathbb{Z}_m$
  > Key $K = (A_i, B)$
  > Rem: $A_i B_i S_i$ are $\lceil log_2(m) \rceil$ bits long

- Attacking
  - Oscar knows $x_1, x_2, x_3$
  1. Oscar computes $S_1, S_2, S_3$
  2. $S_2 \equiv A* S_1 + B\ \bmod m$
     $S_3 \equiv A* S_2 + B\ \bmod m$
  3. $A = (S_2-S_3)(S_1-S2)^{-1} \bmod m$
     $B = (S_2-S_1)(S_1-S2)^{-1} \bmod m$

# Lecture 4
---
- intro to LFSR
- general LFSR
- Attacks

## Intro to Lineair Feedback Shift Registers
- Goal
  - Stream cipher that = small (= low power) in hardware
  - good statistical properties ==> "random"
  - bad cryptographically
    - combine several as building blocks
- E.g.
  - A5/1 cipher in GSM
     - consists of 3 LFSR (1 ≠ secure)

### Atomic element: Flip-flop

> stores 1 Bit

@import "flip-flop.png"
[principle of a flip-flop]

@import "wavedrom.png"

- we want a PRNG now

@import "scheme-3flipflops.png"

> you need an initial value (no zero vector)
> we generate first clock pulse to change 0-output
> compute new input for block 1

@import "3flipflops-complete.png"

- we run through a cycle after 7th clock
  - keystreambits: 0010111
  - <hl>period</hl> of 7


### mathematical description

$s_3 \equiv s_1 + s_0 \bmod 2$
$s_4 \equiv s_2 + s_1 \bmod 2$
$s_{i+3} \equiv s_{i+1} + s_i \bmod 2$

## General LFSRs

> - multiplier acts as a <hl>switch</hl>
>   - $p_i = 1 \implies B = p_i A = A$
>   - $p_i = \emptyset \implies B = p_i A = \emptyset$
> - multiply XOR-gates; multiple flip-flops

@import "general-lfsr.png"

### $s_m$?

$s_m = s_{m-1}p_{m-1}+s_{m-2}p_{m-2} + … + s_0p_0 \bmod 2$
$s_{m+1} = s_{m}p_{m-1}+s_{m-1}p_{m-2} + … + s_2p1+ s_1p_0\ "$

<hl>$s_{m+i} \equiv \displaystyle\sum_{j=0}^{m-1}s_{i+j} p_j \bmod 2$</hl>  $(i = 0,1,2)$

### Theorem

> 1. The maximum period (or sequence length) generated by an LFSR of degree m is $2^m -1$

> 2. Only certain feedback configurations  ($p_{m-1}, …, p_0$) yield maximum length sequences

- **ex 1.**

m = 4, $p_3=p_2=0, p_1=p_0=1$

period = 15

- **ex 2.**

m = 4, $p_3=p_2=p_1=p_0=1$

period = 5

### Notation

- LFSRs are often specified by
$P(x) =x^m +p_{m-1}x^{m-1}+…+p_1x+p_0$
- Only LFSRs w/ "primitive polynomials" yield maximum length sequences

## Attacking LFSRs

- Oscars Goal
  - stream cipher
- given
  - all $y_i$
  - degree m
  - $x_0, … , x_{2m-1}$

### Step 1

$y_i \equiv x_i +s_i \bmod 2$
$s_i \equiv x_i + y_i \bmod 2$
$i=0,1,…, 2m-1$

### Step 2
- recover $s_2m, s_{2m+1}, …$
- Q: $p_{m-1}=?$


  $s_m \equiv s_{m-1}p_{m-1}+…+p_0s_0 \bmod 2$
  $s_{m+1} = s_m p_{m-1} + … + s_1 p_0 "$
  $\vdots$
  $s_{2m-1} \equiv s_{2m-2}p_{m-1}+…+s_{m-1}p_0 "$


- linear equations w/ m unknowns
$\implies$ can easily be solved w/ Gaussian elimination (or matrix inversion)

### Step 3

- using ($p_{m-1}, …, p_0$) "build" LFSR
- compute $s_0, …, s_{2m-1}, s_{2m}, s_{2m+1} …$
- decipher $x_i \equiv y_i + s_i \bmod 2; i = 0,1,2 …$

> If an attacker knows (at least) 2^m output values of an LFSR, he can recover the entire LFSR configuration

# Lecture 5: DES

- DES Intro
- Feistel networks
- DES internals

## 5.1 Data Encryption Standard

- block cipher
  - 8 bytes at 1 time

### Facts

- `1974`: proposed by IBM w/ input from NSA
- `1977 … 1998`: US Standard
- best studied cipher in the world
- unsecure today (key too short)
  - 3DES = very secure
    - encrypt 3 times

### Structure

- 64 bits in 64 bits out & key
  - keysize = 56 bits
- Q: How do we build a block cipher?

### Block cipher

- Shannon: 2 atomic operations
  1. confusion
    - relationship between plain & cipher text = obscured
    - ex.: substitution table (caesar cipher)
  2. Diffusion
    - the influence of each plaintext bit is spread over many ciphertext bit
    - ex.: permutation

  ==> combine confusion & diffusion many times to build a strong block cipher

  <br/>

  > x $\to$ confusion $\to$ diffusion $\to$ confusion $\to$ diffusion $\to$ … $\to$ y "product cipher"

## 5.2 Feistel networks

> Many of today's ciphers are feistel ciphers (but not all!)

- 16 encryption rounds in DES

### Inside encryption round

- split input: 32 & 32
- Right part in f-function with subkey $k_1$ (48 bits)
- output f = XOR-ed with $L_0$
- switch left & right side

> (only) $L_0$ = encrypted using an XOR-operation

@import "feistel-xor-detail.png"

- Q: what's left to do?
  - details
    - f-function
    - transforms

## 5.3 DES internals

### a IP and $IP^{-1}$

- simple bit permutation (not rounds)

> IP: 1 becomes 40; 58 $\to$ 1
> $IP^{-1}$: inverse IP

- Why?
  - table is public, but …
  - it is easier to get data in & out chip (EE)
  - allegedly to slow it down in software

### Details of the f-function

@import "f-function.png"

**E-Box**: provides diffusion
**S-Boxes**: 'heart' of DES & provides confusion
  - use table in slides
  - unusual decoding of the S-box tables
  - take middle 4 bits: columns; remaining: rows
  - ex.: S1(37)= S1(100101) = 1000
**Final permutation**

### Breaking

- differential analysis
  - based on structure S-box

# Lecture 6
---

## Key schedule

> Q: how to compute 16 subkeys $K_1 …\ K_{16}$

[Fig 3.14]

- Key schedule consists of simple operations
- input: 64; output: 56

### PC-1 permutation choice 1

- drops bits 8, 16, 24, …, 64
- Effective key length of DES: 64 - 8 = 56

### L$S_i$

- left shift (really: left rotate)
- specific by nº of bits you shift
  - either 1 position shift, i = 1,2,9,16
  - otherwise 2 position shift

> Note: total # of bit position shifted
> $$
> 4 \cdot 1 + 12 \cdot 2 = 28
> $$
> $\implies c_{16} = c_0\ \&\ D_{16}= D_0$

### PC-2 permuted choice 2

- 8 bits are dropped $\implies$ the remaining 48 input bits = permuted

> Observation: Each key $K_1, \ldots, K_{16}$ is merely a permutation of the original 56 bit key

## DES decrypt

- Reverse IP-1 $\implies$ IP
- Rounds w/ index d
  - First is opposite of $R_{16}^e$
- At the end IP-1

> Q: How do we reverse one round?
> Goal: Show that $R_1^d$ reverses $R_{16}^d$

- To show: $L_1^d = R_{15}^e \land R_1^d = L_{15}^e$
- $L_1^d = R_{15}^e$ (Green line)
- $R_1^d = L_0^d \oplus f(K_i, R_0^d)$
- $R_1^d = L_{15}^e \oplus f(K_16, R_15^e) \oplus f(K_i, R_0^d)$
- $" = L_{15}^e \oplus f(K_{16}, R_{15}^e) \oplus f(K_{16}, R_{15}^e)$
- $= L_{15}^e \oplus (00000000000000000000 … 32\ \text{times}) = L_{15}$

> The remaining round reversals work the same:
>   Round 2d reverses 15e
>   …
>   16d // 1e

## DES security

- 2 families of attack

### a) Analytical attacks

- Differential cryptanalysis: requires $2^{47} (x,y)$ pairs
  - never works in practice
- Linear cryptanalysis: // $2^{43}$ //

### b) Brute-force attacks

- given: $(x_0, y_0) \ \ \ DES^{-1}_{k_i}(y_0) = x_0$
  - $i=0,1, \ldots, 2^{56} - 1$
- Deep Crack: special-purpose DES hardware cracking
- 2007: COPACOBANA: //; $10,000

> DES <hl>can be broken</hl> in a few days

## DES alternatives

|cipher|comment|
|------|-------|
|AES|de facto world standard|
|3DES|still very secure, but lighter|
|AES-Finalists|4 ciphers, all very secure|

# Lecture 7
---
## Motivation-AES

- 128 IO; Key 128/192/256
- all internal operations of AES = based on <hl>finite fields</hl>

## Intro FF (finite fields)

### Terminology

- Finite field = Galois field
- 3 basic algebraic structures
  1. Group
    - set of elements w/ 2 operations
    - + and inverse $\implies$ -
  2. Ring
    - w/ multiplication
  3. Field
    - w/ inverse

> Formal def. of fields: [4.3.2 in textbook]
> Very informally: A field = a set of numbers in which we can add, subtract, multiply and divide.

- EX.: $\R, \mathbb{C}$
- in crypto we almost always need <hl>finite</hl> sets

$\implies$ ff only exist if they have $p^m$ statements
  - p: Prime
  - m $\in \N$

- EX.: there = a ff w/ 11 elements: GF(11)
- // w/ 81 elements: GF(81) = GF($3^4$)
- // w/ 256 //: GF(256) = GF($2^8$) <hl>*(AES field)*</hl>
- There is not a ff w/ 12 elements: $12 = 2^2 \cdot 3$

### Types of ff

1. m = 1
  - prime fields: GF(p)
2. m > 1
  - extension fields: GF($p^m$)
    - remark: especially important in crypto: GF($2^m$)

## Prime Fields Arithmetic

- The elements of a prime field GF(p) = the integers $\{0,1, \ldots, p-1\}$

### Add, subtract & multiply

- let a,b $\in GF(p) = \{0,1, \ldots, p-1\}$
- $a+b \equiv c \bmod p$
- $a-b \equiv d \bmod p$
- $a\cdot b \equiv e \bmod p$

> Note that all conditions of fields are satisfied w/ these computations

### Inversion

- $a \in GF(p)$
- The inverse $a^{-1}$ must satisfy rule nº 4
- $a \cdot a^{-1} \equiv 1 \bmod p$
  - $a^{-1}$ can be computed with the extended Euclidean algorithm

## Extension fields GF($2^m$) Arithmetic

### Element representation

- The elements of GF($2^m$) = polynomials

$a_{m-1}x^{m-1} + \ldots + a_1x + a_0 = A(x) \in GF(2^m)$

$a_i \in GF(2) = \{0,1\}$

- Ex.: GF($2^3$) = GF(8)

$A(x) = a_2x^2 + a_1x + a_0 = (a_2, a_1, a_0)$
$GF(2^3) = \{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1 \}$

> Q: How to compute w/ three elements?

### Addition & subtraction in GF($2^m$)

- See definition [4.3.3]

$\implies$ use regular polynomial addition/subtraction, where the coefficients = computed in GF(2)

- Ex.: GF($2^3$)
  $A(x) = x^2 + x + 1$
  $B(x) = x^2 +1$

  $A + B = (1 + 1)x^2 + x + (1+1)$
    $= 0x^2 + x + 0$
    $= x$

- Note: Addition & subtraction in GF($2^m$) = the same operations

### Multiplication in GF($2^m$)

- Intuition: Just do regular polynomial mult.
- Ex.: GF($2^3$)
  $A\cdot B = (x^2+x+1)(x^2+1)$
    $= x^4 + x^3 +x^2 + x^2+x+1$
    $= x^4+x^3+x+1 = C'(x)$ (not in the field)

  - Solution: Reduce C'(x) modulo a polynomial that "behaves like a prime". These = called <hl>irreducible polynomials</hl>
  - Recall prime fields
    - Ex.: GF(7) = $\{0,1,\ldots,6\}$
      - $3\cdot 4 = 12 \equiv 5 \bmod 7$
- Irr. poly. for GF($2^3$)
  - $p(x) = x^3+x+1$
  - $(x^4 + x^3 + x + 1):(x^3+x+1) = x + 1$
  - Remainder: $x^2 + x \equiv A \cdot B \bmod p(x)$
- For every field GF($2^m$) there = several irr. polynomials.
  - Ex.: $p(x) = x^3+x^2+1$
  - The "AES irr. polynomial": <hl>$p(x)=x^8+x^4+x^3+x+1$</hl>

### Inversion in GF($2^m$)

- Again, the inverse $A^{-1}(x)$ of an elt. $A(x) \in GF(2^m)$ must satisfy
  $A(X) \cdot A^{-1}(x) \equiv 1 \bmod p(x)$
              extended Euclidean algorithm

# Lecture 8
---
## Intro to AES

## Structure of AES

## AES internals

## Decryption