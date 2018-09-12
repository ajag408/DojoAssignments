public class StringManipulatorTest {
    public static void main(String[] args) {
      StringManipulator manipulator = new StringManipulator();
      String str = manipulator.trimAndConcat("    Hello     ","     World    ");
      System.out.println(str); // HelloWorld 
    }
}
