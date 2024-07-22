"""
Remove all the symbols,digits, spaces from a string.

Example:
my_string = "a%b@c9d_e.f"

Result:
"abcdef"
"""

my_string = "abccrrhgjkdsdddffgtyzzzzhhhhhh"
result = ""

for ch in my_string:
    if ord("a") <= ord(ch) <= ord("z"):
        result += ch

print(result)
