from tkinter import *
from customtkinter import *
from tkinter import messagebox as m
import random as r

def title(root):
	l=CTkLabel(root,text="Tic Tac Toe",font=("Arial",120),text_color="green",corner_radius=20)
	l.place(relx=0.07,rely=0.1)
	l.place(relx=0.07,rely=0.1)    

def r_destroy():
	if m.askokcancel(title="exit",message="Are You sure You want To quit?"):
		root.destroy()
	else:
		pass

def menu_back():
	ch_th.place(relx=0.05,rely=0.02)
	ch_th.set("Theme")
	exit.place(relx=0.68,rely=0.02,relheight=0.04,relwidth=0.3)
	tp.place(relx=0.3,rely=0.4,relheight=0.05,relwidth=0.4)
	op.place(relx=0.3,rely=0.3,relheight=0.05,relwidth=0.4)
	frm.place_forget()
	back.place_forget()
	reset.place_forget()
	try:
		Turn.place_forget()
	except:
		pass
	back.place_forget()

def menu():
	global root,ch_th,exit,op,tp
	root=CTk()
	root.geometry("800x760")
	root.resizable(False,False)
	set_appearance_mode("light")
	title(root)

	op=CTkButton(root,text="One player",command=onep_game,corner_radius=40,font=('Arial',50,"bold"))
	op.place(relx=0.3,rely=0.3,relheight=0.05,relwidth=0.4)

	tp=CTkButton(root,text="Two player",command=twop_game,corner_radius=40,font=('Arial',50,"bold"))
	tp.place(relx=0.3,rely=0.4,relheight=0.05,relwidth=0.4)

	exit=CTkButton(root,text="Exit",command=r_destroy,fg_color="red",font=('Arial',50,"bold"),corner_radius=40)
	exit.place(relx=0.68,rely=0.02,relheight=0.04,relwidth=0.3)

	#change theme
	ch_th=CTkOptionMenu(root,values=["blue","dark-blue","green"],corner_radius=40,font=('Arial',50,"bold"),dropdown_font=('Arial',40,"bold"),width=200,height=80,command=change_theme)
	ch_th.place(relx=0.05,rely=0.02)
	ch_th.set("Theme")

	root.mainloop()
 
def change_theme(c):
	global ch_th
	set_default_color_theme(c)
	ch_th.set("Theme")
	root.destroy()
	menu()
	
def restart():
	for row in range(3):
		for column in range(3):
			buttons[row][column].config(text=" ")
			buttons[row][column].config(bg="white")
	try:
		Turn.config(text=select+" turn")
	except:
		pass

def empty_space():
	sp=9
	for row in range(3):
		for column in range(3):
			if buttons[row][column]['text']!=" " :
				sp-=1
	if sp==0:
		return True
	else:
		return False 

def wck():
	if select=="Your":
		w_color="blue"
	else:
		w_color="red"
	for row in range(3):
		if buttons[row][0]['text']==buttons[row][1]['text']==buttons[row][2]['text']!=" ":
			buttons[row][0].config(bg=w_color)
			buttons[row][1].config(bg=w_color)
			buttons[row][2].config(bg=w_color)
			return True
	for column in range(3):
		if buttons[0][column]['text']==buttons[1][column]['text']==buttons[2][column]['text'] !=" ":
			buttons[0][column].config(bg=w_color)
			buttons[1][column].config(bg=w_color)
			buttons[2][column].config(bg=w_color)
			return True
	if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text'] !=" ":
		buttons[0][0].config(bg=w_color)
		buttons[1][1].config(bg=w_color)
		buttons[2][2].config(bg=w_color)
		return True 
	elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text'] !=" ":
		buttons[0][2].config(bg=w_color)
		buttons[1][1].config(bg=w_color)
		buttons[2][0].config(bg=w_color)
		return True 
	elif empty_space():
		return "tie"
	else:
		return False 	
 		
