import java.awt.*;
import java.util.ArrayList;
import javax.swing.*;

class Block{
  private int x,y;
  private ArrayList<Block> blockList = new ArrayList<Block>();
  private Rectangle rect;
  private int nround;
  private Image[]blpics;// In Order: {Red, Orange, Yellow, Green, Blue, Pink}
  ArkanoidPanel ap;
  
public Block(ArkanoidPanel a){
  ap = a;
  nround = 0;
  blpics = new Image[6];  
  for(int i = 0; i<6; i++){
   blpics[i] = new ImageIcon("sprites"+"/"+"block"+i+".png").getImage();
  }
  round();
}
public Block(int xx, int yy){
   x = xx;
   y = yy;
}
 
public Rectangle getRect(Rectangle ball, PowerUp p){
  for(Block b: new ArrayList<Block>(blockList)){
    rect = new Rectangle(b.x,b.y,50,25);
    if(ball.intersects(rect)){
      blockList.remove(b);
      System.out.println("removed");
      power(b,p);
      break;
    }
  }
  return rect;
}

//public void collision(Block b,PowerUp p){
////  System.out.println(b.x);
//  blockList.remove(b);
//  System.out.println("removed");
////  System.out.println(b.x);
//}

public void power(Block b, PowerUp p){
    p.add(b.x+25,b.y+12,p);
}

public Boolean isEmpty(){
  if(blockList.size() == 0){
    System.out.println("new lvl");
    round();
    return true;
  }
  else{
    return false;
  }
}

public void round(){
  nround++;
  ap.addRound();
  if(nround == 1){
    for(int yy=100;yy<250;yy+=25){
      for(int xx=25;xx<600;xx+=50){
        blockList.add(new Block(xx,yy));
      }
    }
  }
  else if(nround >= 2){
    for(int yy=100;yy<400;yy+=25){
      int blockadd = 0;
      int nblock = (yy-100)/25 + 1;
      for(int xx=25;xx<600;xx+=50){
        if(blockadd != nblock){
          blockList.add(new Block(xx,yy));
          blockadd++;
        }
      }
    }
//    System.out.println(blockList);
  }
}

public void draw(Graphics g){
//   g.setColor(Color.GREEN);
   for(Block b: blockList){
//     g.fillRect(b.x,b.y,50,25);
     int pos = (b.y-100)/25 - 6*((b.y-100)/25/6);
     g.drawImage(blpics[pos], b.x, b.y, null);
     }
   }
}