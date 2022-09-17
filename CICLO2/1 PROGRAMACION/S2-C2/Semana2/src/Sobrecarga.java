public class Sobrecarga {
    // En Java varios metodos pueden tener el mismo nombre con diferentes parametros
    // static significa que puedo acceder al metodo sin necesidad de instanciar(sin crear un objeto para)
    static int suma(int a, int b) {
        return a + b;
    }
    static float suma(float a, float b) {
        return a + b;
    }
    public static void main(String[] args) {
        int s1 = suma(7, 8);
        System.out.println(s1);
        float s2 = suma(45.8F, 3.2F); //el numero va con F al final ya que su tamaño en bits es mas grande, sin la F quiere decir que el dato que va a retomar es un double pero debo cambiar toda la estructura (double a, double b)
        System.out.println(s2);
    }
}
