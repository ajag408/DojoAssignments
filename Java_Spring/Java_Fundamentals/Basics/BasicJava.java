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

    public void iterateArr(Object[] array){
      for (int i = 0; i < array.length; i++){
        System.out.println(array[i]);
      }
    }

    public void findMax(int[] array){
      int max = array[0];
      for (int i = 1; i < array.length; i++){
        if(array[i]>max){
          max = array[i];
        }
      }
      System.out.println(max);
    }

    public void getAve(int[] arr){
      int sum = 0;
      for (int i = 0; i<arr.length; i++){
        sum = sum + arr[i];
      }
      int ave = sum/arr.length;
      System.out.println(ave);
    }

    public ArrayList<Integer> arrOdd255(){
      ArrayList<Integer> y = new ArrayList<Integer>();
      for (int i = 1; i<=255; i=i+2){
        y.add(i);
      }
      return y;
    }

    public void greaterThanY(int[] arr, int y){
      int count = 0;
      for (int i = 0; i<arr.length; i++){
        if(arr[i]>y){
          count++;
        }
      }
      System.out.println(count);
    }

    public ArrayList<Integer> squareArr(int[] arr){
      ArrayList<Integer> squareArr = new ArrayList<Integer>();
      for (int i = 0; i<arr.length; i++){
         squareArr.add(arr[i] * arr[i]);
      }
      return squareArr;
    }

    public ArrayList<Integer> posArr(int[] arr){
      ArrayList<Integer> posArr = new ArrayList<Integer>();
      for (int i = 0; i<arr.length; i++){
         if(arr[i]<0){
           arr[i] = 0;
         }
         posArr.add(arr[i]);
      }
      return posArr;
    }

    public ArrayList<Integer> minMaxAve(int[] arr){
      int max = arr[0];
      int min = arr[0];
      int sum = 0;
      for (int i = 1; i<arr.length; i++){
        if(arr[i]>max){
          max = arr[i];
        }
        if(arr[i]<min){
          min = arr[i];
        }
        sum = sum + arr[i];
      }
      int ave = sum/arr.length;
      ArrayList<Integer> minMaxAve = new ArrayList<Integer>();
      minMaxAve.add(max);
      minMaxAve.add(min);
      minMaxAve.add(ave);
      return minMaxAve;
    }

    public ArrayList<Integer> shiftFront(int[] arr){
      ArrayList<Integer> shifted = new ArrayList<Integer>();
      for (int i = 0; i<arr.length-1; i++){
        shifted.add(arr[i+1]);
      }
      shifted.add(0);
      return shifted;
    }


}
