#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：陈雅婧
日期：2020.4.9
"""
import random
def name_to_number(name):
	"""
    将游戏对象对应到不同的整数
    """
	if name=="石头":
		number=0
	elif name=="史波克":
		number=1
	elif name=="布":
		number=2
	elif name=="蜥蜴":
		number=3
	elif name=="剪刀":
		number=4
	return number
def number_to_name(number):
	"""
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
	if number==0:
		name="石头"
	if number==1:
		name="史波克"
	if number==2:
		name="布"
	if number==3:
		name="蜥蜴"
	if number==4:
		name="剪刀"
	return name	
def rpsls(player_choice):
	"""
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
	print("----------------")# 分割
	print("您的选择为：%s"%player_choice)# 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
	player_choice_number=name_to_number(player_choice)# 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
	comp_number=random.randint(0,4)# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
	comp_choice=number_to_name(comp_number)# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
	print("计算机的选择为：%s"%comp_choice)# 在屏幕上显示计算机选择的随机对象
	# 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
	if player_choice_number==comp_number:
		print("您和计算机出的一样呢")
	elif player_choice_number==0:
		if comp_number==3 or comp_number==4:
			print("您赢了!")
		else:
			print("机器赢了")
	elif player_choice_number==1:
		if comp_number==0 or comp_number==4:
			print("您赢了！")
		else:
			print("机器赢了")
	elif player_choice_number==2:
		if comp_number==0 or comp_number==1:
			print("您赢了!")
		else:
			print("机器赢了")
	elif player_choice_number==3:
		if comp_number==1 or comp_number==2:
			print("您赢了!")
		else:
			print("机器赢了")
	elif player_choice_number==4:
		if comp_number==2 or comp_number==3:
			print("您赢了!")
		else:
			print("机器赢了")
# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
if choice_name=="石头" or choice_name=="史波克" or choice_name=="布" or choice_name=="蜥蜴" or choice_name=="剪刀":
	rpsls(choice_name)
else:
	print("Error: No Correct Name")

