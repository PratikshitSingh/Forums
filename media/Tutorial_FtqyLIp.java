
import java.util.*;


class Tutorial {

  
    public static void main(String[] args) {
       Scanner in = new Scanner(System.in);
       int n = in.nextInt();
       int[] arr =  new int[n];
       for(int i=0;i<n;i++){
           arr[i] = in.nextInt();
           }
       Arrays.sort(arr);
       long maxpair = arr[n-2]*arr[n-1];
       System.out.println(maxpair);
    }
    
}