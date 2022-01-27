#import models
import time
from tkinter import *
import sqlite3

root=Tk()
root.configure(background=("black")) 
root.title("Ping Pong")
root.geometry("1366x768")

#Creating important varibles
time_elapsed1=0
time_elapsed2=0
time_elapsed3=0
time1=0
time2=0
ttt=Label(text='1-STOL'.zfill(1),bg='black',fg='blue',font=('default',15,'bold'))
ttt.place(x=280,y=10,width=100,height=25)
np=Label(text='',bg='white',fg='white',font=('default',10,'bold'))
np.place(x=0,y=375,width=1366,height=10)
wp=Label(text='',bg='white',fg='white',font=('default',10,'bold'))
wp.place(x=678,y=0,width=10,height=768)
#Functions
def create_label(text,_x,_y):
	label=Label(root,text=text,fg='white',bg='black',font=('default',10,'bold'))
	label.place(x=_x,y=_y,width=100,height=45)
def start():

	start_button.place_forget()
	resume_button.place_forget()
	stop_button.place(x=20,y=300,width=200,height=75)
	global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2
	time2=int(time.time())
	if time2!=time1:
		time1=time2
		if time_elapsed1<59:
			time_elapsed1+=1
			clock_frame.config(text=(str(time_elapsed3).zfill(2)+':'+str(time_elapsed2).zfill(2)+':'+str(time_elapsed1).zfill(2)))
		else:
			time_elapsed1=0
			if time_elapsed2<59:
				time_elapsed2+=1	
				clock_frame.config(text=(str(time_elapsed3).zfill(2)+':'+str(time_elapsed2).zfill(2)+':'+str(time_elapsed1).zfill(2)))
			else:
				time_elapsed2=0
				if time_elapsed3>=24:
					time_elapsed1=0
					time_elapsed2=0
					time_elapsed3=0
				else:
					time_elapsed3+=1
					clock_frame.config(text=(str(time_elapsed3).zfill(2)+':'+str(time_elapsed2).zfill(2)+':'+str(time_elapsed1).zfill(2)))
	self_job=root.after(1000,start)

def stop():
	global self_job
	if self_job is not None:
		root.after_cancel(self_job)
		self_job=None
	stop_button.place_forget()
	resume_button.place(x=20,y=300,width=200,height=75)
def clear():
	global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2,label
	try:
		stop()
	except:
		start()
		stop()
	clock_frame.config(text="1-STOL")
	time_elapsed1=0
	time_elapsed2=0
	time_elapsed3=0
	time1=0
	time2=0
	resume_button.place_forget()
	start_button.place(x=20,y=300,width=200,height=75)
	lap_button.place(x=470,y=300,width=200,height=75)
	reset_button.place(x=240,y=300,width=200,height=75)
	clock_frame.place(x=30,y=40,width=600,height=200)


def lap():
	global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2
	nn = Label(text=('1-STOL'+'\n'+str(time_elapsed3).zfill(1)+':'+str(time_elapsed2).zfill(1)+':'+str(time_elapsed1).zfill(1)+'\n'+str(f'{(2000/6)*(time_elapsed3*60+time_elapsed2):.2f}').zfill(1)+" so'm"),bg='black',fg='blue',font=('default',45,'bold'))
	nn.place(x=740,y=460,width=600,height=200)
	ti = str(time_elapsed3)+':'+str(time_elapsed2)+':'+str(time_elapsed1)
	li = f'{(2000/6)*(time_elapsed3*60+time_elapsed2):.2f}'
	print(li)
	print(type(li))
	name='1-STOL'
#Creating the buttons and widgets
clock_frame=Label(text="1-STOL",bg='black',fg='blue',font=('default',50,'bold'))
start_button=Button(text="START",bg='green',fg='black',command=start,font=('default',20,'bold'))
stop_button=Button(text="STOP",bg='red',fg='black',command=stop,font=('default',20,'bold'))
resume_button=Button(text="RESUME",bg='green',fg='black',command=start,font=('default',18,'bold'))
lap_button=Button(text="LAP",bg='yellow',fg='black',command=lap,font=('default',20,'bold'))
reset_button=Button(text="RESET",bg='orange',fg='black',command=clear,font=('default',20,'bold'))

#Placing the buttons and widgets
start_button.place(x=20,y=300,width=200,height=75)
lap_button.place(x=470,y=300,width=200,height=75)
reset_button.place(x=240,y=300,width=200,height=75)
clock_frame.place(x=30,y=40,width=600,height=200)

#############################################################################################################################

