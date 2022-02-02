def ReceberGrau():
  
  print ('Seja Bem Vindo')
  print('Informe qual o tipo (1 = esferico 2 = cilindrico) e o grau do seu olho esquerdo:')
  tipo_esq = int(input('Tipo: '))
  grau_esq = float(input('Grau: '))
 
  print('Agora informe qual o tipo e o grau do seu olho esquerdo e o grau do seu direito:')
  tipo_dir = int(input('Tipo: '))
  grau_dir = float(input('Grau: '))

  #Verifica se é multiplo de 0.25
  if grau_esq % 0.25 != 0 or grau_dir % 0.25 != 0:
    print('Valor informado está incorreto! Tente novamente!')
    ReceberGrau()
  
  #dDefine Lente
  else:
    if (tipo_esq == 2 and tipo_dir == 2):
      if (grau_esq >= -2 and grau_dir >= -2):
        print('Sua lente é a Prime!')
      else:
        print('Sa lente é Vision!')
    elif ((tipo_esq == 2 and grau_esq >= -2) or (tipo_dir == 2 and grau_dir >= -2)):
      if (-3 >= grau_esq  >= -10 or -3 >= grau_dir >= -10):
        print ('Sua lente é Prime!')
      else:
        print ('Sua lente é Vision!')
    else:
      print('Sua lente não é Prime!')
    if (tipo_esq == 1 and tipo_dir == 1):
      if (-3 <= grau_esq  >= 12 and -3 <= grau_dir >= -12):
        print ('Sua lente é Prime!')
