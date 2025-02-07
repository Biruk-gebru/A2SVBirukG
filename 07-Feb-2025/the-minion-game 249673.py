# Problem: the-minion-game - https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    countV, countC = 0, 0
    vowels = {"a":1, "e": 2, "i":3, "o":4, "u": 5}
    string = string.lower()
    for i in range(len(string)):
        if string[i] in vowels:
            countV += len(string) - i
        else:
            countC += len(string) - i
    
    if countC > countV:
        print("Stuart", countC)
    elif countC < countV:
        print("Kevin", countV)
    else:
        print("Draw")
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)