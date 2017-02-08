def words(n):

    a = [int(s) for s in n.split() if s.isdigit()]
    b = [str(i) for i in n.split() if  i.isdigit()==False]
    c = a + b

    dicw = {}
    for i in c:
        x = c.count(i)
        dicw[i]=x
    return dicw


    
