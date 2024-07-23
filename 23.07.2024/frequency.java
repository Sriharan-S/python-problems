import java.util.HashMap;
import java.util.Scanner;

public class FrequencyCount {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the number of elements: ");
        int n = scanner.nextInt();
        
        int[] arr = new int[n];
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        
        HashMap<Integer, Integer> frequencyMap = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            if (frequencyMap.containsKey(arr[i])) {
                frequencyMap.put(arr[i], frequencyMap.get(arr[i]) + 1);
            } else {
                frequencyMap.put(arr[i], 1);
            }
        }
        
        System.out.println("Frequency of elements:");
        for (int key : frequencyMap.keySet()) {
            System.out.println(key + ": " + frequencyMap.get(key));
        }
    }
}
