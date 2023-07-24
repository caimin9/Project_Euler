def fib(n):
    fib_store = [1,2]
    fib_store_even = 2
    for i in range(2,n):
        fib_value = fib_store[i-1] + fib_store[i-2]
        fib_store.append(fib_value)
        if fib_value % 2 == 0:
            fib_store_even += fib_value
        if fib_store[i] > 4000000:
            break
        else: 
            continue
    return fib_store_even  
