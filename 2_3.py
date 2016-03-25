import threading

def writer(x, event_for_wait, event_for_set):
    for i in xrange(10):
        event_for_wait.wait()
        event_for_wait.clear()
        print "I`m {} thread".format(x)
        event_for_set.set()

def main():
    e1 = threading.Event()
    e2 = threading.Event()
    thread1 = threading.Thread(target=writer, args=(1, e1, e2))
    thread2 = threading.Thread(target=writer, args=(2, e2, e1))
    thread1.start()
    thread2.start()
    e1.set()
    thread1.join()
    thread2.join()


if __name__ == '__main__':
    main()