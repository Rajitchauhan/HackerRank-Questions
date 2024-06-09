# input : this is string
# output : string is this

class Rev:
    def reverse(self , st):
        st = st.split()
        print(st)
        st = st[::-1]
        print(st)
        return " ".join(st)

if __name__ == '__main__':
    s = input()
    obj = Rev()
    res = obj.reverse(s)
    print(res)