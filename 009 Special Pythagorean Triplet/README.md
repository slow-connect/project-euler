# 9. Special Pythagorean triplet - Project Euler

[Website](https://projecteuler.net/problem=9)

_Created: 2023-01-05_

## Problem
A Pythagorean triplet is a set of three natural numbers, $a < b < c$, for which,

$$a^2 + b^2 = c^2$$

For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.

There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.

Find the product $abc$.


## Idea
- From $a < b < c$ and $a + b + c = 1000$, it follows that $a < 333$.
- From there we can determine the range of $b$ and calculate $c$ from the condition $a + b + c = 1000$.

## Code
See [here](https://github.com/slow-connect/project-euler/blob/main/9.%20Special%20Pythagorean%20Triplet/main.py) for the code.

## Solution
<details>
31875000
</details>
