n = int(input())
l=[]
for i in range(n):
    n1 = input()
    l.append(input().split())
for i in l:
    for j in i[::-1]:
        print(j,end=" ")
    print()
