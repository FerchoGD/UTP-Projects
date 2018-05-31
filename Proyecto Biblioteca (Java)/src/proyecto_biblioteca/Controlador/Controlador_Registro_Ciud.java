package proyecto_biblioteca.Controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JOptionPane;
import proyecto_biblioteca.Modelo.Ciudadano;
import proyecto_biblioteca.Modelo.Libro;
import proyecto_biblioteca.Modelo.Modelo_operaciones;
import proyecto_biblioteca.Vista.Registro_Ciudadano;
import proyecto_biblioteca.Vista.Buscar;

public class Controlador_Registro_Ciud implements ActionListener {
    
    Modelo_operaciones ModeloRegCiud=new Modelo_operaciones();
    Registro_Ciudadano VistaRegCiud=new Registro_Ciudadano();
    Ciudadano c=new Ciudadano(null,null,null,null,null,null);
    
    public Controlador_Registro_Ciud(Modelo_operaciones M,Registro_Ciudadano R){
        this.ModeloRegCiud=M;
        this.VistaRegCiud=R;
        this.VistaRegCiud.AceptarBT.addActionListener(this);
    }
    
    
    public void actionPerformed(ActionEvent e){
        String id=VistaRegCiud.UserCode.getText();
        String Nombre=VistaRegCiud.NombreUser.getText();
        String Ciudad=VistaRegCiud.City.getText();
        String Telefono=VistaRegCiud.Telefono.getText();
        String Edad=VistaRegCiud.EdadUser.getText();
        String Direccion=VistaRegCiud.Direccion.getText();
        c.setId(id);
        c.setCiudad(Ciudad);
        c.setDireccion(Direccion);
        c.setNombre(Nombre);
        c.setTel(Telefono);
        c.setEdad(Edad);
        ModeloRegCiud.Ciudadanos.add(c);
        Buscar vistaB=new Buscar();
        Controlador_Buscar ContB=new Controlador_Buscar(vistaB,ModeloRegCiud);
        vistaB.setVisible(true);
        vistaB.setLocationRelativeTo(null);
        VistaRegCiud.setVisible(false);
    }
    
}
