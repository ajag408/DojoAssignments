import java.util.ArrayList;
public class BasicJavaTest {
    public static void main(String[] args) {
      BasicJava basic = new BasicJava();


      // basic.print255();

      // basic.printOdd255();

      // basic.printSum255();

      // Object[] myArr = {1,3,5,7,9,13};
      // basic.iterateArr(myArr);

      // int[] myArr = {1,3,0,-3,-5,-7};
      // basic.findMax(myArr);

      // int[] myArr = {3,9,100};
      // basic.getAve(myArr);

      // ArrayList<Integer> y = basic.arrOdd255();
      // System.out.println(y);

      // int[] myArr = {1,3,5,7};
      // basic.greaterThanY(myArr,3);

      // int[] myArr = {1,5,10,-2};
      // ArrayList<Integer> returnSquareArr = basic.squareArr(myArr);
      // System.out.println(returnSquareArr);

      // int[] myArr = {1,5,10,-2};
      // ArrayList<Integer> posArr = basic.posArr(myArr);
      // System.out.println(posArr);

      // int[] myArr = {0};
      // ArrayList<Integer> tripleThreat = basic.minMaxAve(myArr);
      // System.out.println(tripleThreat);

      int[] myArr = {1, 5, 10, 7, -2};
      ArrayList<Integer> shifted = basic.shiftFront(myArr);
      System.out.println(shifted);
    }
}
