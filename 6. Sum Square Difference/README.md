# 6. Sum Square Difference


[Website](https://projecteuler.net/problem=6)

_Created: 2024-01-03_

## Problem
The sum of the squares of the first ten natural numbers is,
$$1^2 + 2^2 + ... + 10^2 = 385$$
The square of the sum of the first ten natural numbers is,
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025$$
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

## Idea:
- We can use the formula for the sum of the first $n$ natural numbers.
$$\sum_{i=1}^n i = \frac{n(n+1)}{2}$$
- We can use the formula for the sum of the first $n$ squares.
$$\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$$
- We can use these formulas to find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

## Code:
see [here](https://github.com/slow-connect/project-euler/blob/main/6.%20Sum%20Square%20Difference/main.py) for the code.

## Answer:
<details>
25164150
</details>
