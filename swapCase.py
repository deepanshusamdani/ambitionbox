def swap(a):
    s = []
    for i in a:
        if i.islower():
            s.append(i.upper())
        else:
            s.append(i.lower())
    out = ''.join(s)
    return out

if __name__ == "__main__":
    input = 'HackerRank.com presents "Pythonist 2"'
    res = swap(input)
    print(res)
