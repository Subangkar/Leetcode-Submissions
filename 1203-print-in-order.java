class Foo {
    private int n=0;
    // private String lock="lock";
    public Foo() {
        
    }

    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        n=1;
        synchronized (this){
            notifyAll();
        }
    }

    public void second(Runnable printSecond) throws InterruptedException {
        
        synchronized (this){
            while(n<1)
                wait();
            // printSecond.run() outputs "second". Do not change or remove this line.
            printSecond.run();
            n=2;
            notifyAll();
        }
    }

    public void third(Runnable printThird) throws InterruptedException {
        
        synchronized (this){
            while(n<2)
                wait();
            // printThird.run() outputs "third". Do not change or remove this line.
            printThird.run();
        }
    }
}