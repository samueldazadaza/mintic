public class Condi {
    public static void main(String[] args){
        int temperatura = 39;
        if(temperatura > 37){
            System.out.println("temperatura alta");
        }else if (temperatura >= 36 && temperatura <=37){ //condicionales: &&:and, ||:or, !:not 
            System.out.println("temperatura ok");
        }else{
            System.out.println("Temperatura baja");
        }

        //forma corta del if
        String mensaje = (temperatura > 37) ? "Temp alta" : "Temp ok"; //operador ternario
        System.out.println(mensaje);
    }
}