import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Arkanoid extends JFrame{
 ArkanoidPanel game= new ArkanoidPanel();
  
    public Arkanoid() {
  super("Arkanoid");
  setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  add(game);
  pack();  // set the size of my Frame exactly big enough to hold the contents
  setVisible(true);
    }    
    public static void main(String[] arguments) {
  new Arkanoid();  
    }
}