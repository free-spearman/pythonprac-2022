
"""Модуль для запуска MUD $python3 -m MUD."""

from .logic import GameMap
from .interface import Repl


def start():
    """Функция для запуска игры."""
    Repl(GameMap()).cmdloop()


start()
