
import tkinter as tk
from tkinter import messagebox,simpledialog
root=tk.Tk()
root.title("WORLD QUIZ GAME")
root.geometry("600x600")
top_frame=tk.Frame(root,bg="#f4f4f9",height=300,width=300)
top_frame.pack(side="top",fill="both",expand=True)
bottom_frame=tk.Frame(root,bg="#ffffff",height=300,width=300)
bottom_frame.pack(side="bottom",fill="both",expand=True)
canvas_btn=tk.Canvas(root,bg="#4a90e2",height=200,width=200,highlightthickness=0)
canvas_btn.place(relx=0.5,rely=0.5,anchor="center")
circle=canvas_btn.create_oval(0,0,195,195,fill="white",outline="")
text=canvas_btn.create_text(100,100,text="Log In",fill="yellow",font=("Arial",25,"bold italic"))
import json
with open("World_quiz.json","r") as file:
    question_data=json.load(file)
import json
with open("Technology_and_innovation.json","r") as file:
    question_data_data=json.load(file)
score=0
current_index=0
question_Label=None
def enter_name(event):
    canvas_btn.place_forget()
    user_name=simpledialog.askstring("Hello","Please Enter your name.")
    while True:
        if not user_name or not user_name.strip():
           messagebox.showwarning("HELLO","ENTER YOUR NICK NAME OR WE WILL BE REGISTERED YOU AS GUEST.")
           user_name=simpledialog.askstring("HEllo","Enter your name please.")
           if not user_name or not user_name.strip():
              messagebox.showinfo("HELLO","WE REGISTERED YOU AS A GUEST.")
              user_name="GUEST".upper().strip()
              break
        else:
           user_name=user_name.strip()
           break
    show_main_menu()
canvas_btn.tag_bind(circle,"<Button-1>",enter_name)
canvas_btn.tag_bind(text,"<Button-1>",enter_name)
def show_main_menu():
    for  widget in top_frame.winfo_children():
        if isinstance(widget,(tk.Label,tk.Button)) and  widget not in (title_Label,end_btn):
            widget.place_forget()
    for widget in bottom_frame.winfo_children():
            widget.place_forget()
    restart_btn.place_forget()
    end_btn.place(relx=1.0,rely=0.0,anchor="ne") 
    title_Label.place(relx=0.5,rely=0.1,anchor="n")
    info_la.place(relx=0.5,rely=0.6,anchor="center")
    world_quiz_button.place(relx=0.5,rely=0.5,anchor="center")
    tect_quiz_button.place(relx=0.55,rely=0.65,anchor="center")
def world_quiz():
    global score,current_index
    score=0
    current_index=0
    title_Label.place_forget()
    info_la.place_forget()
    world_quiz_button.place_forget()
    tect_quiz_button.place_forget()
    open_quiz()
def tect_quiz():
    global score,current_index
    score=0
    current_index=0
    title_Label.place_forget()
    info_la.place_forget()
    world_quiz_button.place_forget()
    tect_quiz_button.place_forget()
    open_tect_quiz()
def reset_game():
    show_main_menu()
def open_quiz():
    global question_Label,current_index,score
    for widget in top_frame.winfo_children():
        widget.place_forget()
    for widget in bottom_frame.winfo_children():
        if widget !=world_quiz_button:
          if widget !=tect_quiz_button:
             widget.destroy()
    if question_Label:
        question_Label.destroy()
    restart_btn.place(relx=0.0,rely=0.0,anchor="nw")
    end_btn.place(relx=1.0,rely=0.0,anchor="ne")
    question_list=question_data["questions"]
    if current_index<len(question_list):
        question_dict=question_list[current_index]
        question_Label=tk.Label(top_frame,text=question_dict["question"],bg="#2d4a3e",fg="white",font=("Arial",30,"bold italic"),wraplength=450,justify="center")
        question_Label.place(relx=0.5,rely=0.1,anchor="n")
        for i,option in enumerate(question_dict["options"]):
            y_position=0.2 + (i*0.18)
            option_button=tk.Button(bottom_frame,text=option,bg="#f4f4f9",fg="#1b2e24",font=("Arial",15,"bold italic"),command=lambda opt=option: check_answer(opt))
            option_button.place(relx=0.5,rely=y_position,anchor="center")
    else:
        end_Label=tk.Label(top_frame,text=f"GAME OVER!YOUR SCORE IS :{score}/{len(question_list)}",bg="white",fg="#1b2e24",font=("Arial",12,"bold italic"))
        end_Label.place(relx=0.5,rely=0.0,anchor="ne")
