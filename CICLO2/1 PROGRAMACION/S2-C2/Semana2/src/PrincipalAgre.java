public class PrincipalAgre {
    public static void main(String[] args){
        EstudianteAgre est1 = new EstudianteAgre("Luis", 123456, "MAT");
        EstudianteAgre est2 = new EstudianteAgre("Carolina", 456789, "SOC");
        EstudianteAgre est3 = new EstudianteAgre("Carlos", 987654, "MAT");
        EstudianteAgre est4 = new EstudianteAgre("Sofia", 654321, "SOC");

        //traer estudiantes por departamentos
        String[] estudiantesMat = {est1.nombre, est3.nombre};
        String[] estudiantesSoc = {est2.nombre, est4.nombre};

        DepartamentoAgre dpMat = new DepartamentoAgre("MAT", estudiantesMat);
        DepartamentoAgre dpSoc = new DepartamentoAgre("SOC", estudiantesSoc);

        //recorrer solo nombre de estudiantes de departamento Matematicas
        String[] tempo = dpMat.getEstudiantes();
        for(String i: tempo){
            System.out.println(i);
        }
        //recorrer solo nombre de estudiantes de departamento Sociales
        tempo = dpSoc.getEstudiantes();
        for(String i: tempo){
            System.out.println(i);
        }
        
        
    }
}
