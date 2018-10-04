import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
public class PuzzleJava{
    // public String trimAndConcat(String one, String two) {
    //   String oneTrim = one.trim();
    //   String twoTrim = two.trim();
    //   String concat = oneTrim + twoTrim;
    //   return concat;
    // }
    //
    // public Integer getIndexOrNull(String word, char letter){
    //   int index = word.indexOf(letter);
    //   if(index >= 0){
    //     return index;
    //   } else{
    //     return null;
    //   }
    // }

    public ArrayList<Integer> puzzleOne(int[] arr){
      int sum = 0;
      ArrayList<Integer> tenPlus = new ArrayList<Integer>();
      for (int i = 0; i<arr.length; i++){
        if(arr[i]>10){
          tenPlus.add(arr[i]);
        }
        sum = sum + arr[i];
      }
      System.out.println("Sum: "+ sum);
      return tenPlus;
    }

}
