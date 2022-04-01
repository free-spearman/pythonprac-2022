from .logic import GameMap
from .interface import Repl  

def start ():
	""" функция для запуска игры """
	Repl(GameMap()).cmdloop()

start()