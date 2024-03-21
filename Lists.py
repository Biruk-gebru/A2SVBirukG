N = int(input())
ls=[]
for i in range(N):
    command=list(map(str,input().split()))
    if command[0]=="insert":
        ls.insert(int(command[1]),int(command[2]))
    elif command[0]=="print":
        print(ls)
    elif command[0]=="remove":
        ls.remove(int(command[1]))
    elif command[0]=="append":
        ls.append(int(command[1]))
    elif command[0]=="sort":
        ls=sorted(ls)
    elif command[0]=="pop":
        ls.pop()
    else:
        ls=ls[::-1]
