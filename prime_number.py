def prime_number(number):

    if isinstance(number, int):
        lst = []
        if number>5:
            lst = [2,3,5]
            for i in range(2, number):
                if i%2!=0 and i%3!=0 and i%5!=0:
                    lst.append(i)
        elif number>1 and number<5:
            lst = [2,3,5]
        else:
            return "Not prime number in range"
        print lst
    else:
        print "invalid input"

prime_number(100)

            
        
