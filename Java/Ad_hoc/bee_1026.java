package Java.Ad_hoc;

import java.io.IOException;
import java.util.Scanner;
public class bee_1026 {
 
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()){
            long u = sc.nextLong();
            long m = sc.nextLong();
            System.out.println(u ^ m);
        }
 
    }
 
}
