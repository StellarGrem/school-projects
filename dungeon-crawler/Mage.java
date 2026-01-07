/* Mage
 * Samuel Huang
 * Enemy mage, located in every room, it will spawn in a random loaction within in the room
 * and not move. Every ~2 seconds, it will launch a spell towards the user
 */

import java.awt.*;
import java.util.ArrayList;
import javax.swing.*;

class Mage extends Enemy{
 private int delay=0,frame=0;
 private Image[] mage_back;
 private Image[] mage_front;
 private Image[] mage_left;
 private Image[] mage_right;
 private ArrayList<Projectile> spellList = new ArrayList<Projectile>();
 private static final double SPEED=3,WAIT=38;
 //                 projectile speed, wait time between frames
 
 public Mage(int x, int y){
   super(x,y,75,"mage"); // This calls the constructor from Unit
   attackCD=200;
   loadSprites();
 }
 
 public void loadSprites(){
   mage_back = new Image[6]; // When mage aims straight up
   mage_front = new Image[6]; // When mage aims straight down
   mage_left = new Image[6]; // When mage aims left
   mage_right = new Image[6]; // When mage aims right
   for(int i=0;i<6;i++){
     mage_back[i] = new ImageIcon("sprites/mage/mage_back"+i+".png").getImage();
     mage_front[i] = new ImageIcon("sprites/mage/mage_front"+i+".png").getImage();
     mage_left[i] = new ImageIcon("sprites/mage/mage_left"+i+".png").getImage();
     mage_right[i] = new ImageIcon("sprites/mage/mage_right"+i+".png").getImage();
   }
 }
 
 public ArrayList<Projectile> getSList(){return spellList;}
 public Rectangle getRect(){return new Rectangle((int)x-10,(int)y-10,20,20);}
 public void hit(int damage){ // when the user hits the mage
   hp -= damage; // mage takes damage
   System.out.println(hp);
 }
 
 public void draw(Graphics g){
   for(Projectile p: spellList){ // projectiles it casts
     p.draw(g);
   }
   if(u != null && u.getRoom().getRect().contains(x,y)){ // only animate frames when it is in the same room as the player
     delay += 1;
     if(delay % WAIT == 0){
       frame = (frame + 1) % 6;
     }
   }
//   g.setColor(Color.BLUE);
//   g.fillOval(x-10,y-10,20,20);
   // limitations that determine which sprite to use
   if(Math.abs(400-x) < 30 && 300 < y){ // uses the mage sprite that aims up
     g.drawImage(mage_back[frame], x-mage_back[frame].getWidth(null)/2, y-mage_back[frame].getHeight(null)/2, null);
   }
   else if(Math.abs(400-x) < 30 && 300 > y){ // uses the mage sprite that aims down
     g.drawImage(mage_front[frame], x-mage_front[frame].getWidth(null)/2, y-mage_front[frame].getHeight(null)/2, null);
   }
   else if(400 < x){ // uses the mage sprite that aims left
     g.drawImage(mage_left[frame], x-mage_left[frame].getWidth(null)/2, y-mage_left[frame].getHeight(null)/2, null);
   }
   else if(400 > x){ // uses the mage sprite that aims right
     g.drawImage(mage_right[frame], x-mage_right[frame].getWidth(null)/2, y-mage_right[frame].getHeight(null)/2, null);
   }
 }
 
 public void move(ArrayList<Enemy> list, Player user){
   if(u == null){u = user;} // sets u to the user to be accessed when user isn't sent through a parameter (mainly draw)
   if(attackCD != 0){
     attackCD--; // lowers cooldown
   }
   attack(user);
 }
 
 private void attack(Player user){
   double dist = Math.hypot(user.getX() - x, user.getY() - y);
   double vx = SPEED * (user.getX() - x) / dist;
   double vy = SPEED * (user.getY() - y) / dist;
   
   if(attackCD == 0){
     spellList.add(new Projectile(x,y,vx,vy));
     attackCD = 200;
   }
   for(Projectile p: new ArrayList<Projectile>(spellList)){
     p.move();
     if(p.getRect().intersects(user.getHitbox())){ // hits the player
       spellList.remove(p);
       user.hit(5);
     }
     if(!user.getRoom().getRect().contains((int)p.getX(),(int)p.getY())){ // hits the walls of the room
       spellList.remove(p);
     }
   }
 }
}