time_elapsed4=0
time_elapsed5=0
time_elapsed6=0
time3=0
time4=0
qqq=Label(text='2-STOL'.zfill(1),bg='black',fg='blue',font=('default',15,'bold'))
qqq.place(x=280,y=400,width=100,height=25)
lp=Label(text='',bg='white',fg='white',font=('default',10,'bold'))
lp.place(x=0,y=375,width=1366,height=10)
pl=Label(text='',bg='white',fg='white',font=('default',10,'bold'))
pl.place(x=678,y=0,width=10,height=768)
#Functions
def create_labels1(text,_x,_y):
	label=Label(root,text=text,fg='white',bg='black',font=('default',10,'bold'))
	label.place(x=_x,y=_y,width=100,height=45)
def start1():

	start_button1.place_forget()
	resume_button1.place_forget()
	stop_button1.place(x=20,y=660,width=200,height=75)
	global time_elapsed4,time_elapsed5,time_elapsed6,time3,self_job1,time4
	time4=int(time.time())
	if time4!=time3:
		time3=time4
		if time_elapsed4<59:
			time_elapsed4+=1
			clock_frame1.config(text=(str(time_elapsed6).zfill(2)+':'+str(time_elapsed5).zfill(2)+':'+str(time_elapsed4).zfill(2)))
		else:
			time_elapsed4=0
			if time_elapsed5<59:
				time_elapsed5+=1	
				clock_frame1.config(text=(str(time_elapsed6).zfill(2)+':'+str(time_elapsed5).zfill(2)+':'+str(time_elapsed4).zfill(2)))
			else:
				time_elapsed5=0
				if time_elapsed6>=24:
					time_elapsed4=0
					time_elapsed5=0
					time_elapsed6=0
				else:
					time_elapsed6+=1
					clock_frame1.config(text=(str(time_elapsed6).zfill(2)+':'+str(time_elapsed5).zfill(2)+':'+str(time_elapsed4).zfill(2)))
	self_job1=root.after(1000,start1)

def stop1():
	global self_job1
	if self_job1 is not None:
		root.after_cancel(self_job1)
		self_job1=None
	stop_button1.place_forget()
	resume_button1.place(x=20,y=660,width=200,height=75)

def clear1():
	global time_elapsed4,time_elapsed5,time_elapsed6,time3,self_job1,time4,label1,i,j
	try:
		stop1()
	except:
		start1()
		stop1()
	clock_frame1.config(text="2-STOL")
	time_elapsed4=0
	time_elapsed5=0
	time_elapsed6=0
	time3=0
	time4=0
	resume_button1.place_forget()
	start_button1.place(x=20,y=660,width=200,height=75)
	lap_button1.place(x=470,y=660,width=200,height=75)
	reset_button1.place(x=240,y=660,width=200,height=75)
	clock_frame1.place(x=30,y=430,width=600,height=200)

def lap1():
	global time_elapsed4,time_elapsed5,time_elapsed6,time3,self_job1,time4
	pp = Label(text=('2-STOL'+'\n'+str(time_elapsed6).zfill(1)+':'+str(time_elapsed5).zfill(1)+':'+str(time_elapsed4).zfill(1)+'\n'+str(f'{(2000/6)*(time_elapsed6*60+time_elapsed5):.2f}').zfill(1)+" so'm"),bg='black',fg='blue',font=('default',45,'bold'))
	pp.place(x=740,y=460,width=600,height=200)
	ti1 = str(time_elapsed6)+':'+str(time_elapsed5)+':'+str(time_elapsed4)
	li1 = f'{(2000/6)*(time_elapsed6*60+time_elapsed5):.2f}'

#Creating the buttons and widgets
clock_frame1=Label(text="2-STOL",bg='black',fg='blue',font=('default',50,'bold'))
start_button1=Button(text="START",bg='green',fg='black',command=start1,font=('default',20,'bold'))
stop_button1=Button(text="STOP",bg='red',fg='black',command=stop1,font=('default',20,'bold'))
resume_button1=Button(text="RESUME",bg='green',fg='black',command=start1,font=('default',18,'bold'))
lap_button1=Button(text="LAP",bg='yellow',fg='black',command=lap1,font=('default',20,'bold'))
reset_button1=Button(text="RESET",bg='orange',fg='black',command=clear1,font=('default',20,'bold'))

#Placing the buttons and widgets
start_button1.place(x=20,y=660,width=200,height=75)
lap_button1.place(x=470,y=660,width=200,height=75)
reset_button1.place(x=240,y=660,width=200,height=75)
clock_frame1.place(x=30,y=430,width=600,height=200)

#########################################################################################################

