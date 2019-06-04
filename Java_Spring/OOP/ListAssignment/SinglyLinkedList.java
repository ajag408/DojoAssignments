public class SinglyLinkedList {
    public Node head;
    public SinglyLinkedList() {
        head = null;
    }
    // SLL methods go here. As a starter, we will show you how to add a node to the list.
    public void add(int value) {
        Node newNode = new Node(value);
        if(head == null) {
            head = newNode;
        } else {
            Node runner = head;
            while(runner.next != null) {
                runner = runner.next;
            }
            runner.next = newNode;
        }
    }

    public void remove(){
      if(head == null){
        System.out.println("List is empty");
      }else{
        Node runner = head;
        if(runner.next == null){
          head = null;
        } else{
          while(runner.next.next != null){
            runner = runner.next;
          }
          runner.next = null;
        }
      }
    }

    public void printValues(){
      if(head == null){
        System.out.println("List is empty");
      }else{
        Node runner = head;
        while(runner.next != null){
          System.out.println(runner.value);
          runner = runner.next;
        }
        System.out.println(runner.value);
      }
    }

    public Node find(int value){
        boolean found = false;
        Node runner = head;
        while(runner != null){
          if(runner.value == value){
            found = true;
            break;
          }
          runner = runner.next;
        }
        if(found == false){
          System.out.println("Node not found");
          return null;
        } else {
          return runner;
        }
    }

    public void removeAt(int index){
      Node runner = head;
      int counter = 0;
      if(index == 0){
        if(runner == null){
          System.out.println("Index not valid, list empty");
        }else if(runner.next != null){
          head = runner.next;
        }else{
          head = null;
        }
      }else{
        while(counter<index-1 && runner!=null){
          runner = runner.next;
          counter++;
        }
        if(counter!=index-1 || runner == null){
          System.out.println("Index not valid");
        }else{
          runner.next = runner.next.next;
        }
      }
    }
}
