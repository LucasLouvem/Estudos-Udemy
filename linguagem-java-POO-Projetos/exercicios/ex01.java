import java.util.Scanner;

public class ex01 {
    public static void main(String[] args){
        int x, y;

        Scanner sc = new Scanner(System.in);
        System.out.print("Digite o primeiro valor: ");
        x = sc.nextInt();
        System.out.print("Digite o segundo valor: ");
        y = sc.nextInt();
        int soma = x + y;
        System.out.println("A soma dos dois valores é: " + soma);
        sc.close();
    }
}