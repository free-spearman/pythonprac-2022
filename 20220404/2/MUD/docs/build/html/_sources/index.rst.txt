.. MUD documentation master file, created by
   sphinx-quickstart on Wed Apr  6 14:10:12 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MUD's documentation!
===============================

Программа, реализующая простейший multi-user dungeon

#. имеется поле 10х10 клеток (по каждой оси нумерация с 0 по 9);
#. в каждой клетке может находиться 0 или более монстров, у каждого монстра есть имя и число очков здоровья (hp - hit points)
#. по полю ходит игрок; попав на клетку с монстром, он может его атаковать, нанося урон (списывая очки здоровья)
#. в начале игры игрок появляется в клетке (0, 0)
#. клетка с координатами (0, 0) находится в левом верхнем углу поля
#. настройка поля и игровой процесс организованы при помощи командной строки (shlex/cmd);

.. toctree::
   :maxdepth: 4
   :caption: Содержание:

   MUD.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
