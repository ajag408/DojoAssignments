public class PythagoreanTest {
    public static void main(String[] args) {
        Pythagorean triangle = new Pythagorean(); // 1
        double hypotenuse = triangle.calculateHypotenuse(3,4); // 2
        System.out.println("The hypotenuse is: " + String.valueOf(hypotenuse)); // 3
    }
}
