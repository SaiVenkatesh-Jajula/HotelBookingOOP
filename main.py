import pandas as pd

df = pd.read_csv("hotels.csv", dtype={'id': str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient='records')
df_secards = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df["id"] == self.hotel_id, 'name'].squeeze()
        self.hotel_city = df.loc[df["id"] == self.hotel_id, 'city'].squeeze()

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


# Extending Feature
class Payment:
    def __init__(self, card, exdate, cvv, holder):
        self.cc = card
        self.exp = exdate
        self.cvv = cvv
        self.holder = holder

    def payment(self):
        card_data = {'number': self.cc, 'expiration': self.exp, 'cvc': self.cvv, 'holder': self.holder}
        if card_data in df_cards:
            return True
        else:
            return False


class SecurePayment(Payment):
    def validate(self, passward):
        password = df_secards.loc[df_secards['number'] == self.cc, 'password'].squeeze()
        if password == passward:
            return True
        else:
            return False


class Ticket:
    def __init__(self, name, hotel_obj):
        self.name = name
        self.hotel = hotel_obj

    def main_generate(self):
        data = f"""
        Here the Ticket details:
        Name : {self.name}
        HotelName : {self.hotel.hotel_name}
        City: {self.hotel.hotel_city}
        """
        return data


class AllTickets(Ticket):
    def spa_generate(self):
        data = f"""
        Thanks for booking SPA reservation
        Here the SPA details:
        Name : {self.name}
        HotelName : {self.hotel.hotel_name}
        City: {self.hotel.hotel_city}
        """
        return data


print(df)
hotel_id = input("Select the Hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    card_number = "1234"
    expiry_date = "12/26"
    cvv = "123"
    card_holder = "JOHN SMITH"
    payment = SecurePayment(card_number, expiry_date, cvv, card_holder)
    if payment.payment():
        if payment.validate(passward="mypass"):
            hotel.book()
            name = input("Enter Your Name: ")
            ticket = AllTickets(name, hotel)
            print(ticket.main_generate())
            spa = input("DO you want a SPA package?")
            if spa == 'yes':
                print(ticket.spa_generate())
            else:
                print("Thanks!")
        else:
            print("Authentication Failed")
    else:
        print("Something went wrong in payment")
else:
    print("Hotel is Full")
