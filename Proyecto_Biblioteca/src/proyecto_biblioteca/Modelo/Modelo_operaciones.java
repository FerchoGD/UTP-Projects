/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyecto_biblioteca.Modelo;

import java.util.ArrayList;

/**
 *
 * @author sebastian
 */
public class Modelo_operaciones {
    
    public ArrayList<Libro> Libreria=new ArrayList<Libro>();
    public ArrayList<Estudiante> Estudiantes=new ArrayList<Estudiante>();
    public ArrayList<Profesor> Profesores=new ArrayList<Profesor>();
    public ArrayList<Ciudadano> Ciudadanos=new ArrayList<Ciudadano>();
    
    //Aquí vamos a insertar los libros que nos van a servir como base de datos
    Libro L1=new Libro("Cien años de soledad","x","Novela","Gabriel","1111",true,null,null,null);
    
    Libro L4=new Libro("El Resplandor","x","Terror","Stphen","1121",true,null,null,null);
    
    
    public void Llenar_libreria(){
        Libreria.add(L1);
        
        Libreria.add(L4);
        
    }
    
    Estudiante E1=new Estudiante("Fernando Giraldo","23","5555","3105909612","UTP","Ingenieria de sistemas");
    Ciudadano C1=new Ciudadano("Benito", "54", "31403545","2140657","Pereira","Cll 12 #12-33");
    Profesor P1=new Profesor ("Sebastian","32","39856748","2121212","UTP","Matematicas");
    //Aquí vamos a insertar los usuarios que nos van a servir como BD
    public void Llenar_Usuarios(){
        Estudiantes.add(E1);
        Ciudadanos.add(C1);
        Profesores.add(P1);
    }   
    
    String codeLibAux;
    String NombreLib;
    String CodePerson;
    Libro LibAux;
    String ClassPerson;
    
     public String getTypePerson(){
        return ClassPerson;
    }
    
    public String getCodeLib(){
        return codeLibAux;
    }
    
    public String getNombLib(){
        return NombreLib;
    }
    
    public String IdPerson(){
        return CodePerson;
    }
    
    public Libro getLibAux(){
        return LibAux;
    }
    
    public boolean BuscarLibro(String nombre){
        boolean disponible=false;
        for(int i=0;i<this.Libreria.size();i++){
            if(this.Libreria.get(i).getNombre().equals(nombre) && this.Libreria.get(i).isDisponible())
                disponible=true;
                this.codeLibAux=this.Libreria.get(i).getCodigo();
                NombreLib=nombre;
                this.LibAux=this.Libreria.get(i);
        }        
        return disponible;
    }
    
    public boolean BuscarPersona(String ID,String c){       
        boolean existe=false;
        if(c.equals("Ciudadano")){
            for(int i=0;i<this.Ciudadanos.size();i++){
            if(this.Ciudadanos.get(i).getId().equals(ID)){
                existe=true;
                this.ClassPerson="Ciudadano";
            }
            }
        }
        else if (c.equals("Estudiante")){
            for(int i=0;i<this.Estudiantes.size();i++){
            if(this.Estudiantes.get(i).getId().equals(ID)){
                existe=true;                 
                this.ClassPerson="Estudiante";
            }
            } 
        }
        else {
            for(int i=0;i<this.Profesores.size();i++){
            if(this.Profesores.get(i).getId().equals(ID))
                existe=true;                
               this.ClassPerson="Profesor";
        }           
        }
        this.CodePerson=ID;
        return existe;
    }
    public ArrayList<Libro> LibrosAmano;
    public void Prestar(Libro L,String FechaEntrega,String FechaDevolucion){
        L.setFecha_entrega(FechaEntrega);
        L.setFecha_devolucion(FechaDevolucion);
        L.setDisponible(false);
        
    }
  

    
    public void Devolver(Libro L){
        L.setFecha_entrega(null);
        L.setFecha_devolucion(null);
        L.setDisponible(true);
        
    }
    
    
    
}
