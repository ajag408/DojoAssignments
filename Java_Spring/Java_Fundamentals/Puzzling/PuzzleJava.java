import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
import java.nio.charset.Charset;
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

    public ArrayList<String> puzzleTwo(ArrayList<String> arr){
      Collections.shuffle(arr);
      ArrayList<String> gtFive = new ArrayList<String>();
      for(int i = 0; i<arr.size(); i++){
        System.out.println(arr.get(i));
        if(arr.get(i).length() > 5){
          gtFive.add(arr.get(i));
        }
      }
      return gtFive;

    }

    public void puzzleThree(ArrayList<Character> arr){
      Collections.shuffle(arr);
      System.out.println("Last one: " + arr.get(25));
      char first = arr.get(0);
      System.out.println("First one: " + first);
      if(first == 'a' || first == 'e' || first == 'i' || first == 'o' || first == 'u'){
        System.out.println("First is a vowel");
      }
    }

    public int[] puzzleFour(){
      Random r = new Random();
      int[] randArr = new int[10];
      for(int i = 0; i<10; i++){
        // System.out.println(r.nextInt(46));
        randArr[i] = r.nextInt(46) + 55;
      }
      return randArr;
    }

    public ArrayList<Integer> puzzleFive(){
      Random r = new Random();
      ArrayList<Integer> randArr = new ArrayList<Integer>();
      for(int i = 0; i<10; i++){
        // System.out.println(r.nextInt(46));
        randArr.add(r.nextInt(46) + 55);
      }
      Collections.sort(randArr);
      return randArr;
    }

    public String puzzleSix(){
      byte[] array = new byte[5];
      new Random().nextBytes(array);
      String generatedString = new String(array, Charset.forName("UTF-8"));

      return generatedString;
    }

    public ArrayList<String> puzzleSeven(){
      ArrayList<String> randArr = new ArrayList<String>();
      for(int i = 0; i<10; i++){
        byte[] array = new byte[5];
        new Random().nextBytes(array);
        String generatedString = new String(array, Charset.forName("UTF-8"));
        randArr.add(generatedString);
      }
      return randArr;
    }

}
