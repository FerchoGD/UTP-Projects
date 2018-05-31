package proyecto_biblioteca.Controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JOptionPane;
import proyecto_biblioteca.Modelo.Libro;
import proyecto_biblioteca.Modelo.Modelo_operaciones;
import proyecto_biblioteca.Vista.Devolver;
import proyecto_biblioteca.Vista.Menu;

public class Controlador_Devolver implements ActionListener {
    Devolver vistaDevolver=new Devolver();
    Modelo_operaciones modeloDevolver=new Modelo_operaciones();
    
    public Controlador_Devolver(Devolver vistaDev,Modelo_operaciones modeloDev){
        this.modeloDevolver= modeloDev;
        this.vistaDevolver=vistaDev;
        this.vistaDevolver.AceptarButton.addActionListener(this);
    }
         
    public void actionPerformed(ActionEvent e){
        Libro L=modeloDevolver.getLibAux();
        vistaDevolver.CodeLibro.setText(modeloDevolver.getCodeLib());
        String code=modeloDevolver.IdPerson();
        String Codelib=vistaDevolver.CodeLibro.getText();
        modeloDevolver.Devolver(L);
        JOptionPane.showMessageDialog(vistaDevolver, "Proceso realizado con exito");
        JOptionPane.showMessageDialog(vistaDevolver, "Muchas gracias por su visita");
        vistaDevolver.setVisible(false);
        Menu Nuevo=new Menu();
        Controlador_Menu ContNuevo=new Controlador_Menu(Nuevo,modeloDevolver);
        Nuevo.setVisible(true);
        Nuevo.setLocationRelativeTo(null);
    }
    
}

