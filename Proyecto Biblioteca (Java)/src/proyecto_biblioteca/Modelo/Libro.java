package proyecto_biblioteca.Modelo;

import java.util.ArrayList;
import proyecto_biblioteca.Modelo.*;

public class Libro {
    String Nombre;
    String Editorial;
    String Categoria;
    String Autor;
    String Codigo;
    boolean disponible;
    String Fecha_entrega;
    String Fecha_devolucion;
    String Usuario_libro;
    
    public Libro(String Nombre,String Editorial,String Categoria,String Autor,String Code,boolean disp,String FechaEntrega,String FechaDevolucion,String Usuario_libro){
        this.Nombre= Nombre;
        this.Autor=Autor;
        this.Categoria=Categoria;
        this.Editorial=Editorial;
        this.Codigo=Code;
        this.disponible=disp;
        this.Fecha_entrega=FechaEntrega;
        this.Fecha_devolucion=FechaDevolucion;
        this.Usuario_libro=Usuario_libro;
        
        
    }

    public String getUsuario_libro() {
        return Usuario_libro;
    }

    public void setUsuario_libro(String Usuario_libro) {
        this.Usuario_libro = Usuario_libro;
    }

    public String getCodigo() {
        return Codigo;
    }

    public void setCodigo(String Codigo) {
        this.Codigo = Codigo;
    }

    public boolean isDisponible() {
        return disponible;
    }

    public void setDisponible(boolean disponible) {
        this.disponible = disponible;
    }

    public String getFecha_entrega() {
        return Fecha_entrega;
    }

    public void setFecha_entrega(String Fecha_entrega) {
        this.Fecha_entrega = Fecha_entrega;
    }

    public String getFecha_devolucion() {
        return Fecha_devolucion;
    }

    public void setFecha_devolucion(String Fecha_devolucion) {
        this.Fecha_devolucion = Fecha_devolucion;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public String getEditorial() {
        return Editorial;
    }

    public void setEditorial(String Editorial) {
        this.Editorial = Editorial;
    }

    public String getCategoria() {
        return Categoria;
    }

    public void setCategoria(String Categoria) {
        this.Categoria = Categoria;
    }

    public String getAutor() {
        return Autor;
    }

    public void setAutor(String Autor) {
        this.Autor = Autor;
    }
    
     
    
}
