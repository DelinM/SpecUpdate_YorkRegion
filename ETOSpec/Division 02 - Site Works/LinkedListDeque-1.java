package deque;

public class LinkedListDeque<T> {

    private class StuffNode {
        public IntNode prev;
        public T item;
        public IntNode next;

        public StuffNode(StuffNode p, T i, StuffNode n) {
            prev = p;
            item = i;
            next = n;
    }

    private StuffNode first;
    public int size;
    
    public LinkedListDeque(T x) {
        first = new StuffNode(null, x, null);
        size = 1;
    }

    
    public void addFirst(T x) {
        first.prev = new StuffNode(null, x, first)
        size++;

    }

    public void addLast(T x) {
        first.next = new StuffNode(first, x, null);

    }

    public boolean isEmpty() {

    }

    public int size() {

    }

    public void printDeque() {

    }

    public T removeFirst() {

    }

    public T removeLast() {

    }

    public T get(int index) {

    }

    public Iterator<T> iterator() {

    }

    public boolean equals(Object o) {

    }

    public static void main(String[] args){

    }
}

