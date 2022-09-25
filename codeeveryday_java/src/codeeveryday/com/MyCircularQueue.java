package codeeveryday.com;

class MyCircularQueue {
    private int[] queue;
    private int front=0;
    private int rear=0;

    private int used =0;

    private int size;

    public MyCircularQueue(int k) {
        this.queue=new int[k];
        this.size = k;
    }

    public boolean enQueue(int value) {
        if (isFull()){
            return false;
        }
        else if (front < queue.length-1){
            queue[front+1] = value;
            front += 1;
        }
        else if (front == queue.length){
            queue[0]=value;
            front=0;
        }
        used ++;
        return true;
    }

    public boolean deQueue() {

        if (isEmpty()==true){
            return false;
        }
        else if (rear < queue.length-1){
            rear += 1;
        }
        else if (rear == queue.length){
            rear=0;
        }
        used --;
        return true;
    }

    public int Front() {
        if (isEmpty()){
            return -1;
        }
        return queue[front];
    }

    public int Rear() {
        if (isEmpty()){
            return -1;
        }
        return queue[rear];
    }

    public boolean isEmpty() {
        if (used == 0){
            return true;
        }
        return false;
    }

    public boolean isFull() {
        if (used == size){
            return true;
        }
        return false;
    }
}
