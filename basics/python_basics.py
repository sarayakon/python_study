
# 変数の宣言

# 数値型

a = 1

print(a, type(a))  # 1 <class 'int'>

# 文字列型

b = "test"

print(b, type(b))  # test <class 'str'>

# Boolean型

c = True

print(c, type(c))  # True <class 'bool'>

# 変数に異なる型の値を入れる場合

d = 1
e = "taro"
d = e
print(d, type(d))  # taro <class 'str'>

# 型の変更を行う

f = "1"
new_f = int(f)
print(new_f, type(new_f))  # 1 <class 'int'>

