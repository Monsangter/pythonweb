#상속
# : 클래스들이 중복된 코드를 제거하고 유지보수를
# 편하게 하기 위해 사용.

# 부모 클래스
class Monster:
    def __init__(self,name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def move(self):
      print(f"[{self.name}]지상에서 이동하기")

# 자식 클래스
class Wolf(Monster):
    pass

class Shark(Monster):
  def move(self):
    print(f"[{self.name}]헤엄치기") # 메소드 오버라이딩
    
class Dragon(Monster):
  def move(self):
    print(f"[{self.name}]날기")

wolf = Wolf("울프",1500, 200)
wolf.move()

Shark = Shark("울프",1500, 200)
Shark.move()

Dragon = Dragon("울프",1500, 200)
Dragon.move()