public class Main{
    public long solution(){
        long sum = 0;
        long sum_of_squares = 0;
        for(int i = 1; i <= 100; i++){
            sum += i;
            sum_of_squares += (i * i);
        }

        return ((sum * sum) - sum_of_squares);
    }

    public static void main(String[] args) {
        Main myObj = new Main();
        System.out.println(myObj.solution());
    }

}