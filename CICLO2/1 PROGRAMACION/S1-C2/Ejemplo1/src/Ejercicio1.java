import java.util.Scanner;

public class Ejercicio1 {
    // Variables (atributos o propiedades)
    // metodos o funciones
    // metodo main = podemos ejecutar main sin necesidad de intanciar a la clase (punto de arranque del programa)
    // instanciar = es crear un objeto de una clase
    // void = meodo que no retorna valor
    // public = el retorno puede ser visto por otras clases

    //variables
    private String nombre;
    private float nota; //dato primitivo
    private Scanner sc;

    //crear metodos
    public void  capturar(){
        sc = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        nombre = sc.nextLine();
        System.out.println("Digite su nota: ");
        nota = sc.nextFloat();
    }

    public void imprimir() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Nota: " + nota);
    }

    public void aprobar() {
        if (nota>=3) {
            System.out.println("Aprobado");
        }else {
            System.out.println("NO aprobo");
        }
    }

    //crear main para ejecutar al principio
    public static void main(String[] args) {
        Ejercicio1 obj1 = new Ejercicio1(); //crea una instacia de la clase Ejercicio1
        obj1.capturar(); //ya obj1 ya tiene metodos que podemos utilizar
        obj1.imprimir();
        obj1.aprobar();

    }


}
