import java.util.Scanner;


/*
Practice problem from codechef.com

Problem:
    Life, the Universe, and Everything Problem Code: TEST

    Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything. More precisely… rewrite small numbers from input to output. Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.

*/

// Solution

class Problem2{
    public static void main(String[] args) {
        int num;
        Scanner sc = new Scanner(System.in);

        while(true){
            num = sc.nextInt();
            if(num == 42){
                break;
            }
            System.out.println(num);

        }

        sc.close();
    }
}