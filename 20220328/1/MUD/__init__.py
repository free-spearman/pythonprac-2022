"""
MUD - пакет реализующий простейший multi-user dungeon

Имеется поле 10х10 клеток (по каждой оси нумерация с 0 по 9); рисовать поле и
его наполнение - не нужно в каждой клетке может находиться 0 или более
монстров, у каждого монстра есть имя и число очков здоровья (hp - hit points)
по полю ходит игрок; попав на клетку с монстром, он может его атаковать,
нанося урон (списывая очки здоровья) в начале игры игрок появляется в
случайной клетке (0, 0) клетка с координатами (0, 0) находится в левом верхнем
углу поля настройка поля и игровой процесс организованы при помощи
командной строки.

:copyright: (c) 2022 by Ilya Badekin
:license: MIT, see COPYING for more details.
"""
from MUD import logic, interface, constans  # noqa: F401
