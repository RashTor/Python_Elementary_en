import time,random


class profile:
    def __init__(self):
        self.num_of_calls = 0
        self.name_of_func_s = []

    def __call__(self, fun_name):
        self.num_of_calls+=1
        self.name_of_func_s.append(fun_name.__name__)
        print self.num_of_calls
        print self.name_of_func_s
        def decor_comp_time(fun_arg):
             beg_time=time.clock()
             fun_name(fun_arg)
             print time.clock()-beg_time
        return decor_comp_time


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
    obj_class_profile=profile()
    #unsort_list=generate_range(input("Input max number of elements:"))
    decor_bubble_sort=obj_class_profile(bubble_sort)
    decor_gen_range=obj_class_profile(generate_range)
    #print type (generate_range(input("Input max number of elements:")))
    decor_bubble_sort(generate_range(input("Input max number of elements:")))
    decor_gen_range(8)


if __name__ == '__main__':
    main()