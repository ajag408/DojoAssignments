import java.util.ArrayList;
import java.util.Collections;
public class PuzzleJavaTest {
    public static void main(String[] args) {
      // int[] myArr = {1, 5, 10, 7, -2};
      // ArrayList<Integer> shifted = basic.shiftFront(myArr);
      // System.out.println(shifted);

      PuzzleJava puzzling = new PuzzleJava();

      // int[] myArr = {3,5,1,2,7,9,8,13,25,32};
      // ArrayList<Integer> tenPlus = puzzling.puzzleOne(myArr);
      // System.out.println(tenPlus);

      ArrayList<String> myArr = new ArrayList<String>();
      Collections.addAll(myArr, "Nancy", "Jinichi", "Fujibayashi", "Momochi", "Ishikawa");
      ArrayList<String> names = puzzling.puzzleTwo(myArr);
      System.out.println(names);
    }
}
