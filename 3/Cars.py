from os.path import splitext
import csv

class CarBase:
    def __init__(
            self,
            car_type: str,
            photo_file_name: str,
            brand: str,         
            carrying: float
            ) -> None:
        self.__car_type = car_type
        self.__brand = brand
        self.__photo_file_name = photo_file_name        
        self.__carrying = carrying

    def __str__(self) -> str:
        return (
            f"{self.__car_type}\t"
            f"{self.__brand}\t"
            f"{self.__photo_file_name}\t"
            f"carrying={self.__carrying}\t"
        )

    def get_photo_file_ext(self) -> str:
        """Возращает расширение файла с фото."""
        
        return splitext(self.__photo_file_name)[1]
    
    @property
    def photo_file_name(self) -> str:
        return self.__photo_file_name
    
    @property
    def brand(self) -> str:
        return self.__brand
    
    @property
    def carrying(self) -> float:
        return self.__carrying

class Car(CarBase):
    def __init__(
            self,  
            photo_file_name: str, 
            brand: str, 
            carrying: float,
            passenger_seats_count: int
            ) -> None:
        super().__init__("car", photo_file_name, brand, carrying)
        self.__passenger_seats_count = passenger_seats_count

    def __str__(self) -> str:
        return (
            f"{super().__str__()}\t"
            f"passenger_seats_count={self.__passenger_seats_count}\t"
        )
    
    @property
    def passenger_seats_count(self) -> int:
        return self.__passenger_seats_count

class Truck(CarBase):
    def __init__(
            self, 
            photo_file_name: str, 
            brand: str, 
            carrying: float,
            body_width: float,
            body_height: float,
            body_length: float
            ) -> None:
        super().__init__("truck", photo_file_name, brand, carrying)
        self.__body_width = body_width
        self.__body_height = body_height
        self.__body_length = body_length

    def __str__(self) -> str:
        return (
                f"{super().__str__()}\t"
                f"body_height={self.__body_height}\t"                
                f"body_width={self.__body_width}\t"
                f"body_length={self.__body_length}\t"
            )

    def get_body_volume(self) -> float:
        """Возращает объем кузова грузового автомобиля."""

        return self.__body_height * self.__body_length * self.__body_width
    
    @property
    def body_whl(self) -> tuple[float, float, float]:
        return (self.__body_length, self.__body_width, self.__body_height)

class SpecMachine(CarBase):
    def __init__(
            self, 
            photo_file_name: str, 
            brand: str, 
            carrying: float,
            extra: str) -> None:
        super().__init__("spec_machine", photo_file_name, brand, carrying)
        self.__extra = extra

    def __str__(self) -> str:
        return f"{super().__str__()}\t{self.__extra}\t"
    
    @property
    def extra(self) -> str:
        return self.__extra

def get_car_list(csv_filename: str) -> list[CarBase]:
    """Возращает список объектов из файла, наследованных от CarBase. 
    Например Car, Truck, SpecMachine."""

    def get_rows()->list[list]:
        with open(csv_filename, encoding="utf-8") as file:
            rows = csv.reader(file, delimiter=";")
            next(rows)
            return list(rows)

    def parse(row: list[str])->CarBase:
        car_type: str = row[0]
        brand: str = row[1]
        photo_file_name: str = row[3]
        carrying: float = float(row[5])
            
        if splitext(photo_file_name)[1] == '':
            raise ValueError

        try:
            body_whl: list[str] = row[4].split('x')
            (body_length, body_width, body_height) = (
                float(body_whl[0]), float(body_whl[1]), float(body_whl[2])
            )
        except:
            (body_length, body_width, body_height) = (0.0, 0.0, 0.0)

        match car_type:
            case "car":
                return Car(photo_file_name, brand, carrying, passenger_seats_count=int(row[2]))
            case "truck":
                return Truck(photo_file_name, brand, carrying, body_width, body_height, body_length)
            case "spec_machine":
                return SpecMachine(photo_file_name, brand, carrying, extra= row[6])
            case _:
                raise TypeError

    car_list = []
    rows = get_rows()
    
    """
        Альтернативный вариант:
            for row in rows:
                try:
                    yield parse(row)
                except:
                    pass
        но по заданию нужно вернуть список.
    """

    for row in rows:
        try:
            car_list.append(parse(row))
        except:
            print(f"Unable to parse a value in {rows.index(row) + 1} row")    
    
    return car_list