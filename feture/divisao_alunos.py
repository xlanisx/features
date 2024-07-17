def is_par(numero):
  return numero % 2 == 0

print("BEM VINDO A OLIMPIADA DO CONHECIMENTO")
matricula = int(input("Digite a sua matricula: "))

if is_par(matricula):
  print("VOCÊ ESTÁ NO TIME AZUL")
else:
  print("VOCÊ ESTÁ NO TIME AMARELO")