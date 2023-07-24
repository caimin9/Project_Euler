##### Find the sum of all the multiples 3 and 5 below 1000
def my_func(n):
    my_sum = 0
    for i in range(1,n):
        if  i %5 ==0 or i%3 ==0:
            my_sum += i
    return(my_sum)   
