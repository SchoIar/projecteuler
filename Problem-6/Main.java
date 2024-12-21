/**
 * Anton Ilic, Dec 20, 2024
 * Solution to https://projecteuler.net/problem=6
 * 
 */
public class Main {

    /**
     * Returns the difference of sum of squares and square of sum for 1 to n.
     * 
     */
    public long solution(int n) {
        long sum = 0;
        long sum_of_squares = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
            sum_of_squares += (i * i);
        }

        return ((sum * sum) - sum_of_squares);
    }

    public static void main(String[] args) {
        Main myObj = new Main();
        System.out.println(myObj.solution(100));
    }

}