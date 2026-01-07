import java.awt.*;
import java.util.ArrayList;

class PowerUp{
 private int x, y;
 private String type;
 private ArrayList<PowerUp> pwrList = new ArrayList<PowerUp>();
 Platform p;
 ArkanoidPanel ap;
 
 public void add(int xx,int yy,PowerUp pwr){
   if(pwrList.size() == 0){
     String power = Util.powerup();
     if(!power.equals("") && !p.getPower().contains(power)){
       pwrList.add(new PowerUp(xx,yy,power));
       System.out.println("added");
     }
   }
 }
 
 public void reset(){
   pwrList = new ArrayList<PowerUp>();
 }
 
 public PowerUp(ArkanoidPanel a){
   ap = a;
 }
 
 public PowerUp(int xx,int yy,String t){
   x = xx;
   y = yy;
   type = t;
 }
 
 public Rectangle getRect(){
   return new Rectangle (x,y,10,10);
 }
 
 public void move(Platform plat,Block bl){
   p = plat;
//   System.out.print(list);
   for(PowerUp pw:pwrList){
     pw.y += 5;
     Rectangle pr = pw.getRect(); // Power rectangle
     if(pr.intersects(plat.getRect())){
       System.out.printf("You recieved %s\n",pw.type);
       ap.addScore(1000);
       plat.powerup(pw.type);
       pwrList.remove(pw);
       break;
     }
     else if(pw.y > 610){
       pwrList.remove(pw);
       break;
     }
   }
 }
   
 public void draw(Graphics g){
  g.setColor(Color.MAGENTA);
   for(PowerUp pw:pwrList){
     g.fillOval(pw.x,pw.y,10,10);
   }
 }
}