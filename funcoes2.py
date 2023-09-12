# VERSÃO ONDE O USUÁRIO DEFINE AS FUNÇÕES

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
  operacoes = int(input("\n\nSelecione a opção: \n1 - Fazer operações com função \n2 - Sair\n"))

  if operacoes == 1:
    operadorf = int(input("\n\nO que você deseja fazer na função f(x)?\n1 - Somar\n2 - Subtrair \n3 - Multiplicar \n4 - Dividir\n\n"))
    valorf = int(input("\nInsira o valor para usar na função f(x):\n"))
    
    if operadorf == 1:
      def funcao_f(x):
        return x + valorf
      print(f"\n\nFUNÇÃO F(x) = x + {valorf}")
    
    elif operadorf == 2:
      def funcao_f(x):
        return x - valorf
      print(f"\n\nFUNÇÃO F(x) = x - {valorf}")

    elif operadorf == 3:
      def funcao_f(x):
        return x * valorf
      print(f"\n\nFUNÇÃO F(x) = x ⋅ {valorf}")


    elif operadorf == 4:
      def funcao_f(x):
        return x / valorf
      print(f"\n\nFUNÇÃO F(x) = x ÷ {valorf}")
    
    else:
      print("\nOpção inválida!")
    

    operadorg = int(input("\n\nO que você deseja fazer na função g(x)?\n1 - Somar\n2 - Subtrair \n3 - Multiplicar \n4 - Dividir\n\n"))
    valorg = int(input("\nInsira o valor para usar na função g(x):\n"))
    
    if operadorg == 1:
      def funcao_g(x):
        return x + valorg
      print(f"\n\nFUNÇÃO G(x) = x + {valorg}")

    elif operadorg == 2:
      def funcao_g(x):
        return x - valorg
      print(f"\n\nFUNÇÃO G(x) = x - {valorg}")

    elif operadorg == 3:
      def funcao_g(x):
        return x * valorg
      print(f"\n\nFUNÇÃO G(x) = x ⋅ {valorg}")

    elif operadorg == 4:
      def funcao_g(x):
        return x / valorg
      print(f"\n\nFUNÇÃO G(x) = x ÷ {valorg}")
    
    else:
      print("\nOpção inválida!")
    
  
    valor_de_x = int(input("\n\nInsira o valor de x: "))
    
    print(f"\n\ng ° f({valor_de_x}) = {gf()}")
    print(f"g ° g ({valor_de_x}) = {gg()}")
    print(f"f ° f ({valor_de_x}) = {ff()}")
    print(f"f ° g ({valor_de_x}) = {fg()}")
    
  elif operacoes != 1 and operacoes != 2:
    print("\nOpção inválida!")
