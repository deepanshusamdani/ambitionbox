" check the substring is available in main string and if it is print its's index else (-1,-1)"
import re

string = input()
substring = input()

pattern = re.compile(substring)
match = pattern.search(string)

if not match: print('(-1, -1)')
while match:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(string, match.start() + 1)