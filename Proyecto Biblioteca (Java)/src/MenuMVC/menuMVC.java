/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the edi
 */
package MenuMVC;

import proyecto_biblioteca.Controlador.Controlador_Menu;
import proyecto_biblioteca.Modelo.Modelo_operaciones;
import proyecto_biblioteca.Vista.Menu;

/**
 *
 * @author sebastian
 */
public class menuMVC {
    
    public static void main(String[] args) {
        Menu vistaM=new Menu();
        Modelo_operaciones modeloM=new Modelo_operaciones();
        modeloM.Llenar_libreria();
        modeloM.Llenar_Usuarios();
        Controlador_Menu ControladorM= new Controlador_Menu(vistaM,modeloM);
        vistaM.setVisible(true);
        vistaM.setLocationRelativeTo(null);
    }
    
}
