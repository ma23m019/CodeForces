"""
Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round, as long as
the contestant earns a positive score..." — an excerpt from contest rules.

A total of n participants took part in the contest (n ≥ k), and you already know their scores. Calculate how many participants 
will advance to the next round.

Input: The first line of the input contains two integers n and k (1 ≤ k ≤ n ≤ 50) separated by a single space. The second line 
contains n space-separated integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ 100), where ai is the score earned by the participant who got the 
i-th place. The given sequence is non-increasing (that is, for all i from 1 to n - 1 the following condition is fulfilled: 
a_i ≥ a_(i+1).

Output: Output the number of participants who advance to the next round.
"""

a = input("Enter the number of participants and value of k separated by a single space: ")

n = int(a[0:a.find(' ')])
k = int(a[a.find(' ')+1:])

scores = input(f"Enter space-separated scores of {n} participants: ")

spaces = []

for i in range(len(scores)):
    if scores[i] == ' ':
        spaces.append(i)
        
if spaces != []:
    f = []
    f.append(scores[0:spaces[0]])

    for i in range(len(spaces)-1):  
        f.append(scores[spaces[i]+1:spaces[i+1]])

    f.append(scores[spaces[-1]+1:])

    counter = 0
    if int(f[k-1]) != 0:
        for i in range(n):
            if int(f[i]) >= int(f[k-1]):
                counter = counter + 1
    else:
        for i in range(n):
            if int(f[i]) > int(f[k-1]):
                counter = counter + 1

elif scores == '0':
    counter = 0
    
else:
    counter = 1

print(counter)
