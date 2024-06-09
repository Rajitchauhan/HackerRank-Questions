# input :: this is string
# output :: gnirts si siht

class Rev:
    def reverse(self , st):
        return s[::-1]

if __name__ == '__main__':
    s = input()
    obj = Rev()
    res = obj.reverse(s)
    print(res)