# This script can only convert from base up to 36

def convert(N, b):
    dec_val = 0
    N = str(N)
    indx = len(N)
    for i in range(indx):
        indx -= 1
        try:
            dec_val += int(N[indx])*(b**i)
        except:
            code = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}

            dec_val = dec_val + code[N[indx]]*(b**i)
    print(dec_val)

if __name__=='__main__':
        N = input("Enter the value: ")
        b = int(input("Enter the base: "))
        convert(N, b)