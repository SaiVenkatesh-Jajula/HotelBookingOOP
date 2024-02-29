import pandas
from abc import ABC, abstractmethod
df = pandas.read_csv("../hotels.csv", dtype={"id": str})

class Hotel:
    domain = 'Reliance'
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    @classmethod
    def total_hotels(cls):
        return len(df)

    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False

class ticket(ABC):

    @abstractmethod
    def generate(self):
        #we can hide the implementation
        pass
class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    @property
    def the_customer_name(self):
        updatedname = self.customer_name.title()
        return updatedname

    @staticmethod
    def convert(amount):
        return amount*80

hotel1=Hotel('134')
hotel2=Hotel('134')
print(hotel1==hotel2)


print(hotel2.domain)
print(Hotel.domain)

print(hotel1.available())
print(Hotel.total_hotels())
print(hotel1.total_hotels())

ticket = ReservationTicket("sai",hotel1)
print(ticket.the_customer_name)

print(ticket.convert(10))
print(ReservationTicket.convert(100))




