import pyautogui
import pandas as pd
import time

# Importar a base de produtos

tabela = pd.read_csv("produtos.csv")
# cprint(tabela)

# Define o tmepo de espera os comandos do Pyautogui

pyautogui.PAUSE = 0.3

# Abrir sistema
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

time.sleep(1.5)

# Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Espera carregar
time.sleep(3)

# Fazer login (aqui pode preencher com qualquer dado de login)
pyautogui.click(x=580, y=360)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")  # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Aqui precisamos percorrer as linhas da tabela.
# Para cada linha vamos cadastrar um produto.

# Seleciona apenas as duas primeiras linhas
for linha in tabela.iloc[:10].index:
    pyautogui.click(x=573, y=243)  # Clica no 1° Campo
    # Pega o código da tabela e escreva no campo
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")  # Passa pro proximo campo
    # agora repete isso para os outros campos
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")  # Passa pro proximo campo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))  # Passa pro proximo campo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # Verifica se esiste informação em obs, caso contrario não precisa preencher
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")  # Clica no botão cadastrar
    # Faz scroll para baixo para cadastrar o próximo produto
    pyautogui.scroll(5000)
