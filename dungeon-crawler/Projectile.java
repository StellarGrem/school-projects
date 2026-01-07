/* Projectile
 * Class for the projectiles that boss and mage creates
 */

import java.awt.*;

class Projectile{
 private double x,y,vx,vy;
 
 public Projectile(double xx, double yy, double vxx, double vyy){
  x = xx;
  y = yy;
  vx = vxx;
  vy = vyy;
 }
 
 public double getX(){return x;}
 public void setX(double v){x = v;}
 public double getY(){return y;}
 public void setY(double v){y = v;}
 
 public Rectangle getRect(){return new Rectangle((int)x,(int)y,10,10);}
 
 public void move(){
   x += vx;
   y += vy;
 }
 
 public void draw(Graphics g){
   g.setColor(Color.RED);
   g.fillOval((int)x,(int)y,10,10);
 }

}
