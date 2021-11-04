import java.util.Scanner;

public class Problem9 {

    // Declaring a function to take input(int) from the user
    public static int userInputInt(String prompt){
        Scanner sc = new Scanner(System.in);
        System.out.println(prompt);
        int userInt = sc.nextInt();
        return userInt;
    }
    public static void main(String[] args) {
        /*
            This practice set is taken from chapter 4 practiceSet from codeWithHarry's :
            "java Tutorials for beginners " youtube playlist. all credit goes to https://www.youtube.com/playlist?list=PLu0W_9lII9agS67Uits0UnJyrYiXhDS6q
        */

        // Q1. What will be the output of the below program:
        // int a = 10;
        // if(a = 11)
            //     System.out.println("I am 11");
            // else 
            //     System.out.println("I am not 11");

        // The above program will print out an error because a single = sign means it's an assignment statement, and hence it's not comparing those two values.

        // Testing the code below
        //    int a = 10;
        // if(a = 11)
        //         System.out.println("I am 11");
        //     else 
        //         System.out.println("I am not 11");

        // Q2. Write a program to find out whether a student is pass or fail; if it requires total 40% and atleast 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user;

        // initializing the variables to hold marks
        int maths,science,physics;

        // Taking input from user
        maths = userInputInt("Enter marks in maths");
        science = userInputInt("Enter marks in science");
        physics = userInputInt("Enter marks in physics");

        // calculating the average
        float average = (maths+science+physics)/3.0f;

        if(average >= 40 && maths >= 33 && science >= 33 && physics >= 33){
            System.out.println("The student has passed");
        }
        else{
            System.out.println("The student has failed");
        }
        

    }
}
