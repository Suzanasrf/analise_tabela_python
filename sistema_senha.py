from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    def __init__(self, nome, sobrenome, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__senha = cryp.hash(senha, rounds=1000, salt_size=10)

    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome

    def get_senha(self):
        return self.__senha

    def imprimirNomeSobrenome(self):
        nome = self.get_nome()
        sobrenome = self.get_sobrenome()
        print(f"Nome: {nome}, Sobrenome: {sobrenome}")

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

# Coletar informações do usuário
while True:
    nome = input('Nome:')
    sobrenome = input('Sobrenome:')
    senha = input('Senha:')
    conf_senha = input('Confirme a senha:')

    if senha == conf_senha:
        user = Usuario(nome, sobrenome, senha)  # Criar uma instância da classe Usuario
        break
    else:
        print('As senhas não conferem')

print('Usuário criado com sucesso!!')

# Verificar a senha e conceder acesso
senha_input = input('Digite a senha para acessar:')
if user.checa_senha(senha_input):
    print("Acesso permitido!!")
else:
    print('Acesso negado!!!')
