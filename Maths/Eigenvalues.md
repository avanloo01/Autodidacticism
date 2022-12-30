# Intro to Eigenvalues & Eigenvectors
T: $\R^m\ \to \R^n$
$T(\nabla) = \lambda \nabla$

$\nabla$: eigenvector for T
$\lambda$: eigenwaarde verbonden met $\nabla$

## Example 1
$\overrightarrow{\rm v} = \begin{bmatrix} 1 \\ 2\end{bmatrix}$

> Flips vector over the line

$T(\overrightarrow{\rm v_1}) = 1 * \overrightarrow{\rm v_1}$

$\implies \lambda = 1$

## Example 2

$\overrightarrow{\rm v_2} = \begin{bmatrix}2 \\ -1 \end{bmatrix}$

$T \implies \lambda = -1$

## Use
- Interesting basis-vectors
  - easier computations
  - better coordinate systems

# Example eigenvalue of a 2x2-matrix

$A = \begin{bmatrix} 1 & 2 \\ 4 & 3\end{bmatrix}$

$\lambda\ \text{is an eigenvalue of A} \iff det(\lambda I_n\ - A) = 0$

(prev. video)

$\implies \begin{vmatrix}\lambda - 1 & -2 \\ -4 & \lambda -3\end{vmatrix} = 0$

$\iff (\lambda - 1)(\lambda - 3) - 8 = 0$

$\iff \lambda^2 - 4\lambda - 5 = 0$ (<hl>characteristic</hl> polynomial)

# Eigenvector of same 2x2-matrix

Eigenspace $E_\lambda = N(\lambda I_n - A)$

$E_5 = N(\begin{bmatrix}4 & -2 \\ -4 & 2\end{bmatrix})$

$\implies rref(\begin{bmatrix}4 & -2\\ -4 & 2\end{bmatrix}) = \begin{bmatrix} 1 & -1/2 \\ 0 & 0\end{bmatrix}$

$E_5 = \{\begin{bmatrix}v_1 \\ v_2 \end{bmatrix} = t \begin{bmatrix}1/2 \\ 1 \end{bmatrix}, t \in \R \}$
$E_5 = span(\begin{bmatrix}1/2 \\ 1 \end{bmatrix})$

<br/>

> Same method for $E_2$

$\implies E_2 = \text{span}(\begin{bmatrix}1 \\ -1 \end{bmatrix})$

# Eigenvalues for a 3x3-matrix

$$
A = \begin{bmatrix} -1 & 2 & 2 \\ 2 & 2 & -1 \\ 2 & -1 & 2 \end{bmatrix} \\$$

<hl>$det(\lambda I_n - A) = 0$</hl>
$\iff \lambda^3-3\lambda^2-9\lambda + 27 = 0$
$\iff \lambda^2(\lambda-3)-9(\lambda -3) = 0$
$\iff (\lambda+3)(\lambda -3)^2 = 0$

# Eigenvectors //

$\begin{bmatrix} 4 & -2 & -2 \\ -2 & 1 & 1 \\ -2 & 1 & 1 \end{bmatrix}*\overrightarrow{v}= \overrightarrow{0}$

$E_3 = \{a\begin{bmatrix} -1/2 \\ 1\\ 0\end{bmatrix} + b\begin{bmatrix} 1/2 \\ 1\\ 0\end{bmatrix} | a,b \in \R \}$ 
