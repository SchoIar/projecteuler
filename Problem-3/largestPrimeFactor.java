
public class largestPrimeFactor {
    public static void main(String[] args) {
        long number =  600851475143L;
        largestPrimeFactor factor = new largestPrimeFactor();
        long largestPrimeFactor = factor.findLargestPrimeFactor(number);
        System.out.println(largestPrimeFactor);
    }

    /**
     * Finds the largest prime factor of the number. 
     * 
     * @param number Number which we wish to find the largest Prime factor of. 
     * @return largest Prime Factor
     */
    private long findLargestPrimeFactor(long number){
        long i = 2;
        while(i * i < number){
            while(number % i == 0){
                number = number / i;
            }
            i = i + 1;
        }
        return number;
    }

}
