import java.util.ArrayList;
public class BasicJava{
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

    public void print255(){
      for(int i = 1; i<256; i++){
        System.out.println(i);
      }
    }

    public void printOdd255(){
      for(int i = 1; i<256; i=i+2){
        System.out.println(i);
      }
    }

    public void printSum255(){
      int sum = 0;
      for(int i = 0; i<256; i++){
        sum = sum + i;
        System.out.println("New number: " + i + " Sum: " + sum);
      }
    }



  }
