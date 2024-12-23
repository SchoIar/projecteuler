/**
 * Solution to https://projecteuler.net/problem=8
 * Anton Ilic, Dec 22. 
 */
public class Main {

    /**
     * Returns the value of the character at the index in the number
     */
    int getValue(String numStr, int index) {
        return Character.getNumericValue(numStr.charAt(index));
    }

    /*
     * Finds the largest product of n consecutive characters within the integer
     */
    int findLargestProduct(String number, int n){
        int largestProduct = 0;
        for(int i = 0; i <= number.length() - n; i++){
            //iterate thru current products
            int currentProduct = 1;

            for (int j = i; j < i + n; j++) {
                currentProduct *= getValue(number, j);
            }

            if (currentProduct > largestProduct) {
                largestProduct = currentProduct;
            }

        }

        return largestProduct;
    }
    public static void main(String[] args) {

    }
}
