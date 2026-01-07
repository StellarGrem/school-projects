# Warrior class is kinda glitchy. It sorta works, but not as intended/consistently
# In the itemDescription function, those marked at "incomplete" were not finished
# You may experience crashes from time to time, as the waves get higher. I don't know why.
# The primary one is itemDescription. Unable to get_width().

from pygame import *
from random import *
from math import *

font.init()
comicFont = font.SysFont("Comic Sans MS", 60)
statFont = font.SysFont("Comic Sans MS", 20)
screen = display.set_mode((1080, 720))

sec = 0
x, y = 540, 360
offx, offy = 0, 0
bx, by = -10, -10

wave = 0

enemies = []
enemyType = ["goblin", "swordsman", "gunner"]

explist = []
expval = []
exp = 0
exptot = 50
lvl = 0

explen = 0
hplen = 210 # rectangle length of hp bar
stunHitbox = Rect(9999,9999,1,1)
def drawScene(screen, user, enemies, attack, page, explist, explen, hplen):
    if page == "intro":
        screen.fill(0xffffff)
        txt = comicFont.render("Wave Survival", True, (255,0,0))
        wid = txt.get_width()
        hei = txt.get_height()
        screen.blit(txt, ((1080 - wid) // 2, 72))       
        # Play button
        txt = comicFont.render("PLAY", True, (0, 0, 0))
        wid = txt.get_width()
        hei = txt.get_height()
        draw.rect(screen,0,((1080 - wid) // 2 -10, (720 - hei) // 2 - 10, wid+20, hei+20),2)
        screen.blit(txt, ((1080 - wid) // 2, (720 - hei) // 2))
        # Quit button
        txt = comicFont.render("QUIT", True, (0, 0, 0))
        wid = txt.get_width()
        hei = txt.get_height()
        draw.rect(screen,0,((1080 - wid) // 2 -10, (2160 - 2 *hei) // 4 - 10, wid+20, hei+20),2)
        screen.blit(txt, ((1080 - wid) // 2, (2160 - 2 * hei) // 4, wid, hei))

    elif page == "selection":
        screen.fill(0xffffff)
        # Warrior
        txt = comicFont.render("WARRIOR", True, (0, 0, 0))
        wid = txt.get_width()
        hei = txt.get_height()
        screen.blit(txt, ((1080 - 2 * wid) // 4, (0 + hei) // 4))
        screen.blit(image.load("warriorstats.png"),((1080 - 2 * wid) // 4 - 60, 360-314/1.5))
        draw.rect(screen, (0), ((1080 - 2 * wid) // 4 - 60,(0 + hei) // 4 + hei + 15, wid + 120, 400), 2)
        # Archer
        txt = comicFont.render("ARCHER", True, (0, 0, 0))
        wid = txt.get_width()
        hei = txt.get_height()
        screen.blit(txt, ((3240 - 2 * wid) // 4, (0 + hei) // 4))
        screen.blit(image.load("archerstats.png"),((3240 - 2 * wid) // 4 - 65, 360-297/1.5))
        draw.rect(screen, (0), ((3240 - 2 * wid) // 4 - 60,(0 + hei) // 4 + hei + 15, wid + 120, 400), 2)
        # Select box
        txt = comicFont.render("SELECT", True, (0, 0, 0))
        wid = txt.get_width()
        hei = txt.get_height()
        # Select Warrior
        draw.rect(screen, (0),((1080 - 2 * wid) // 4 - 10,(7 * 720 - 4 * hei) // 8 - 10, wid + 20, hei + 20), 2)
        screen.blit(txt, ((1080 - 2 * wid) // 4, (7 * 720 - 4 * hei) // 8))
        # Select Archer
        draw.rect(screen, (0),((3240 - 2 * wid) // 4 - 10,(7 * 720 - 4 * hei) // 8 - 10, wid + 20, hei + 20), 2)
        screen.blit(txt, ((3240 - 2 * wid) // 4, (7 * 720 - 4 * hei) // 8))

    elif page == "game":
        global lvl
        global wave
        global maxhp
        global playerClass
        hp, atk, defence = pstats
        x,y = user
        bx,by = attack
        
        screen.fill((0, 0, 0))
        # Attack Projectile
        if playerClass == "archer":
            arrowAttack(offx, offy, bx, by)
##            draw.circle(screen, (255, 255, 255), (attack), 5)
        elif playerClass == "warrior":
            global sec,rate,attackHitbox, stunHitbox
            if sec == rate:
                slashAttack(x,y,mx,my)
##                print(attackHitbox)
            # Relocates hitbox so that enemies don't constantly take damage
            elif 1 < sec < rate:
                attackHitbox = Rect(9999,9999,1,1)
            # Relocates hitbox so that enemies are no longer stunned after 1.5 seconds 
            if sec == 90:
                stunHitbox = Rect(9999,9999,1,1)
                
        # Player
        pic,width,height = sprite(0,frame,0)
        screen.blit(pic,(x-width/2,y-height/2))
##        draw.circle(screen, (0, 255, 0), (user), 15)        
        # Enemy
        for i in enemies:
            if i[2] == "goblin":
                pic,width,height = sprite(1,frame,(x-i[0]))
            elif i[2] == "swordsman":
                pic,width,height = sprite(2,frame,(x-i[0]))
            elif i[2] == "gunner":
                pic,width,height = sprite(3,frame,(x-i[0]))
            elif i[2] == "boss":
                pic,width,height = sprite(4,frame,(x-i[0]))
##            draw.circle(screen, (255, 0, 0), (i[0],i[1]), 15)
            if 0 <= i[0] <= 1080 and 30 <= i[1] <= 720:
                screen.blit(pic,(i[0]-width/2,i[1]-height/2))       
        # Experience Orb/Crystal
        for expx,expy in explist:
            screen.blit(image.load("experience.png"),(expx - 12.5, expy-12.5))
            draw.circle(screen, (0, 0, 255), (expx,expy), 5)
        # EXP bar
        draw.rect(screen, (0,0, 255), (0, 0, 1080, 30))
        draw.rect(screen, (135, 206, 235), (0, 0, explen, 30))
        # Player Level
        txt = statFont.render(f"Level {lvl}", True, (255, 255, 255))
        wid = txt.get_width()
        hei = txt.get_height()
        screen.blit(txt, ((1080 - wid), 0))
        # HP bar
        draw.rect(screen, (255, 0, 0), (0, 60, 210, 30))
        draw.rect(screen, (0, 255, 0), (0, 60, hplen, 30))
        # Amount of health
        txt = statFont.render(f"{hp}/{maxhp}", True, (255, 255, 255))
        wid = txt.get_width()
        hei = txt.get_height()
        screen.blit(txt, ((210 - wid), 65))
        # Wave Number
        txt = statFont.render(f"Wave {wave}", True, (255, 255, 255))
        wid = txt.get_width()
        hei = txt.get_height()
        screen.blit(txt, ((1080 - wid)//2, 30))        
    elif page == "death":
        # Retry
        txt = comicFont.render("RETRY", True, (255, 255, 255))
        wid = txt.get_width()
        hei = txt.get_height()
        screen.blit(txt, ((1080 - wid) // 2, (620 - hei) // 2))
        # Menu
        txt = comicFont.render("MENU", True, (255, 255, 255))
        wid = txt.get_width()
        hei = txt.get_height()
        screen.blit(txt, ((1080 - wid) // 2, (820 - hei) // 2))

    elif page == "level up":
        global option0,option1,option2
        global options

        draw.rect(screen,(0xffffff),option0)
        draw.rect(screen,(0xffffff),option1)
        draw.rect(screen,(0xffffff),option2)

        txt = statFont.render(f"{options[0]} Lvl {equipped.count(options[0])+1}", True, (0))
        wid = txt.get_width()
        hei = txt.get_height()
        screen.blit(txt, ((1080 - wid) // 2, 30))
        desc = itemDescription(options[0],equipped.count(options[0])+1)
        screen.blit(desc,((1080 - desc.get_width())//2,130))

        txt = statFont.render(f"{options[1]} Lvl {equipped.count(options[1])+1}", True, (0))
        wid = txt.get_width()
        hei = txt.get_height()
        screen.blit(txt, ((1080 - wid) // 2, 260))
        desc = itemDescription(options[1],equipped.count(options[1])+1)
        screen.blit(desc,((1080 - desc.get_width())//2,360))

        txt = statFont.render(f"{options[2]} Lvl {equipped.count(options[2])+1}", True, (0))
        wid = txt.get_width()
        hei = txt.get_height()
        screen.blit(txt, ((1080 - wid) // 2, 490))
        desc = itemDescription(options[2],equipped.count(options[2])+1)
        screen.blit(desc,((1080 - desc.get_width())//2,590))

    elif page == "You win":
        txt = comicFont.render("CONTINUE", True, (255, 255, 255))
        wid = txt.get_width()
        hei = txt.get_height()
        screen.blit(txt,((1080 - 2 * wid) // 4, (7 * 720 - 4 * hei) // 8))

        txt = comicFont.render("MENU", True, (255, 255, 255))
        wid = txt.get_width()
        hei = txt.get_height()
        screen.blit(txt,((3240 - 2 * wid) // 4, (7 * 720 - 4 * hei) // 8))

# Game Mechanics
def menu():
    global page
    global playerClass
    global pstats
    global upgradelist,equipped

    if page == "intro":
        txt = comicFont.render("PLAY", True, (0, 0, 0))
        wid = txt.get_width()
        hei = txt.get_height()
        play = Rect((1080 - wid) // 2, (720 - hei) // 2, wid, hei)

        txt = comicFont.render("QUIT", True, (0, 0, 0))
        wid = txt.get_width()
        hei = txt.get_height()
        quit = Rect((1080 - wid) // 2, (2160 - 2 * hei) // 4, wid, hei)
        # Sends player to character selection screen
        if play.collidepoint(mx, my):
            page = "selection"
        # Closes the program
        elif quit.collidepoint(mx, my):
            global running
            running = False

    elif page == "selection":
        txt = comicFont.render("SELECT", True, (0, 0, 0))
        wid = txt.get_width()
        hei = txt.get_height()
        # The "select" rect for each class
        warrior = Rect((1080 - 2 * wid) // 4, (7 * 720 - 4 * hei) // 8, wid,hei)
        archer = Rect((3240 - 2 * wid) // 4, (7 * 720 - 4 * hei) // 8, wid,hei)
        # Player becomes warrior class
        if warrior.collidepoint(mx, my):
            playerClass = "warrior"
            pstats = stats(playerClass,1)
            upgradelist.append("sword")
            equipped.append("sword")
            page = "game"
        # Player becomes archer class
        if archer.collidepoint(mx, my):
            playerClass = "archer"
            pstats = stats(playerClass,1)
            upgradelist.append("bow")
            equipped.append("bow")
            page = "game"

    elif page == "death":
        txt = comicFont.render("RETRY", True, (255, 255, 255))
        wid = txt.get_width()
        hei = txt.get_height()
        retry = Rect((1080 - wid) // 2, (620 - hei) // 2, wid, hei)

        txt = comicFont.render("MENU", True, (255, 255, 255))
        wid = txt.get_width()
        hei = txt.get_height()
        menu = Rect((1080 - wid) // 2, (820 - hei) // 2, wid, hei)
        # Game is restarted back to wave 1
        if retry.collidepoint(mx, my):
            reset()  # Resets all variables as if the user opened up the program
            pstats = stats(playerClass,1)  # Resets character stats
            page = "game"
        # Sends user back to the title screen
        if menu.collidepoint(mx, my):
            reset()  # Resets all variables as if the user opened up the program
            page = "intro"

    elif page == "level up":
        global options,option0,option1,option2

        if option0.collidepoint(mx,my):
            chosenUpgrade(options[0])
            page = "game"
        if option1.collidepoint(mx,my):
            chosenUpgrade(options[1])
            page = "game"
        if option2.collidepoint(mx,my):
            chosenUpgrade(options[2])
            page = "game"

    elif page == "You win":
        txt = comicFont.render("CONTINUE", True, (255, 255, 255))
        wid = txt.get_width()
        hei = txt.get_height()
        contin = Rect((1080 - 2 * wid) // 4, (7 * 720 - 4 * hei) // 8, wid,hei)

        txt = comicFont.render("MENU", True, (255, 255, 255))
        wid = txt.get_width()
        hei = txt.get_height()
        menu = Rect((3240 - 2 * wid) // 4, (7 * 720 - 4 * hei) // 8, wid,hei)

        # Resumes game
        if contin.collidepoint(mx, my):
            page = "game"
        # Sends user back to the title screen
        if menu.collidepoint(mx, my):
            reset()  # Resets all variables as if the user opened up the program
            page = "intro"

def reset():
    global sec, x, y, offx, offy, bx, by
    global wave, enemies
    global explist, expval, exp, exptot, lvl, explen, hplen
    global upgradelist, equipped, sprites
    global iframe, tick, duration, rate, frame

    sec = 0
    x, y = 540, 360
    offx, offy = 0, 0
    bx, by = -10, -10
    wave = 0
    enemies = []
    explist = []
    expval = []
    exp = 0
    exptot = 50
    lvl = 0
    explen = 0
    hplen = 210 # rectangle length of hp bar
    upgradelist = []
    equipped = []
    sprites = []
    iframe = 0
    tick = 0
    duration = 0
    rate = 180  # 180 = 3 seconds
    frame = 0

def waves(wave, numEnemy):
    global enemies, estats
    global page
    enemies = []
    estats = []
    while len(enemies) != numEnemy:
        ex = randint(-100, 1180)
        ey = randint(-100, 820)
        if ex < -90 or ex > 1170 or ey < -90 or ey > 810:
            if wave < 5:
                enemies.append([ex,ey,enemyType[0],""])
            elif wave < 8:
                typepos = choice([0, 0, 0, 0, 1, 1])
                enemies.append([ex,ey,enemyType[typepos],""])
            elif wave >= 8:
                typepos = choice([0, 0, 1, 1, 1, 2, 2])
                enemies.append([ex,ey,enemyType[typepos],""])
    if wave % 10 == 0:
        enemies.append([0,0,"boss",""])
    for n in enemies:
        estats.append(stats(n[2],wave))


def hitbox(player, enemies, attack):
    global playerHitbox, attackHitbox, enemyHitbox

    x, y = player
    bx, by = attack
    enemyHitbox = []
    playerHitbox = Rect(x, y, 1, 1)
    attackHitbox = Rect(bx - 5, by - 5, 5, 5)
    for i in enemies:
        ex = i[0]
        ey = i[1]
        if i[2] == "boss":
            enemyHitbox.append(Rect(ex-111/2,ey-111/2,111,111))
        else:
            enemyHitbox.append(Rect(ex - 15, ey - 15, 30, 30))

def collision(player, attack, enemy, estat, pstat, iframe):
    global pstats
    global estats
    global page
    for hitbox in enemy:
        pos = enemy.index(hitbox)
        # Player attack hits enemy
        if attack.colliderect(hitbox):
            global bx,by
            # Begins fire tick damage
            if equipped.count("fire") > 0 and enemies[pos][3] == "":
                enemies[pos][3] = 0            
            # Explosion arrows (Incomplete)
            if equipped.count("bow") == 5 and Rect(bx-25,by-25,50,50).colliderect(hitbox):
                bx,by = bx,by
                hp, atk, defence = damage(estats[pos], pstats, enemies[pos][3],pos)
            # Basic damage
            hp, atk, defence = damage(estats[pos], pstats, enemies[pos][3],pos)
            if hp <= 0:
                experience((enemies[pos][0],enemies[pos][1]), enemies[pos][2])
                del enemies[pos]
                del enemyHitbox[pos]
                del estats[pos]
            else:
                estats[pos] = hp, atk, defence
        # Enemy collides with player
        elif hitbox.colliderect(player) and iframe == 0 and randint(1,10) > equipped.count("mobilityCape"):
            global hplen
            iframe += 1
            hp, atk, defence = damage(pstats, estats[pos],0,-1)
            hplen = (hp / maxhp) * 210
            if hplen > 210:
                hplen = 210
            if hp <= 0:
                page = "death"
            else:
                pstats = hp, atk, defence
    # Player collects experience
    global exp, explen, explist
    for xy in explist:
        pos = explist.index(xy)
        # if experience if within 100 px of player
        # the experience will move towards the player
        if Rect(x - 100, y - 100, 200, 200).collidepoint(xy):
            expx,expy = xy
            d = ((x - expx)**2 + (y - expy)**2)**0.5
            if d == 0:
                d = 1
            expx += 8 * (x - expx) / d
            expy += 8 * (y - expy) / d
            explist[pos] = expx,expy
        # When player collects experience, it disappears from list
        if Rect(x - 15, y - 15, 30, 30).collidepoint(xy):
            exp += expval[pos]
            del explist[pos]
            del expval[pos]
        explen = (exp / exptot) * 1080
    return iframe

def damage(receiver, attacker, status, pos):
    hp, atk, defence = attacker
    rhp, ratk, rdefence = receiver
    if equipped.count("bow") >= 2 and pos == -1:    # Defense-piercing arrows
        rhp -= atk
    else:
        rhp -= atk - rdefence
    if status != "" and status % 60 == 0:
        global tick, duration
        if status == duration:
            enemies[pos][3] = ""
        else:
            enemies[pos][3] = tick
        if equipped.count("fire") == 1:
            rhp -= 2
##            print("burning")
        elif equipped.count("fire") == 2:
            rhp -= 3
##            print("burning")
        elif equipped.count("fire") == 3:
            rhp -= 4
##            print("burning")
    return rhp, ratk, rdefence

def stats(classes,wave):
    global maxhp
    if classes == "warrior":
        maxhp = 200
        hp = 200
        atk = 20
        defence = 10
    elif classes == "archer":
        maxhp = 125
        hp = 125
        atk = 15
        defence = 5
    elif classes == "goblin":
        hp = round(100 * 1.1**wave-1,None)
        atk = round(15 * 1.05**wave-1,None)
        defence = 5
    elif classes == "swordsman":
        hp = round(150 * 1.1**wave-7,None)
        atk = round(35 * 1.05**wave-7,None)
        defence = 5
    elif classes == "gunner":
        hp = round(100 * 1.1**wave-8,None)
        atk = round(30 * 1.05**wave-8,None)
        defence = 5
    elif classes == "boss":
        hp = 1250
        atk = 50
        defence = 0
    return hp, atk, defence


# Entity Mechanics
def enemyMovement(enemyLocation, x, y):
    global enemyHitbox, attackHitbox, stunHitbox
    for i in enemyLocation:
        ex = i[0]
        ey = i[1]
        pos = enemies.index(i)
        d = ((x - ex)**2 + (y - ey)**2)**0.5
        if d == 0:
            d = 1
        ex += 4 * (x - ex) / d
        ey += 4 * (y - ey) / d
        # Stuns if in stunHitbox
        if equipped.count("sword") <= 4 and stunHitbox.collidepoint(i[0],i[1]):
            enemies[pos][0] = i[0]
            enemies[pos][1] = i[1]       
        else:
            enemies[pos][0] = ex
            enemies[pos][1] = ey
            enemyHitbox[pos] = Rect(ex-15, ey-15, 30, 30)
        ## Copied // Prevents clumping
        for rect2 in enemyHitbox[pos+1:]:
            enemyHitbox[pos] = AdjustPositionOnCollide(enemyHitbox[pos], rect2)
            if enemyHitbox[pos] != Rect(ex-15, ey-15, 30, 30):
                enemies[pos][0] = enemyHitbox[pos].x+15
                enemies[pos][1] = enemyHitbox[pos].y+15  
        # Damages from fire (for some reason, it's instantaneous)
        if i[3] != "":
            estats[pos] = damage(estats[pos], pstats, i[3],pos)
## Copied from
## https://www.reddit.com/r/PygameCreative/comments/1c2zyph/how_to_calculate_rectangle_collision_blocking/
def ShiftX(x, y, width, height, x2, y2, width2, height2):
    return -(x + width - x2) if abs(x + width - x2) < abs(x2 + width2 - x) else x2 + width2 - x

def ShiftY(x, y, width, height, x2, y2, width2, height2):
    return -(y + height - y2) if abs(y + height - y2) < abs(y2 + height2 - y) else y2 + height2 - y

def AdjustPositionOnCollide(rectangle_1, rectangle_2):
    if rectangle_1.colliderect(rectangle_2):
        shift_x, shift_y = ShiftX(*rectangle_1, *rectangle_2), ShiftY(*rectangle_1, *rectangle_2)
        if abs(shift_x) < abs(shift_y):
            rectangle_1.x += shift_x
        else:
            rectangle_1.y += shift_y
    return rectangle_1
##

def userMovement(enemyLocation, explist):
    global playerHitbox
    global bx,by
    playerHitbox = Rect(x, y, 1, 1)
    if keys[K_w]:
        by += 4
        for i in enemyLocation:
            ex = i[0]
            ey = i[1]
            pos = enemies.index(i)
            enemies[pos][1] = ey+4
            enemyHitbox[pos] = Rect(ex-15,ey-11,30,30)
        for i in explist:
            expx, expy = i
            pos = explist.index(i)
            explist[pos] = expx,expy+4
    if keys[K_s]:
        by -= 4
        for i in enemyLocation:
            ex = i[0]
            ey = i[1]
            pos = enemies.index(i)
            enemies[pos][1] = ey-4
            enemyHitbox[pos] = Rect(ex-15,ey-19,30,30)
        for i in explist:
            expx, expy = i
            pos = explist.index(i)
            explist[pos] = expx,expy-4
    if keys[K_a]:
        bx += 4
        for i in enemyLocation:
            ex = i[0]
            ey = i[1]
            pos = enemies.index(i)
            enemies[pos][0] = ex+4
            enemyHitbox[pos] = Rect(ex-11,ey-15,30,30)
        for i in explist:
            expx, expy = i
            pos = explist.index(i)
            explist[pos] = expx+5,expy
    if keys[K_d]:
        bx -= 4
        for i in enemyLocation:
            ex = i[0]
            ey = i[1]
            pos = enemies.index(i)
            enemies[pos][0] = ex-4
            enemyHitbox[pos] = Rect(ex-19,ey-15,30,30)
        for i in explist:
            expx, expy = i
            pos = explist.index(i)
            explist[pos] = expx-4,expy
ang = 0
def arrowAttack(offx, offy, arrowX, arrowY):
    global attackHitbox
    global ang, sec, rate
    global bx,by
    bx += offx
    by += offy
    attackHitbox = Rect(bx - 5, by - 5, 5, 5)
    # Image
    if sec == rate:
        if my < y:
            ang = degrees(acos((mx-x)/dist((mx,my),(x,y))))
        else:
            ang = degrees(-1*acos((mx-x)/dist((mx,my),(x,y))))
    arrowPic = image.load("arrow.png")
    arrow = transform.rotate(arrowPic,ang)
    hei = arrow.get_height()
    wid = arrow.get_width()
    return screen.blit(arrow,(bx-wid/2, by-hei/2))

def slashAttack(x,y,mx,my):
    global attackHitbox, stunHitbox
    if my < y:
        ang = degrees(acos((mx-x)/dist((mx,my),(x,y))))
    else:
        ang = degrees(-1*acos((mx-x)/dist((mx,my),(x,y))))
    if equipped.count("sword") == 5:
        slashPic = image.load("slash.gif")
    else:
        slashPic = image.load("slash2.png")
    slash = transform.rotate(slashPic,ang)
    hei = slash.get_height()
    wid = slash.get_width()
    if mx > x:
        attackHitbox = Rect(x,y-hei/2,wid/2,hei)
        stunHitbox = Rect(x-wid,y-hei/2,wid,hei)
    elif mx < x:
        attackHitbox = Rect(x-wid/2,y-hei/2,wid/2,hei)
        stunHitbox = Rect(x-wid/2,y-hei/2,wid,hei)
    return screen.blit(slash,(x-wid/2,y-hei/2))

# Level Up Mechanic
def experience(enemyLoc, enemyType):
    if enemyType == "goblin":
        exp = 10
        expval.append(exp)
    elif enemyType == "swordsman":
        exp = 20
        expval.append(exp)
    elif enemyType == "gunner":
        exp = 25
        expval.append(exp)
    explist.append(enemyLoc)

def level():
    global lvl
    global exptot
    global page
    page = "level up"
    lvl += 1
    exptot = round(exptot * 1.5, None)
    upgrade()

leveluplist = ["upgrade","passives","stat bonus"]
upgradelist = []
passivelist = ["attackArmor","mobilityCape","fire"]
statbonuslist = ["hp","atk","defence"]
equipped = []

option0 = Rect(1080/8,30,3*1080/4,200)
option1 = Rect(1080/8,260,3*1080/4,200)
option2 = Rect(1080/8,490,3*1080/4,200)

def upgrade():
    global options
    options = []
    while len(options) < 3: # always generates 3 options
        option = choice(leveluplist)
        if option == "upgrade":
            if len(upgradelist) == 0:
                upgrade = choice(statbonuslist)
            else:
                upgrade = choice(upgradelist)
        elif option == "passives":
            upgrade = choice(passivelist)
        elif option == "stat bonus":
            upgrade = choice(statbonuslist)
        if upgrade not in options: # Add upgrade if it's not an option
            options.append(upgrade)

def chosenUpgrade(option):
    global page
    global maxhp, pstats
    global equipped, upgradelist
    hp,atk,defence = pstats
    # Upgrades/Part of upgrades that change player stats
    if option == "hp":
        maxhp += 10
    elif option == "atk":
        atk += 10
    elif option == "defence":
        defence += 2    
    elif option == "bow" and equipped.count(option)+1 == 2 or option == "sword" and equipped.count(option)+1 == 3:
        global rate
        rate = 180*0.9  # 10% increase, so 90% remains
    elif option == "bow" and equipped.count(option)+1 == 4:
        atk += 15
    elif option == "sword" and equipped.count(option)+1 == 2:
        atk += 10
    elif option == "attackArmor":
        if equipped.count(option)+1 == 1:
            atk += 10
            defence -= 5
        elif equipped.count(option)+1 == 2:
            atk += 15
            defence -= 5            
        elif equipped.count(option)+1 == 3:
            atk += 25
            defence -= 10             
    elif option == "mobilityCape":
        if equipped.count(option)+1 == 1:
            maxhp -= 10
        elif equipped.count(option)+1 == 2:
            maxhp -= 5       
        elif equipped.count(option)+1 == 3:        
            maxhp -= 10
    elif option == "fire":
        global duration
        if equipped.count(option)+1 == 1:
            duration = 3*60
        elif equipped.count(option)+1 == 2:
            duration = 5*60
    pstats = hp,atk,defence
    #
    if option != "hp" and option != "atk" and option != "defence":
        equipped.append(option)
        if equipped.count(option) == 5 and option == "bow" or option == "sword":
            upgradelist.remove(option)
        elif equipped.count(option) == 3 and option in passivelist:
            upgradelist.remove(option)
        elif option not in upgradelist:
            upgradelist.append(option)
        print(equipped,upgradelist)


def itemDescription(item,lvl):
    if item == "bow":
        if lvl == 2:
            txt = statFont.render("Shoot 10% faster", True, 0)
            return txt
        elif lvl == 3:
            txt = statFont.render("Defence-piercing arrows", True, 0)
            return txt
        elif lvl == 4:
            txt = statFont.render("Increase damage by 15", True, 0)
            return txt
        elif lvl == 5:  # Incomplete
            txt = statFont.render("Explosive arrows - Damage enemies within a 50px radius", True, 0)
            return txt
    elif item == "sword":
        if lvl == 2:
            txt = statFont.render("Increase damage by 10", True, 0)
            return txt
        elif lvl == 3:
            txt = statFont.render("Swing 10% faster", True, 0)
            return txt
        elif lvl == 4:  # Incomplete
            txt = statFont.render("Stuns for 1.5 seconds", True, 0)
            return txt
        elif lvl == 5:
            txt = statFont.render("Bigger Sword", True, 0)
            return txt
    elif item == "attackArmor":
        if lvl == 1:
            txt =  statFont.render("+10 ATK  -5 Defence", True, 0)
            return txt
        elif lvl == 2:
            txt = statFont.render("+25 ATK  -10 Defence", True, 0)
            return txt
        elif lvl == 3:
            txt = statFont.render("+50 ATK  -20 Defence", True, 0)
            return txt
    elif item == "mobilityCape":
        if lvl == 1:
            txt = statFont.render("10% dodge chance  -10 HP", True, 0)
            return txt
        elif lvl == 2:
            txt = statFont.render("20% dodge chance  -15 HP ", True, 0)
            return txt
        elif lvl == 3:
            txt = statFont.render("30% dodge chance  -25 HP", True, 0)
            return txt
    elif item == "fire":
        if lvl == 1:
            txt = statFont.render("Enemy takes 2 ticks of damage for 3 seconds", True, 0)
            return txt
        elif lvl == 2:
            txt = statFont.render("Enemy takes 3 ticks of damage for 5 seconds", True, 0)
            return txt
        elif lvl == 3:
            txt = statFont.render("Enemy takes 4 ticks of damage for 5 seconds", True, 0)
            return txt
    elif item == "hp":
        txt = statFont.render("Increase HP by 10", True, 0)
        return txt
    elif item == "atk":
        txt = statFont.render("Increase ATK by 10", True, 0)
        return txt
    elif item == "defence":
        txt = statFont.render("Increase Defence by 2", True, 0)
        return txt
    
def pictures():
    global playerClass
    pics = []
                                # Image file,      Folder,  name of image
    pics.append(list(image.load("%s/%s%01d.png" % ("Player",f"{playerClass}",i)) for i in range(0,5)))# Player 
    pics.append(list(image.load("%s/%s%01d.png" % ("Enemy","goblin",i)) for i in range(0,8)))# Goblin
    pics.append(list(image.load("%s/%s%01d.png" % ("Enemy","swordsman",i)) for i in range(0,6)))# Swordsman
    pics.append(list(image.load("%s/%s%01d.png" % ("Enemy","gunner",i)) for i in range(0,4)))# Gunner
    pics.append(list(image.load("%s/%s%01d.png" % ("Enemy","boss",i)) for i in range(0,3)))# Boss
    return pics

sprites = []
def sprite(entity,frame,enemyDirection):
    global sprites
    # prevents lag by not reloading the images everytime it calls on pictures function
    if len(sprites) == 0:   
        sprites = pictures()
    # Goblin movement frames
    if entity == 1:
        if frame > 7:
            frame = 0
        pic = sprites[entity][int(frame)]
    # Swordsman movement frames
    elif entity == 2:
##        if frame > 5:
        frame = frame % 5
        pic = sprites[entity][int(frame)]
    # Gunner movement frames
    elif entity == 3:
##        if frame > 3:
        frame = frame % 4
        pic = sprites[entity][int(frame)]
    # Boss movement frames
    elif entity == 4:
##        if frame > 2:
        frame = frame % 3
        pic = sprites[entity][int(frame)]
    # Player movement frames
    if keys[K_w] or keys[K_a] or keys[K_s] or keys[K_d] and entity == 0:
##        if frame > 4:
        frame = frame % 4
        pic = sprites[entity][int(frame)]
    elif entity == 0:   # Player idle frame
        pic = sprites[entity][0]
    # Flips player sprite vertically to look at mouse direction
    if mx > x and entity == 0:
        pic = transform.flip(pic,True,False)
    # Flips enemy sprite vertically to match direction of movement
    elif enemyDirection < 0 and entity != 0:
        pic = transform.flip(pic,True,False)
    width = pic.get_width()
    height = pic.get_height()
    return pic,width,height
    
running = True
myClock = time.Clock()
page = "intro"
sec = 0
iframe = 0
tick = 0
duration = 0
rate = 180  # 180 = 3 seconds
frame = 0
while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            menu()
            print(page)

    mx, my = mouse.get_pos()
    keys = key.get_pressed()

    if page == "game":
        # Generates wave
        if len(enemies) == 0:
            wave += 1
            enemyAlive = 15 + 5 * wave
            waves(wave, enemyAlive)
            # Intitalizes hitboxes
            hitbox((x, y), enemies, (bx, by))

        # Attack rate
        if sec == rate:
            if playerClass == "archer":
                bx, by = x, y
                d = ((mx - x)**2 + (my - y)**2)**0.5
                if d == 0:
                    d = 1
                # The speed the arrows moves in the x-axis
                offx = 5 * (mx - x) / d
                # The speed the arrows moves in the y-axis
                offy = 5 * (my - y) / d
            sec = 0

        userMovement(enemies, explist)
        enemyMovement(enemies, x, y)
##        if playerClass == "archer":
##            bx, by = arrowAttack(offx, offy, bx, by)
        # hitbox((x, y), enemies, (bx, by))
        iframe = collision(playerHitbox,attackHitbox,enemyHitbox,estats,pstats,iframe)

        # Reach level up requirement
        if explen >= 1080:
            exp -= exptot
            level()

        # iframe grants player 1/4 of a second of damage immunity
        # prevents player from instantly dying when running into a
        # group of enemies
        if 0 < iframe <= 31:
            iframe += 1
        else:
            iframe = 0
        # tick is the counter for fire damage
        if 0 <= tick < duration:
            tick += 1
        else:
            tick = 0
        # Frame animation number
        frame += 0.25
        # Starts back to frame 0
        # when it reaches the sprite with the highest animation frames
        if frame > 7:
            frame = 0
        sec += 1
        # When final wave is beaten
        if wave == 10 and len(enemies) == 0:
            page = "You win"
            
    drawScene(screen, (x, y), enemies, (bx, by), page, explist, explen, hplen)
    display.flip()
    myClock.tick(60)

quit()
