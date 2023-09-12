# FUNCAO F(x) = x + 1
def funcao_f(x):
  return x + 1


#FUNCAO g(X) = X - 5
def funcao_g(x):
  return x - 5


def gf(x):
  return funcao_g(funcao_f(x))


def gg(x):
  return funcao_g(funcao_g(x))


def ff(x):
  return funcao_f(funcao_f(x))


def fg(x):
  return funcao_f(funcao_g(x))


valor_de_x = int(input("Insira um valor: "))

print(f"\n\ng ° f({valor_de_x}) = {gf(valor_de_x)}\n")
print(f"g ° g({valor_de_x}) = {gg(valor_de_x)}\n")
print(f"f ° f({valor_de_x}) = {ff(valor_de_x)}\n")
print(f"f ° g({valor_de_x}) = {fg(valor_de_x)}\n")
