import sys

usuario_cadastro = input('Digite seu usuario: ').strip()
senha_cadastro = input('Digite sua senha: ').strip()
cadastro_inicial = usuario_cadastro, senha_cadastro

if not usuario_cadastro or not senha_cadastro:
    print('Não há usuario ou senha.')
    sys.exit()


print('Cadastro feito com sucesso!')
print('Faça o login novamente.')
usu_login = input('Digite seu usuario: ')
sen_login = input('Digite sua senha: ')

if usu_login == usuario_cadastro and sen_login == senha_cadastro:
    print('Login feito com sucesso.')
else:
    print('Usuario ou senha não se coincidem.')



