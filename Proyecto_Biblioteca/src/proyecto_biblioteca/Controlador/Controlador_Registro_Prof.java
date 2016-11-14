package proyecto_biblioteca.Controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import proyecto_biblioteca.Modelo.Profesor;
import proyecto_biblioteca.Modelo.Modelo_operaciones;
import proyecto_biblioteca.Vista.Buscar;
import proyecto_biblioteca.Vista.Registro_Profesor;

public class Controlador_Registro_Prof implements ActionListener {
    
    Modelo_operaciones ModeloRegProf=new Modelo_operaciones();
    Registro_Profesor VistaRegProf=new Registro_Profesor();
    Profesor p=new Profesor(null,null,null,null,null,null);
    
    public Controlador_Registro_Prof(Modelo_operaciones M,Registro_Profesor P){
        this.ModeloRegProf=M;
        this.VistaRegProf=P;
        this.VistaRegProf.AceptarBT.addActionListener(this);
    }
    
    
    public void actionPerformed(ActionEvent e){
        String id=VistaRegProf.UserCode.getText();
        String Institucion=VistaRegProf.Institucion.getText();
        String Campo=VistaRegProf.CampoEns.getText();
        String Telefono=VistaRegProf.Telefono.getText();
        String Edad=VistaRegProf.EdadUser.getText();
        String Nombre=VistaRegProf.NombreUser.getText();
        p.setEdad(Edad);
        p.setNombre(Nombre);
        p.setId(id);
        p.setInstitucion(Institucion);
        p.setCampo(Campo);
        p.setTel(Telefono);        
        ModeloRegProf.Profesores.add(p);
        Buscar vistaB=new Buscar();
        Controlador_Buscar ContB=new Controlador_Buscar(vistaB,ModeloRegProf);
        vistaB.setVisible(true);
        vistaB.setLocationRelativeTo(null);
        VistaRegProf.setVisible(false);
    }
    
}
