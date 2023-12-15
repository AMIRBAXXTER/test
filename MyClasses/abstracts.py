from abc import ABC, abstractmethod


class Manager():
    def __init__(self, _class):
        self._class = _class

    def search(self, **kwargs):
        pass



class IdStore(ABC):
    _id = 0
    objects_list = None
    manager = None

    def __init__(self, *args, **kwargs):
        self.id = self.id()
        self.store(self)
        super().__init__(*args, **kwargs)

    @classmethod
    def id(cls):
        cls._id += 1
        return cls._id

    @classmethod
    def store(cls, obj):
        if cls.objects_list is None:
            cls.objects_list = []
        cls.objects_list.append(obj)


class Property(IdStore):

    def __init__(self, meterage, rooms, age, address, fullname, phone_number, name, *args, **kwargs):
        self.seller = Seller(fullname, phone_number)
        self.meterage = meterage
        self.rooms = rooms
        self.age = age
        self.district = District(name)
        self.address = address
        super().__init__(*args, **kwargs)


class Seller(IdStore):
    def __init__(self, fullname, phone_number, *args, **kwargs):
        self.fullname = fullname
        self.phone_number = phone_number
        super().__init__(*args, **kwargs)


class District(IdStore):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)


class Apartment(Property):
    def __init__(self, floor, parking, elevator, *args, **kwargs):
        self.elevator = elevator
        self.parking = parking
        self.floor = floor
        super().__init__(*args, **kwargs)


class Villa(Property):
    def __init__(self, yard, floors, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.yard = yard
        self.floors = floors


class Shop(Property):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Sale(ABC):
    def __init__(self, price_per_meter, discount, exchange, *args, **kwargs):
        self.price_per_meter = price_per_meter
        self.discount = discount
        self.exchange = exchange
        super().__init__(*args, **kwargs)


class Rent(ABC):
    def __init__(self, mortgage, rent, discount, convertable, *args, **kwargs):
        self.mortgage = mortgage
        self.rent = rent
        self.discount = discount
        self.convertable = convertable
        super().__init__(*args, **kwargs)

