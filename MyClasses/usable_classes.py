from abstracts import *


class ApartmentSale(Apartment, Sale):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ApartmentRent(Apartment, Rent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class VillaSale(Villa, Sale):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class VillaRent(Villa, Rent):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


class ShopSale(Shop, Sale):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


class ShopRent(Shop, Rent):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


obj = ApartmentRent(meterage="250", rooms="2", age="10", address="fardis", fullname="amirmasoodpormahdi",
                    phone_number="09356107427", name="falake 4", mortgage="yes", rent="10000", discount="10%",
                    convertable="no", elevator="yes", parking="yes", floor="4")
obj3 = ApartmentRent(meterage="250", rooms="2", age="10", address="fardis", fullname="amirmasood",
                     phone_number="09356207427", name="falake 4", mortgage="yes", rent="10000", discount="10%",
                     convertable="no", elevator="yes", parking="yes", floor="4")
obj2 = ApartmentSale(meterage="250", rooms="2", age="10", address="fardis", fullname="ahmad",
                     phone_number="09356107428", name="falake 4", elevator="yes", parking="yes", floor="4",
                     discount="10%", price_per_meter=150, exchange=False)
print(obj.id)
print(obj3.id)
print(obj2.id)
print(Property.objects_list)
print(obj2.objects_list)
print(obj.seller.objects_list)


