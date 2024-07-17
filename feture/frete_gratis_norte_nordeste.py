import requests
import sys

ENDPOINT = "https://viacep.com.br/ws"
FORMATO_RETORNO_API = "json"

def main() -> None:
  cep: str = input("Informe seu CEP: ").replace("-", "") 
  if is_cep_valid(cep):
    if tem_frete_gratis(cep):
      print("Parabéns, você ganhou frete grátis!")
    else:
      print(f"O valor do frete para {cep} é R$19,90")
  else:
    print(f"CEP {cep} não é um CEP válido. Informe 08 dígitos e utilize apenas números")

def tem_frete_gratis(cep: str) -> bool:
  dados: dict = consulta_cep(cep)
  return is_norte_nordeste(dados['uf'])

def consulta_cep(cep: str) -> dict:
  response: requests.Response = requests.get(f"{ENDPOINT}/{cep}/{FORMATO_RETORNO_API}")
  dados: dict = response.json()
  if "erro" in dados or response.status_code != 200:
    sys.exit("Houve um problema ao consultar o CEP. Certifique-se que o CEP foi digitado corretamente")
  return dados

def is_norte_nordeste(uf: str) -> bool:
  UF_NORTE = ("AC", "AP", "AM", "PA", "RO", "RR", "TO") 
  UF_NORDESTE = ("AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE")
  return uf.upper() in UF_NORTE or uf.upper() in UF_NORDESTE

def is_cep_valid(cep: str) -> bool:
  return len(cep) == 8 and cep.isdigit()

main()