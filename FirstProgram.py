def my_switch(valor):
    cases = {
        1: "Teste1",
        2: "Teste2",
        3: "Teste3",
    }
    return cases.get(valor, "Valor Invalido")


def soma(a,b):
    soma=a+b;
    return soma;



if __name__ == '__main__':
    valor = int(input("Digite um valor para teste"))
    print(my_switch(valor))
    print(soma(5,10))