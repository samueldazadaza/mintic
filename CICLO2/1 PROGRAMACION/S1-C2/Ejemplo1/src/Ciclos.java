//crear contador
public class Ciclos {
    public static void main(String[] args) {
        int conta = 6;

        //evalua la condicion al principio
        while (conta <= 5){
            System.out.println(conta);
            conta++;
        }
        System.out.println("-----------------------------");
        conta = 1;

        //evalua la condicion al final del ciclo, estoasegura que por lo menos se ejecuta una vez
        do{
            System.out.println(conta);
            conta++;
        }while(conta<=5);

        //ciclo for
        System.out.println("------------------------");
        for(int i=1; i<6; i++){
            System.out.println(i);
        }
    }
}