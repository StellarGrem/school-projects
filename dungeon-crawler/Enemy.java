/* Enemy
 * Samuel Huang
 * A superclass which boss, mage, and swordsman inherits from to
 * have "pre-made" methods and a constructor that they are access and extend from
 * without having to create one for each enemy within the game
 */

import java.awt.*;
import java.util.ArrayList;

class Enemy{
 protected int x, y;
 protected double hp;
 protected int attackCD; // attack cooldown
 protected String type; // type of enemy (boss, mage, or swordsman)
 protected Player u; // variable for the player to access its methods without it in the parameter of methods
 
 // Mage exclusive
 protected ArrayList<Projectile> spellList;
 // Swordsman exclusive (also Boss exclusive)
 protected int ax,ay; // attackX, attackY
 // Boss exclusive
 protected ArrayList<Rectangle> unsafe;
 
 public Enemy(int xx, int yy, int h, String typ){
  x = xx;
  y = yy;
  hp = h;
  type = typ;
 }
 
 // These are placeholders so that subclasses can implement
 public Rectangle getRect(){
   return new Rectangle((int)x,(int)y,20,20);
 }
 
 public void loadSprites(){
 
 }
 
 public void hit(int damage){
 
 }
 
 public void attack(){
   
 }
 
 public void move(ArrayList<Enemy> list,Player user){

 }
 
 public void draw(Graphics g){
  
 }
 
 // Swordsman Exclusive
 
 
 // Mage Exclusive
 public ArrayList<Projectile> getSList(){
   return spellList;
 }
 
 // Boss Exclusive (also Swordsman Exclusive)
 public void setAy(int v){ay = v;}
 public int getAy(){return ay;}
 public void setAx(int v){ax = v;}
 public int getAx(){return ax;}
 public ArrayList<Rectangle> getUnsafe(){return unsafe;}
 
}