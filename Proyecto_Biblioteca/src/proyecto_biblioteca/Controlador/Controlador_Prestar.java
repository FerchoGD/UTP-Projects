package proyecto_biblioteca.Controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JOptionPane;
import proyecto_biblioteca.Modelo.Estudiante;
import proyecto_biblioteca.Modelo.Libro;
import proyecto_biblioteca.Modelo.Modelo_operaciones;
import proyecto_biblioteca.Vista.Menu;
import proyecto_biblioteca.Vista.Prestar;

public class Controlador_Prestar implements ActionListener {
    Prestar vistaPrestarReg=new Prestar();
    Modelo_operaciones modeloPrestarR=new Modelo_operaciones();
    
    
    public Controlador_Prestar(Prestar vistaPrestarReg,Modelo_operaciones modeloPrestarR){
        this.modeloPrestarR= modeloPrestarR;
        this.vistaPrestarReg=vistaPrestarReg;
        this.vistaPrestarReg.AceptarPrest.addActionListener(this);
        
    }
         
    public void actionPerformed(ActionEvent e){
        Libro L=modeloPrestarR.getLibAux();
        String FechaEntrega=vistaPrestarReg.Fecha_Entrega.getText();
        String FechaDevuelta=vistaPrestarReg.Fecha_Devolucion.getText();       
        modeloPrestarR.Prestar(L, FechaEntrega, FechaDevuelta);
        JOptionPane.showMessageDialog(vistaPrestarReg, "Proceso realizado con exito");
        JOptionPane.showMessageDialog(vistaPrestarReg, "Muchas gracias por su visita");
        vistaPrestarReg.setVisible(false);
        Menu Nuevo=new Menu();
        Controlador_Menu ContNuevo=new Controlador_Menu(Nuevo,modeloPrestarR);
        Nuevo.setVisible(true);
        Nuevo.setLocationRelativeTo(null);
    }
    
}
