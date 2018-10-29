from biblioteca import Autor, Livro, Biblioteca

def main():
  autor1 = Autor('Darcy', 'Ribeiro', '26/10/1922', '')
  autor2 = Autor('José', 'Saramago', '16/11/1922', 'de Sousa')

  livro1 = Livro(titulo='O povo brasileiro', ano=1995, autores=[autor1])
  livro2 = Livro(titulo='O ensaio sobre a cegueira', ano=1995, autores=[autor2])

  biblioteca = Biblioteca(livros=[livro1, livro2])


  print(biblioteca)
  print('Livros por autor: ')
  print(biblioteca.livros_por_autor)

if __name__ == "__main__":
    main()
