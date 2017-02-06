def prime_number(number):

    if isinstance(number, int):
        lst = []
        for i in range(2, number):
            if i%2!=0 and i%3!=0 and i%5!=0:
                lst.append(i)
        print lst
    else:
        print "invalid input"

prime_number(100)

            
        
