notas = [10, 9, 8]

def calcula_media(notas):
  quantidade = len(notas)
  soma = 0
  for nota in notas:
    soma = soma + nota

  media = soma / quantidade 

  return media


def status_aluno():
  media = calcula_media(notas)
  if media >= 6:
    print('O aluno foi aprovado')
  elif media >= 4:
    print('O aluno irá para a recuperação')
  else:
    print('O aluno foi reprovado')



print(calcula_media(notas))
status_aluno()
