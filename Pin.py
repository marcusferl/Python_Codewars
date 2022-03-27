"""
ABCD, jeder Buchstaben steht für eine Zahl von 0-9

Folgende Hilfestellung.

B + 2 = D
A - C = C
C * B = A
A/B = D
"""

for A in range(0,10):
    for B in range(0,10):
        for C in range(1,10):
            for D in range(0,10):
                if B + 2 == D and A - C == C and C*B == A and A/B == D:
                    print(A,B,C,D)