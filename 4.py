#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 ? 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

array = []
for i in range(100,999):
    for j in range(100,999):
        x = i * j
        if str(x) == str(x)[::-1]:
            array.append(x)
print(set(array))