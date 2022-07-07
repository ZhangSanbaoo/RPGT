from ast import Break
from glob import escape
from logging import critical
from os import WIFSIGNALED
from signal import pause
from telnetlib import WILL, theNULL
import random

class Charact:

    def __init__(self, name, hp, att, deff, spd, taop):
        self.name = name        # 名字
        self.hp = hp            # 血量
        self.att = att          # 攻击力
        self.deff = deff        # 防御力
        self.spd = spd          # 速度
        self.deffst = False     # 防御状态
        self.jdt = 0            # 进度条
        self.taop = taop        # 逃跑几率
        self.player = False     # 可操控角色确认
        self.boss = False       # Boss确认
    def __str__(self):
        return "Name: %s, HP: %s, Att: %s, Deff: %s, Speed: %s, ID: %s" % (self.name, self.hp, self.att, self.deff, self.spd)
    def escape(self, escap):
        print("%s尝试逃跑。。"%self.name)
        temp = random.randint(1,100)
        if self.taop >= temp:
            print("%s逃跑成功！"%self.name)
            escap = 0
            return escap
        else:
            print("%s逃跑失败。。。"%self.name)
    def Pattack(self,monster_list):
        print("场上怪物：")
        for i in range(len(monster_list)):
            a = i+1
            print("%s. %s\n当前血量：%d"%(a,monster_list[i].name,monster_list[i].hp))
        temp = int(input("请选择攻击对象(编号)："))
        temp -= 1
        mons = monster_list[temp]
        if mons.deffst == True:
            dmg = self.att - mons.deff*2
            mons.hp -= dmg
            print("%s对%s造成了%d点伤害！"%(self.name,mons.name,dmg))
            if mons.hp <= 0:
                print("%s被击败了！"%mons.name)
                monster_list.pop(temp)
                for i in range(len(battle_list)):
                    if battle_list[i] == mons:
                        battle_list.pop(i)
                        break
            return battle_list
        else:
            dmg = self.att - monster_list[temp].deff
            monster_list[temp].hp -= dmg
            print("%s对%s造成了%d点伤害！"%(self.name,monster_list[temp].name,dmg))
            if mons.hp <= 0:
                print("%s被击败了！"%mons.name)
                monster_list.pop(temp)
                for i in range(len(battle_list)):
                    if battle_list[i] == mons:
                        battle_list.pop(i)
                        break
            return battle_list
    def Mattack(self,player_list):
        temp = random.randint(1,2)
        if temp == 1:
            target = random.randint(1,len(player_list))-1
            pla = player_list[target]
            if pla.deffst == True:
                dmg = self.att - pla.deff*2
                pla.hp -= dmg
                print("%s对%s造成了%d点伤害！"%(self.name,pla.name,dmg))
                if pla.hp <= 0:
                    print("%s被击败了！"%pla.name)
                    player_list.pop(target)
                    for i in range(len(battle_list)):
                        if battle_list[i] == pla:
                            battle_list.pop(i)
                            break
                return battle_list
            else:
                dmg = self.att - pla.deff
                pla.hp -= dmg
                print("%s对%s造成了%d点伤害！"%(self.name,pla.name,dmg))
                if pla.hp <= 0:
                    print("%s被击败了！"%pla.name)
                    player_list.pop(target)
                    for i in range(len(battle_list)):
                        if battle_list[i] == pla:
                            battle_list.pop(i)
                            break
                return battle_list
        if temp == 2:
            print("还未添加怪物技能选项")
        pass

def battle(battle_list, round) -> None:
    round = True
    player_list = []
    monster_list = []
    for i in range(len(battle_list)):
        if battle_list[i].player == True:
            player_list.append(battle_list[i])
        else:
            monster_list.append(battle_list[i])
    while round:
        # for循环倒跑，此处加入battle list更新代码
        for i in range(len(battle_list)):
            if len(monster_list) == 0:
                print("%s的队伍获得了胜利！"%Hero.name)
                break
            if len(player_list) == 0:
                print("%s的队伍被击败了。。。"%Hero.name)
                break
            battle_list[i].jdt += battle_list[i].spd
            if battle_list[i].jdt >= 100:
                battle_list[i].jdt -= 100
                battle_list[i].deffst = False
                if battle_list[i].player == True:
                    print("%s\n当前血量:%d"%(battle_list[i].name,battle_list[i].hp))
                    temp = act()
                    if temp == 1:
                        battle_list_len = len(battle_list)
                        battle_list = battle_list[i].Pattack(monster_list)
                        # 对i进行判断，如果i被删除，则i+1变为i，如果i不被删除，则i不变
                        if battle_list_len != len(battle_list):
                            i = i - 1
                        pass
                    if temp == 2:
                        print("还未添加技能功能。")
                        pass
                    if temp == 3:
                        battle_list[i].deffst = True
                        pass
                    if temp == 4:
                        print("还未添加物品功能。")
                        pass
                    if temp == 5:
                        escap = 1
                        escap = battle_list[i].escape(escap)
                        if escap == 0:
                            break
                else:
                    mact = random.randint(1,3)
                    cha = battle_list[i]
                    if mact == 1:
                        cha.Mattack(player_list)
                        pass
                    if mact == 2:
                        cha.deffst = True
                        pass
                    if cha.hp <= cha.hp*0.1 and cha.boss == False:
                        if mact == 3:
                            escap = 1
                            escap = cha.escape(escap)
                            if escap == 0:
                                monster_list.remove(cha)
                                battle_list.remove(cha)
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


Hero = Charact("鲁卡", 100, 20, 15, 5, 50)
Hero.player = True
Npc1 = Charact("蕾娜",90,15,10,6, 50)
Npc1.player = True
Monster1 = Charact("Orc", 100, 15, 8, 2, 15)
Monster2 = Charact("Hilichurl", 80, 12, 6, 3, 15)

battle_list = []
battle_list.append(Hero)
battle_list.append(Npc1)
battle_list.append(Monster1)
battle_list.append(Monster2)
battle(battle_list, round)
