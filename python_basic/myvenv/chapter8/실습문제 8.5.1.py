class Item():
    def __init__(self,name,price,weight,isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable    
    def sale(self):
        print(f"[{self.name}] 판매가격은 [{self.price}]")
    def discard(self):
        if self.isdropable == False:
            print(f"[{self.name}]은 버릴 수 없습니다!")
        else:
            print(f"[{self.name}] 버렸습니다.")

class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable,effect):
        super().__init__(name,price,weight,isdropable)
        self.effect = effect
    def wear(self):
        print(f"[{self.name}]을 착용했습니다. {self.effect}")

class UsableItem(Item):
    def __init__(self, name, price, weight, isdropable,effect):
        super().__init__(name,price,weight,isdropable)
        self.effect = effect
    def wear(self):
        print(f"[{self.name}]을 사용했습니다. {self.effect}가 지속됩니다.")

    # 인스턴스 생성

    sword = WearableItem("이가닌자의 검", 30000, 3.5, True, "체력 5000증가, 마력 2000증가")
    sword.wear()
    sword.sale()
    sword.discard()