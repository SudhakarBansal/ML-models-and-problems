# Linear Transformations, Backprop Deep Dive & Computation Graphs
## (Week 1, Day 5 — April 17, 2026)

---

## Linear Transformations — What a Matrix Actually Is

A **linear transformation** is a function that takes a vector and returns a vector, subject to two rules:

1. **Origin stays fixed** — the zero vector maps to the zero vector
2. **Grid lines stay straight and evenly spaced** — no curving, no warping

If both hold, the transformation is linear, and it can always be represented by a matrix.

### The Key Mental Model (3B1B LA Ep 3)

> **The columns of a matrix tell you where the basis vectors land after the transformation.**

Originally $\hat{i} = [1, 0]$ and $\hat{j} = [0, 1]$. Apply matrix $W$, and those basis vectors move somewhere new. Where they land *is* what the columns of $W$ store.

**Example**:

$$W = \begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix}$$

- $\hat{i} = [1, 0]$ lands at $[2, 0]$ — the **first column**
- $\hat{j} = [0, 1]$ lands at $[1, 3]$ — the **second column**

That's the whole idea. A matrix is a "basis vector destination map."

---

## Matrix-Vector Multiplication — The 3B1B Way

Forget the row-dot-product rule. There's a cleaner mental picture:

> **$W \cdot [a, b]$ = $a$ copies of column 1, plus $b$ copies of column 2.**

The input vector's components are **scaling factors** for the columns.

**Example**: Compute $W \cdot [2, 1]$ using $W$ from above.

$$W \cdot \begin{bmatrix} 2 \\ 1 \end{bmatrix} = 2 \cdot \begin{bmatrix} 2 \\ 0 \end{bmatrix} + 1 \cdot \begin{bmatrix} 1 \\ 3 \end{bmatrix} = \begin{bmatrix} 4 \\ 0 \end{bmatrix} + \begin{bmatrix} 1 \\ 3 \end{bmatrix} = \begin{bmatrix} 5 \\ 3 \end{bmatrix}$$

### Why this view is better
- It directly connects to the "span" and "linear combination" ideas from LA Ep 2
- It reveals *why* matrix multiplication is just function composition (next section)
- The old row-dot-product rule is just this same calculation written differently

### Beware the common slip
A "horizontal stretch by $k$" only touches $x$: $(x, y) \rightarrow (k \cdot x, y)$. It does NOT scale $y$. Same for "vertical stretch by $k$" — only $y$ moves. If both move, that's a **uniform scale**, which is a different transformation.

---

## Why Matrix Multiplication Is Not Commutative

$A \cdot B$ means: **"apply transformation $B$ first, then apply $A$."** Two transformations in sequence.

Order matters because the result of the first transformation feeds into the second — and that result changes depending on which goes first.

### Concrete Proof
Start with the unit square: $(0,0), (1,0), (1,1), (0,1)$.

| | Scenario 1: rotate then stretch | Scenario 2: stretch then rotate |
|---|---|---|
| Rotate 90° CW: $(x,y) \rightarrow (y, -x)$ | First | Second |
| Stretch 2x horiz: $(x,y) \rightarrow (2x, y)$ | Second | First |
| Final corners | $(0,0), (0,-1), (2,-1), (2,0)$ | $(0,0), (0,-2), (1,-2), (1,0)$ |
| Shape | 2 wide × 1 tall rectangle | 1 wide × 2 tall rectangle |

Different shapes → $A \cdot B \neq B \cdot A$. Not an algebraic quirk — a geometric fact about composing transformations.

---

## Chain Rule Deep Dive — The "Wiggle Propagation" View

For $L = f(g(h(x)))$:

$$\frac{dL}{dx} = \frac{df}{dg} \cdot \frac{dg}{dh} \cdot \frac{dh}{dx}$$

### Why multiplication and not addition?
Because sensitivities **compose by scaling**, not by parallel contribution.

**Mental picture**: nudge $x$ by tiny $\varepsilon$.
- $h$ wiggles by $\frac{dh}{dx} \cdot \varepsilon$
- That wiggle feeds into $g$, so $g$ wiggles by $\frac{dg}{dh} \cdot \frac{dh}{dx} \cdot \varepsilon$
- Then $f$ wiggles by $\frac{df}{dg} \cdot \frac{dg}{dh} \cdot \frac{dh}{dx} \cdot \varepsilon$

Each stage **scales** the incoming wiggle. The total effect is the product of the scalings. **Multiplication, not addition, because it's a chain, not parallel tracks.**

