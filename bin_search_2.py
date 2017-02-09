class BinarySearch(list):

    def __init__(self,a,b):
        self.a = a
        self.b = b

        for num in range(self.a):
            list.append(self, self.b)
            self.b += b

        self.length = self.a

    def search(self, number):
        upper = (self.length - 1)
        lower = 0
        count = 0
        found = False
        try:
            index = self.index(number)
            found = True
        except ValueError:
            index = -1
            found = False
        while lower <= upper and found and number != self[upper]:
            mid = (lower + upper) //2
            mid_value = self[mid]
            if number > mid_value:
                lower = mid + 1
                count += 1
            elif number < mid_value:
                upper = mid - 1
                count += 1
            else:
                count += 1
                break
        return {'count': count, 'index': index}
