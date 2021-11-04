import java.util.Scanner;

class Problem7{

    public static String input( String prompt){

        // Importing Scanner class and creating a scanner object
        Scanner sc = new Scanner(System.in);
        String userInput;
        
        // Asking the input
        System.out.println(prompt);
        userInput = sc.nextLine();
        
        return userInput;

    }
    public static void main(String[] args) {
        // Practice set 3 Java

        // Question 1
        // Write a java program to convert a string to lower case
        // Solution:
        // Store the user input inside a variable
        // String userInp = input("Enter Your string");

        // String lowerString = userInp.toLowerCase();
        // System.out.println("Your string in lowercase is:\n "+lowerString);

        // Question 2
        // Write a java program to replace spaces with underscores;
        // Solution:

        // String userInp = input("Enter String: ");

        // String convertedString = userInp.replace(" ", "_");
        // System.out.println(convertedString);

        // Question 3
        // Write a java program to fill in a letter template which looks like:
        // letter = "Dear <|name|>, Thanks a lot"
        // replace <|name|> with a string (some name);

        // Create the template for the name 
        // String letterTemplate = "Dear name, Thanks a lot";

        // // ask the user for input
        // String userInp = input("Enter your name");

        // // replace name placeholder with a actuall name
        // String replaced = letterTemplate.replace("name", userInp);

        // // print out the results
        // System.out.println(replaced);

        // Question 4 
        // Write a java program to detect doubel and triple spaces in a string.

        // Solution:

        // String strWithSpaces = "This string has double spaces  and triple    spaces";

        // Check for the double or triple spaces using .contains function
        // if(strWithSpaces.contains("  ") || strWithSpaces.contains("   ")){
        //     System.out.println("The string has double or triple spaces");
        // }
        // else{
        //     System.out.println("The string does not have double or triple spaces");
        // }

        // Question 5
        // Write a program to format the following letter using escape sequence characters.
        // letter = "Dear Harry, This java Course is nice. Thanks"

        // We can achieve the above by escaping the double quotes
        String letter = "\"Dear Harry, This Java Course is nice. Thanks \"";
        System.out.println(letter);



        


    }
}