---

## Backprop Revisited — The Structure of $dL/dW$

For a 2-layer NN:

$$z_1 = W_1 \cdot x, \quad a_1 = \sigma(z_1), \quad z_2 = W_2 \cdot a_1, \quad L = \text{loss}(z_2, y)$$

### The gradient w.r.t. $W_1$:

$$\frac{dL}{dW_1} = \underbrace{\frac{dL}{dz_2} \cdot \frac{dz_2}{da_1} \cdot \frac{da_1}{dz_1}}_{\text{error signal (from output, walking backward)}} \cdot \underbrace{\frac{dz_1}{dW_1}}_{\text{local input}}$$

### The crucial observation
Since $z_1 = W_1 \cdot x$, the local factor is:

$$\frac{dz_1}{dW_1} = x$$

**Every weight's gradient = (error signal from later layers) × (the input that layer saw).**

For $W_2$, the local factor is $a_1$ (activation from previous layer). Same pattern.

### Why frameworks cache activations
During the forward pass, PyTorch / TensorFlow / JAX save every layer's activations. Not for optimization — it's **structural**. The backward pass literally needs them because every weight's gradient has one factor that equals the layer's input.

> **Gradient at a weight = error signal × local input. Cache the inputs on the way forward, or you can't compute gradients on the way back.**

### What flows backward during backprop?
Not weights. Not activations. The **gradient of the loss with respect to each layer's output**:

$$\frac{dL}{dz_2} \rightarrow \frac{dL}{da_1} \rightarrow \frac{dL}{dz_1} \rightarrow \frac{dL}{dW_1}$$

Each step multiplies the previous gradient by one local derivative. That's why it's called back**propagation** — you're propagating gradient signals from the output back toward the inputs.

---

## Computation Graphs — The Visual Version

A **computation graph** draws out every operation as a node and every data flow as an arrow.

For the 2-layer NN:

```
x ──→ [·W1] ──→ z1 ──→ [σ] ──→ a1 ──→ [·W2] ──→ z2 ──→ [loss] ──→ L
```

Each box is one function. The arrow direction is the forward pass.

### Forward vs Backward Pass

| Pass | Direction | What's computed |
|------|-----------|-----------------|
| Forward | Left → Right | Evaluate each node, produce the next value, end at $L$ |
| Backward | Right → Left | Start with $dL/dL = 1$, multiply by each node's local derivative, end at $dL/dW_1$ |

At each node during the backward pass, you only need:
1. The **local derivative** of that box ($d(\text{output})/d(\text{input})$)
2. The **gradient flowing in from the right** (from the next node's backward computation)

Multiply these two — you now have the gradient at this node's input. Pass it to the next node on the left. Repeat.

**Chain rule, executed node by node.**

---

## The Big Unification

Chain rule, linear transformations, and computation graphs all describe **the same underlying idea**:

> **Neural networks are compositions of functions.**

| Topic | Role in the composition |
|-------|------------------------|
| Linear transformation (matrix) | One common type of function in the composition (a layer's linear part) |
| Chain rule | The mathematical rule for differentiating a composition |
| Computation graph | The visual picture of the composition |
| Backpropagation | The algorithm that walks the graph backward applying the chain rule |

Once the "everything is function composition" frame clicks, deep learning stops feeling like magic. The forward pass evaluates the composition. The backward pass differentiates it. Matrices are just one common form those functions take. Computation graphs are just the composition drawn on paper.

---

## Key Takeaways (Re-read First)

1. **Matrix = where basis vectors land.** Columns are their landing spots.
2. **Matrix-vector multiply = linear combination of columns**, with input components as scalars.
3. **Matrix multiplication is non-commutative** because it's transformation composition, and order matters.
4. **Chain rule multiplies because wiggles scale stage-by-stage** through nested functions.
5. **Gradient at a weight = error signal × local input.** This is why activations are cached during the forward pass.
6. **Backprop = chain rule walked node-by-node across a computation graph.**
7. **Everything is function composition** — the rest is bookkeeping.

---

## Resources Watched
- 3B1B Essence of Linear Algebra — [Ep 3: Linear transformations and matrices](https://www.youtube.com/watch?v=kYB8IZa5AuE)
- 3B1B Essence of Calculus — [Ep 3: Power rule, chain rule intro](https://www.youtube.com/watch?v=S0_qX4VJhMQ)
- Andrew Ng DLS Course 2 Week 2 — backprop + computation graph lectures (finished)
