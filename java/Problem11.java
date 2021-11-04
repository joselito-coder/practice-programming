import java.util.Scanner;

public class Problem11 {
    public static void main(String[] args) {
//        This practice problem is taken from the chapter 5 practice set
//        Q.1 Write a program to print the following pattern
//        ****
//        ***
//        **
//        *

//        Solution:
        for (int i = 4 ; i >= 0; i-- ){
            for (int j = 0 ; j <i ; j++){
                System.out.print("*");
            }
            System.out.println();
        }

    }
}
