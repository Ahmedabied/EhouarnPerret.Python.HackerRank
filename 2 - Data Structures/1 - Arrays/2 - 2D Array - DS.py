"""
Given a 2D Array, A, we define an hourglass in to be a subset of values
with indices falling in this pattern in A's graphical representation:
a b c
  d
e f g
There are hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
"""

intlst=lambda x:[int(i) for i in x]
lst,ist=[intlst(i) for i in [input().split() for f in range(6)]],[]
for line in range(4):
    for start in range(4):
        end=start+3
        ist.append(sum(lst[line][start:end])+lst[line+1][start+1]+sum(lst[line+2][start:end]))
print(max(ist))

