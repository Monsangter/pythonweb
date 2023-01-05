#상속
# : 클래스들이 중복된 코드를 제거하고 유지보수를
# 편하게 하기 위해 사용.

#클래스 변수
#: 인스턴스들이 모두 공유하는 변수. 
# 반면 멤버변수처럼 생성자로 매개변수값을 통해 인스턴스가 갖는 값은 각각 고유의 값임.

import random
# 부모 클래스
class Monster:
    max_num = 1000
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1
    def move(self):
      print(f"[{self.name}]지상에서 이동하기")

# 자식 클래스
class Wolf(Monster):
    pass

class Shark(Monster):
  def move(self):
    print(f"[{self.name}]헤엄치기") # 메소드 오버라이딩
    
class Dragon(Monster):
  def __init__(self, name, health, attack):
    super().__init__(name, health, attack) # 부모 클래스의 생성자를 가져올 수 있다.
    self.skills = ("불뿜기", "꼬리치기", "날개치기")

  def move(self):
    print(f"[{self.name}]날기")
  def skill(self):
    print(f"[{self.name}] 스킬 사용 {self.skills[random.randint(0,2)]}" )

wolf = Wolf("울프",1500, 200)
wolf.move()
print(wolf.max_num)

shark = Shark("샤크",1500, 200)
shark.move()
print(shark.max_num)

dragon = Dragon("드래곤", 1500, 200)
dragon.move()
dragon.skill()
print(dragon.max_num)
#가장 싫어하는건 중복.. 드래곤 생성할때마다 이렇게 호출할거임? 아니다. 드래곤 클래스의 멤버변수에 스킬을 추가해주자.
#Dragon = Dragon("드래곤",1500, 200, ("불뿜기", "꼬리치기", "날개치기")) #스킬을 고정돼 있으니 튜플로
#Dragon.move()