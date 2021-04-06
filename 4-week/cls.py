# result1=0
# result2=0


# def add1(num):
#     global result1
#     result1 +=num
#     return result1

# def add2(num):
#     global result2
#     result2 +=num
#     return result2

# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(7))

# class Calculator:
#     def __init__(self, add_data):
#         self.result = add_data
    
#     def add(self, num):
#         self.result += num
#         return self.result

# cal1 = Calculator(10)
# cal2 = Calculator(5)

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

class NPC:
    hp=100
    mp=100

    def attack(self):
        return f"{self.tribe}이 공격을 시도했다."

    def __init__(self):
        print("새로운 NPC가 태어났다")


class Human_NPC(NPC):
    hp = 100
    mp = 100
    tribe = "인간"
    skill = "제련"

    def __init__(self):
        super().__init__()
        print("그 NPC는 인간이였다.")


    def attack(self):
        return f"{self.tribe}이 무기를 이용해 공격을 시도했다."

class Orc_NPC(NPC):
    hp = 100
    mp = 100
    tribe = "오크"
    skill = "돌격"

class Fairy_NPC(NPC):
    hp = 100
    mp = 100
    tribe = "요정"
    skill = "마법"

npc1=Human_NPC()
npc2=Orc_NPC()
npc3=Fairy_NPC()

print(npc1.attack())
print(npc2.attack())
print(npc3.attack())