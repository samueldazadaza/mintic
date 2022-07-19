public class Cadenas {
    public static void main(String[] args){
        //clase String
        String ciudad = "Barranquilla";
        System.out.println(ciudad.length()); // ver cantidad de caracteres de una cadena, con el metodo .length
        System.out.println(ciudad.indexOf("arr")); //devuelve la posicion de una parte de cadena
        System.out.println(ciudad.toUpperCase()); // metodo que convierte a mayusculas
        System.out.println(ciudad.equals("Barranquilla"));//compara 2 cadenas de caracteres y devuelve un boleano
    }
}
