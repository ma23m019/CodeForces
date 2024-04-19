"""
You have n sticks, numbered from 1 to n with numbers a_1, a_2,..., a_n. The length of the i-th stick is 2^(a_i).

You want to choose exactly 3 sticks out of the given n sticks, and form a non-degenerate triangle out of them, using the 
sticks as the sides of the triangle. A triangle is called non-degenerate if its area is strictly greater than 0.

You have to calculate the number of ways to choose exactly 3 sticks so that a triangle can be formed out of them. Note that 
the order of choosing sticks does not matter (for example, choosing the 1-st, 2-nd and 4-th stick is the same as choosing the
2-nd, 4-th and 1-st stick).

Input: The first line contains one integer t — the number of test cases.
Each test case consists of two lines: The first line contains one integer n.
The second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n).

Additional constraint on the input: the sum of n over all test cases does not exceed 3⋅105.

Output: For each test case, print one integer — the number of ways to choose exactly 3 sticks so that a triangle can be formed 
out of them.
"""

from math import comb

t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    
    *P, = map(int, a.split())
    
    d = [0]*(n+1)
    for i in range(n):
        d[P[i]] += 1
        
    l = 0; k = 0
    for i in range(1,n+1):        
        k += d[i-1]
        if d[i] == 0:
            continue
        l += comb(d[i],3) + comb(d[i],2) * k
            
    l += comb(d[0],3)
    
    print(l)
