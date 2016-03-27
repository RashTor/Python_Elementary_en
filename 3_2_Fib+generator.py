def fib_numbers(number_of_elem,f_n=0,f_n_1=1):
    print f_n,"\n",f_n_1
    for count in xrange(number_of_elem-2):
        f_n_2=f_n+f_n_1
        f_n=f_n_1
        f_n_1=f_n_2
        yield f_n_2


def main():
    fib_gen=fib_numbers(input("Input amount of Fibonacci numbers: "))
    for next_fib_num in fib_gen:
        print next_fib_num


if __name__ == '__main__':
    main()