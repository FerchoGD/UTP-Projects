package proyecto_biblioteca.Controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JOptionPane;
import proyecto_biblioteca.Modelo.Modelo_operaciones;
import proyecto_biblioteca.Vista.Buscar;
import proyecto_biblioteca.Vista.Devolver;
import proyecto_biblioteca.Vista.Menu;
import proyecto_biblioteca.Vista.Prestar;

public class Controlador_Buscar implements ActionListener {    
   
    Buscar vistaBuscar=new Buscar();
    Modelo_operaciones modeloBuscar=new Modelo_operaciones();
   
    
    public Controlador_Buscar(Buscar vistaBuscar,Modelo_operaciones modeloBuscar){
        this.modeloBuscar=modeloBuscar;
        this.vistaBuscar=vistaBuscar;
        this.vistaBuscar.BuscarButton.addActionListener(this);
        
    }
    
    
    public void actionPerformed(ActionEvent e){
        boolean a=false;
        String b=null;
        String Nombre= vistaBuscar.LibroNombre.getText();
        String Operacion=String.valueOf(vistaBuscar.POD.getSelectedItem());
        a= modeloBuscar.BuscarLibro(Nombre);
        
        if(a){
            if(Operacion=="Prestamo"){
                Prestar vistaPrestar=new Prestar();
                vistaPrestar.CodeLibro.setText(modeloBuscar.getCodeLib());
                Controlador_Prestar ContPrest=new Controlador_Prestar(vistaPrestar,modeloBuscar);
                vistaPrestar.setVisible(true);
                vistaPrestar.setLocationRelativeTo(null);
                vistaBuscar.setVisible(false);
                
            
             }else{ Devolver vistaDevolver=new Devolver();
                    vistaDevolver.CodeUser.setText(modeloBuscar.IdPerson());
                    vistaDevolver.CodeLibro.setText(modeloBuscar.getCodeLib());
                    Controlador_Devolver contDev=new Controlador_Devolver(vistaDevolver,modeloBuscar);
                    vistaDevolver.setVisible(true);
                    vistaDevolver.setLocationRelativeTo(null);
                    vistaBuscar.setVisible(false);
                
             }        
        }else{
            if(Operacion == "Prestamo"){
                JOptionPane.showMessageDialog(vistaBuscar, "operacion no disponible");
            }else{
                Devolver vistaDevolver=new Devolver();
                    vistaDevolver.CodeUser.setText(modeloBuscar.IdPerson());
                    vistaDevolver.CodeLibro.setText(modeloBuscar.getCodeLib());
                    Controlador_Devolver contDev=new Controlador_Devolver(vistaDevolver,modeloBuscar);
                    vistaDevolver.setVisible(true);
                    vistaDevolver.setLocationRelativeTo(null);
                    vistaBuscar.setVisible(false);
            }
                
        }
    }
}
