import java.util.Locale;
import java.util.Scanner;

public class ex04 {

    public static void main(String[] args){
        Locale.setDefault(new Locale("pt", "BR"));
        Scanner scanner = new Scanner(System.in);

        int number;
        double horasTrabalhadas;
        double valorHora;
        double salario;

        System.out.print("Digite o número do funcionário: ");
        number = scanner.nextInt();
        System.out.print("Digite as horas trabalhadas: ");
        horasTrabalhadas = scanner.nextDouble();
        System.out.print("Digite o valor da hora trabalhada: ");
        valorHora = scanner.nextDouble();

        salario = horasTrabalhadas * valorHora;
        System.out.printf("Número: %d%n", number);
        System.out.printf("Salário: R$ %.2f%n", salario);    
    }    
}
