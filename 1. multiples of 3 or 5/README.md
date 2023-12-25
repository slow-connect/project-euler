# Multiples of 3 and 5 - Project Euler
[Website](https://projecteuler.net/problem=1)
_Created_: 2023-12-25
## Problem
What is the sum of all the multiples of 3 or 5 below 1000?
## Idea:
- Use Inclusion-Exclusion Principle:
$$\vert A \cup B \vert = \vert A \vert + \vert B \vert - \vert A \cap B \vert$$
- We count all multiples of 3 and 5 lower then 1000, and subtract the multiples of 15.
## Code:
see [here](./main.py)
## Answer:
<details>
233168
</details>
