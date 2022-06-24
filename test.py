from ast import Break
from glob import escape
from logging import critical
from os import WIFSIGNALED
from signal import pause
from telnetlib import WILL, theNULL
import random

class Monster:
    Mcount = 0

    def __init__(self, name, hp, att, deff, spd):
        self.name = name
        self.hp = hp
        self.att = att
        self.deff = deff
        self.spd = spd
        Monster.Mcount += 1
        self.id = Monster.Mcount
        self.jdt = 0
        self.life = True
    def __str__(self):
        return "Name: %s, HP: %s, Att: %s, Deff: %s, Speed: %s, ID: %s" % (self.name, self.hp, self.att, self.deff, self.spd, self.id)

    def Mattack(self,HeroU):
        if HeroU.deffst == False:
            temp = self.att - HeroU.deff
            if temp >0:
                HeroU.hp -= temp
                print("%s受到了%d点伤害"%(HeroU.name,temp))
            else:
                print("%s没有造成伤害"%self.name)
        else :
            temp = self.att - HeroU.deff*2
            if temp >0:
                HeroU.hp -= temp
                print("%s受到了%d点伤害"%(HeroU.name,temp))
            else:
                print("%s没有造成伤害"%self.name)

class Hero:
    def __init__(self, name, hp, att, deff, spd):
        self.name = name
        self.hp = hp
        self.att = att
        self.deff = deff
        self.spd = spd
        self.deffst = False  #防御状态
        self.jdt = 0         #进度条
        self.taop = 50       #逃跑几率

    def Hattack(self, list_monster):
        temp = self.att - list_monster[0].deff
        list_monster[0].hp -= temp
        print("%s对%s造成了%d点伤害！"%(self.name,list_monster[0].name,temp))
        if list_monster[0].hp <= 0:
            print("%s被击败了！"%list_monster[0].name)
            del(list_monster[0])

    def Hescape(self,escap):
        temp = random.randint(1,100)
        if self.taop < temp:
            print("%s未能逃跑成功。。。" %self.name)
        else:
            print("%s逃跑了。。。" %self.name)
            escap = 0
            return escap

def battle(HeroU, list_monster,round) -> None:
    round = True
    while round:
        list_monster = list_monster
        if len(list_monster) == 0:
            print("%s获得了胜利！" % HeroU.name)
            round = False
        elif HeroU.hp <= 0:
            print("%s被击败了！" % HeroU.name)
        else:
            HeroU.jdt += HeroU.spd
            if HeroU.jdt >= 20:
                HeroU.deffst = False
                temp = act()
                if temp == 1:
                    HeroU.Hattack(list_monster)
                    HeroU.jdt = 0
                    pass
                if temp == 2:
                    HeroU.jdt = 0
                    pass
                if temp == 3:
                    HeroU.deffst = True
                    HeroU.jdt = 0
                    pass
                if temp == 4:
                    HeroU.jdt = 0
                    pass
                if temp == 5:
                    HeroU.jdt = 0
                    escap = 1
                    a = HeroU.Hescape(escap)
                    if a == 0:
                        break

            for i in list_monster:
                i.jdt += i.spd
                if i.jdt >= 20:
                    i.Mattack(HeroU)
                    i.jdt = 0
                    pass


def act():
    try:
        print("你的回合。")
        selection = int(input(
            "请选择你的行动： 1.攻击\n                 2.技能\n                 3.防御\n                 4.物品\n                 5.逃跑\n您的选择："))
        if selection > 5 or selection < 1:
            raise ValueError('请输入1-5之间的数字！')
        else:
            return selection
    except ValueError:
        print("请输入1-5之间的数字！")
        return act()


HeroU = Hero("鲁卡", 100, 20, 15, 5)
Monster1 = Monster("Orc", 100, 15, 8, 2)
Monster2 = Monster("Hilichurl", 80, 12, 6, 3)

list_monster = []
list_monster.append(Monster1)
list_monster.append(Monster2)
battle(HeroU, list_monster,round)

# Hname = input("请输入勇者姓名：")
# Hhp = int(input("请输入勇者的生命值："))
# Hatt = int(input("请输入勇者的攻击数值："))
# Hdeff = int(input("请输入勇者的防御数值："))
# Hspd = int(input("请输入勇者的速度数值："))

# HeroU = Hero(Hname, Hhp, Hatt, Hdeff, Hspd)

# Monster1.battle(bcounter)
# Monster2.battle(bcounter)

# def battle(self, bcounter):
#     print("%s与%s相遇了。" % (HeroU.name, self.name))
#     if self.spd > HeroU.spd:
#         bcounter = 1
#         print("%s对%s发动了攻击" % (self.name, HeroU.name))
#         self.bp(bcounter)
#     else:
#         bcounter = 2
#         print("%s对%s发动了攻击" % (HeroU.name, self.name))
#         self.bp(bcounter)

#     def bp(self, bcounter):
#         while True:
#             if bcounter % 2 == 0:
#                 diff = HeroU.att - self.deff
#                 bcounter += 1
#                 if diff <= 0:
#                     print("%s造成了0点伤害。" % HeroU.name)
#                 else:
#                     self.hp -= diff
#                     print("%s造成了%d点伤害。" % (HeroU.name, diff))
#                     if self.hp > 0:
#                         pass
#                     else:
#                         print("%s被打败了" % self.name)
#                         break
#             else:
#                 diff = self.att - HeroU.deff
#                 bcounter += 1
#                 if diff <= 0:
#                     print("%s造成了0点伤害" % self.name)
#                 else:
#                     HeroU.hp -= diff
#                     print("%s造成了%d点伤害" % (self.name, diff))
#                     if HeroU.hp > 0:
#                         pass
#                     else:
#                         print("%s被打败了" % HeroU.name)
#                         break
