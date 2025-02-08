# Problem: Swap Cases - https://www.hackerrank.com/challenges/swap-case?isFullScreen=true

def swap_case(s):
    sol = []
    for elem in s:
        if elem >= "a" and elem <= "z":
            sol.append(elem.upper())
        elif elem >= "A" and elem <= "Z":
            sol.append(elem.lower())
        else:
            sol.append(elem) 
    return "".join(sol)


