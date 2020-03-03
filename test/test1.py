from xinlangcaijing import myThread

if __name__ == '__main__':
    thread1 = myThread(1, '003853')
    thread2 = myThread(1, '003017')
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(thread1.text)
    print(thread2.text)
