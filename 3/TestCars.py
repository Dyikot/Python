from Cars import *
import unittest

car = Car(
    photo_file_name="photo1.png",
    brand="bmw",
    carrying=2.5,
    passenger_seats_count=4
)
truck = Truck(
    photo_file_name="photo2.png",
    brand="man",
    carrying=20,
    body_height=8,
    body_length=2,
    body_width=3
)
spec_machine = SpecMachine(
    photo_file_name="photo3.png",
    brand="lovol",
    carrying=6,
    extra="мини-трактор"
)

class TestCars(unittest.TestCase):
    def test_instance_check(self):
        self.assertIsInstance(car, CarBase)
        self.assertIsInstance(truck, CarBase)
        self.assertIsInstance(spec_machine, CarBase)

    def test_file_ext(self):
        self.assertEqual(car.get_photo_file_ext(), ".png")

    def test_truck_body_volume(self):
        (height, width, length) = truck.body_whl
        self.assertEqual(truck.get_body_volume(), height * width * length)


if __name__ == "__main__":
    unittest.main()