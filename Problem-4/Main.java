/*
 * #Anton Ilic, Dec. 18, 2024
 * https://projecteuler.net/problem=4
 * 
 */

public class Main {

    // String reversal function from https://www.geeksforgeeks.org/java-reverse-number-program/
    int reverse_function(int n){
        int rem; 
        int rev = 0;
        while (n > 0) { 
            rem = n % 10; 
            rev = (rev * 10) + rem; 
            n = n / 10; 
        } 
  
        return rev; 
    }

    boolean isPalindrome(int input){
        return (reverse_function(input) == input);
    }

    int findLargestPalindrome(){
        int max = 0;
        for(int i = 0; i < 1000; i++){
            for(int j = 0; j < 1000; j++){
                int product = i * j;
                if(isPalindrome(product) & product > max){
                    max = product;
                }
            }
        }

        return max;
    }

    public static void main(String[] args) {
        Main myObj = new Main();
        System.out.println(myObj.findLargestPalindrome());
    }

}
