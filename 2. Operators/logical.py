"""
Logical Operators
To operate on 2 or more conditions 

AND
C1  C2  Result
F   F   F
F   T   F
T   F   F
T   T   T

OR
C1  C2  Result
F   F   F
F   T   T
T   F   T
T   T   T

NOT
Reverses the result
"""

physics = 23
chemistry = 21

# print(physics > 33 and chemistry > 33)
# print(physics > 33 or chemistry > 33)
# print(not (physics > 33 and chemistry > 33))
print(not physics > 33 and not chemistry > 33)
# not F and not F
# T and T
# T
