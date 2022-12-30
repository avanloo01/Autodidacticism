# Fourier series: p1 & p2

$f(x) = \frac{A_0}{2} + \sum_{k=1}^\infty (A_k \cos(\frac{2\pi kx}{L}) + B_k\sin(\frac{2\pi kx}{L}))$

$A_k = 2/L \int_{0}^L f(x)\cos(\frac{2\pi kx}{L})dx$
$B_k = 2/L \int_{0}^L f(x)\sin(\frac{2\pi kx}{L})dx$

- Basically the same as a vector <hl>projected on orthogonal basis</hl>

# Complex Fourier series

> $e^{ikx} = \cos(kx) + i\sin(kx)$

<br/>

$f(x) =  \sum_{k=-\infty}^\infty (c_k e^{ikx})$
$(c_k = \bar{c}_{-k} \iff f(x) \in \R)$
$\psi_k = e^{\frac{ikx\pi}{L}}$
# The Fourier Transform
- infinite domain
- not periodic anymore
  - "hat function" from (-)L to (-)infinity
  - f decays to 0 w/ approaching infinity

$\omega_l=\frac{k\pi}{L} = k  \Delta \omega$
$\implies \Delta \omega = \frac{\pi}{L}$
<br/>
$f(x) = \lim_{\Delta \omega \to 2} \sum_{k=-\infty}^{\infty} \frac{\Delta \omega}{2\pi} \int_{-\pi/\Delta \omega}^{\pi/\Delta \omega}f(\xi)e^{-ik\Delta \omega \xi}d\xi e^{ik\Delta \omega x}$

$f(x) = \int_{-\infty}^{\infty} \frac{1}{2\pi} \int_{-\infty}^{\infty}f(\xi)e^{-ik\omega \xi}\ d\xi\ e^{ik\omega x} d\omega$

<br/>

$\implies \hat{f}(\omega)= \digamma(f(x)) = \int_{-\infty}^{\infty}f(x)e^{i\omega x}dx$

- rest of previous function is inverse transform

# Fourier transform & derivatives

$\digamma(\frac{d}{dx}f(x)) = \int_{-\infty}^{\infty}\frac{df}{dx}e^{-i\omega x}dx$ (nu met partiele)
$= i\omega \digamma(f(x))$

- turn partial differential equations to ordinary ones
- $u_{tt} = c u_{xx} \implies \hat{u}_{tt} = -\omega^2 \hat{u}$

# Fourier transform & Convolution integrals

$(f * g) = \int_{-\infty}^{\infty}f(x-\xi)g(\xi)d\xi$

<br/>

$\implies \digamma(f*g) = \digamma(f)\digamma(g) = \hat{f} \hat{g}$

$\digamma^{-1}(\hat{f}\hat{g})(x)= \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{f}(\omega)\hat{g}(\omega)e^{i\omega x}d\omega$

> Replace $\hat{g}$ w/ Fourier def. & dummy variable $y$

$\implies \frac{1}{2\pi}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\hat{f}(\omega)g(y)e^{i\omega(x-y)}d\omega dy$
$\iff \frac{1}{2\pi}\int_{-\infty}^{\infty}g(y)\int_{-\infty}^{\infty}\hat{f}(\omega)e^{i\omega(x-y)}d\omega dy$
$\iff \int_{\infty}^{\infty}g(y)f(x-y)dy$

- use in heat equation

# Parseval's Theorem

$\digamma(\alpha f(x)+ \beta g(x)) = \alpha \digamma(f) + \beta \digamma(g) \implies \text{lineair operation}$

$\int_{-\infty}^{\infty}|\hat{f}(\omega)|d\omega = 2\pi \int_{-\infty}^{\infty}|f(x)|^2dx$

- we can ignore small fourier coefficients, but still do a good approximation

# Heat equation

$u_t = \alpha ^ 2 u_{xx}$

