class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number = number_of_floors

    def go_to(self, new_floor):

        if not(new_floor < 1 or new_floor > self.number):
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print(f'В доме "{self.name}" этажа с номером "{new_floor}" не существует!')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)