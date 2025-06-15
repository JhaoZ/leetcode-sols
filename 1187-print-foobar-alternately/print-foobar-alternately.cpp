class FooBar {
private:
    int n;
    bool foo_next = true;
    std::mutex mtx;
    std::condition_variable cv;


public:
    FooBar(int n) {
        this->n = n;
    }

    void foo(function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            std::unique_lock<std::mutex> lock(mtx);
            while (foo_next == false) {
                cv.wait(lock);
            }
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
            foo_next = false;
            cv.notify_all();
            lock.unlock();
        }
    }

    void bar(function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            std::unique_lock<std::mutex> lock(mtx);
            while (foo_next == true) {
                cv.wait(lock);
            }
            
        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
            foo_next = true;
            cv.notify_all();
            lock.unlock();
        }
    }
};