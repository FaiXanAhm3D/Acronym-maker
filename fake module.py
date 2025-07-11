import faker
fake=faker.Faker()
print("Fake name")
print(fake.name())
print("Fake address")
print(fake.address())
print("Fake text")
print(fake.text())
print("Fake email")
print(fake.email())
print("Fake country")
print(fake.country())
print("Fake Latitude and longitude ")
print(fake.latitude(),fake.longitude())
print("Fake url")
print(fake.url())
print("Fake credit card details")
print(fake.credit_card_full())
print("Fake phone number")
print(fake.phone_number())
print("Fake license plate")
print(fake.license_plate())
print("Fake currency")
print(fake.currency())
print("Fake Color name")
print(fake.color_name())
print("Fake local location")
print(fake.local_latlng())
print("Fake domain")
print(fake.domain_name())
print("Fake company")
print(fake.company())










with open('faker_module.txt','w') as dir_faker:
    a=dir(faker)
    for i in a:
        dir_faker.write(i+'\n')
    dir_faker.write('================================\n')
    dir_faker.write('Faker()\n')
    b=dir(fake)
    for i in b:
        dir_faker.write(i+'\n')
