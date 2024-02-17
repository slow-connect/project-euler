# 18. Maximum Path Sum I - Project Euler

[Website](https://projecteuler.net/problem=18)

_Created: 2024-02-17_

## Problem

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is $23$.

```
   3
  7 4
 2 4 6
```

That is, $3 + 7 + 4 + 9 = 23$.

Find the maximum total from top to bottom of the triangle.

## Idea
- Use dynamic programming to solve the problem.
- Start from the bottom of the triangle and chose the value that is larger between the two adjacent values.
- Add the chosen value to the value of the current position.

## Code
The code can be found [here](https://github.com/slow-connect/project-euler/blob/main/018%20Maximum%20Path%20Sum%201/main.py)

## Solution
<details>
1074
</details>
