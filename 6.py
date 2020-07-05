#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sq_sum(n): 
    s1=0
    s2=0
    ind=0
    r=range(1,n+1)
    for i in r:
        s1+=(i**2)
        s2+=(i**2)
        for j in r[ind+1:]:
            s1+=2*i*j
        ind+=1
    return s1-s2