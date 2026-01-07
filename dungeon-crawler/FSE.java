/* FSE
 * Runs the whole game, it creates the player's character and the rooms the player will have to go through.
 * It controls what the player can see on the screen through the draw method.
 */

import java.awt.*;
import java.awt.event.*;
import java.awt.MouseInfo;
import java.util.ArrayList;
import javax.swing.*;

public class FSE extends JFrame{
 GamePanel game= new GamePanel();
  
    public FSE() {
  super("Dungeon crawler");
  setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  add(game);
  pack();  // set the size of my Frame exactly big enough to hold the contents
  setVisible(true);
    }
    
    public static void main(String[] arguments) {
  new FSE();  
    }
}

class GamePanel extends JPanel implements KeyListener, ActionListener, MouseListener{
 public static final int INTRO=0, GAME=1,INFO=2;
 private boolean []keys;
 private int screen = INTRO;
 private Rectangle menuPlay,menuInfo,menuBack; // button hitboxes
 private Font fontComic,fontTitle;
 private Point mouse = new Point(0,0);
 private int mx,my; // mouse x, mouse y
 private Player user;
 private Room rooms;
 Timer timer;
 
 public GamePanel(){
  keys = new boolean[KeyEvent.KEY_LAST+1];
  user = new Player(KeyEvent.VK_W, KeyEvent.VK_S, KeyEvent.VK_A, KeyEvent.VK_D, KeyEvent.VK_SPACE);
  rooms = new Room();
  
  fontComic = new Font("Comic Sans MS", Font.PLAIN,32); // text font
  fontTitle = new Font("Comic Sans MS", Font.PLAIN,64); // Title font
  
  menuPlay = new Rectangle(300,400,200,50); // Play button
  menuInfo = new Rectangle(300,500,200,50); // FAQ button
  menuBack = new Rectangle(20,20,100,50); // Button to return to INTRO screen
  
  setPreferredSize(new Dimension(800, 600));
  timer = new Timer(10, this);
  timer.start();
  setFocusable(true);
  requestFocus();
  addKeyListener(this);
  addMouseListener(this);
 }

 public void move(){
// Player cursor location`
   try{ // use try and catch since it will sometimes crash when it doesn't detect mouse position
     mouse = MouseInfo.getPointerInfo().getLocation();
     Point offset = getLocationOnScreen();
     mouse.translate(-offset.x, -offset.y);
   }
   catch(IllegalComponentStateException ex){ // error it gives when it doesn't detect mouse
     System.out.println(ex);
   }
   if(screen == GAME){ // When player playing the game
     user.move(keys,rooms,mouse);
     rooms.newFloor();
     if(user.getHp() <= 0){ // When player dies, reset to floor 1
       rooms.setFloor(1);
       rooms.reset();
       user.setY(300);
       user.setHp(user.getMaxhp());
       screen = INTRO;
     }
   }
 }
 
 
 @Override
 public void actionPerformed(ActionEvent e){
  move();
  repaint();
 }
 
 @Override
 public void keyReleased(KeyEvent ke){
  int key = ke.getKeyCode();
  keys[key] = false;
 } 
 
 @Override
 public void keyPressed(KeyEvent ke){
  int key = ke.getKeyCode();
  keys[key] = true;
 }
 
 @Override
 public void keyTyped(KeyEvent ke){}

 @Override
 public void mouseClicked(MouseEvent e){}

 @Override
 public void mouseEntered(MouseEvent e){}

 @Override
 public void mouseExited(MouseEvent e){}

 @Override
 public void mousePressed(MouseEvent e){
  if(screen == INTRO){
    if(menuPlay.contains(mouse)){ // Click Play button: send to game screen
      screen = GAME;
    }
    if(menuInfo.contains(mouse)){ // Click FAQ button: send to FAQ screen
      screen = INFO;
    }
  }
  else if(screen == INFO){
    if(menuBack.contains(mouse)){ // Click back arrow: send to intro screen
      screen = INTRO;
    }
  }
  else if(screen == GAME){ // When in game, if clicked, attack or open inventory
    user.attack(mouse.x,mouse.y,e.getButton());
    user.inventory(mouse.x,mouse.y,e.getButton());
  }
 }

 @Override
 public void mouseReleased(MouseEvent e){
   
 }
 
 @Override
 public void paint(Graphics g){
   // Background
   g.setColor(Color.BLACK);
   g.fillRect(0,0,getWidth(),getHeight());
   //
   if(screen == INTRO){
     g.setColor(Color.RED);
     // Play Button
     g.fillRect((int)menuPlay.getX(),(int)menuPlay.getY(),(int)menuPlay.getWidth(),(int) menuPlay.getHeight());
     // FAQ Button
     g.fillRect((int)menuInfo.getX(),(int)menuInfo.getY(),(int)menuInfo.getWidth(),(int) menuInfo.getHeight());
     // Fonts
     g.setColor(Color.WHITE);
     g.setFont(fontComic);
     g.drawString("PLAY", 355,435);
     g.drawString("FAQ", 360,535);
     g.setFont(fontTitle);
     g.drawString("DUNGEON", 250,200);
     g.drawString("CRAWLER", 250,300);
   }
   if(screen == INFO){
     Image info = new ImageIcon("sprites/info.png").getImage(); // FAQ image
     g.drawImage(info, 0, 0,null);
     Image arrow = new ImageIcon("sprites/arrow.png").getImage(); // arrow image
     g.drawImage(arrow,(int)menuBack.getX(),(int)menuBack.getY(),null);
//     g.setColor(Color.RED);
//     g.fillRect((int)menuBack.getX(),(int)menuBack.getY(),(int)menuBack.getWidth(),(int) menuBack.getHeight());
   }
   if(screen == GAME){
     rooms.draw(g);
     user.draw(g);
   }
 }
}