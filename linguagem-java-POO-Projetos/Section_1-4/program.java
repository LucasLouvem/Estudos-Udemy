// import java.util.Locale;

// void main(){
//     IO.print("Hello World"); // -> print() -> sem quebra de linha 
//     IO.println("\nBom dia"); // -> println() -> com quebra de linha

//     int x = 10;
//     IO.println(x);

//     double y = 3.145877512;
//     System.out.printf("%.2f%n", y); // -> %.2f -> formatação para 2 casas decimais

//     Locale.setDefault(new Locale("pt", "BR")); // -> setDefault() -> define o local para formatação de números
//     System.out.printf("%.2f%n", y); // -> %.2f -> formatação para 2 casas decimais

//     System.out.printf("Resultado: %.2f%n", y); // -> printf() -> com formatação de string
// }

// void main(){
//     String nome = "Lucas";
//     int idade = 23;
//     double renda = 2500.00;
//     System.out.printf("Nome: %s \nIdade: %d \nRenda: %.2f%n", nome, idade, renda); // -> printf() -> com formatação de string
// }

public class program {
    public static void main(String[] args){
        int a,b;
        double resultado;

        a = 10;
        b = 3;
        resultado = (double) a / b; // -> (double) -> casting para double
        System.out.printf("Resultado: %.2f%n", resultado); // -> %.2f -> formatação para 2 casas decimais
    }

    public static void main2(String[] args){
        double a;
        int b;

        a = 10;
        b = (int) a; // -> (int) -> casting para inteiro
        
        System.out.printf("Valor de b: %d%n", b); // -> %d -> formatação para inteiro
    }
}