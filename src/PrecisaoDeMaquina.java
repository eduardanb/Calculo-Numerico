public class PrecisaoDeMaquina {
    public static void main(String[] args) {
        // Programa com o objetivo de determinar a precisão de uma máquina
        float eps = 1.0f;
        float eps1;
        do {
            eps = eps / 2;
            eps1 = eps + 1;
            System.out.printf(" - EPS = %f vale zero%n", eps);
            System.out.printf(" - EPS1 = %f vale zero%n", eps1);
        } while (eps1 > 1.0);
        
        System.out.printf("A máquina acha que EPS = %f vale zero%n", eps);
    }
}
