public class Arrays {
    public static void main(String[] args) {
        //declarar un array unidimensional
        String[] nombres = {"Juan", "Ana", "Pedro", "Sofia"};
        System.out.println(nombres[3]); //imprimir nombre sofia, posicion 3
        System.out.println("------------------------");
        
        for(int i = 0; i < nombres.length; i++){ //recorremos con los indices
            System.out.println(nombres[i]);
            
        }
        System.out.println("------------------------"); 
        // ciclo for each
        for(String nom:nombres) {
            System.out.println(nom);
        }
        
        System.out.println("------------------------");
        int[][] numeros = {{45,22,89},{12,36,78}}; // array bidimensional
        // 45  22  89
        // 12  36  78
        System.out.println(numeros[1][1]); // imprimir numero 36 [1,1] (columna1, fila 1)
        System.out.println("-----------------------------------");

        //recorrido de un array bidimensional con 2 for anidados
        for (int i=0; i<numeros.length; i++) {
            for (int j=0; j<numeros[i].length; j++) {
                System.out.println(numeros[i][j]);
            }
        }
        
        //recorrido de un array bidimensional con for each
        System.out.println("-----------------------------------------------");
        for (int[] i: numeros) {
            for (int j: i){
                System.out.println(j);
            }
        }

    }
}
