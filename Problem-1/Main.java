// Description: Solution to Project Euler, Question 1;
//              Computes the sum of multiples of 3 OR 5 under 1000
public class Main {
    int solution(){
        int sum = 0;
        for(int i = 0; i < 1000; i++){
            if(i % 3 == 0 || i % 5 == 0){
                sum += i;
            }
        }
        return sum;
    }
    public static void main(String[] args) {
      Main myObj = new Main();
      System.out.println(myObj.solution());
  }
}