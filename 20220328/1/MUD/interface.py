
"""
Интерфейс для игры пакета MUD.

Содержит в себе класс Repl.
"""

import shlex
import cmd
from MUD.constans import X_AXIS, Y_AXIS, NAME, HP, CRDS


class Repl(cmd.Cmd):
    """
    class Repl - консольный интерфейс.

    Методы:
    - do_show;
    - do_attack;
    - do_add;
    - do_move;
    - do_exit.
    """

    prompt = '>-<'

    def __init__(self, GameMap):
        """
        __init__, p - GameMap.

        Дополняет родителя и уст map.
        """
        super(Repl, self).__init__()
        self.map = GameMap

    def do_show(self, args):
        """Показать всех монстров."""
        if args.strip() != 'monsters ':
            print("Error comand")
            return
        self.map.show_monsters()

    def do_attack(self, name):
        """Атакует <имя монстра>."""
        name = ' '.join(shlex.split(name))
        coords = self.map.player_coords
        field = self.map.map[coords[Y_AXIS]][coords[X_AXIS]]
        if not field:
            print(f"no {name} here")
            return
        tgt_monster = ''
        for m in field:
            if m.name == name:
                tgt_monster = m
        if not tgt_monster:
            print(f"no {name} here")
            return
        # если смертт, то ложь
        if not tgt_monster.take_damage(10):
            field.remove(tgt_monster)
            self.map.map[coords[Y_AXIS]][coords[X_AXIS]] = field
            self.map.monsters.remove(tgt_monster)

    def do_add(self, args):
        """Добавляет объект (пока только монстра) на карту."""
        args = shlex.split(args)
        if len(args) < 8:
            print("Error comand")
            return
        if args[0] != 'monster' or args[1] != 'name':
            print("Error comand")
            return
        args = args[2:]

        if 'hp' not in args:
            print("Error comand")
            return
        index = args.index('hp')
        name = ' '.join(args[:index])
        hp = int(args[index+1])
        coords = (int(args[-1]), int(args[-2]))
        monster = {NAME: name, HP: hp, CRDS: coords}
        self.map.add_obj(coords, self.map.create_monster(monster))

    def do_move(self, args):
        """
        Перемещает персонажа.

        Перемещает в одном из направлений: up, down, left, right.
        """
        trend = shlex.split(args)
        if len(trend) != 1:
            print("Error comand")
            return
        print(trend)
        trend = trend[0]
        if trend == 'up':
            self.map.move(Y_AXIS, -1)
        elif trend == 'down':
            self.map.move(Y_AXIS, 1)
        elif trend == 'left':
            self.map.move(X_AXIS, -1)
        elif trend == 'right':
            self.map.move(X_AXIS, 1)
        else:
            print("Error comand")
        return

    def complete_move(self, prefix, allcommand, beg, end):
        """Дает подсказки по TAB для move."""
        l_dir = ['up', 'down', 'right', 'left']
        return [s for s in l_dir if s.startswith(prefix)]

    def complete_add(self, prefix, allcommand, beg, end):
        """Дает подсказки по TAB для add."""
        hepl_ms = ("monster name <monster's name> hp <hp points> coords <X> <Y>", )  # noqa: E501
        return [s for s in hepl_ms if s.startswith(prefix)]

    def complete_attack(self, prefix, allcommand, beg, end):
        """Дает подсказки по TAB для attack."""
        coords = self.map.player_coords
        field = self.map.map[coords[Y_AXIS]][coords[X_AXIS]]
        monsters_list = (s.name for s in field)
        return [s for s in monsters_list if s.startswith(prefix)]

    def complete_show(self, prefix, allcommand, beg, end):
        """Дает подсказки по TAB для show."""
        return [s for s in ("monsters",) if s.startswith(prefix)]

    def do_exit(self, arg):
        """Exit the command line."""
        print("Come back soon")
        return True
