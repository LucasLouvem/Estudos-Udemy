#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    // escrever na tela
    
    //strings
    printf("Oi Galera!\n");
    
    //Valor de uma variavel
    int a = 10;
    printf("%d\n", a);
    a = 20;
    printf("%d\n", a);

    //Texto misturado com variavel
    printf("O valor de a é: %d\n", a);

    //receber valor do usuario
    int b;
    printf("Digite um valor para b: ");
    scanf("%d", &b);
    printf("O valor de b é: %d\n", b);
}
