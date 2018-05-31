package proyecto_biblioteca.Modelo;

import java.util.ArrayList;

public class Usuario {
    private String Nombre;
    private String Edad;
    private String Id;
    private String Tel;
 //   private double Multas;
   // private int CantLib;
    
    
    public Usuario(String Nombre,String Edad,String Id,String Tel){
        this.Nombre= Nombre;
        this.Edad=Edad;
        this.Id=Id;
        this.Tel=Tel;
     //   this.Multas=0;
       // this.CantLib=0;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public String getEdad() {
        return Edad;
    }

    public void setEdad(String Edad) {
        this.Edad = Edad;
    }

    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }

    public String getTel() {
        return Tel;
    }

    public void setTel(String Tel) {
        this.Tel = Tel;
    }

   

    
}
