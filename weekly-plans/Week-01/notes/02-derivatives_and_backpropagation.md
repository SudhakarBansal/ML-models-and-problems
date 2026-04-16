# Derivatives & Backpropagation
## (Week 1, Day 3 — April 16, 2026)

---

## What Is a Derivative?

The derivative of a function at a point tells you the **rate of change** of the output $y$ with respect to a tiny nudge in the input $x$.

$$f'(x) = \frac{dy}{dx} = \text{how much } y \text{ changes per tiny change in } x$$

**Example**: If $f(x) = x^2$ and $f'(3) = 6$, that means: nudge $x$ from 3 to 3.001 (a nudge of 0.001), and the output changes by roughly $6 \times 0.001 = 0.006$.

### The Geometric Intuition (3B1B)

If you zoom into a curve far enough, it looks like a straight line. The derivative is the **slope of that line** — the slope of the tangent at that point.

You can visualize it as a tiny triangle: the horizontal side is the nudge in $x$ ($dx$), the vertical side is the resulting change in $y$ ($dy$), and the hypotenuse is the tangent line. The slope $\frac{dy}{dx}$ is the derivative.

---

## Why Derivatives Matter for ML

In gradient descent:
- $x$ is your weight $\theta$
- $y$ is your cost $J(\theta)$

The derivative $\frac{\partial J}{\partial \theta}$ tells you: **if I nudge $\theta$ slightly, how does the cost change?**
- Derivative is positive → cost is increasing → move $\theta$ the other way
- Derivative is negative → cost is decreasing → keep going that direction

That's all gradient descent does — nudge weights in the direction that reduces cost, scaled by the learning rate.

---

## The Chain Rule & Backpropagation

### The Problem
In a neural network, a weight in layer 1 doesn't directly touch the cost function. The signal passes through multiple layers:

$$w_1 \rightarrow z_1 \rightarrow a_1 \rightarrow z_2 \rightarrow a_2 \rightarrow J$$

How do you know how much $w_1$ affects $J$?

### The Chain Rule
Multiply the local rate of change at each step along the path:

$$\frac{\partial J}{\partial w_1} = \frac{\partial J}{\partial a_2} \cdot \frac{\partial a_2}{\partial z_2} \cdot \frac{\partial z_2}{\partial a_1} \cdot \frac{\partial a_1}{\partial z_1} \cdot \frac{\partial z_1}{\partial w_1}$$

Each fraction asks: **"how much does this thing change when I nudge the thing before it?"**

### Backpropagation
Backpropagation is just the chain rule computed efficiently — from right to left (output → input), reusing the derivatives you've already calculated at each layer instead of recomputing them.

### One-Sentence Summary
**The chain rule lets us figure out how much a weight deep in the network affects the final cost, by multiplying the local rates of change at each step along the path from that weight to the output.**

---

## Key Distinctions

| Concept | What it does |
|---------|-------------|
| Derivative | Tells you the rate of change — how much output changes per input nudge |
| Gradient | Vector of all partial derivatives — points in the direction of steepest ascent |
| Gradient Descent | Move weights in the *opposite* direction of the gradient to reduce cost |
| Chain Rule | Multiplies local derivatives to get the total effect of a deep weight on the cost |
| Backpropagation | Efficient algorithm to compute chain rule derivatives from output to input |

---

## Resources Watched
- 3B1B Essence of Calculus — Ep 1 (watched 3x for deep understanding)
- 3B1B Neural Networks — [Ch 2: Gradient Descent](https://www.youtube.com/watch?v=IHZwWFHWa-w)
- 3B1B Neural Networks — [Ch 3: Backpropagation](https://www.youtube.com/watch?v=Ilg3gGewQ5U)
