from logging import critical
from telnetlib import theNULL


class Monster:
    MCount = 0
    def __init__(self,name,hp,att,deff,spd):
        self.name =  name
        self.hp = hp
        self.att = att
        self.deff = deff
        self.spd = spd
        Monster.MCount += 1


class Hero:
    def __init__(self,name,hp,att,deff,spd):
        self.name =  name
        self.hp = hp
        self.att = att
        self.deff = deff
        self.spd = spd

def battle(bcounter):
    print("%s与%s相遇了。" % (HeroU.name,Monster1.name))
    if Monster1.spd>HeroU.spd:
        bcounter = 1
        print("%s对%s发动了攻击" %(Monster1.name,HeroU.name))
        bp(bcounter)
    else:
        bcounter = 2
        print("%s对%s发动了攻击" %(HeroU.name,Monster1.name))
        bp(bcounter)

def bp(bcounter):
    while True:
        if bcounter%2 == 0:
            diff = HeroU.att - Monster1.deff
            bcounter += 1
            if diff <= 0:
                print("%s造成了0点伤害。"%HeroU.name)
            else:
                Monster1.hp -= diff
                print("%s造成了%d点伤害。"%(HeroU.name,diff))
                if Monster1.hp > 0:
                    pass
                else:
                    print("%s被打败了" %Monster1.name)
                    break
        else:
            diff = Monster1.att-HeroU.deff
            bcounter += 1
            if diff <= 0:
                print("%s造成了0点伤害"%Monster1.name)
            else:
                HeroU.hp -= diff
                print("%s造成了%d点伤害"%(Monster1.name,diff))
                if HeroU.hp > 0:
                    pass
                else:
                    print("%s被打败了" %HeroU.name)
                    break


bcounter = 0
Monster1=Monster("Orc",50,5,2,2)

Hname = input("请输入勇者姓名：")
Hhp = int(input("请输入勇者的生命值："))
Hatt = int(input("请输入勇者的攻击数值："))
Hdeff = int(input("请输入勇者的防御数值："))
Hspd = int(input("请输入勇者的速度数值："))

HeroU = Hero(Hname,Hhp,Hatt,Hdeff,Hspd)
battle(bcounter)