def add_num(x):
    def add_some_another_num(y):
        def add_third_num(z):
            print z+x+y
        print x+y
        return add_third_num
    return add_some_another_num


def main():
    add_num(2)(3)



if __name__ == '__main__':
    main()