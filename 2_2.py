import random, time


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


def comp_time_of_func(fun_to_decor):
    def decor_comp_time(rand_range):
        beg_time=time.clock()
        fun_to_decor(rand_range)
        print time.clock()-beg_time
    return decor_comp_time


def main():
    #unsort_list=generate_range(input("Input max number of elements:"))
    decor_bubble_sort=comp_time_of_func(bubble_sort)
    decor_bubble_sort(generate_range(input("Input max number of elements:")))

if __name__ == '__main__':
    main()