def n_turn(row,column):
	global select,Turn
	if buttons[row][column]['text']==" " and wck() is False:
		if select==options[0]:
			buttons[row][column]['text']=options[0]
			select=options[1]
		elif select==options[1]:
			buttons[row][column]['text']=options[1]
			select=options[0]
		Turn.config(text=select+" turn")
		if wck() is True:
			if select==options[0]:
				select=options[1]
			elif select==options[1]:
				select=options[0]
			Turn.config(text=f'{select} wins!!')
			m.showinfo(title="Result",message=f'{select} wins!!!')
		elif wck()=="tie":
			Turn.config(text="Tie!!")
			if m.askretrycancel(title="Result",message="It's Tie"):
				twop_game()
			else:
				menu_back()
			
def oneck(select):
	
	if wck() is True:
		if select=="Your":
			m.showinfo(title="Result",message="You wins!!!")
			return "Y"
		elif select=="Computer's":
			if m.askretrycancel(title="Result",message="You Lose!!!") is True:
				restart()
			else:
				menu_back()	
			return"N"
		
	elif wck()=="tie":
		if m.askretrycancel(title='Result',message="It's Tie") is True:
			onep_game()
		else:
			tp.destroy()
		
			
		
		
	

def o_n_turn(row,column):
	global select,tp
	if buttons[row][column]['text']==" " and wck() is False:
		if select=="Your":
			buttons[row][column]['text']=options[0]
			kkk=oneck(select)
			if kkk!='Y':
				while True:
					r_w=r.randint(0,2)#row
					c_m=r.randint(0,2)#column 
					if buttons[r_w][c_m]['text']==" " :
						buttons[r_w][c_m]['text']=options[1]
						break
					if empty_space() is True:
						break 
				select="Computer's"
				oneck(select)
			select="Your"
	
	


def onep_game():
	global select,frm,back,reset
	try:
		restart()
	except:
		pass
	ch_th.place_forget()
	exit.place_forget()
	op.place_forget()
	tp.place_forget()

	select="Your"
	
	
	
	#back to Menu 
	back=CTkButton(root,text="Back",command=menu_back,fg_color="red",font=('Arial',50,"bold"),corner_radius=40)
	back.place(relx=0.68,rely=0.02,relheight=0.04,relwidth=0.3)
	
	frm=Frame(root,bd=8,relief="solid")
	frm.place(relx=0.35,rely=0.3)
	for row in range(3):
		for column in range(3):
			buttons[row][column]=Button(frm,text=" ",font=('Arial',20),width=5,height=3,bg="white",command= lambda row=row, column=column: o_n_turn(row,column))
			buttons [row][column].grid(row=row,column=column)
	reset=CTkButton(root,text="Restart",font=('Arial',100),command=restart,corner_radius=40)
	reset.place(relx=0.25,rely=0.75,relwidth=0.5,relheight=0.1)



		
def twop_game():
	global select, Turn,frm,back,reset
	try:
		restart()
	except:
		pass
	ch_th.place_forget()
	exit.place_forget()
	op.place_forget()
	tp.place_forget()

	select=r.choice(options)
	Turn=Label(root,text=select+" turn",font=('Arial',20),fg="blue")
	Turn.place(relx=0.45,rely=0.25)
	
	#back to Menu 
	back=CTkButton(root,text="Back",command=menu_back,fg_color="red",font=('Arial',50,"bold"),corner_radius=40)
	back.place(relx=0.68,rely=0.02,relheight=0.04,relwidth=0.3)
	
	frm=Frame(root,bd=8,relief="solid")
	frm.place(relx=0.35,rely=0.3)
	for row in range(3):
		for column in range(3):
			buttons[row][column]=Button(frm,text=" ",font=('Arial',20),width=5,height=3,bg="white",command= lambda row=row, column=column: n_turn(row,column))
			buttons [row][column].grid(row=row,column=column)
	reset=CTkButton(root,text="Restart",font=('Arial',100),command=restart,corner_radius=40)
	reset.place(relx=0.25,rely=0.75,relwidth=0.5,relheight=0.1)
	
	
#Main_Code_______________	
buttons=[[0,0,0],[0,0,0],[0,0,0]]
options=['X','O']
select=""
Turn=None
set_default_color_theme("green")





menu()
