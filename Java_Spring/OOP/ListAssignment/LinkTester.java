public class LinkTester {
    public static void main(String[] args) {
        SinglyLinkedList sll = new SinglyLinkedList();
        sll.add(3);
        sll.add(4);
        sll.add(10);
        sll.add(5);
        sll.add(15);
        sll.add(2);
        sll.removeAt(1);

        // Node newNode = sll.find(2);
        // System.out.println(newNode.value);
        sll.printValues();
    }
}
