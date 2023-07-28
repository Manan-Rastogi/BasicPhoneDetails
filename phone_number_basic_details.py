from phonenumbers import timezone, carrier, geocoder
import phonenumbers

class PhoneDetails:
    def __init__(self, phone_number) -> None:
        self.number = phone_number

    def get_phone_number_details(self):
        phone = phonenumbers.parse(self.number)
        time = timezone.time_zones_for_number(phone)
        carrier_n = carrier.name_for_number(phone, lang='en')
        registration = geocoder.description_for_number(phone, lang='en')

        return dict({
            "Phone": phone,
            "TZ": time,
            "Carrier": carrier_n,
            "Registration": registration
        })
    

ph = PhoneDetails("+9189******12")
print(ph.get_phone_number_details())