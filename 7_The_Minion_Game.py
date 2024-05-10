# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(s):
    # your code goes here
    vowels = ['a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U']
    Slen = len(s)

    Kevin , Stuart = 0  , 0

    for i in range(Slen):
        if s[i] in vowels:
            Kevin += Slen - i 
        else:
            Stuart += Slen - i
    
     # Print
    if Kevin>Stuart:
        print('Kevin',Kevin)
    elif Kevin<Stuart:
        print('Stuart',Stuart)
    else:
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)