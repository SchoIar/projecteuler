/*
 * Anton Ilic, Dec. 18, 2024
 * https://projecteuler.net/problem=5
 * 
 */
public class Main {

    /**
     * GCD using Euclidean algorithm, by copilot. 
     * 
     * @return GCD of a, b
     */
    public long GCD(long a, long b) {
        if (a == 0)
            return b;

        while (b != 0) {
            if (a > b)
                a = a - b;
            else
                b = b - a;
        }

        return a;
    }

    /**
     * Finds LCM of x, y
     * 
     * @return LCM using GCD
     */
    long find_LCM(long x, long y) {
        return ((x * y) / GCD(x, y));
    }

    /**
     * Finds smallest number that is evenly divisible by 1 to n
     * 
     * @param n integer
     * @return smallest number evenly divisible
     */
    long findSmallestNumber(int n) {
        long LCM = 1;
        for (int i = 1; i < n + 1; i++) { 
            LCM = find_LCM(LCM, i);
        }
        return LCM;
    }

    public static void main(String[] args) {
        Main myObj = new Main();
        System.out.println(myObj.findSmallestNumber(20));
    }
}
