# 7. $10001$st Prime - Project Euler

[Website](https://projecteuler.net/problem=7)

_Created: 2024-01-03_

## Problem
By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.

What is the $10001$st prime number?

## Idea:
- We use the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) to find the $10001$st prime number.
- We start with a list of boolean values of some length $n$ (hoping that we have enough primes in the intervall)
- We use a `for` loop to iterate over the list from $2$ to $n$. If the value is `True`, we know that the number is prime and set all multiples of this number to `False`. We increment our counter by $1$.
- If the counter reaches $10001$, we have found our prime number, and break the loop.

## Code:
see [here](https://github.com/slow-connect/project-euler/blob/main/7.%2010001st%20Prime/main.py) for the code.

## Answer:

<details>
104743
<details>
