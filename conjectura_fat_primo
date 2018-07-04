#VERIFICAR SE ASOMA DOS DIVISORES DOS PRIMOS TBM É UM PRIMO

facs = {} #dicionario

for f in range (2, int (n/2)  +1):
   while (n % f == 0):
       n = n/f
       if f in facs:
           facs[f] = facs.get (f) + 1
       else:
           if is_prime(f):
                facs[f] = 1
           else:
               print (str(n) + "  não tem fatoração prima")
               return {}
               
          
