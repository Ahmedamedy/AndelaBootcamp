def find_missing(lista,listb):
  
  if lista == [] or listb == []:
    return 0
    
  elif lista == listb:
    return 0 
  else:
    listc = [i for i in listb if i not in lista]+ [i for i in lista if i not in listb]
    return listc[0]
