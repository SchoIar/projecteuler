/*
 * Anton Ilic, Dec. 20, 2024
 * https://projecteuler.net/problem=7
 * 
 */
public class Main {

    public boolean isPrime(int n){
        if(n == 2){
            return true;
        }

        if(n % 2 == 0){
            return false;
        }

        for(int i = 3; i < n; i++){
            if(n % i == 0){
                return false;
            }
        }
        return true;
    }

    public int solution(){
        int i = 2; int primeCount = 0;
        while(true){
            if(isPrime(i)){
                primeCount += 1;
                if(primeCount == 10001){
                    return i;
                }
            }
            i++;
        }
    }

    public static void main(String[] args) {
        Main main = new Main();
        System.out.println(main.solution());
    }
}
