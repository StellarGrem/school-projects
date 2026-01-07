/* Boss
 * Controls what the boss does when the player reaches floor 5.
 *  - Its attacks, hp, the damage done to the player and itself
 *  - Attacks: bullet-hell, targetted meteor, 3 lava-boxes
 */

import java.awt.*;
import java.util.ArrayList;
import javax.swing.*;

class Boss extends Enemy{
 private int time=-100;
 private int phase=1; // was to depict the phase the boss was at, but was never implemented
 private int ax,ay,mode;
 private double radius;
 private double ang = 90;
 private Boolean userHurt = false; // for meteor attack: only hurt player once if hit
 private ArrayList<Rectangle> unsafe = new ArrayList<Rectangle>();
 private ArrayList<Projectile> spellList = new ArrayList<Projectile>();
 private Image bosspic = new ImageIcon("sprites/boss.png").getImage();
 private static final double SPEED=3;
         //    400       200
 public Boss(int x, int y){
   super(x,y,2500,"boss");
   attackCD = 100;
 }

 public ArrayList<Projectile> getSList(){return spellList;}
 public ArrayList<Rectangle> getUnsafe(){return unsafe;}
 public Rectangle getRect(){return new Rectangle(x-bosspic.getWidth(null)/2, y-bosspic.getHeight(null)/2,bosspic.getWidth(null),bosspic.getHeight(null));}
 
 public void setAy(int v){ay = v;}
 public int getAy(){return ay;}
 public void setAx(int v){ax = v;}
 public int getAx(){return ax;}
 
 public void hit(int damage){
   if(time > 1000 && time <= 1500){
     hp -= damage;
     System.out.println(hp);
   }
 }
 
 public void draw(Graphics g){
   if(mode==1 || spellList.size() != 0){ // bullet-hell
     for(Projectile p: spellList){
       p.draw(g);
     }
   }
   else if(mode==2){ // meteor attack
     g.setColor(Color.RED);
     g.drawOval(ax-50,ay-50,100,100); // max radius before it actually hurts the player
     g.fillOval((int)(ax-radius),(int)(ay-radius),(int)(2*radius),(int)(2*radius)); // showcases how close it is to completion
   }
   else if(mode==3){ // 3 lava-boxes
     if(attackCD > 70){
       g.setColor(new Color(255,0,0,100)); // transparent to tell user the danger spots to avoid
     }
     else{
       g.setColor(Color.RED); // the color when it will hurt the player
     }
     for(Rectangle r: unsafe){
       g.fillRect((int)r.getX(),(int)r.getY(),(int)r.getWidth(),(int)r.getHeight());
     }
   }
   g.drawImage(bosspic,x-bosspic.getWidth(null)/2, y-bosspic.getHeight(null)/2, null); // boss sprite
   // Boss Hp bar
   // Background of bar
   g.setColor(Color.BLACK);
   g.fillRect(x-50,(int)y-69/2-25,100,20);
   // Foreground of bar
   g.setColor(Color.RED);
   g.fillRect(x-50,(int)y-69/2-25,(int)(100*(hp/2500)),20);
 }
 
 public void move(ArrayList<Enemy> list, Player user){
   if(attackCD != 0){ // Decreases attack cooldown when it's on cooldown
     attackCD--;
   }
   attack(user);
   // When the attacks hurt the user
   if(mode == 2 && radius == 50){
     if(userHurt == false && new Rectangle(ax-50,ay-50,100,100).intersects(user.getHitbox())){
       user.hit(20); // damages player for 20 hp
       userHurt = true;
     }
   }
   else if(mode == 2){
     radius += 0.5; // increases radius until it reaches the max (50)
   }
   if(mode == 3 && attackCD <= 70 && attackCD % 5 == 0){
     for(Rectangle r: unsafe){
       if(r.intersects(user.getHitbox())){ // if player's hitbox is within the unsafe sections
                                           // damage player for 5 hp
         user.hit(5);
       }
     }
   }
   time++;
 }
 
 public void attack(Player user){
   if(time == 1500){ // 500 ms interval to attack boss
     time = -20; // To give the user some time before it resumes attacking
   }
   else if(time > 1000){ // resets everything related to attacks in preparation for the next one
                         // time > 1000 is when it stops attacking
     mode = 0;
     spellList.clear();
     ang = 90;
     ax = -100;
     ay = -100;
   }
   if(attackCD == 0){ // When ready to attack it will select a mode if the damage interval is over
     if(time == 0){
       mode = Util.randint(1,3);
//       mode = 3;
     }
     if(time < 1000 && mode == 1){ // bullet-hell-ish
       ang += 0.53;
       double vx = SPEED * Math.cos(ang); // x-velocity of projectile 
       double vy = SPEED * Math.sin(ang); // y-velocity of projectile
       spellList.add(new Projectile(x,y,vx,vy));
       attackCD = 0;
     }
     else if(time < 1000 && mode == 2){ // targeted meteor
       userHurt = false;
       ax = user.getX();
       ay = user.getY();
       radius = 0;
       attackCD = 150;
     }
     else if(time < 1000 && mode == 3){ // 3 lava boxes
       unsafe.clear();
       Rectangle[] spots = {new Rectangle(x-400+20,y-200,400-20,300),new Rectangle(x,y-200,400-20,300), // Locations of lava spots
                            new Rectangle(x-400+20,y+100,400-20,300),new Rectangle(x,y+100,400-20,300)};
       Rectangle tmp = spots[Util.randint(0,3)]; // Location where it is safe for the player to be in
       for(int i=0;i<4;i++){
         if(spots[i] != tmp){unsafe.add(spots[i]);}
       }
       attackCD = 100;
     }
   }
   for(Projectile p: new ArrayList<Projectile>(spellList)){ // move the projectiles generated through the bullet-hell attack
     p.move();
     if(p.getRect().intersects(user.getHitbox())){
       spellList.remove(p);
       user.hit(5); // damages player for 5 hp
     }
     if(!user.getRoom().getRect().contains((int)p.getX(),(int)p.getY())){
       spellList.remove(p); // removes projectile if it hits the wall of the room
     }
   }
 }
 

}
