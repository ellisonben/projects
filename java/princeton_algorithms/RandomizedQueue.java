import edu.princeton.cs.algs4.StdRandom;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class RandomizedQueue<Item> implements Iterable<Item> {
    
    private Item[] queue;
    private int itemCount;    
    
    // construct an empty randomized queue
    public RandomizedQueue() {
        itemCount = 0;
        queue = (Item[]) new Object[2];
    }
    
    // is the queue empty?
    public boolean isEmpty() {
        return itemCount == 0;
    }
    
    // return the number of items on the queue
    public int size() {
        return itemCount;
    }
    
    // used to resize the array
    private void resize(int capacity) {
        assert capacity >= itemCount;

        Item[] temp = (Item[]) new Object[capacity];
        for (int i = 0; i < itemCount; i++) {
            temp[i] = queue[i];
        }
        queue = temp;
    }
    
    // add the item
    public void enqueue(Item item) {
        if (item == null) {
            throw new NullPointerException("item cannot be null value");
        }
        if (itemCount == queue.length) { 
            resize(2*queue.length);
        }
        queue[itemCount++] = item;
    }
    
    // remove and return a random item
    public Item dequeue() {
        if (isEmpty()) {
            throw new NoSuchElementException("stack underflow");
        }
        int rand = StdRandom.uniform(itemCount);
        
        Item item = queue[rand];
        queue[rand] = queue[--itemCount];
        queue[itemCount] = null;
               
        if (itemCount > 0 && itemCount == queue.length/4) {
            resize(queue.length/2);
        }
        return item;
    }
    
    // return (but do not remove) a random item
    public Item sample() {
        if (isEmpty()) {
            throw new NoSuchElementException("stack underflow");
        }
        return queue[StdRandom.uniform(itemCount)];
    }
    
    // return an independent iterator over items in random order
    public Iterator<Item> iterator() {
        return new RandQueueIterator();
    }
    
    private class RandQueueIterator implements Iterator<Item> {

        private int i;
        
        public RandQueueIterator() {
            i = itemCount - 1;
            StdRandom.shuffle(queue, 0, itemCount-1);
        }
        
        public boolean hasNext() { 
            return i >= 0;
        }
        
        public void remove() { 
            throw new UnsupportedOperationException("remove() not supported");
        }
        
        public Item next() {
            if (hasNext()) {
                return queue[i--];
            } else {
                throw new NoSuchElementException("no more items in iteration");
            }
        }
    }
    
    // unit testing
    public static void main(String[] args) {
    }
}