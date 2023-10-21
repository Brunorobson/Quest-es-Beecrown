
import java.io.IOException;
import java.util.Scanner;
public class bee_1008 {
 
    public static void main(String[] args) throws IOException {
 
          Scanner entrada = new Scanner(System.in);
        int funcionarios = entrada.nextInt();
        int horas = entrada.nextInt();
        double valorPorHora = entrada.nextDouble();
        
        double salario = horas * valorPorHora;
        
        System.out.println("NUMBER = " + funcionarios);
        System.out.println(String.format("SALARY = U$ %.2f" , salario));
 
    }
 
}
