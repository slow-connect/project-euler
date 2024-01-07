# 11. Largest Product in a Grid - Project Euler

(Website)[https://projecteuler.net/problem=11]

_Created: 2024-01-07_

## Problem
In a $20\times20$ grid, find the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally).

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the $20\times20$ grid?

## Idea
- Any number in the grid can be the first factor of such a product.
- The second factor can be any of the four numbers to the right, down,  diagonally down-right or diagonally down-left of the first factor.
- We check if we can actually multiply four numbers in the same direction. If not, we skip this direction.
- We check each possible product and keep the largest one.

## Solution
See [here](https://github.com/slow-connect/project-euler/blob/main/11.%20Largest%20Product%20in%20a%20Grid/main.py) for the code.

## Answer
<details>
70600674
</details>
