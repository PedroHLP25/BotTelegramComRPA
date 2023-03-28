import telebot
import pyautogui
import pyperclip
import time

CHAVE_API = "chave"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["Computacao_ReceberPDF"])
def Computacao_ReceberPDF(mensagem):
    pyautogui.PAUSE = 1

    #Navegação e Dowload do PDF da GRADE
    pyautogui.press("win")
    pyautogui.write("opera")
    pyautogui.press("enter")
    pyperclip.copy("http://www.uabj.ufrpe.br/sites/uabj.ufrpe.br/files/horario_2022-1_QuadroDeAulas_NoSigaa251022_Salas.pdf")
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.click(x=1807, y=125)
    pyautogui.click(x=355, y=457)
    pyautogui.click(x=1033, y=781)

    #E-mail

    pyautogui.hotkey("ctrl","t")
    pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(x=129, y=192)
    pyperclip.copy("pedrohlp2067@gmail.com")
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyperclip.copy("PDF com informações dos Horários da Grade de todos os períodos de engenharia da computação UFRPE/UABJ")
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.click(x=1422, y=1002)
    pyautogui.click(x=1518, y=939)
    pyautogui.click(x=379, y=456)
    pyautogui.click(x=516, y=443)
    pyautogui.hotkey("ctrl","enter")
    pyautogui.hotkey("ctrl","enter")
    
    bot.send_message(mensagem.chat.id, "O  PDF referente a grade e horários de computação foi enviado para seu e-mail com sucesso")

@bot.message_handler(commands=["ControleAutomacao_ReceberPDF"])
def ControleAutomacao_ReceberPDF(mensagem):
    bot.send_message(mensagem.chat.id, "Por enquanto só computação está recebendo o  pdf por e-mail")

@bot.message_handler(commands=["Quimica_ReceberPDF"])
def Quimica_ReceberPDF(mensagem):
    bot.send_message(mensagem.chat.id, "Por enquanto só computação está recebendo o  pdf por e-mail")

@bot.message_handler(commands=["Hidrica_ReceberPDF"])
def Hidrica_ReceberPDF(mensagem):
    bot.send_message(mensagem.chat.id, "Por enquanto só computação está recebendo o  pdf por e-mail")

@bot.message_handler(commands=["grade"])
def grade(mensagem):
    texto = """
    Escolha sua engenharia para receber o pdf com a grade e os horários por e-mail! (Clique em uma opção)
    /Computacao_ReceberPDF
    /ControleAutomacao_ReceberPDF
    /Quimica_ReceberPDF
    /Hidrica_ReceberPDF"""
    bot.send_message(mensagem.chat.id, texto)


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Para saber mais (Clique no item):
     /grade 
Responder qualquer outra coisa não vai funcionar"""
    bot.reply_to(mensagem, texto)

bot.polling()