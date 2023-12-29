# 5. Smallest Multiple


[Website](https://projecteuler.net/problem=5)

_Created: 2023-12-29_

## Problem
$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from $1$ to $20$?

## Idea:
- Numbers from $1$ to $20$ are not all primes, some are a composition of smaller primes.
- We can use this to our advantage.
- We can find all primes $p$ from $1$ to $20$.
- Then we can find the largest power $k$ of each prime $p$ that is less than $20$.
$$p^k < 20$$
- Then we can multiply all of these together to get the smallest number that is evenly divisible by all of the numbers from $1$ to $20$.

## Code:
see [here](https://github.com/slow-connect/project-euler/blob/main/5.%20Smallest%20Multiple/main.py) for the code.

## Solution:
<details>
232792560
</details>
