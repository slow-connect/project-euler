# 14. Longest Collatz sequence - Project Euler

[Website](https://projecteuler.net/problem=14)

_Created: 2024_01_15_

## Problem
The following iterative sequence is defined for the set of positive integers:

$$
n \longrightarrow \frac{n}{2}\quad \text{ (n is even)} \\
n \longrightarrow 3n + 1 \quad \text{ (n is odd)}
$$

Using the rule above and starting with $13$, we generate the following sequence:

$$13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$$

It can be seen that this sequence (starting at $13$ and finishing at $1$) contains $10$ terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at $1$.

Which starting number, under one million, produces the longest chain?

**NOTE:** Once the chain starts the terms are allowed to go above one million.

## Idea

- Brute force
- For each number, we calculate the length of the chain. For each term, below 1 million, we save, how long the chain is. If in some higher itteration, we hit the same number once again, we can just add the saved number to the current length of the chain.

## Code

See [here](https://github.com/slow-connect/project-euler/blob/main/014%20Longest%20Collatz%20Sequence/main.py) for the code.

## Solution

<details>
837799
</details>
