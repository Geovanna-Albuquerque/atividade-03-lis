#Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a mèdia

listaNotas = []
  media = 0
  print ('Informe as 4 notas')
  for i in range(4):
 	listaNotas.append(float(input('Nota '+ str(i+1) + ':\n')))
 	media += listaNotas[i]
  media = media/4
  print (listaNotas) 
  print (media)




