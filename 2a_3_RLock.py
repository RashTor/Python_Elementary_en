import time,threading,random

lock = threading.RLock()

class thread_class(threading.Thread):
    def __init__(self,fact_meth,max_num):
        threading.Thread.__init__(self)
        #self.daemon = True
        #self.interval = interval
        self.max_num=max_num
        self.fact_meth=fact_meth
    def run(self):
        lock.acquire()
        try:
            print "I`m a {} and my answer is {}".format(self.getName(),self.fact_meth(self.max_num))
        finally:
            lock.release()


def rec_fact(max_num):
    if max_num==0:
        return 1
    else:
        return max_num*rec_fact(max_num-1)


def cyc_fact(max_num):
    factorial_of_num=1
    for i in range(1,max_num+1):
        factorial_of_num*=i
    return factorial_of_num


def main():
    max_num=input("Input max size of seq:")
    #thread_div_2 = threading.Thread(target=rec_fact, args=(max_num))
    #thread_div_3 = threading.Thread(target=cyc_fact, args=(max_num))
    first_thread=thread_class(rec_fact,max_num)
    second_thread=thread_class(cyc_fact,max_num)
    first_thread.start()
    second_thread.start()
    first_thread.join()
    second_thread.join()


if __name__ == '__main__':
    main()