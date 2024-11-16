# test_class.py
class slime:
    # HP = 30    
    def __init__(self, HP):
        # インスタンス変数としてHPを設定
        self.HP = HP

    # HPを答えるメソッドの定義
    def say_HP(self):
        print(f"my HP is {self.HP} .")

    # ダメージメソッドの定義
    def damage(self, damage_point):
        self.HP -= damage_point

# インスタンスの生成
enemy1 = slime()
# enemy1 = slime(100)

# HPを答えるメソッドの呼び出し
enemy1.say_HP()

# ダメージメソッドで5ポイントダメージ
enemy1.damage(5)
enemy1.say_HP()



'''
class slime:
    HP = 30    

    # HPを答えるメソッドの定義
    def say_HP(self):
        print(f"my HP is {self.HP} .")

    # ダメージメソッドの定義
    def damage(self, damage_point):
        self.HP -= damage_point

# インスタンスの生成
enemy1 = slime()

# HPを答えるメソッドの呼び出し
enemy1.say_HP()

# ダメージメソッドで5ポイントダメージ
enemy1.damage(5)
enemy1.say_HP()

'''