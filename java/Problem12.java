import java.util.Scanner;

public class Problem12 {
    public static void main(String[] args) {

//        Q.2 write a program to sum first n even numbers using while loop

//        Solution:
        int i = 0;
        int n;
        int sum = 0;

//        Take user input for n
//        use scanner class for taking input
        Scanner sc = new Scanner(System.in);
//        prompt the user for input
        System.out.println("Enter a number");
//        Store user input in variable n
        n = sc.nextInt();

//        Get the first n even numbers
        n = n * 2;
        while ( i <= n ){
//          If the number is even add it to sum
            if ( i %2 == 0){
                sum += i;
            }
//          increment the counter
            i++;
        }
//      Print the final sum
        System.out.println("The sum is : "+sum );

    }
}
