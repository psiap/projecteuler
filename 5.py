#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def nkt():
    count = 0
    while (True):
        count += 1
        temp_i = []
        for i in range(1, 21):
            temp_i.append(i)
            print("Count: %s | I: %s | Count I: %s" % (count,i, count % i ))
            if count % i != 0:
                break
            elif i == 20 and count % i == 0:
                return count
print(nkt())