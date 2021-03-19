# importing modules
from tkinter import *
import requests

# Sending request to kayne website using their api 
def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    # Getting hold of quote
    quote = data["quote"]
    # changing our user interface with quote 
    canvas.itemconfig(quote_text, text=quote)

#creating window class from tk module
window = Tk()
# Setting parameters
window.title("Kanye Says...")
window.config(padx=50, pady=50)
#creating canvas from tk modules to show interface
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click My Face To Get Some Quotes", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
