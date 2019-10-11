
a = 2
b = 6
c = 4

delta = (b ** 2) - a * a * c

if (delta > 0):
    x1 = ((-1*b) + math.sqrt(delta)) / (2*a)
    x2 = ((-1*b) -   math.sqrt(delta)) / (2*a)
    print ("As raízes são " + str(x1) "e" + str (x2))
elif delta == 0:
    x = ((-1*b) + math.sqrt(delta)) / (2*a)
    
    
