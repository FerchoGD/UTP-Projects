package proyecto_biblioteca.Modelo;

import java.util.ArrayList;


public class Ciudadano extends Usuario {
    String Ciudad;
    String Direccion;


    public Ciudadano(String Nombre, String Edad, String Id,String Tel,String Ciudad,String Direccion) {
        super(Nombre, Edad, Id,Tel);
        this.Ciudad=Ciudad;
        this.Direccion=Direccion;
    }

    public String getCiudad() {
        return Ciudad;
    }

    public void setCiudad(String Ciudad) {
        this.Ciudad = Ciudad;
    }
    
    public String getDireccion() {
        return Direccion;
    }

    public void setDireccion(String Dir) {
        this.Direccion = Dir;
    }
    
 /*   public boolean VerificarLib(Ciudadano c){
        if(c.getCantLibros()<2)
            return true;
        else
            return false;            
    }
   */ 
}
