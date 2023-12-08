import customtkinter as CTk
from telebot import types
import webbrowser as web
import pyautogui as pg
import telebot
import time

bot = telebot.TeleBot("6453593089:AAHezm0x8W1V32d3lMHcprhaCQ7-Dv9XIsU")

CTk.set_default_color_theme("blue")
CTk.set_appearance_mode("dark")

app = CTk.CTk()
app.title("AutoPost")
app.geometry("300x350")

def post(id, text, btn_name, btn_url):
    btn = types.InlineKeyboardButton(text=btn_name, url=btn_url)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(btn)
    bot.send_message(chat_id=id, text=text, reply_markup=keyboard)

id_input = CTk.CTkEntry(app, text_color="white", width=230)
text_input = CTk.CTkEntry(app, text_color="white", width=230)
btn_name_input = CTk.CTkEntry(app, text_color="white", width=230)
btn_url_input = CTk.CTkEntry(app, text_color="white", width=230)
btn_ok = CTk.CTkButton(app, text_color="white", text="Post", width=230, command=lambda: post(id=id_input.get(), text=text_input.get(), btn_name=btn_name_input.get(), btn_url=btn_url_input.get()))
btn_bot = CTk.CTkButton(app, text_color="white", text="Bot", width=115, command=lambda: web.open("https://t.me/PostYourBot"))
btn_id_bot = CTk.CTkButton(app, text_color="white", text="ID Bot", width=115, command=lambda: web.open("https://t.me/username_to_id_bot"))

text_id = CTk.CTkLabel(app, text="ID Chat", text_color="white")
text = CTk.CTkLabel(app, text="Text Message", text_color="white")
text_btn_name = CTk.CTkLabel(app, text="Button Name", text_color="white")
text_btn_url = CTk.CTkLabel(app, text="URL", text_color="white")

id_input.place(x=37, y=55, anchor='w')
text_input.place(x=37, y=115, anchor='w')
btn_name_input.place(x=37, y=175, anchor='w')
btn_url_input.place(x=37, y=235, anchor='w')
btn_ok.place(x=37, y=275, anchor='w')
btn_bot.place(x=37, y=315, anchor='w')
btn_id_bot.place(x=153, y=315, anchor='w')

text_id.place(x=38, y=25, anchor='w')
text.place(x=38, y=85, anchor='w')
text_btn_name.place(x=38, y=145, anchor='w')
text_btn_url.place(x=38, y=205, anchor='w')

if __name__ == "__main__":
    app.mainloop()
    bot.infinity_polling()