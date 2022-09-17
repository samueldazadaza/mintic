public class Constructor { //metodo constructor es que tiene el mismo nombre de la clase
    String nombre;
    int edad;
    public Constructor() { // el nombre del constructor debe coincider con el nombre de la clase, no tiene retorno
        nombre = "Maria";
        edad = 25;
    }
    public static void main(String[] args) {
        Constructor c = new Constructor();
        System.out.println(c.nombre);
        System.out.println(c.edad);
    }
}
