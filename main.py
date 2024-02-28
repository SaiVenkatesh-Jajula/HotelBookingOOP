import pandas as pd

df = pd.read_csv("hotels.csv", dtype={'id':str})

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df["id"]==self.hotel_id, 'name'].squeeze()
        self.hotel_city = df.loc[df["id"]==self.hotel_id, 'city'].squeeze()
    def book(self):
        """Book a hotel by changing its availabity as no"""
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        """Check whether hotel is available"""
        check = df.loc[df['id'] == self.hotel_id]['available'].squeeze()
        if check == 'yes':
             return True
        else:
             return False

class Ticket:
    def __init__(self,name,hotel_obj):
        self.name = name
        self.hotel = hotel_obj

    def generate(self):
        data = f"""
        Here the Ticket details:
        Name : {self.name}
        HotelName : {self.hotel.hotel_name}
        City: {self.hotel.hotel_city}
        """
        return data

print(df)
hotel_id = input("Select the Hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("Enter Your Name: ")
    ticket = Ticket(name, hotel)
    print(ticket.generate())
else:
    print("Hotel is Full")



