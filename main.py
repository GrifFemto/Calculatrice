import customtkinter

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.title('Caclulatrice 1.0')
app.geometry("380x600")

screen_font = ("Courrier",55,'bold')
screen = customtkinter.CTkLabel(app,text="0",font=screen_font)
screen.grid(row=0,column=0,sticky="E",padx=(10,10),pady=(20,30),columnspan=4)


font_bouton = ("Arial",30,"bold")

btn_0 = customtkinter.CTkButton(app,text="0",width=75, height=75, font=font_bouton)
btn_1 = customtkinter.CTkButton(app,text="1",width=75, height=75, font=font_bouton)
btn_2 = customtkinter.CTkButton(app,text="2",width=75, height=75, font=font_bouton)
btn_3 = customtkinter.CTkButton(app,text="3",width=75, height=75, font=font_bouton)
btn_4 = customtkinter.CTkButton(app,text="4",width=75, height=75, font=font_bouton)
btn_5 = customtkinter.CTkButton(app,text="5",width=75, height=75, font=font_bouton)
btn_6 = customtkinter.CTkButton(app,text="6",width=75, height=75, font=font_bouton)
btn_7 = customtkinter.CTkButton(app,text="7",width=75, height=75, font=font_bouton)
btn_8 = customtkinter.CTkButton(app,text="8",width=75, height=75, font=font_bouton)
btn_9 = customtkinter.CTkButton(app,text="9",width=75, height=75, font=font_bouton)
btn_plus = customtkinter.CTkButton(app,text="+",width=75, height=180, font=font_bouton)
btn_moins = customtkinter.CTkButton(app,text="-",width=75, height=75, font=font_bouton)
btn_fois = customtkinter.CTkButton(app,text="x",width=75, height=75, font=font_bouton)
btn_diviser = customtkinter.CTkButton(app,text="/",width=75, height=75, font=font_bouton)
btn_point = customtkinter.CTkButton(app,text=".",width=75, height=75, font=font_bouton)
btn_egal = customtkinter.CTkButton(app,text="=",width=75, height=75, font=font_bouton)
btn_reset = customtkinter.CTkButton(app,text="Caca",width=75, height=75, font=font_bouton)

btn_0.grid(row=5,column=0,padx=(10,10),pady=(10,10))
btn_1.grid(row=4,column=0,padx=(10,10),pady=(10,10))
btn_2.grid(row=4,column=1,padx=(10,10),pady=(10,10))
btn_3.grid(row=4,column=2,padx=(10,10),pady=(10,10))
btn_4.grid(row=3,column=0,padx=(10,10),pady=(10,10))
btn_5.grid(row=3,column=1,padx=(10,10),pady=(10,10))
btn_6.grid(row=3,column=2,padx=(10,10),pady=(10,10))
btn_7.grid(row=2,column=0,padx=(10,10),pady=(10,10))
btn_8.grid(row=2,column=1,padx=(10,10),pady=(10,10))
btn_9.grid(row=2,column=2,padx=(10,10),pady=(10,10))
btn_plus.grid(row=4,column=3,padx=(10,10),pady=(10,10),rowspan=2)
btn_moins.grid(row=3,column=3,padx=(10,10),pady=(10,10))
btn_fois.grid(row=2,column=3,padx=(10,10),pady=(10,10))
btn_diviser.grid(row=1,column=3,padx=(10,10),pady=(10,10))
btn_point.grid(row=5,column=1,padx=(10,10),pady=(10,10))
btn_egal.grid(row=5,column=2,padx=(10,10),pady=(10,10))
btn_reset.grid(row=1,column=0,padx=(10,10),pady=(10,10))


app.mainloop()