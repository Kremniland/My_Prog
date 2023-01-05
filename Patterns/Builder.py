class Fundament:
    """Фундамент"""


class Wall:
    """Стены"""


class Roof:
    """Крыша"""


class Inner_wall:
    """Внутрення отделка"""


class Builder:
    def build_fundament(self):
        raise NotImplementedError()

    def build_wall(self):
        raise NotImplementedError()

    def build_roof(self):
        raise NotImplementedError()

    def build_inner_wall(self):
        raise NotImplementedError()


class House:
    def __init__(self, fundament, wall, roof, inner_wall):
        self.fundament = fundament
        self.wall = wall
        self.roof = roof
        self.inner_wall = inner_wall
        self.electricy = False

    def on(self):
        self.electricy = True

    def off(self):
        self.electricy = False


class HouseBuilder(Builder):
    def build_fundament(self):
        return Fundament()

    def build_wall(self):
        return Wall()

    def build_roof(self):
        return Roof()

    def build_inner_wall(self):
        return Inner_wall()

    def build_house(self):
        fundament = self.build_fundament()
        wall = self.build_wall()
        roof = self.build_roof()
        inner_wall = self.build_inner_wall()
        return House(fundament, wall, roof, inner_wall)

    def build_house_wout_inwall(self):
        fundament = self.build_fundament()
        wall = self.build_wall()
        roof = self.build_roof()
        return House(fundament, wall, roof, None)


# Pattern Builder
# Создание Дома
builder_IVAN = HouseBuilder()
house = builder_IVAN.build_house()

house_wout_inwall = builder_IVAN.build_house_wout_inwall()
# Окончание создания дома

print(house.electricy)
house.on()
print(house.electricy)
house.off()
print(house.electricy)

print(house.fundament)
print(house.wall)
print(house.roof)
print(house.inner_wall)

# Без паттерна

fundament = Fundament()
wall = Wall()
roof = Roof()
inner_wall = Inner_wall()

house = House(fundament, wall, roof, inner_wall)

house_wout_inwall = House(fundament, wall, roof, None)


