package proyecto_biblioteca.Controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JOptionPane;
import proyecto_biblioteca.Modelo.Ciudadano;
import proyecto_biblioteca.Modelo.Estudiante;
import proyecto_biblioteca.Modelo.Modelo_operaciones;
import proyecto_biblioteca.Modelo.Profesor;
import proyecto_biblioteca.Vista.Buscar;
import proyecto_biblioteca.Vista.Menu;
import proyecto_biblioteca.Vista.Prestar;
import proyecto_biblioteca.Vista.Registro_Ciudadano;
import proyecto_biblioteca.Vista.Registro_Estudiante;
import proyecto_biblioteca.Vista.Registro_Profesor;


public class Controlador_Menu implements ActionListener {
    Menu vistaMenu=new Menu();
    Modelo_operaciones modeloMenu=new Modelo_operaciones();
    Ciudadano C=new Ciudadano(null,null,null,null,null,null); 
    Profesor P=new Profesor(null,null,null,null,null,null);
    Estudiante E=new Estudiante(null,null,null,null,null,null);
    
    public Controlador_Menu(Menu vistaMenu,Modelo_operaciones modeloMenu){
        this.modeloMenu= modeloMenu;
        
        this.vistaMenu=vistaMenu;
        this.vistaMenu.AceptarMenu.addActionListener(this);  
    }    
  
    public void actionPerformed(ActionEvent e){
        boolean a = false;
        String id= vistaMenu.identificacion.getText();
        String Categoria= String.valueOf(vistaMenu.Desplegable.getSelectedItem());
        a=modeloMenu.BuscarPersona(id, Categoria); 
        
        if(a){
            JOptionPane.showMessageDialog(vistaMenu,"Bienvenido");
            Buscar vistaB=new Buscar();
            Controlador_Buscar ContB=new Controlador_Buscar(vistaB,modeloMenu);
            vistaB.setVisible(true);
            vistaB.setLocationRelativeTo(null);
            vistaMenu.setVisible(false);
            
        }else{
            JOptionPane.showMessageDialog(vistaMenu,"usuario no registrado");
            switch (Categoria) {
                case "Profesor":
                    Registro_Profesor vistaRP=new Registro_Profesor();
                    vistaRP.UserCode.setText(id);
                    Controlador_Registro_Prof ContRP=new Controlador_Registro_Prof(modeloMenu,vistaRP);
                    vistaRP.setVisible(true);
                    vistaRP.setLocationRelativeTo(null);                  
                    vistaMenu.setVisible(false);
                    break;
                case "Estudiante":
                    Registro_Estudiante vistaRE=new Registro_Estudiante();
                    vistaRE.UserCode.setText(id);
                    Controlador_Registro_Est ContRE=new Controlador_Registro_Est(modeloMenu,vistaRE);
                    vistaRE.setVisible(true);
                    vistaRE.setLocationRelativeTo(null);
                    vistaMenu.setVisible(false);
                    break;
                default:
                    Registro_Ciudadano vistaRC=new Registro_Ciudadano();
                    vistaRC.UserCode.setText(id);
                    Controlador_Registro_Ciud ContRC=new Controlador_Registro_Ciud(modeloMenu,vistaRC);
                    vistaRC.setVisible(true);
                    vistaRC.setLocationRelativeTo(null);
                    vistaMenu.setVisible(false);
                    break;
            }
        }   
            
        
    }

    
    
}
