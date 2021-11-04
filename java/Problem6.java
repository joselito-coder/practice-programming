public class Problem6 {
    public static void main(String[] args) {
        // Implementing Selection sort Algorithm

        // Define the temperory number;
        int temp;

        // Define an array of intergers
        int arr[] = {3,1,4,9,5,10};

        // print out the numbers after sort
        System.out.println("Before Sort");
        for (int i : arr) {
            System.out.print(i+" ");
        }
        System.out.println();

        System.out.println("After sort");

        // The First loop is for checking the Ith number
        for(int i = 0 ; i<arr.length ; i++){

            // The Second loop is To check the iTh number against all other numbers
            for(int j = 0 ; j<arr.length ; j++){
                // If the number at i'th is less then the one at the Jth, swap out the number with j  
                if(arr[i] < arr[j]){
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }

        }

        // print out the numbers after sort
        for (int i : arr) {
            System.out.print(i+" ");
        }
        System.out.println();



    }
}