$\digamma(u(x,t)) = \hat{u}(\omega, t)$
$\digamma(u_x) = i\omega \hat{u}$
$\digamma(u_{xx} = -\omega^2\hat{u}(\omega, t)$

$u_t = \alpha ^ 2 u_{xx}$
$\implies \frac{d}{dt}\hat{u} = -\omega^2\hat{u}$
$\iff \hat{u}(\omega, t) = e^{-\omega^2 \alpha^2 t}\hat{u}(\omega, t_0)$
$\implies u(x,t) =\digamma^{-1}(\hat{u}(\omega, t)) = \digamma^{-1}(e^{-\omega^2 \alpha^2 t})*u(x, t_0)$

# Discrete fourier transform (DFT)

- to compute in computers
- actually a <hl>fourier series</hl> (finite period)
- leads to fast fourier transform (FFT)

$$
\begin{bmatrix}\hat{f}_0 \\ \hat{f}_1 \\ \hat{f}_2 \\ … \\ \hat{f}_n\end{bmatrix} =
\begin{bmatrix} 1 & 1 & 1 & … & 1\\
1 & \omega_n & \omega_n^2  & … & \omega_n^{n-1} \\
1 & \omega_n ^ 2 & \omega_n^4 & … & \omega_n^{2(n-1)} \\
… & … & … & … & … \\ 1 & \omega_n^{n-1} & \omega_n^{2(n-1)} & … & \omega_n^{(n-1)^2}
\end{bmatrix}
\begin{bmatrix}f_0 \\ f_1 \\ f_2 \\ … \\ f_n\end{bmatrix}
$$

## DFT

$\hat{f}_k = \displaystyle\sum_{j=0}^{n-1}f_je^{-i2\pi jk/n}$
$f_k = \frac{1}{n}\sum_{j=0}^{n-1}\hat{f}_je^{j2\pi jk/n}$

$\omega_n = e^{-2\pi i/n}$

# FFT
- <hl>computing DFT</hl> in a fast way
  - image, audio, satellite TV compression

## Need
- <hl>speed</hl>
  - O(n^2) ==> slow computation
  - FFT O(n log(n))
  - n = 44 * 10^5 for 10 secs audio
    - DFT = 10^11
    - FFT = 10^6
- Derivative approximation
  - PDEs
- Denoise data
- Data analysis
- compression
  - audio & images

## How
Case: n = 2^10 = 1024

$$\hat{f} = \digamma_{1024} f =
\begin{bmatrix}I_{512} & -D_{512} \\ I_{512} & -D_{512}\end{bmatrix}
\begin{bmatrix}\digamma_{512} & 0 \\ 0 & \digamma_{512}\end{bmatrix}
\begin{bmatrix}f_{even} \\ f_{odd}\end{bmatrix}$$

$D_{512} = \begin{bmatrix}1 & 0 \\0 & \omega & 0 \\ 0 & 0 & \omega^2 & 0 \\ 0 & 0 & 0 & … & 0 \\0 & 0 & 0 & 0 & \omega_{512} \end{bmatrix}$

<br/>

> we can do same trick w/ $\digamma_{512}$ cuz those are DFTS

# Gabor transform $\implies$ Spectograms

- use a Gausian window and slide over 'recording' i.f.o. time
  - 'weighted' fourier transform
- used in Shazam
  - matches peaks in spectogram

$G(f) = \hat{f}_g(t,\omega) = \int_{-\infty}^{\infty}f(\tau)e^{-i\omega \tau}g(t- \tau)d\tau$

# Uncertainty principles

- <hl>trade-off</hl> based on time/frequency ~ Heisenberg uncertainty

$(\int_{-\infty}^{\infty}x^2|f(x)|^2dx)(\int_{-\infty}^{\infty}\omega^2f(\omega)^2d\omega) \geqslant	\frac{1}{16\pi^2}$

- spectogram is balance between previous two

# Wavelets & multiresolution analysis

- <hl>supercharged</hl> Fourier transform
- image & audio compression
- time of spectogram
- for higher frequencies <hl>more & more temporal data</hl> $\implies$ hiearchical
  - lower frequencies don't require as much temporal data

## Principle
- mother wavelet $\psi_t$
- $\psi_{a,b}(t) = \frac{1}{\sqrt{a}}\psi(\frac{t-b}{a})$
- $W_\psi(f)(a,b) =\ <f(t), \psi_{a,b}(t)>$

## Example
- Haar wavelet 1910
  - 1 if x<0; -1 if x>0 $\psi_{(1,0)}$
  - +1 to -1 in left half $\psi_{(1/2,0)}$
  - -1 to +1 in right half $\psi_{(1/2,1/2)}$
- others
  - doubachie
  - Mexican hat
  - coiflet

# Image Compression & the FFT2
- most <hl>useful</hl> application

> FFT2
> FFT every row , then, FFT on columns (or vice versa)
> result = plus with weird flowr cos(ky)sin(jy)

## Compression

- 1MP $\digamma \implies$ Fourier (1m) $\implies$ threshold
- keep only 100 of largest Fourier coefficients
- $\implies$ IFFT, but very few loss of picture (Parseval's Theorem)
$\implies JPG$

# Laplace transform: generalized Fourier transform

- culmination of Fourier
  - PDE $\to$ ODE
  - PD to algebraic
  - control theory
- weighted one-sided Fourier tranform
- examples
  - heavy
    - 0 if x < 0
    - 1 if x>=0
- solution
  - multiply $f(t)$ by $e^{-\gamma t}H(t)$
  - $f(t) e^{-\gamma t} \to 0$ as $t \to \infty$
  - $\digamma(t) = f(t)e^{-\gamma t}H(t)$ 0 if t<0; $f(t)e^{-\gamma t} if t>=0$
  $\hat{\digamma}(\digamma) = \int_{-\infty}^{\infty}\digamma(t)e^{-i\omega t}dt = \int_0^{\infty}f(t)e^{-\gamma t} e^{-i \omega t}dt$
  $= \int_0^{\infty}f(t) e^{-(\gamma+i\omega)t}dt$
  $= \int_0^{\infty}f(t) e^{-st}dt = \bar{f}(s)$


## inverse
$\digamma(t)=\frac{1}{2\pi}
\int_{-\infty}^{\infty}\hat{\digamma}(\omega)e^{i\omega t}d\omega$
$e^{\gamma t}\digamma(t)=e^{\gamma t}\frac{1}{2\pi}
\int_{-\infty}^{\infty}\hat{\digamma}(\omega)e^{i\omega t}d\omega$
$=f(t)$
$= \frac{1}{2\pi}\int_{-\infty}^{\infty}\bar{f}(s)e^{(\gamma + i\omega)t}d\omega$
$= \frac{1}{2i\pi}\int_{\gamma-i\infty}^{\gamma +i\infty}\bar{f}(s)e^{st}ds$


## Pair
$\bar{f}(s) = \int_0^{\infty}f(t) e^{-st}dt$
$f(t) = \frac{1}{2i\pi}\int_{\gamma-i\infty}^{\gamma +i\infty}\bar{f}(s)e^{st}ds$

# Laplace transform on differential equations

$\"{x}+\frac{c}{m}\dot{x}+ \frac{k}{m}x=0$
$\ddot{x}+5\dot{x}+4x=0$

$x(0)=2$
$\dot{x}(0)=-5$

$L \implies s^2 \bar{x}-sx(0) -\dot{x}(0) + 5(s\bar{x}-x(0))+4\bar{x} = 0$
$\implies (s^2+5s+4)\bar{x}(s)= 2s-5+10 = 2s+5$
$\bar{x}(s)=\frac{2s+5}{s^2+5s+4} = \frac{2s+5}{(s+4)(s+1)}$
$=\frac{1}{s+4}+\frac{1}{s+1}$

$\implies x(t)= e^{-4t}+e^{-t}$

## Forcing
$\ddot{x}+5\dot{x}+4x=u(t)$

$L \implies s^2 \bar{x}-sx(0) -\dot{x}(0) + 5(s\bar{x}-x(0))+4\bar{x} = \bar{u}(t)$
$\implies (s^2+5s+4)\bar{x}(s)= 2s+5 +\bar{u}$

$\bar{x}(s)=\frac{2s+5}{s^2+5s+4} + \frac{\bar{u}}{s^2+5s+4}$

# Laplace transform examples

- $L\{f\}=\bar{f}(s)$
- $L\{\frac{df}{dt}\}=\int_{0}{\infty}\frac{df}{dt}e^{-st}dt$
$= [e^{-st}f(t)]_0^{\infty}+s\int_0^{\infty}f(t)e^{-st}dt$
$= -f(0) + s\bar{f}(s)$

- $L\{f(t)*g(t)\} = L\{f(t)\}L\{g(t)\} = \bar{f}(t)\bar{g}(t)$