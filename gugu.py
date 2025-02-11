import sys

def gugu(arg):
    
    a = int(arg[0][:-1])
    b = int(arg[1])
    
    # print(a, type(a))
    # print(b, type(b))
    
    for i in range(a,a+b):
        print(f'\n{str(i)+"단":=^14}')
        for j in range(1,10):
            print(f'{i} X {j} = {i*j}')
            

args = sys.argv[1:]
gugu(args)
print('\n')