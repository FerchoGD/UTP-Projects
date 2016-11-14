
package proyecto_biblioteca.Modelo;

import java.util.ArrayList;

public class Profesor extends Usuario {
    String institucion;
    String campo_ensenanza;
    
    
    public Profesor (String Nombre,String Edad,String Id,String Tel,String institucion,String campo){
        super(Nombre,Edad,Id,Tel);
        this.institucion=institucion;
        this.campo_ensenanza=campo;
    }

    public String getInstitucion() {
        return institucion;
    }

    public void setInstitucion(String institucion) {
        this.institucion = institucion;
    }

    public String getCampo() {
        return campo_ensenanza;
    }

    public void setCampo(String c) {
        this.campo_ensenanza = c;
    }
    
    /*public boolean VerificarLib(Profesor c){
        if(c.getCantLibros()<6)
            return true;
        else
            return false;            
    }
    */
    
}
