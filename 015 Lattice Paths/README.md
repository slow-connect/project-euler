# 15. Lattice Paths - Project Euler

[Website](https://projecteuler.net/problem=15)

_Created: 2024-01-18_

## Problem
Starting in the top left corner of a $2\times2$ grid, and only being able to move to the right and down, there are exactly $6$ routes to the bottom right corner.

![p015](https://projecteuler.net/project/images/p015.png)

How many such routes are there through a $20\times20$ grid?

## Idea:
- As we can only go right or down, we can only have $20$ right moves and $20$ down moves.
- So the problem is equivalent to find the number of permutation of these 40 moves.
- This is given by:

$$\frac{40!}{20!\:20!}$$

## Code
See [here](https://github.com/slow-connect/project-euler/blob/main/015%20Lattice%20Paths/main.py) for the code

## Solution
<details>
137846528820
</details>
