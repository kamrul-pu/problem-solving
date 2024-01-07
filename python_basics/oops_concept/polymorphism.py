class Bird:
    def intro(self) -> None:
        print("There are many types of birds.")

    def flight(self) -> None:
        print("Most of the birds can fly but some cannot.")


class Sparrow(Bird):
    def flight(self) -> None:
        print("Sparrows can fly.")


class Ostrich(Bird):
    def flight(self) -> None:
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