def check_answer(user_choice):
    global score,current_index
    question_list=question_data["questions"]
    correct_answer=question_list[current_index]["answer"]
    if user_choice==correct_answer:
        score+=1
        messagebox.showinfo("Result","Correct")
    else:
        messagebox.showinfo("Result",f"Wrong\nThe correct answer is: {correct_answer}")
    current_index+=1
    open_quiz()
def open_tect_quiz():
    global question_Label,current_index,score
    for widget in top_frame.winfo_children():
        widget.place_forget()
    for widget in bottom_frame.winfo_children():
        if widget !=world_quiz_button:
          if widget !=tect_quiz_button:
             widget.destroy()
    if question_Label:
        question_Label.destroy()
    restart_btn.place(relx=0.0,rely=0.0,anchor="nw")
    end_btn.place(relx=1.0,rely=0.0,anchor="ne")
    question_list=question_data_data["questions"]
    if current_index<len(question_list):
        question_dict=question_list[current_index]
        question_Label=tk.Label(top_frame,text=question_dict["question"],bg="#1e1e2e",fg="#8be9fd",font=("Arial",30,"bold italic"),wraplength=450,justify="center")
        question_Label.place(relx=0.5,rely=0.1,anchor="n")
        for i,option in enumerate(question_dict["options"]):
            y_position=0.2 + (i*0.18)
            option_button=tk.Button(bottom_frame,text=option,bg="#252538",fg="white",font=("Arial",15,"bold italic"),command=lambda opt=option: check_ans(opt))
            option_button.place(relx=0.5,rely=y_position,anchor="center")
    else:
        end_Label=tk.Label(top_frame,text=f"GAME OVER!YOUR SCORE IS :{score}/{len(question_list)}",bg="#1e1e2e",fg="#8be9fd",font=("Arial",12,"bold italic"))
        end_Label.place(relx=0.5,rely=0.0,anchor="ne")
def check_ans(user_choice):
    global score,current_index
    question_list=question_data_data["questions"]
    correct_answer=question_list[current_index]["answer"]
    if user_choice==correct_answer:
        score+=1
        messagebox.showinfo("Result","Correct")
    else:
        messagebox.showinfo("Result",f"Wrong\nThe correct answer is: {correct_answer}")
    current_index+=1
    open_tect_quiz()
title_Label=tk.Label(top_frame,text="WELCOME TO THE WORLD QUIZ",bg="#1e1e2e",fg="#f4f4f9",font=("Arial",25,"bold italic"))
title_Label.place(relx=0.5,rely=0.1,anchor="n")
info_la=tk.Label(top_frame,text="Each Category contains 30 questions",bg="#1e1e2e",fg="#8be9fd",font=("Consolas",25,"italic"))
world_quiz_button=tk.Button(bottom_frame,text="WORLD QUIZ",command=world_quiz,bg="#2d4a3e",fg="white",font=("Arial",25,"bold italic"),bd=0,relief="flat")
tect_quiz_button=tk.Button(bottom_frame,text="tech QUIZ",command=tect_quiz,bg="#252538",fg="#8be9fd",font=("Arial",25,"bold italic"),bd=0,relief="flat")
restart_btn=tk.Button(top_frame,text="Restart",command=reset_game)
end_btn=tk.Button(top_frame,text="EXIT",command=root.destroy)
end_btn.place(relx=1.0,rely=0.0,anchor="ne")
root.mainloop()
