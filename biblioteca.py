class Autor:
    def __init__(self, primeiro_nome, ultimo_nome, data_nascimento, nome_meio=''):
        self.primeiro_nome = primeiro_nome
        self.nome_meio = nome_meio
        self.ultimo_nome = ultimo_nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f'Autor: {self.nome_como_citado}'

    @property
    def nome_como_citado(self):
        return f'{self.ultimo_nome.upper()} {self.primeiro_nome[0].upper()}.'

    @property
    def nome(self):
        return f'{self.primeiro_nome, self.nome_meio, self.ultimo_nome}'

class Livro:
    def __init__(self, titulo, ano, autores=[]):
        self.titulo = titulo
        self.ano = ano
        self.autores = autores

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, val):
        if val is None:
            raise ValueError("Titulo não pode ficar em branco")
        self._titulo = val

    def __str__(self):
        return f'Livro: {self.titulo}'

class Biblioteca:
    def __init__(self, livros):
        self.livros = livros

    @property
    def livros_por_autor(self):
            data = {}
            for livro in self.livros:
                for autor in livro.autores:

                    if autor.nome not in data:
                        data[autor.nome] = []

                    data[autor.nome].append(livro.titulo)

            return data
    def __str__(self):
        return 'BIBLIOTECA: \n'
