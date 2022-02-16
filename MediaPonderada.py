# valor=int(input())
# i=0
# while i<valor:
#     A,B,C = input().split()
#     A=float(A)
#     B=float(B)
#     C=float(C)
#     soma=(A*2)+(B*3)+(C*5)
#     media=soma/10
#     print(round(media,1))
#     i+=1

list=[]
meuarray = [1,2,3,5,6,8,9,10,11,12,13,14]
for value in meuarray:
    if(value%2==0):
        list.append(value)
print(list)
print(1 and 3 in meuarray)

