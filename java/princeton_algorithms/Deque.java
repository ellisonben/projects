import java.util.NoSuchElementException;
import java.util.Iterator;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;

public class Deque<Item> implements Iterable<Item> {
    
    private Node first;
    private Node last;
    private int itemCount;
    
    private class Node {
        private Item item;
        private Node next;
        private Node previous;
    }
        
    // construct an empty deque
    public Deque() {
        itemCount = 0;
        first = null;
        last = null;
        assert check();
    }
    
    // is the deque empty?
    public boolean isEmpty() {
        return itemCount == 0;
    }
    
    // return the number of items on the deque
    public int size() {
        return itemCount;
    }
    
    // add the item to the front
    public void addFirst(Item item) {
        if (item == null) {
            throw new NullPointerException("item cannot be null value");
        }
        
        Node oldfirst = first;
        first = new Node();
        first.item = item;
        first.next = oldfirst;
        first.previous = null;
                
        if (isEmpty()) {
            last = first;
        } else {
            oldfirst.previous = first;
        }
        
        itemCount++;
        
        assert check();
    }
    
    // add the item to the end
    public void addLast(Item item) {
        if (item == null) {
            throw new NullPointerException("item cannot be null value");
        }
        
        Node oldlast = last;
        last = new Node();
        last.item = item;
        last.next = null;
        last.previous = oldlast;
        
        if (isEmpty()) {
            first = last;
        } else {
            oldlast.next = last;
        }
        
        itemCount++;
        
        assert check();
    }
    
    // remove and return the item from the front
    public Item removeFirst() {
        if (isEmpty()) {
            throw new NoSuchElementException("stack underflow");
        }
        Item item = first.item;
        first = first.next;
        
        itemCount--;
        
        if (isEmpty()) {
            last = null;
        } else {
            first.previous = null;
        }
        assert check();
        return item;
    }
    
    // remove and return the item from the end
    public Item removeLast() {
        if (isEmpty()) {
            throw new NoSuchElementException("stack underflow");
        }
        Item item = last.item;
        last = last.previous;
        
        itemCount--;
        
        if (isEmpty()) { 
            first = null;
        } else {
            last.next = null;
        }
        
        assert check();
        return item;
    }
    
    // return an iterator over items in order from front to end
    public Iterator<Item> iterator() {
        return new DequeIterator();
    }
    
    private class DequeIterator implements Iterator<Item> {
        private Node current = first;
        
        public boolean hasNext() { 
            return current != null; 
        }
        public void remove() { 
            throw new UnsupportedOperationException("remove() not supported");
        }
        public Item next() {
            if (hasNext()) {
                Item item = current.item;
                current = current.next;
                return item;
            } else {
                throw new NoSuchElementException("no more items in iteration");
            }
        }
    }
    
    
    private boolean check() {

        // check a few properties of instance variable 'first'
        if (itemCount < 0) {
            return false;
        }
        if (itemCount == 0) {
            if (first != null) return false;
        }
        else if (itemCount == 1) {
            if (first == null)      return false;
            if (first.next != null) return false;
        }
        else {
            if (first == null)      return false;
            if (first.next == null) return false;
        }

        // check internal consistency of instance variable n
        int numberOfNodes = 0;
        for (Node x = first; x != null && numberOfNodes <= itemCount; x = x.next) {
            numberOfNodes++;
        }
        if (numberOfNodes != itemCount) return false;

        return true;
    }
    
    // unit testing
    public static void main(String[] args) {
        Deque<String> deque = new Deque<String>();
        while (!StdIn.isEmpty()) {
            String item = StdIn.readString();
            if (!item.equals("-")) {
                deque.addFirst(item);
            }
            else if (!deque.isEmpty()) {
                StdOut.print(deque.removeFirst() + " ");
            }
        }
        StdOut.println("(" + deque.size() + " left in deque)");
    }
}