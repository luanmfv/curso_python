def fatorial(num=1):  #o num=1 significa que se não tiver nenhum valor, será preenchido com 1
    f =1
    for c in range(num, 0, -1): #aqui seria começar do num=1, ir até 0 voltando de 1 em 1
        f*= c
    return f

#Fatorial é o resultado da multiplicação de um número por todos os números menores que ele até 1.

#Exemplo:

#5! (lê-se "5 fatorial") = 5 × 4 × 3 × 2 × 1 = 120

#3! = 3 × 2 × 1 = 6

#1! = 1

#0! = 1 (por definição)


n = int(input('Digite um número: '))
print(f'O fatorial de {n}  é igual a {fatorial(n)}')

print('-' *30)

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados fatoriais de 5, 4 e 1 são de: {f1}, {f2} e {f3}.')

print('-' *30)

def par(n=0):
    if n % 2==0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(f'O valor {num} é par? A resposta é[True/False]  : {par(num)}')
# ou poderia ser
#if part(num):
#   print('É par!')
#else:
#   print('Não é par!')