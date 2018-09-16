public class StringManipulator {
    public String trimAndConcat(String one, String two) {
      String oneTrim = one.trim();
      String twoTrim = two.trim();
      String concat = oneTrim + twoTrim;
      return concat;
    }

    public Integer getIndexOrNull(String word, char letter){
      int index = word.indexOf(letter);
      if(index >= 0){
        return index;
      } else{
        return null;
      }
    }

    public Integer getIndexOrNull(String word, String substring){
      int index = word.indexOf(substring);
      if(index >= 0){
        return index;
      } else{
        return null;
      }
    }

    public String concatSubstring(String first, int one, int two, String second){
      String subby = first.substring(one, two);
      String concat = subby + second;
      return concat;
    }
  }
