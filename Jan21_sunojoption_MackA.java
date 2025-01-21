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
    
    }
}
