import java.util.Locale;
import java.util.Scanner;

public class scanner {
    public static void main(String[] args) {
        Locale.setDefault(new Locale("pt", "BR"));
        Scanner sc = new Scanner(System.in);
        
        // int x;
        // double y;
        // String name;

        // System.out.print("Digite um número inteiro: ");
        // x = sc.nextInt();
        // System.out.print("Digite um número decimal: ");
        // y = sc.nextDouble();
        // System.out.print("Digite seu nome: ");
        // name = sc.next();
        // char primeira_letra = name.charAt(0);
        

        // System.out.println("x = " + x);
        // System.out.println("y = " + y);
        // System.out.println("name = " + name);
        // System.out.println("primeira_letra = " + primeira_letra);

        int a;
        String ft1, ft2, ft3;

        a = sc.nextInt(); // -> vai ler um número inteiro, mas não consome a quebra de linha
        sc.nextLine(); // -> nextLine() -> para consumir a quebra de linha pendente
        ft1 = sc.nextLine();
        ft2 = sc.nextLine();
        ft3 = sc.nextLine();
        
        
        System.out.println("Comandos Digitados:");
        System.out.println(a);
        System.out.println(ft1);
        System.out.println(ft2);
        System.out.println(ft3);
        sc.close();
    }
}