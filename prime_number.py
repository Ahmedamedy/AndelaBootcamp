def prime_number(number):

    if isinstance(number, int):
        lst = []
        if number>8:
            lst = [2,3,5,7]
            for i in range(2, number):
                if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
                    if i % i**0.5 != 0:
                        lst.append(i)
        elif number>1 and number<3:
            lst = [2]
        elif number>1 and number<4:
            lst = [2,3]
        elif number>1 and number<6:
            lst = [2,3,5]
        elif number>1 and number<8:
            lst = [2,3,5,7]
        else:
            return "No prime number in range"
        return lst
    else:
        return "invalid input"




            
        
