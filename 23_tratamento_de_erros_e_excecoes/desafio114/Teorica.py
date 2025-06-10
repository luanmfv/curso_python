try: #tentar
    a = int(input('Numerador:'))
    b = int(input('Denominador:'))
    r = a / b
except (ValueError, TypeError): # se der erro
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'Problema econtrado foi {erro.__class__}')  # erro.__class__ ele mostra o tipo de erro
else: #se der certo
    print(f'O resultado é {r:.1f}')
finally:  #usado sempre mesmo se estiver certo ou errado
    print('Volte sempre!')