from logging import critical
from telnetlib import theNULL


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

    def battle(self, bcounter):
        print("%s与%s相遇了。" % (HeroU.name, self.name))
        if self.spd > HeroU.spd:
            bcounter = 1
            print("%s对%s发动了攻击" % (self.name, HeroU.name))
            self.bp(bcounter)
        else:
            bcounter = 2
            print("%s对%s发动了攻击" % (HeroU.name, self.name))
            self.bp(bcounter)

    def bp(self, bcounter):
        while True:
            if bcounter % 2 == 0:
                diff = HeroU.att - self.deff
                bcounter += 1
                if diff <= 0:
                    print("%s造成了0点伤害。" % HeroU.name)
                else:
                    self.hp -= diff
                    print("%s造成了%d点伤害。" % (HeroU.name, diff))
                    if self.hp > 0:
                        pass
                    else:
                        print("%s被打败了" % self.name)
                        break
            else:
                diff = self.att - HeroU.deff
                bcounter += 1
                if diff <= 0:
                    print("%s造成了0点伤害" % self.name)
                else:
                    HeroU.hp -= diff
                    print("%s造成了%d点伤害" % (self.name, diff))
                    if HeroU.hp > 0:
                        pass
                    else:
                        print("%s被打败了" % HeroU.name)
                        break

    def battlegroupe(self):
        print("%s进入战斗状态。" % HeroU.name)


class Hero:
    def __init__(self, name, hp, att, deff, spd):
        self.name = name
        self.hp = hp
        self.att = att
        self.deff = deff
        self.spd = spd

bcounter = 0
Monster1 = Monster("Orc", 50, 5, 2, 2)
print(Monster1.name,Monster1.hp,Monster1.att,Monster1.deff,Monster1.spd,Monster1.id)
Monster2 = Monster("Hilichurl", 100, 15, 5, 5)
print(Monster2.name,Monster2.hp,Monster2.att,Monster2.deff,Monster2.spd,Monster2.id)

# Hname = input("请输入勇者姓名：")
# Hhp = int(input("请输入勇者的生命值："))
# Hatt = int(input("请输入勇者的攻击数值："))
# Hdeff = int(input("请输入勇者的防御数值："))
# Hspd = int(input("请输入勇者的速度数值："))

# HeroU = Hero(Hname, Hhp, Hatt, Hdeff, Hspd)

# Monster1.battle(bcounter)
# Monster2.battle(bcounter)
