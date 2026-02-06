class User:
    def __init__(self, name):
        self._name = name # encapsulation of name even though you can actually access it.

    # --- Getter: 负责“出” ---
    @property
    def username(self):
        print(">>> 正在通过 Getter 读取数据")
        return self._name.upper()  # 这里可以对输出进行加工（比如变大写）

    # --- Setter: 负责“进” --- "safety guard"
    @username.setter
    def username(self, value):
        print(f">>> 正在通过 Setter 修改数据为: {value}")
        if len(value) >= 3:
            self._name = value  # 这里可以进行安全检查
        else:
            print("拒绝修改：名字太短了！")
    def __str__(self):
        return self._name


# --- 实际操作 ---
u = User("nabi")
print(u)
u = User("nana")
print(u)
# 触发 Setter
u.username = "xiaojiujiu"  
# 触发 Getter
print(u.username)

