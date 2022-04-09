import csv

class Helper:
    def __init__(self) -> None:
        pass

    # return new KM/H after applied the brak pressure.
    def brak_efficent(speed, brak_pressure):
        # just a simple equation, real world is more complicated
        # just to demostrate our modle can avoid collision.
        return 0 if speed <= 0 else speed - brak_pressure * 0.75

    def explot_csv(name, data):
        with open(name, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            writer.writerows(data)

