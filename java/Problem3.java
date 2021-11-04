import java.util.Scanner;

/*
Buy Please Problem Code: BUYPLSE
 
Problem:
    Chef went to a shop and buys a pens and b pencils. Each pen costs x units and each pencil costs y units. Now find what is the total amount Chef will spend to buy a pens and b pencils.

*/

public class Problem3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String inp = sc.nextLine();
        sc.close();

        String[] split = inp.split(" ");

        int[] nums = new int[split.length];

        for (int i = 0; i < split.length; i++) {
        nums[i] = Integer.parseInt(split[i]); 
        }


        int total = 0;
        for (int i = 0; i < nums.length -1 ; i++) {
           if( i % 2 == 0){
               total += nums[i] * nums[i+1];
           }
            
        }

        System.out.println(total);
    
    }

}
