# CMPS 2200 Assignment 4
## Answers

**Name:Rhegan Barrett**


Place all written answers from `assignment-04.md` here for easier grading.

1a) The greedy criteria is to choose the largest denomination first. We take as many coins of the largest available denomination we can, then go to the next largest denomination until we can make exact change with the coin denominations of 2^k.

1b) 

1c) Both the work and span are O(log n)

2a) If we want to make change for 10 but there's coin denominations of 7,1, and 5. We would chose 1 coin with a value of 7 and 3 coins with a value of one to make exact change. However, the optimal solution would be to start with coins of a value of 5 and pick 2.

2b)

2c) The number of distinct subproblems is N * k, and each memoization take O(1) work. Therefore the work and span are O(N*k) 

