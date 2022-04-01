from .constans import * 

class GameObj:
    """ Class GameObj. Родительский класс для игровых объектов"""
    def __init__(self, args):
        self.hp = int(args[HP])
        self.coords = args[CRDS]
        self.name = args[NAME]
    def __str__(self):
        result = f"{self.name} at ({self.coords[X_AXIS]} {self.coords[Y_AXIS]}) hp {self.hp}"
        return result
    def take_damage(self, dmg):
        """ если убили - False, иначе hp"""
        self.hp = self.hp - dmg
        if self.hp < 1:
            print(f"{self.name} dies")
            return False
        print(f"lost 10 hp, now has {self.hp} hp")        
        return self.hp  

class Monster(GameObj):
    """ Class Monster, наследник GameObj"""
    def __init__(self, args):
        super().__init__(args)
        self.type = MONSTER

class GameMap:
    """ карта """
    def __init__(self):
        self.map = [[False for _ in range(X_SIZE)] for _ in range(Y_SIZE)]
        print()
        self.player_coords = [0, 0]
        print('Player at', *(self.player_coords))
        self.monsters = []
    
    def show_monsters (self):
        """ Вывод всех монстров на карте"""
        if not self.monsters:
            print("Добавьте монтсров пожалуйста, пока все тихо и пусто")
            return
        for m in self.monsters:
            print(m)    
    
    def check_coord_exit(axis,coord):
        """
        Проверка на выход за границу
        Вышли за границу - True, иначе False
        """
        if coord < 0 or coord > MAP_SIZE[axis] - 1:
            return True
        else:
            return False    
    
    def move(self, axis, step):
        """
        Return true if everything is bad, false - moving successfully
        """
        new_coord = self.player_coords[axis] + step
        if GameMap.check_coord_exit(axis ,new_coord):
            print (MOVE_ERROR_MESS)
            return True
        self.player_coords[axis] = new_coord
        print(f"Player at {self.player_coords[X_AXIS]} {self.player_coords[Y_AXIS]}")
        field = self.map[self.player_coords[Y_AXIS]][self.player_coords[X_AXIS]]
        if not field:
            return False
        for m in field:
            print(m)
        return False

    def add_obj(self, coords, obj):
        """
        добавляет объект на карту
        """
        if GameMap.check_coord_exit(Y_AXIS,coords[Y_AXIS]) or GameMap.check_coord_exit(X_AXIS,coords[X_AXIS]):
            print (MOVE_ERROR_MESS)
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
        
        if  flag_m:    
            field.append(obj)
            self.map[coords[Y_AXIS]][coords[X_AXIS]] = field 
            self.monsters.append(obj)