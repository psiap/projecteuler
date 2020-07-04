#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

count = 600851475143
i = 1
while(True):
    i += 1
    if count % i == 0:
        print("Count: %s, i: %s" % (count,i))
    else:
        if i > 10**3:
            break