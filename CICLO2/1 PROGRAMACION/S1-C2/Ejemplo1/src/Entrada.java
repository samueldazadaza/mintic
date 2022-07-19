import java.util.Scanner;

public class Entrada {
    public static void main(String[] args){
        //clase entradas de consola
        Scanner entrada = new Scanner(System.in); //importar texto de consola
        System.out.println("Digite su nombre");
        String nombre = entrada.nextLine(); //metodo para leer string
        System.out.println("Digite su edad");
        int edad = entrada.nextInt(); //metodo para leer entero
        entrada.close(); // se recomienda cerrar la entrada de datos
        System.out.println("Te llamas: " + nombre + " y tu edad es: " + edad); //imprimir datos ingresados
    }
}
