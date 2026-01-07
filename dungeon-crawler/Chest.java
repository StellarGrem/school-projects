/* Chest
 * Samuel Huang
 * Chests will contain a loot table ranging from swords, axes, rapiers, shields, 
 * helmets, chest-plates, leggings with a naming-convention that will depict how good they are 
 * and how much bonus stat they will add.
 *                 Chance   1/2    1/4       1/8     1/16
 *                   Names Newbie Novice Experienced Hero
 *                  Bonus  +0     +2        +5      +10
 * 
 * It also contains the class Gear which helped store the given gear type to the player.
 * By storing the title of the gear (newbie, novive, etc.), the type (sword, axe, helm, etc.),
 * the amount of bonus stats, and the sprite used.
 */
import java.awt.*;
import javax.swing.*;

class Chest{
 private int x,y;
 private Boolean open = false;
 private String[] weapon = {"sword", "axe", "rapier", "shield"};
 private String[] armor = {"helm", "chest", "legs"};
 private String[] status = {"newbie", "novice","experienced", "hero"};
 private Image[] cpics = new Image[2]; // chest sprites
 
 public Chest(int xx, int yy){
  x = xx;
  y = yy;
  cpics[0] = new ImageIcon("sprites/room/closed_chest.png").getImage(); // sprite for closed chest
  cpics[1] = new ImageIcon("sprites/room/open_chest.png").getImage(); // sprites for open chest
 }
 
 public int getX(){return x;}
 public void setX(int v){x = v;}
 public int getY(){return y;}
 public void setY(int v){y = v;}
 
 public Boolean getOpen(){return open;}
 
 public Rectangle getRect(){return new Rectangle(x,y,40,20);}
 
 public Gear loottable(){
   String [] lt = {"sword", "axe", "rapier", "shield", "helm", "chest", "legs"}; // loot-table
   open = true;
   int chance = Util.randint(1,16);
   if(chance == 16){ // ~1/16
     return new Gear(lt[Util.randint(0,6)],status[3]); // Hero title
   }
   else if(chance > 12 && chance < 16){ // ~1/8
     return new Gear(lt[Util.randint(0,6)],status[2]); // Experienced title
   }
   else if(chance > 8 && chance <= 12){ // ~1/4
     return new Gear(lt[Util.randint(0,6)],status[1]); // Novice title
   }
   else{ // ~1/2
     return new Gear(lt[Util.randint(0,6)],status[0]); // Newbie title
   }
 }
 
 public void draw(Graphics g){
   if(open == false){
     g.drawImage(cpics[0], x, y, null); // draw closed chest sprite
//     g.setColor(Color.YELLOW);
   }
   else{
     g.drawImage(cpics[1], x, y, null); // draw open chest sprite
//     g.setColor(Color.ORANGE);
   }
//   g.drawRect(x,y,40,20);
 }
}

class Gear{
  private int bonus;
  private String gear;
  private String name;
  private int x,y;
  private Image sprite;
  
  public Gear(String type, String n){
    gear = type;
    name = n;
    // Amount of bonus it gets based on the name(title)
    if(n.equals("newbie")){
      bonus = 0;
    }
    else if(n.equals("novice")){
      bonus = 2;
    }
    else if(n.equals("experienced")){
      bonus = 5;
    }
    else if(n.equals("hero")){
      bonus = 10;
    }
    // Getting the appropriate sprite
    if(gear.equals("sword")){
      sprite = new ImageIcon("sprites"+"/"+type+".png").getImage();
    }
    else if(gear.equals("axe")){
      sprite = new ImageIcon("sprites"+"/"+type+".png").getImage();
    }
    else if(gear.equals("rapier")){
      sprite = new ImageIcon("sprites"+"/"+type+".png").getImage();
    }
    else if(gear.equals("shield")){
      sprite = new ImageIcon("sprites"+"/"+type+".png").getImage();
    }
    else if(gear.equals("helm")){
      sprite = new ImageIcon("sprites"+"/"+type+".png").getImage();
    }
    else if(gear.equals("chest")){
      sprite = new ImageIcon("sprites"+"/"+type+"plate"+".png").getImage();
    }
    else if(gear.equals("legs")){
      sprite = new ImageIcon("sprites"+"/"+type+".png").getImage();
    }
  }
  
  public int getBonus(){return bonus;}
  public String getName(){return name;}
  public String getGear(){return gear;}
  public Rectangle getRect(){return new Rectangle(x-5,y-5,40,40);}
  
  public void draw(Graphics g,int xx,int yy){
    x = xx;
    y = yy;
    // Title color
    if(name.equals("newbie")){
      g.setColor(new Color(0,255,0,127)); // Green w/ tranparency
//      g.setColor(Color.GREEN);
    }
    else if(name.equals("novice")){
      g.setColor(new Color(0,0,255,127)); // Blue w/ tranparency
//      g.setColor(Color.BLUE);
    }
    else if(name.equals("experienced")){
      g.setColor(new Color(255,0,255,127)); // Magenta w/ tranparency
//      g.setColor(Color.MAGENTA);
    }
    else if(name.equals("hero")){
      g.setColor(new Color(255,255,0,127)); // Yellow w/ tranparency
//      g.setColor(Color.YELLOW);
    }
    // Gear type
    if(gear.equals("sword")){
      g.fillRect(x,y,30,30);
      g.drawImage(sprite, x, y, null);
    }
    else if(gear.equals("axe")){
      g.fillRect(x,y,30,30);
      g.drawImage(sprite, x, y, null);
    }
    else if(gear.equals("rapier")){
      g.fillRect(x,y,30,30);
      g.drawImage(sprite, x, y, null);
    }
    else if(gear.equals("shield")){
      g.fillRect(x,y,30,30);
      g.drawImage(sprite, x, y, null);
    }
    else if(gear.equals("helm")){
      g.fillRect(x,y,30,30);
      g.drawImage(sprite, x, y+3, null);
    }
    else if(gear.equals("chest")){
      g.fillRect(x,y,30,30);
      g.drawImage(sprite, x, y+3, null);
    }
    else if(gear.equals("legs")){
      g.fillRect(x,y,30,30);
      g.drawImage(sprite, x, y, null);
    }
  }
}