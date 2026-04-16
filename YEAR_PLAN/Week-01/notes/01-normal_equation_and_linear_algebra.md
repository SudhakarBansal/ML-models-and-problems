# Normal Equation & Linear Algebra Connections
---

## Normal Equation — What It Actually Does

The Normal Equation is an **analytical** (closed-form) solution to linear regression. Unlike gradient descent, it doesn't iterate or initialize weights — it solves for the optimal weights in one shot.

**Formula**:

$$\theta = (X^T X)^{-1} X^T y$$

- $X$ is $(m \times n)$ — $m$ samples, $n$ features
- $X^T X$ gives an $(n \times n)$ matrix (NOT $X X^T$, which gives $m \times m$ — wrong dimensions)
- The result $\theta$ is an $(n \times 1)$ vector of weights

**Where the formula comes from**: It's the result of taking the derivative of the cost function $J(\theta)$, setting it to zero, and solving for $\theta$ algebraically:

$$\frac{\partial J(\theta)}{\partial \theta} = 0 \quad \Rightarrow \quad \theta = (X^T X)^{-1} X^T y$$

The calculus was done once to derive the formula — at runtime, you just plug in $X$ and $y$. No derivatives are computed during execution.

**Key distinction**: Gradient descent *uses* derivatives repeatedly at runtime. The Normal Equation *was derived using* derivatives but doesn't compute them at runtime. That's why it's one-shot.

**When to use**: Works well when number of features $n < \sim10{,}000$. Beyond that, gradient descent is more efficient because inverting the $(n \times n)$ matrix becomes expensive.

**No feature scaling needed**: Unlike gradient descent, the Normal Equation doesn't need feature scaling. GD needs scaling because unscaled features create elongated contours — the gradient bounces along the narrow direction instead of heading straight to the minimum, requiring many more iterations. The Normal Equation has no iterations, no step size, no convergence path — the algebra gives the same answer regardless of feature scale.

---

## Connecting 3Blue1Brown to Linear Regression

### Feature columns are vectors
Each column of $X$ (e.g., sq_ft, num_bedrooms, house_age) is a **vector** with $m$ entries — one per house.

### Weights are scalars in a linear combination

$$\hat{y} = \theta_1 \cdot \text{sq\_ft} + \theta_2 \cdot \text{num\_bedrooms} + \theta_3 \cdot \text{house\_age}$$

This is a **linear combination** of the feature column vectors. The weights $(\theta)$ are the scalars.

### The span limits what you can predict
The span of the feature columns is all possible vectors reachable by their linear combinations. With $n$ feature columns in $m$-dimensional space $(m \gg n)$, the span is only an $n$-dimensional subspace — a tiny slice of the full space.

The target vector $y$ (actual prices) almost certainly does NOT live in this subspace.

### Linear regression = projection
Linear regression finds the **closest point in the feature subspace to $y$**. That closest point is $\hat{y}$ (predictions). The gap between $y$ and $\hat{y}$ is the residual.

- More features = larger span = subspace gets closer to $y$ = lower error
- But too many features = subspace shaped to match noise = overfitting

---

## Ridge Regularization — Why $\alpha I$ Shrinks Weights (Task 4)

### Normal Equation vs Ridge

| | Formula | What it does |
|---|---------|-------------|
| Normal | $\theta = (X^T X)^{-1} X^T y$ | Finds exact best-fit weights |
| Ridge  | $\theta = (X^T X + \alpha I)^{-1} X^T y$ | Finds best-fit weights with a shrinkage penalty |

### The Mechanics — A Clean Example

**Setup**: 5 data points, 2 features. True relationship is $y = x_1 + x_2$ (perfect, no noise).

$$X = \begin{bmatrix} 1 & 2 \\ 2 & 3 \\ 3 & 4 \\ 4 & 5 \\ 5 & 6 \end{bmatrix}, \quad y = \begin{bmatrix} 3 \\ 5 \\ 7 \\ 9 \\ 11 \end{bmatrix}$$

**Step 1** — Compute $X^T X$:

$$X^T X = \begin{bmatrix} 55 & 70 \\ 70 & 90 \end{bmatrix}$$

**Step 2** — Add $\alpha I$ and compare:

| $\alpha$ | $X^T X + \alpha I$ | Resulting $\theta$ | Fit quality |
|----------|-------------------|-------------------|-------------|
| 0 | $\begin{bmatrix} 55 & 70 \\ 70 & 90 \end{bmatrix}$ | $[1.0, \ 1.0]$ — perfect | Exact fit |
| 1 | $\begin{bmatrix} 56 & 70 \\ 70 & 91 \end{bmatrix}$ | $[0.89, \ 1.07]$ — slight shrinkage | Very close |
| 10 | $\begin{bmatrix} 65 & 70 \\ 70 & 100 \end{bmatrix}$ | $[0.81, \ 1.03]$ — noticeable shrinkage | Mild underfit |
| 100 | $\begin{bmatrix} 155 & 70 \\ 70 & 190 \end{bmatrix}$ | $[0.51, \ 0.65]$ — heavy shrinkage | Significant underfit |

### Why Does This Happen?

For a $2 \times 2$ matrix $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$, the inverse is:

$$A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

Adding $\alpha$ to the diagonal makes $a$ and $d$ bigger $\rightarrow$ $(ad - bc)$ grows $\rightarrow$ $\frac{1}{ad - bc}$ shrinks $\rightarrow$ the entire inverse matrix gets smaller $\rightarrow$ weights get smaller.

In short: **bigger denominator before inverting = smaller values after inverting = smaller weights.**

### Why Would You Want Smaller Weights?

- Large weights = model overreacts to small feature changes = overfitting (learning noise)
- One large weight can dominate the entire prediction, making the model fragile
- Ridge forces the model to find a solution that fits the data AND keeps weights small

### When Ridge Hurts

In the example above, the true relationship IS $y = x_1 + x_2$. The weights $[1.0, 1.0]$ are perfect — there's no noise to overfit. Adding regularization here only introduces **bias** (underfitting). Ridge doesn't know if the weights are "too big" or "just right" — it shrinks them regardless.

### The Bias-Variance Tradeoff in One Knob

- $\alpha = 0$: Zero bias, perfect fit, but vulnerable to noise in real data
- $\alpha$ = small: Slight bias, weights slightly constrained, more stable across noisy datasets
- $\alpha$ = large: High bias, underfits, very stable but misses true patterns

**$\alpha$ controls where you sit on the bias-variance tradeoff.** In the house price project, Ridge with $\alpha = 1000$ worked well because polynomial features created many large weights that needed taming.

### Interview Answer — 3 Levels Deep

1. **What**: Ridge adds a penalty to prevent overfitting by shrinking weights
2. **How**: Adding $\alpha I$ to $X^T X$ before inverting makes the inverse smaller, which mechanically shrinks all weights
3. **Tradeoff**: On clean data it underfits (introduces bias). On noisy/overparameterized data it prevents overfitting. $\alpha$ is the knob.

---

## Summary
Linear regression is not just "fitting a line." Geometrically, it's **projecting a target vector onto the subspace spanned by feature columns**, and finding the scalars (weights) that produce that projection.

---

## Lab Reference
- **Hands-on notebook**: [01-Normal Equation vs Ridge Regularization.ipynb](../labs/01-Normal%20Equation%20vs%20Ridge%20Regularization.ipynb)
