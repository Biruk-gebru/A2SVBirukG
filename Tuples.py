n = int(input())
integer_list = map(int, input().split())
intt=tuple(integer_list)
print(hash(intt))
