/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package edu.faytecc.jan21_sunojoption_macka;

import javax.swing.JOptionPane;

/**
 *
 * @author macka2859
 */
public class Jan21_sunojoption_MackA {

    public static void main(String[] args) {
       // say hello in Joptionpane
       // it's probably kind of like cin and cout?
       JOptionPane.showMessageDialog(null, "Suno Helper", "", JOptionPane.WARNING_MESSAGE);
       // what I want the program to do is
       // I can type in like "rap" and phonk"
       // And it makes string like this:
       // "rap, rap, rap, phonk"
       // reason is, I want to try stuff in suno and automating things is easier
       String firstGenre = JOptionPane.showInputDialog(null, "What's one song genre?");   
       String secondGenre = JOptionPane.showInputDialog(null, "What's another song genre?"); 
      
       
       
       
       
       
       String mix = firstGenre +"," + secondGenre;  
       // String mix = secondGenre + firstGenre; // would be the other way
       // TODO: add a mic icon instead
       JOptionPane.showMessageDialog(null,mix, "here's your custom mix", JOptionPane.INFORMATION_MESSAGE);
       // Can we make this less typing? Yes! we'll do it later
       //tell(mix);
   
    }

    public static String ask(String question) {
        return JOptionPane.showInputDialog(null, question);
    }
   
    public static void tell(String mix) {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }

}   
    
    
    
    
    
    
    
    

