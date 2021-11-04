import java.util.Scanner;

class Problem5{
    public static void main(String[] args) {
        // Implementing Linear search in java
        int userNum;

        // Taking the user input
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Your number to be search");
        userNum =  sc.nextInt();

        // Get The user Input

        //array of intergets 
        int arr[] = {1,2,3,4,5,7};

        for(int i = 0 ; i<arr.length ; i++)
        {
            if(arr[i] == userNum)
            {
                System.out.println("Your number is found");
                return;
            }
        }

        System.out.println("Your number is not found ;(");

    }
}