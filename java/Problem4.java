import java.util.Scanner;

public class Problem4{
    public static int inputHeight(String prompt){
        System.out.println(prompt);
        Scanner sc = new Scanner(System.in);
        int h;
        do{
            h = sc.nextInt();

        }while(h<1 || h > 8);

        return h;
    } 
    public static void main(String[] args) {

        int height  = inputHeight("Enter the height");

        for(int i = 0 ; i<height ;i++){

            for (int j = height-1; j >i; j--) {
                System.out.print(" ");
            }
            
            for( int k = -1 ; k<i; k++){
                System.out.printf("#");
            }
                        
            System.out.println();

        }
        
    }
}