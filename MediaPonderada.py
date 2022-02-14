valor=int(input())
i=0
while i<valor:
    A,B,C = input().split()
    A=float(A)
    B=float(B)
    C=float(C)
    soma=(A*2)+(B*3)+(C*5)
    media=soma/10
    print(round(media,1))
    i+=1