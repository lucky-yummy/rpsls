"""
# 程序目标：完成RPSLS游戏
# 作者：杨孝杰
# """
# # 0 - 石头
# # 1 - 史波克
# # 2 - 纸
# # 3 - 蜥蜴
# # 4 - 剪刀

import random
def name_to_number(name):
    if name == 0:
        return "石头"
    elif name == 1:
        return "史波克"
    elif name == 2:
        return "布"
    elif name == 3:
        return "蜥蜴"
    elif name == 4:
        return "剪刀"
    else:
        return None


def number_to_name(number):
    if number == 0:
        return '石头'
    elif number == 1:
        return '史波克'
    elif number == 2:
        return '布'
    elif number == 3:
        return '蜥蜴'
    elif number == 4:
        return '剪刀'


def rpsls(player_choice):
    player_number = name_to_number(player_choice)
    print('您的选择为',player_number)
    comp_number = random.randrange(0, 4)
    comp_choice = number_to_name(comp_number)
    print('计算机的选择为', comp_choice)


# 输出"-------- "进行分割
# 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

# 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

# 在屏幕上显示计算机选择的随机对象


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
player_choice = int(input())
rpsls(player_choice)
player_number = name_to_number(player_choice)
comp_number = random.randrange(0, 4)
diff=(comp_number - player_choice) % 5
if diff == 1 or diff == 2:
    print("你输了")
elif diff == 3 or diff == 4:
    print("你赢了")
elif diff == 0:
    print("你和计算机一样")
else:
    print("Error:No Correct Name")

    rpsls('石头')
    rpsls('史波克')
    rpsls('布')
    rpsls('蜥蜴')
    rpsls('剪刀')