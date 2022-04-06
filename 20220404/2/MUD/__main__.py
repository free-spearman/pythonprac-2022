
"""Модуль для запуска MUD $python3 -m MUD.

Запускает простейший multi-user dungeon.
Игровые команды:
- show;
- do_attack;
- do_add;
- do_move;
- do_exit.
"""

from .logic import GameMap
from .interface import Repl


def start():
    """Функция для запуска игры."""
    Repl(GameMap()).cmdloop()


start()
