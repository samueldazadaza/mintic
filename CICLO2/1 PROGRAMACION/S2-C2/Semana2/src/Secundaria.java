public class Secundaria {
    //atributos
    private String nombre = "Juan";
    //Encapsulamiento: ocultar los atributos y accederlos a traves de los metodos de la 
    //getters y setter
    public void setNombre(String nombre){ // setters se utilzan para modificar los atributos de la clase
        this.nombre = nombre;
    }
    public String getNombre(){ // el getter si devuelve algo // variable de solo lectura
        return nombre;
    }
}
