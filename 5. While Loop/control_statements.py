"""
Loops

Continue (skips the below part of the code and moves to next loop)
Break (break from the loop)
"""

# i = 1
# while i <= 5:
#     print("Hello")
#     if i == 3:
#         continue
#     i += 1


def func():
    i = 1
    while i <= 5:
        print("Hello")
        if i == 3:
            return
        i += 1
    print("Done")


func()
