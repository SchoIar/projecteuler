public class Main{
    int solution(){
        int current = 1; int next = 1; int temp = 0;
        int fOddSum = 0;
        while(current <= 4000000){
            if(current % 2 != 0)
                fOddSum += current;
            temp = current;
            current = next;
            next = next + temp;
        }
        return fOddSum;
    }

    public static void main(String[] args) {
        Main myObj = new Main();
        System.out.println(myObj.solution());
    }
}