public class ex03 {
    int a, b, c, d;
    
    public static void main(String[] args){
        ex03 obj = new ex03();
        obj.a = 5;
        obj.b = 6;
        obj.c = -7;
        obj.d = 8;
        int diferenca = (obj.a * obj.b - obj.c * obj.d);
        System.out.println("A diferença é: " + diferenca);
    }
}
