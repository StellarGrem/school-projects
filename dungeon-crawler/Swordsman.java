import java.awt.*;
import java.util.ArrayList;
import javax.swing.*;

class Swordsman extends Enemy{
 private int ax,ay;
 private int delay=0,frame=0;
 Image[] swordsman_down;
 Image[] swordsman_left;
 Image[] swordsman_right;
 Image[] swordsman_up;
 
 Image[] swing_down;
 Image[] swing_left;
 Image[] swing_right;
 Image[] swing_up;
 private Boolean attackMode = false;
 private static final double SPEED=2,WAIT=5,WAIT2=18;
 
 public Swordsman(int x, int y){
  super(x,y,150,"swordsman");
  loadSprites();
  attackCD=100;
 }
 
 public void loadSprites(){
   swordsman_down = new Image[5];
   swordsman_left = new Image[5];
   swordsman_right = new Image[5];
   swordsman_up = new Image[5];
   
   swing_down = new Image[5];
   swing_left = new Image[5];
   swing_right = new Image[5];
   swing_up = new Image[5];
   for(int i=0;i<5;i++){
     swordsman_down[i] = new ImageIcon("sprites/swordsman/swordsman_down"+i+".png").getImage();
     swordsman_left[i] = new ImageIcon("sprites/swordsman/swordsman_left"+i+".png").getImage();
     swordsman_right[i] = new ImageIcon("sprites/swordsman/swordsman_right"+i+".png").getImage();
     swordsman_up[i] = new ImageIcon("sprites/swordsman/swordsman_up"+i+".png").getImage();
     
     swing_down[i] = new ImageIcon("sprites/swordsman/swing/swing_down"+i+".png").getImage();
     swing_left[i] = new ImageIcon("sprites/swordsman/swing/swing_left"+i+".png").getImage();
     swing_right[i] = new ImageIcon("sprites/swordsman/swing/swing_right"+i+".png").getImage();
     swing_up[i] = new ImageIcon("sprites/swordsman/swing/swing_up"+i+".png").getImage();
   }
 }
 
 public Rectangle getRect(){return new Rectangle((int)x-10,(int)y-10,20,20);}
 public void hit(int damage){
   hp -= damage;
   System.out.println(hp);
 }
 public void setAy(int v){ay = v;}
 public int getAy(){return ay;}
 public void setAx(int v){ax = v;}
 public int getAx(){return ax;}
 
 
 public void draw(Graphics g){
//  g.setColor(Color.YELLOW);
//  g.fillOval((int)x-10,(int)y-10,20,20);
   if(attackMode==false){
     if(u != null && u.getRoom().getRect().contains(x,y)){
       delay += 1;
       if(delay % WAIT == 0){
         frame = (frame + 1) % 5;
       }
     }
     if(Math.abs(400-x) < 30 && 300 > y){
       g.drawImage(swordsman_down[frame], x-swordsman_down[frame].getWidth(null)/2, y-swordsman_down[frame].getHeight(null)/2, null);
     }
     else if(Math.abs(400-x) < 30 && 300 < y){
       g.drawImage(swordsman_up[frame], x-swordsman_up[frame].getWidth(null)/2, y-swordsman_up[frame].getHeight(null)/2, null);
     }
     else if(400 < x){
       g.drawImage(swordsman_left[frame], x-swordsman_left[frame].getWidth(null)/2, y-swordsman_left[frame].getHeight(null)/2, null);
     }
     else if(400 > x){
       g.drawImage(swordsman_right[frame], x-swordsman_right[frame].getWidth(null)/2, y-swordsman_right[frame].getHeight(null)/2, null);
     }
   }
   else if(attackMode==true){
     if(u != null && u.getRoom().getRect().contains(x,y)){
       delay += 1;
       if(delay % WAIT2 == 0){
         frame = (frame + 1) % 5;
       }
     }
     if(Math.abs(ax-x) < 30 && ay > y){
       g.drawImage(swing_down[frame], x-swing_down[frame].getWidth(null)/2, y-swing_down[frame].getHeight(null)/2, null);
     }
     else if(Math.abs(ax-x) < 30 && ay < y){
       g.drawImage(swing_up[frame], x-swing_up[frame].getWidth(null)/2, y-swing_up[frame].getHeight(null)/2, null);
     }
     else if(ax < x){
       g.drawImage(swing_left[frame], x-swing_left[frame].getWidth(null)/2, y-swing_left[frame].getHeight(null)/2, null);
     }
     else if(ax > x){
       g.drawImage(swing_right[frame], x-swing_right[frame].getWidth(null)/2, y-swing_right[frame].getHeight(null)/2, null);
     }  
   }
//   if(Math.hypot(400 - x, 300 - y) <= 80){g.setColor(Color.RED);}
//   else{g.setColor(Color.YELLOW);}
//   g.drawLine((int)x,(int)y,400,300);
//   if(attackMode == true){
//     g.setColor(Color.RED);
//     g.drawLine((int)x,(int)y,ax,ay);
////    g.drawRect((int)x+10,(int)y-10,80,20);
//   }
 }
 
 public void move(ArrayList<Enemy> list,Player user){
   if(u == null){u = user;}
   // add restriction to movement through wall mask
   double dist = Math.hypot(user.getX() - x, user.getY() - y);
   double vx = SPEED * (user.getX() - x) / dist;
   double vy = SPEED * (user.getY() - y) / dist;
   
   if(dist <= 80 || attackMode == true){
     attack(true,user);
   }
   else{
     x += vx;
     y += vy;
   }
   for(Enemy e : list){
     if(getRect().intersects(e.getRect())){
       // shifting swordsman was refrenced from my old FSE, so in a way, it was copied
       double shiftX = 0;
       double shiftY = 0;
       if(Math.abs((x-10+20) - (e.x-10)) < Math.abs((e.x-10+20) - (x-10))){
         shiftX = -((x-10+20) - (e.x-10));
       }
       else{
         shiftX = ((e.x-10+20) - (x-10));
       }
       if(Math.abs((y-10+20) - (e.y-10)) < Math.abs((e.y-10+20) - (y-10))){
         shiftY = -((y-10+20) - (e.y-10));
       }
       else if(Math.abs((y-10+20) - (e.y-10)) > Math.abs((y-10) - (e.y-10+20))){
         shiftY += Math.abs((y-10+20) - (e.y-10));
       }
       if(Math.abs(shiftX) < Math.abs(shiftY)){
         x += shiftX;
       }
       else if(shiftY < shiftX){
         y += shiftY;
       }
     }
   }
 }
 
 public void attack(Boolean state,Player user){
   if(attackMode == false){
     ax = user.getX();
     ay = user.getY();
   }
   double rad = Math.atan2(y-ay,x-ax);
   if(attackCD == 0 && attackMode == true){
     attackMode = false;
     if(user.getHitbox().contains(ax,ay)){
       user.hit(20);
     }
   }
   else if(attackCD == 0 && state == true){
     attackMode = true;
     attackCD = 100;
     delay = 0;
   }
   else if(attackCD != 0){
     attackCD--;
   }
 }
 
}