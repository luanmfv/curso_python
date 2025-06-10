def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mErro, digite um numero inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[0;31mUsuario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

num = leiaint('Digite um valor: ')
print(f'O valor digitado foi {num}')
