import random


def bubble_sort(elem_range):
    for i in reversed(range(len(elem_range))):
        for j in range(1, i + 1):
            if elem_range[j-1] > elem_range[j]:
                elem_range[j], elem_range[j-1] = elem_range[j-1], elem_range[j]
    print 'Sorted: ',elem_range


def generate_range(max_numb):
    rand_range=[]
    for i in range(1,max_numb+1):
        rand_range.append(random.randrange(1,100,1))
    print 'Unsorted: ',rand_range
    return rand_range


def main():
    var = 1
    while var != 0:
        var = input("Chose var:\n1)\tGenerate random range\n2)\tInput range of numbers\n0)\tExit\n")
        if var == 1:
            bubble_sort(generate_range(input("Input max number of elements:")))
            break
        elif var == 2:
            bubble_sort(list(input('Input numbers in the following manner: num1,num2,num3...')))
            break
        elif var == 0:
            exit()
        else:
            var = input("Chose another var:\n1)\tGenerate random range\n2)\tInput range of numbers\n0)\tExit\n")



if __name__ == '__main__':
    main()