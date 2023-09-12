# VERSÃO ONDE O USUÁRIO DEFINE AS FUNÇÕES

# FUNCAO F(x)
def funcao_f(x):
  return x * x


# FUNCAO G(X)
def funcao_g(x):
  return x - 1


def gf():
  return funcao_g(funcao_f(valor_de_x))


def gg():
  return funcao_g(funcao_g(valor_de_x))


def ff():
  return funcao_f(funcao_f(valor_de_x))


def fg():
  return funcao_f(funcao_g(valor_de_x))


operacoes = 1
contador = 0
while operacoes != 2:
  operacoes = int(input("Selecione a opção: \n1 - Fazer operações com função \n2 - Sair\n"))

  if operacoes == 1:
    #f = int(input("Insira a função f(x) = "))
    #g = int(input("Insira a função g(x) = "))

    
    valor_de_x = int(input("Insira um valor: "))
    
    print(f"\n\ng ° f({valor_de_x}) = {gf()}")
    print(f"g ° g({valor_de_x}) = {gg()}")
    print(f"f ° f({valor_de_x}) = {ff()}")
    print(f"f ° g({valor_de_x}) = {fg()}")
    
  elif operacoes != 1 and operacoes != 2:
    print("\nOpção inválida!")
