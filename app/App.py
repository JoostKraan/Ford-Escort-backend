import customtkinter

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue") 

app = customtkinter.CTk()  
app.geometry("1024x600")

def button_function():
    print("button pressed")


button = customtkinter.CTkButton(master=app, fg_color="#7A7979", text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()