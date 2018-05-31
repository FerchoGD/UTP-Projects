package proyecto_biblioteca.Modelo;

import java.util.ArrayList;

public class Estudiante extends Usuario {
    String programa;
    String institucion;
    
    
    public Estudiante (String Nombre,String Edad,String Id,String Tel,String institucion,String programa){
        super(Nombre,Edad,Id,Tel);
        this.institucion=institucion;
        this.programa=programa;
    }

    public String getPrograma() {
        return programa;
    }

    public void setPrograma(String programa) {
        this.programa = programa;
    }

    public String getInstitucion() {
        return institucion;
    }

    public void setInstitucion(String institucion) {
        this.institucion = institucion;
    }
    
}
