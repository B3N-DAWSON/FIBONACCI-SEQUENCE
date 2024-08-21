def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    seq = [0,1]
    a,b = 0,1
    for i in range(2,n):
        new_fib = a + b
        seq.append(new_fib)
        a,b = b,new_fib

    return seq

seq_length = int(input("Enter the length of the Fibonacci Sequence: "))
fib_seq= fibonacci_sequence(seq_length)
print("the first",seq_length, "numbers of the Fibonacci Sequence are: ", fib_seq)