
import java.util.ArrayList;

public class PowerOfTwoMaxHeap {
    private final ArrayList<Integer> heap;
    private final int branchingFactor; // Equal to 2^branchingPower

    public PowerOfTwoMaxHeap(int branchingPower) {
        if (branchingPower < 0 || branchingPower > 10) {
            throw new IllegalArgumentException("branchingPower must be >= 0 and reasonably small.");
        }
        this.branchingFactor = 1 << branchingPower; // 2^branchingPower
        this.heap = new ArrayList<>();
    }

    public void insert(int value) {
        heap.add(value);
        siftUp(heap.size() - 1);
    }

    public int popMax() {
        if (heap.isEmpty()) {
            throw new IllegalStateException("Heap is empty.");
        }

        int max = heap.get(0);
        int lastIndex = heap.size() - 1;
        if (lastIndex == 0) {
            return heap.remove(0);
        }

        heap.set(0, heap.remove(lastIndex));
        siftDown(0);
        return max;
    }

    private void siftUp(int index) {
        while (index > 0) {
            int parentIndex = (index - 1) / branchingFactor;
            if (heap.get(index) > heap.get(parentIndex)) {
                swap(index, parentIndex);
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    private void siftDown(int index) {
        int size = heap.size();
        while (true) {
            int largest = index;
            for (int i = 1; i <= branchingFactor; i++) {
                int childIndex = branchingFactor * index + i;
                if (childIndex < size && heap.get(childIndex) > heap.get(largest)) {
                    largest = childIndex;
                }
            }
            if (largest != index) {
                swap(index, largest);
                index = largest;
            } else {
                break;
            }
        }
    }

    private void swap(int i, int j) {
        int temp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, temp);
    }

    // Optional: for testing purposes
    public void printHeap() {
        System.out.println(heap);
    }

    public static void main(String[] args) {
        // Example: branchingPower = 1 -> binary heap; branchingPower = 2 -> 4-ary heap
        PowerOfTwoMaxHeap heap = new PowerOfTwoMaxHeap(2);

        int[] testValues = {50, 20, 15, 30, 10, 60, 80, 90};
        for (int val : testValues) {
            heap.insert(val);
        }

        System.out.println("Heap after insertions:");
        heap.printHeap();

        System.out.println("Max value popped: " + heap.popMax());
        System.out.println("Heap after popMax:");
        heap.printHeap();
    }
}
