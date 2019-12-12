import random
def rand_gen(rang, length):
    return random.sample(range(rang),length)
    
def sortuj(x):
    for i in range(50):
        for l in range(49):
            if x[l] > x[l+1]:
                tmp = x[l]                
                x[l] = x[l+1]
                x[l+1] = tmp
    return(x)                

a = rand_gen(1000,50)
b = sortuj(a)
print(b)





