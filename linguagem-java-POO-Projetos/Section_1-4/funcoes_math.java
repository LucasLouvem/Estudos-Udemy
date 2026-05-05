public class funcoes_math {
    // Math.sqrt() - Raiz quadrada
    // Math.pow() - Potenciação
    // Math.abs() - Valor absoluto
    // Math.ceil() - Arredonda para cima
    // Math.floor() - Arredonda para baixo
    // Math.round() - Arredonda para o inteiro mais próximo
    // Math.max() - Retorna o maior valor entre dois números
    // Math.min() - Retorna o menor valor entre dois números
    // Math.random() - Retorna um número aleatório entre 0.0 (inclusive) e 1.0 (exclusive)

    public static void main(String[] args) {
        double numero = 16.0;
        double raizQuadrada = Math.sqrt(numero);
        System.out.println("A raiz quadrada de " + numero + " é: " + raizQuadrada);

        double base = 2.0;
        double expoente = 3.0;
        double potencia = Math.pow(base, expoente);
        System.out.println(base + " elevado a " + expoente + " é: " + potencia);

        double valorNegativo = -5.0;
        double valorAbsoluto = Math.abs(valorNegativo);
        System.out.println("O valor absoluto de " + valorNegativo + " é: " + valorAbsoluto);

        double numeroDecimal = 3.7;
        double arredondadoParaCima = Math.ceil(numeroDecimal);
        System.out.println("Arredondando " + numeroDecimal + " para cima: " + arredondadoParaCima);

        double arredondadoParaBaixo = Math.floor(numeroDecimal);
        System.out.println("Arredondando " + numeroDecimal + " para baixo: " + arredondadoParaBaixo);

        long arredondadoProximo = Math.round(numeroDecimal);
        System.out.println("Arredondando " + numeroDecimal + " para o inteiro mais próximo: " + arredondadoProximo);

        double num1 = 5.0;
        double num2 = 10.0;
        double maximo = Math.max(num1, num2);
        System.out.println("O maior valor entre " + num1 + " e " + num2 + " é: " + maximo);

        double minimo = Math.min(num1, num2);
        System.out.println("O menor valor entre " + num1 + " e " + num2 + " é: " + minimo);

        double numeroAleatorio = Math.random();
        System.out.printf("Número aleatório entre 0 e 100: %d%n", (int)(numeroAleatorio * 100));
    
        int a = 2;
        int b = 8;
        int c = -24;
        double delta;

        delta = Math.pow(b, 2) - 4 * a * c;
        double x1, x2;
        x1 = (-b + Math.sqrt(delta)) / (2 * a);
        x2 = (-b - Math.sqrt(delta)) / (2 * a);
        System.out.println("O valor de delta é: " + delta);
        System.out.println("O valor de x1 é: " + x1);
        System.out.println("O valor de x2 é: " + x2);

    }
}
