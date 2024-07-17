def get_matriculas():
  for _ in range(5):
    yield int(input("Digite uma matricula: "))

def isImpar(numero):
  return numero % 2

for matricula in get_matriculas():
  par_impar = "impar" if isImpar(matricula) else "par"
  print(f"A {matricula} é {par_impar}")