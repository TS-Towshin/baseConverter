# This script can only convert up to base 36

def convert(N, b):
    code = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 25:'P', 26:'Q', 27:'R', 28:'S', 29:'T', 30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'}
    converted_arr = []
    while N != 0:
        remainder = N%b
        N = int(N/b)
        if b > 10 and remainder > 9:
            converted_arr.append(code[remainder])
        else:
            converted_arr.append(remainder)
    converted_str = ''
    for i in converted_arr[::-1]:
        converted_str = converted_str + str(i)
    print(converted_str)

if __name__=='__main__':
    N = int(input("Decimal number: "))
    b = int(input("Enter the base: "))
    convert(N, b)