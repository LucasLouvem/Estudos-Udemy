import java.util.Scanner;

public class ex02 {
    public static void main(String[] args){

    double pi = 3.14159;
    double raio, area;

    Scanner sc = new Scanner(System.in);

    System.out.print("Digite o valor do raio: ");
    raio = sc.nextDouble();
    area = pi * Math.pow(raio, 2);
    System.out.printf("A área do círculo é: %.4f%n", area);
    sc.close();    
    
    }
}