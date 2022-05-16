"""
Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
      order their names alphabetically and print each name on a new line.
"""

l = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
s = []
for i in range(len(l)):
    s.append(l[i][1])
uniq = list(set(s))
uniq.sort()
sec_min = uniq[1]
n = []
for i in range(len(l)):
    if l[i][1] == sec_min:
        n.append(l[i][0])
        n.sort()
for i in range(len(n)):
    print(n[i],end='\n')




# n = ['Harry','Berry','Tina','Akriti','Harsh']
# s = [37.21,37.21,37.2,41.0,39.0]