package proyecto_biblioteca.Controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import proyecto_biblioteca.Modelo.Estudiante;
import proyecto_biblioteca.Modelo.Modelo_operaciones;
import proyecto_biblioteca.Vista.Buscar;
import proyecto_biblioteca.Vista.Registro_Estudiante;

public class Controlador_Registro_Est implements ActionListener {
    
    Modelo_operaciones ModeloRegEst=new Modelo_operaciones();
    Registro_Estudiante VistaRegEst=new Registro_Estudiante();
    Estudiante E=new Estudiante(null,null,null,null,null,null);
    
    public Controlador_Registro_Est(Modelo_operaciones M,Registro_Estudiante E){
        this.ModeloRegEst=M;
        this.VistaRegEst=E;
        this.VistaRegEst.AceptarBT.addActionListener(this);
    }
    
    
    public void actionPerformed(ActionEvent e){
        String id=VistaRegEst.UserCode.getText();
        String Institucion=VistaRegEst.InstitucEst.getText();
        String Carrera=VistaRegEst.Programa.getText();
        String Telefono=VistaRegEst.Telefono.getText();
        String Edad=VistaRegEst.EdadUser.getText();
        String Nombre=VistaRegEst.NombreUser.getText();
        E.setEdad(Edad);
        E.setNombre(Nombre);
        E.setId(id);
        E.setInstitucion(Institucion);
        E.setPrograma(Carrera);
        E.setTel(Telefono);        
        ModeloRegEst.Estudiantes.add(E);
        Buscar vistaB=new Buscar();
        Controlador_Buscar ContB=new Controlador_Buscar(vistaB,ModeloRegEst);
        vistaB.setVisible(true);
        vistaB.setLocationRelativeTo(null);
        VistaRegEst.setVisible(false);
    }
    
}
