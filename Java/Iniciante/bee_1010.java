package Java.Iniciante;

import java.io.IOException;
import java.util.Scanner;
public class bee_1010 {
 
    public static void main(String[] args) throws IOException {
   Scanner entrada = new Scanner(System.in);
        int A = entrada.nextInt();
        int B = entrada.nextInt();
        double C = entrada.nextDouble();
        int D = entrada.nextInt();
        int E = entrada.nextInt();
        double F = entrada.nextDouble();
        double resultado = (B*C)+(E*F);
        System.out.printf("VALOR A PAGAR: R$ %.2f\n",resultado);
    }
 
}