time_elapsed7=0
time_elapsed8=0
time_elapsed9=0
time5=0
time6=0
aaa=Label(text='3-STOL'.zfill(1),bg='black',fg='blue',font=('default',15,'bold'))
aaa.place(x=960,y=10,width=100,height=25)
sp=Label(text='',bg='white',fg='white',font=('default',10,'bold'))
sp.place(x=0,y=375,width=1366,height=10)
ql=Label(text='',bg='white',fg='white',font=('default',10,'bold'))
ql.place(x=678,y=0,width=10,height=768)
#Functions
def create_labels2(text,_x,_y):
	label=Label(root,text=text,fg='white',bg='black',font=('default',10,'bold'))
	label.place(x=_x,y=_y,width=100,height=45)
def start2():

	start_button2.place_forget()
	resume_button2.place_forget()
	stop_button2.place(x=700,y=300,width=200,height=75)
	global time_elapsed7,time_elapsed8,time_elapsed9,time5,self_job2,time6
	time6=int(time.time())
	if time6!=time5:
		time5=time6
		if time_elapsed7<59:
			time_elapsed7+=1
			clock_frame2.config(text=(str(time_elapsed9).zfill(2)+':'+str(time_elapsed8).zfill(2)+':'+str(time_elapsed7).zfill(2)))
		else:
			time_elapsed7=0
			if time_elapsed8<59:
				time_elapsed8+=1	
				clock_frame2.config(text=(str(time_elapsed9).zfill(2)+':'+str(time_elapsed8).zfill(2)+':'+str(time_elapsed7).zfill(2)))
			else:
				time_elapsed8=0
				if time_elapsed9>=24:
					time_elapsed7=0
					time_elapsed8=0
					time_elapsed9=0
				else:
					time_elapsed9+=1
					clock_frame2.config(text=(str(time_elapsed9).zfill(2)+':'+str(time_elapsed8).zfill(2)+':'+str(time_elapsed7).zfill(2)))
	self_job2=root.after(1000,start2)

def stop2():
	global self_job2
	if self_job2 is not None:
		root.after_cancel(self_job2)
		self_job2=None
	stop_button2.place_forget()
	resume_button2.place(x=700,y=300,width=200,height=75)

def clear2():
	global time_elapsed7,time_elapsed8,time_elapsed9,time5,self_job2,time6,label1,i,j
	try:
		stop2()
	except:
		start2()
		stop2()
	clock_frame2.config(text="3-STOL")
	time_elapsed7=0
	time_elapsed8=0
	time_elapsed9=0
	time5=0
	time6=0
	resume_button2.place_forget()
	start_button2.place(x=700,y=300,width=200,height=75)
	lap_button2.place(x=1140,y=300,width=200,height=75)
	reset_button2.place(x=920,y=300,width=200,height=75)
	clock_frame2.place(x=710,y=40,width=600,height=200)

def lap2():
	global time_elapsed7,time_elapsed8,time_elapsed9,time5,self_job2,time6
	pp2 = Label(text=('3-STOL'+'\n'+str(time_elapsed9).zfill(1)+':'+str(time_elapsed8).zfill(1)+':'+str(time_elapsed7).zfill(1)+'\n'+str(f'{(2000/6)*(time_elapsed9*60+time_elapsed8):.2f}').zfill(1)+" so'm"),bg='black',fg='blue',font=('default',45,'bold'))
	pp2.place(x=740,y=460,width=600,height=200)
	ti2 = str(time_elapsed9)+':'+str(time_elapsed8)+':'+str(time_elapsed7)
	li2 = f'{(2000/6)*(time_elapsed9*60+time_elapsed8):.2f}'
#Creating the buttons and widgets
clock_frame2=Label(text="3-STOL",bg='black',fg='blue',font=('default',50,'bold'))
start_button2=Button(text="START",bg='green',fg='black',command=start2,font=('default',20,'bold'))
stop_button2=Button(text="STOP",bg='red',fg='black',command=stop2,font=('default',20,'bold'))
resume_button2=Button(text="RESUME",bg='green',fg='black',command=start2,font=('default',18,'bold'))
lap_button2=Button(text="LAP",bg='yellow',fg='black',command=lap2,font=('default',20,'bold'))
reset_button2=Button(text="RESET",bg='orange',fg='black',command=clear2,font=('default',20,'bold'))

#Placing the buttons and widgets
start_button2.place(x=700,y=300,width=200,height=75)
lap_button2.place(x=1140,y=300,width=200,height=75)
reset_button2.place(x=920,y=300,width=200,height=75)
clock_frame2.place(x=710,y=40,width=600,height=200)

root.mainloop()