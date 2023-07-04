import csv
import random

global main_list

def game_play(number):
	global main_list
	print("This word :: ",main_list[number][0])
	
	answer=main_list[number][1]

	# to get three options apart from the answer to confuse the person
	list_without_ans=main_list.copy()
	list_without_ans.pop(number)
	temp_options=[]
	for i in range(0,3):
		temp_value=random.choice(list_without_ans)[1]
		temp_options.append(temp_value)
	temp_options.append([answer])
	for i in range(0,4):
		random.shuffle(temp_options)

	# To get the correct position
	answer_postion=[index for index,x in enumerate(temp_options) if isinstance(x,list)][0]
	
	# Printing the options
	print("\n Options are ::")
	for i in range(0,4):
		if i%2==0 and i!=0:
			print("\n")
		if isinstance(temp_options[i],list):
			print(f" |||  {i}. {temp_options[i][0]}",end=" ||| ")
		else:
			print(f" ||| {i}. {temp_options[i]}",end=" ||| ")

	# Taking input of the users
	input_answer=input("\n Your Answer :: ")
	if input_answer==str(answer_postion):
		print("\n*** Correct ***\n")
	else:
		print("\n*** Wrong ***\n")
	
	
		
if __name__=='__main__':	
	with open("covered_barron333.csv","r") as dict_file:
		try:
			csv_read=csv.reader(dict_file)
		except Exception as e: 
			print(e)
		main_list=[]
		for index,i in enumerate(csv_read):
			if index==0:
				pass
			else:
				main_list.append(i)
		
		for i in range(0,4):
			random.shuffle(main_list)
		for i in range(0,len(main_list)):
			return_val=game_play(i)
			if return_val==False:
				print("Exiting the game")
				exit(0)
			else:
				continue


