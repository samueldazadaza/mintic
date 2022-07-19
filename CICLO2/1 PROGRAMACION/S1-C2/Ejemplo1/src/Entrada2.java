import java.util.Scanner;
public class Entrada2 {
    public static void main(String[] args){
         //leer varias lineas al tiempo en consola
         Scanner entrada2 = new Scanner(System.in);
         System.out.println("Digita ciudad, edad, estatura");
         String ciudad = entrada2.nextLine();
         int edad2 = entrada2.nextInt();
         double estatura = entrada2.nextDouble();
         entrada2.close(); // cerrar entrada de datos
         System.out.println("ciudad: " + ciudad + ", Edad: " + edad2 + ", estatura: " + estatura );
    }
}
