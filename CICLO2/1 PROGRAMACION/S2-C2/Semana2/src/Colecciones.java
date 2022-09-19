import java.util.ArrayList;

public class Colecciones {
    public static void main(String[] args) {
        // ArrayList
        // principal caracteristica= tiene longitud variable.
        // Es una clase del paquete java.util
        // Es una coleccion compuesta por un solo tipo de objetos.
        ArrayList<String> ciudades = new ArrayList<String>();
        ciudades.add("Cali"); // add, es un metodo que sirve para añadir un elemento al final de la lista
        ciudades.add("Tunja");
        ciudades.add("Barranquilla");
        ciudades.add("Pereira");
        System.out.println(ciudades);
        ciudades.add(2, "Medellin");
        System.out.println(ciudades);
        ciudades.set(0, "Bucaramanga");
        System.out.println(ciudades);
        ArrayList<Integer> numAleatorios = new ArrayList<Integer>();
        for (int i = 0; i < 21; i++){
            Integer numAleatorio = (int)(Math.random()*100);
            numAleatorios.add(numAleatorio);
        }
        System.out.println(numAleatorios);
        
    }
}
