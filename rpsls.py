#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ������
���ڣ�2020.4.9
"""
import random
def name_to_number(name):
	"""
    ����Ϸ�����Ӧ����ͬ������
    """
	if name=="ʯͷ":
		number=0
	elif name=="ʷ����":
		number=1
	elif name=="��":
		number=2
	elif name=="����":
		number=3
	elif name=="����":
		number=4
	return number
def number_to_name(number):
	"""
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
	if number==0:
		name="ʯͷ"
	if number==1:
		name="ʷ����"
	if number==2:
		name="��"
	if number==3:
		name="����"
	if number==4:
		name="����"
	return name	
def rpsls(player_choice):
	"""
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
	print("----------------")# �ָ�
	print("����ѡ��Ϊ��%s"%player_choice)# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
	player_choice_number=name_to_number(player_choice)# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
	comp_number=random.randint(0,4)# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
	comp_choice=number_to_name(comp_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
	print("�������ѡ��Ϊ��%s"%comp_choice)# ����Ļ����ʾ�����ѡ����������
	# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
	if player_choice_number==comp_number:
		print("���ͼ��������һ����")
	elif player_choice_number==0:
		if comp_number==3 or comp_number==4:
			print("��Ӯ��!")
		else:
			print("����Ӯ��")
	elif player_choice_number==1:
		if comp_number==0 or comp_number==4:
			print("��Ӯ�ˣ�")
		else:
			print("����Ӯ��")
	elif player_choice_number==2:
		if comp_number==0 or comp_number==1:
			print("��Ӯ��!")
		else:
			print("����Ӯ��")
	elif player_choice_number==3:
		if comp_number==1 or comp_number==2:
			print("��Ӯ��!")
		else:
			print("����Ӯ��")
	elif player_choice_number==4:
		if comp_number==2 or comp_number==3:
			print("��Ӯ��!")
		else:
			print("����Ӯ��")
# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
if choice_name=="ʯͷ" or choice_name=="ʷ����" or choice_name=="��" or choice_name=="����" or choice_name=="����":
	rpsls(choice_name)
else:
	print("Error: No Correct Name")

