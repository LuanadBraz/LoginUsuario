import time
print('-------------------------------')
print('######## LOGIN USUÁRIO ########')
print('-------------------------------')

nome = str(input('Digite seu nome: '))
senha = str(input('Digite sua senha: '))
print('Carregando...')
time.sleep(1.9)

while (senha == nome):
    senha = str(input('Senha Inválida! Digite novamente: '))
else:
    print('Login efetuado com sucesso!')

print('-------------------------------')
print('######## LOGIN USUÁRIO ########')
print('-------------------------------')