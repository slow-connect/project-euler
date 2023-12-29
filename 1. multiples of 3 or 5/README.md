# 1. Multiples of 3 and 5 - Project Euler

[Website](https://projecteuler.net/problem=1)

_Created: 2023-12-25_

## Problem
What is the sum of all the multiples of 3 or 5 below 1000?

## Idea:
- Use Inclusion-Exclusion Principle:
$$\vert A \cup B \vert = \vert A \vert + \vert B \vert - \vert A \cap B \vert$$
- We count all multiples of 3 and 5 lower then 1000, and subtract the multiples of 15.

## Code:
see [here](https://github.com/slow-connect/project-euler/blob/main/1.%20multiples%20of%203%20or%205/main.py) for the code.

## Answer:
<details>
233168
</details>
