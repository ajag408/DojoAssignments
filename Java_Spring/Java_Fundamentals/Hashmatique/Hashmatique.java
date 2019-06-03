import java.util.HashMap;
import java.util.Set;
public class Hashmatique{
  public static void main(String[] args) {
      HashMap<String, String> trackList = new HashMap<String, String>();
      trackList.put("No Home", "I ain't got no home");
      trackList.put("Red Tie", "Wear a red tie with my tie dye");
      trackList.put("Hare", "Got read hear");
      trackList.put("Scott Danley", "What's a pig to a bigger pig?");
      // get the keys by using the keySet method


      String sample = trackList.get("Hare");
      System.out.println(sample);

      Set<String> keys = trackList.keySet();
      for(String key : keys) {
          System.out.println(key + ": " + trackList.get(key));
      }
  }


}
