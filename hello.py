import time

a = input ("Input a: ")
a = int(a)
while 1 :
    if a % 2==1:
        a = (a+1)*2
    else:
        a=a/2
    print (a)
    time.sleep (0.2)
