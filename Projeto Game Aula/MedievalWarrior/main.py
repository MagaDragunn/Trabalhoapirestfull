import pygame as py

print("Setup Iniciador")
py.init()
window = py.display.set_mode(size=(800, 600))
print("Setup Encerrar")

print("Janela Rodando loop")
while True:
    # Check for all events
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()  # close Windows
            quit()  # end pygame
