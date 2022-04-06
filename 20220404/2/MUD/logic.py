"""
Логика для игры и пакета MUD.

Есть заготовка для создания любых объектов на карте.
Этот модуль вызывается через interface.
"""

from .constans import HP, CRDS, NAME, MONSTER, MOVE_ERROR_MESS
from .constans import Y_AXIS, X_AXIS, MAP_SIZE, X_SIZE, Y_SIZE


class GameObj:
    """Родительский класс для игровых объектов."""

    def __init__(self, args):
        """Устанавливает hp, coords, name."""
        self.hp = int(args[HP])
        self.coords = args[CRDS]
        self.name = args[NAME]

    def __str__(self):
        """Кастомная строка."""
        result = f"{self.name} at ({self.coords[X_AXIS]} "\
                 f"{self.coords[Y_AXIS]}) hp {self.hp}"
        return result

    def take_damage(self, dmg):
        """Если убили - False, иначе hp."""
        self.hp = self.hp - dmg
        if self.hp < 1:
            print(f"{self.name} dies")
            return False
        print(f"lost 10 hp, now has {self.hp} hp")
        return self.hp


class Monster(GameObj):
    """Class Monster, наследник GameObj."""

    def __init__(self, args):
        """Устанавливает type = MONSTER."""
        super().__init__(args)
        self.type = MONSTER


class GameMap:
    """Карта."""

    def __init__(self):
        """Уст map, player_coords, monsters = []."""
        self.map = [[False for _ in range(X_SIZE)] for _ in range(Y_SIZE)]  # noqa: F821 E501
        print()
        self.player_coords = [0, 0]
        print('Player at', *(self.player_coords))
        self.monsters = []

    def show_monsters(self):
        """Вывод всех монстров на карте."""
        if not self.monsters:
            print("Добавьте монтсров пожалуйста, пока все тихо и пусто")
            return
        for m in self.monsters:
            print(m)

    def check_coord_exit(axis, coord):
        """
        Проверка на выход за границу.

        Вышли за границу - True, иначе False.
        """
        if coord < 0 or coord > MAP_SIZE[axis] - 1:
            return True
        else:
            return False

    def move(self, axis, step):
        """Return true if everything is bad, false - moving successfully."""
        new_coord = self.player_coords[axis] + step
        if GameMap.check_coord_exit(axis, new_coord):
            print(MOVE_ERROR_MESS)
            return True
        self.player_coords[axis] = new_coord
        print(f"Player at {self.player_coords[X_AXIS]}"
              f"{self.player_coords[Y_AXIS]}")
        field = self.map[self.player_coords[Y_AXIS]][self.player_coords[X_AXIS]]  # noqa: E501
        if not field:
            return False
        for m in field:
            print(m)
        return False

    def create_monster(self, monster):
        """Интерфейс для вызова class Monster."""
        return Monster(monster)

    def add_obj(self, coords, obj):
        """Добавляет объект на карту."""
        if GameMap.check_coord_exit(Y_AXIS, coords[Y_AXIS]) \
           or GameMap.check_coord_exit(X_AXIS, coords[X_AXIS]):
            print(MOVE_ERROR_MESS)
            return True
        field = self.map[coords[Y_AXIS]][coords[X_AXIS]]
        if not field:
            self.monsters.append(obj)
            self.map[coords[Y_AXIS]][coords[X_AXIS]] = [obj]
            return

        flag_m = True

        for item in field:
            if item.name == obj.name:
                item.hp = obj.hp
                flag_m = False
        if flag_m:
            field.append(obj)
            self.map[coords[Y_AXIS]][coords[X_AXIS]] = field
            self.monsters.append(obj)
