public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        int num = 25; //declarando la variable num
        System.out.println(num);
        String nombre = "Omar"; // string es una clase
        System.out.println(nombre);
        var apellido = "Diaz"; //cuando se declara una variable con var, Java infiere el tipo de variable
        System.out.println(apellido.getClass().getSimpleName());
        System.out.println(((Object)num).getClass().getSimpleName()); //num es un dato primitivo y con object lo convierto en objeto para poder acceder a propiedades y metodos
        Integer conta = 10;
        System.out.println(conta);
    }
}
