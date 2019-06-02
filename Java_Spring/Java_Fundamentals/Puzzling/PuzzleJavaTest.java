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

      // ArrayList<String> myArr = new ArrayList<String>();
      // Collections.addAll(myArr, "Nancy", "Jinichi", "Fujibayashi", "Momochi", "Ishikawa");
      // ArrayList<String> names = puzzling.puzzleTwo(myArr);
      // System.out.println(names);

      // ArrayList<Character> myArr = new ArrayList<Character>();
      // Collections.addAll(myArr, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z');
      // puzzling.puzzleThree(myArr);

      // int[] myArr = puzzling.puzzleFour();
      // for(int i = 0; i<10; i++){
      //   System.out.println(myArr[i]);
      // }

      // ArrayList<Integer> myArr = puzzling.puzzleFive();
      // System.out.println(myArr);
      // int max = myArr.get(0);
      // int min = myArr.get(0);
      // for(int i = 1; i<10; i++){
      //   if(myArr.get(i)>max){
      //     max = myArr.get(i);
      //   }
      //   if(myArr.get(i)<min){
      //     min = myArr.get(i);
      //   }
      // }
      // System.out.println("Min: " + min + " max: " + max);

      // String s = puzzling.puzzleSix();
      // System.out.println(s);

      ArrayList<String> myArr = puzzling.puzzleSeven();
      System.out.println(myArr);
    }
}
