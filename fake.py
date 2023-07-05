import streamlit as st
import random
from faker import Faker
import string

st.set_page_config(page_title='Fake', page_icon='f.png', layout="centered", initial_sidebar_state="auto",
                   menu_items=None)


hide_streamlit_style = """
    <style>
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def usa():
    fake = Faker()

    usa_states = [
        'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
        'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
        'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
        'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
        'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
        'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
        'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
        'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
        'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
        'West Virginia', 'Wisconsin', 'Wyoming'
    ]

    def generate_fake_data(state):
        fake_data = {
            'Full Name': fake.name(),
            'Gender': random.choice(['Male', 'Female']),
            'Birthday': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            'Social Security Number': fake.ssn(),
            'Street': fake.street_address(),
            'City/Town': fake.city(),
            'State/Province/Region': state,
            'Zip/Postal Code': fake.zipcode(),
            'Phone Number': fake.phone_number(),
            'Country': 'United States',
            'Latitude': fake.latitude(),
            'Longitude': fake.longitude(),
            'Credit card brand': fake.credit_card_provider(),
            'Credit card number': fake.credit_card_number(card_type=None),
            'Expire': fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"),
            'CVV': fake.credit_card_security_code(card_type=None),
        }
        return fake_data

    st.markdown(
        "<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>USA Fake Data "
        "Generator</h1></center>",
        unsafe_allow_html=True)

    state = st.selectbox('Select a state:', usa_states)

    if st.button('Generate'):
        fake_data = generate_fake_data(state)

        for key, value in fake_data.items():
            st.write(f"{key}: {value}")


def uk():
    fake = Faker('en_GB')

    uk_counties = [
        'Bedfordshire', 'Berkshire', 'Bristol', 'Buckinghamshire', 'Cambridgeshire',
        'Cheshire', 'City of London', 'Cornwall', 'Cumbria', 'Derbyshire', 'Devon',
        'Dorset', 'Durham', 'East Riding of Yorkshire', 'East Sussex', 'Essex',
        'Gloucestershire', 'Greater London', 'Greater Manchester', 'Hampshire',
        'Herefordshire', 'Hertfordshire', 'Isle of Wight', 'Kent', 'Lancashire',
        'Leicestershire', 'Lincolnshire', 'Merseyside', 'Norfolk', 'North Yorkshire',
        'Northamptonshire', 'Northumberland', 'Nottinghamshire', 'Oxfordshire',
        'Rutland', 'Shropshire', 'Somerset', 'South Yorkshire', 'Staffordshire',
        'Suffolk', 'Surrey', 'Tyne and Wear', 'Warwickshire', 'West Midlands',
        'West Sussex', 'West Yorkshire', 'Wiltshire', 'Worcestershire'
    ]

    def generate_fake_data_uk(county):
        fake_data = {
            'Full Name': fake.name(),
            'Gender': random.choice(['Male', 'Female']),
            'Birthday': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            'National Insurance Number': fake.numerify('##-##-##-#-##-##'),
            'Street': fake.street_address(),
            'City/Town': fake.city(),
            'County': county,
            'Postal Code': fake.postcode(),
            'Phone Number': fake.phone_number(),
            'Country': 'United Kingdom',
            'Latitude': fake.latitude(),
            'Longitude': fake.longitude(),
            'Credit card brand': fake.credit_card_provider(),
            'Credit card number': fake.credit_card_number(card_type=None),
            'Expire': fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"),
            'CVV': fake.credit_card_security_code(card_type=None),
        }
        return fake_data

    st.markdown(
        "<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>UK Fake Data "
        "Generator</h1></center>",
        unsafe_allow_html=True)

    county = st.selectbox('Select a county:', uk_counties)

    if st.button('Generate'):
        fake_data = generate_fake_data_uk(county)

        for key, value in fake_data.items():
            st.write(f"{key}: {value}")


def ca():
    fake = Faker('en_CA')

    canadian_provinces = [
        'Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador',
        'Northwest Territories', 'Nova Scotia', 'Nunavut', 'Ontario', 'Prince Edward Island',
        'Quebec', 'Saskatchewan', 'Yukon'
    ]

    def generate_fake_data_canada(province):
        fake_data = {
            'Full Name': fake.name(),
            'Gender': random.choice(['Male', 'Female']),
            'Birthday': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            'Social Insurance Number': fake.numerify('###-###-###'),
            'Street': fake.street_address(),
            'City/Town': fake.city(),
            'Province': province,
            'Postal Code': generate_postal_code(),
            'Phone Number': fake.phone_number(),
            'Country': 'Canada',
            'Latitude': fake.latitude(),
            'Longitude': fake.longitude(),
            'Credit card brand': fake.credit_card_provider(),
            'Credit card number': fake.credit_card_number(card_type=None),
            'Expire': fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"),
            'CVV': fake.credit_card_security_code(card_type=None),
        }
        return fake_data

    def generate_postal_code():
        postal_code = ''
        for _ in range(3):
            postal_code += random.choice(string.ascii_uppercase)
        for _ in range(3):
            postal_code += random.choice(string.digits)
        return postal_code

    st.markdown(
        "<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Canada Fake Data "
        "Generator</h1></center>",
        unsafe_allow_html=True)

    province = st.selectbox('Select a province:', canadian_provinces)

    if st.button('Generate'):
        fake_data = generate_fake_data_canada(province)

        for key, value in fake_data.items():
            st.write(f"{key}: {value}")


def de():
    fake = Faker('de_DE')

    german_states = [
        'Baden-Württemberg', 'Bavaria', 'Berlin', 'Brandenburg', 'Bremen',
        'Hamburg', 'Hesse', 'Lower Saxony', 'Mecklenburg-Vorpommern',
        'North Rhine-Westphalia', 'Rhineland-Palatinate', 'Saarland', 'Saxony',
        'Saxony-Anhalt', 'Schleswig-Holstein', 'Thuringia'
    ]

    def generate_fake_data_germany(state):
        fake_data = {
            'Full Name': fake.name(),
            'Gender': random.choice(['Male', 'Female']),
            'Birthday': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            'Social Security Number': fake.ssn(),
            'Street': fake.street_address(),
            'City/Town': fake.city(),
            'State': state,
            'Postal Code': fake.postcode(),
            'Phone Number': fake.phone_number(),
            'Country': 'Germany',
            'Latitude': fake.latitude(),
            'Longitude': fake.longitude(),
            'Credit card brand': fake.credit_card_provider(),
            'Credit card number': fake.credit_card_number(card_type=None),
            'Expire': fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"),
            'CVV': fake.credit_card_security_code(card_type=None),
        }
        return fake_data

    st.markdown(
        "<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Germany Fake Data "
        "Generator</h1></center>",
        unsafe_allow_html=True)

    state = st.selectbox('Select a state:', german_states)

    if st.button('Generate'):
        fake_data = generate_fake_data_germany(state)

        for key, value in fake_data.items():
            st.write(f"{key}: {value}")


def spain():
    fake = Faker('es_ES')

    spanish_provinces = [
        'Álava', 'Albacete', 'Alicante', 'Almería', 'Asturias', 'Ávila',
        'Badajoz', 'Barcelona', 'Burgos', 'Cáceres', 'Cádiz', 'Cantabria',
        'Castellón', 'Ciudad Real', 'Córdoba', 'Cuenca', 'Gerona', 'Granada',
        'Guadalajara', 'Guipúzcoa', 'Huelva', 'Huesca', 'Islas Baleares',
        'Jaén', 'La Coruña', 'La Rioja', 'Las Palmas', 'León', 'Lérida',
        'Lugo', 'Madrid', 'Málaga', 'Murcia', 'Navarra', 'Orense', 'Palencia',
        'Pontevedra', 'Salamanca', 'Santa Cruz de Tenerife', 'Segovia',
        'Sevilla', 'Soria', 'Tarragona', 'Teruel', 'Toledo', 'Valencia',
        'Valladolid', 'Vizcaya', 'Zamora', 'Zaragoza'
    ]

    def generate_fake_data_spain(province):
        fake_data = {
            'Full Name': fake.name(),
            'Gender': random.choice(['Male', 'Female']),
            'Birthday': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            'National ID Number': str(random.randint(10000000, 99999999)) + random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
            'Street': fake.street_address(),
            'City/Town': fake.city(),
            'Province': province,
            'Postal Code': fake.postcode(),
            'Phone Number': fake.phone_number(),
            'Country': 'Spain',
            'Latitude': fake.latitude(),
            'Longitude': fake.longitude(),
            'Credit card brand': fake.credit_card_provider(),
            'Credit card number': fake.credit_card_number(card_type=None),
            'Expire': fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"),
            'CVV': fake.credit_card_security_code(card_type=None),
        }
        return fake_data

    st.markdown(
        "<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Spain Fake Data "
        "Generator</h1></center>",
        unsafe_allow_html=True)

    province = st.selectbox('Select a province:', spanish_provinces)

    if st.button('Generate'):
        fake_data = generate_fake_data_spain(province)

        for key, value in fake_data.items():
            st.write(f"{key}: {value}")


def jap():
    fake = Faker('ja_JP')

    japanese_prefectures = [
        'Hokkaido', 'Aomori', 'Iwate', 'Miyagi', 'Akita', 'Yamagata',
        'Fukushima', 'Ibaraki', 'Tochigi', 'Gunma', 'Saitama', 'Chiba',
        'Tokyo', 'Kanagawa', 'Niigata', 'Toyama', 'Ishikawa', 'Fukui',
        'Yamanashi', 'Nagano', 'Gifu', 'Shizuoka', 'Aichi', 'Mie',
        'Shiga', 'Kyoto', 'Osaka', 'Hyogo', 'Nara', 'Wakayama',
        'Tottori', 'Shimane', 'Okayama', 'Hiroshima', 'Yamaguchi',
        'Tokushima', 'Kagawa', 'Ehime', 'Kochi', 'Fukuoka', 'Saga',
        'Nagasaki', 'Kumamoto', 'Oita', 'Miyazaki', 'Kagoshima',
        'Okinawa'
    ]

    def generate_fake_data_japan(prefecture):
        fake_data = {
            'Full Name': fake.name(),
            'Gender': random.choice(['Male', 'Female']),
            'Birthday': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            'Resident Registration Number': fake.random_int(min=100000000000, max=999999999999),
            'Street': fake.street_address(),
            'City/Town': fake.city(),
            'Prefecture': prefecture,
            'Postal Code': fake.postcode(),
            'Phone Number': fake.phone_number(),
            'Country': 'Japan',
            'Latitude': fake.latitude(),
            'Longitude': fake.longitude(),
            'Credit card brand': fake.credit_card_provider(),
            'Credit card number': fake.credit_card_number(card_type=None),
            'Expire': fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"),
            'CVV': fake.credit_card_security_code(card_type=None),
        }
        return fake_data

    st.markdown(
        "<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Japan Fake Data "
        "Generator</h1></center>",
        unsafe_allow_html=True)

    prefecture = st.selectbox('Select a prefecture:', japanese_prefectures)

    if st.button('Generate'):
        fake_data = generate_fake_data_japan(prefecture)

        for key, value in fake_data.items():
            st.write(f"{key}: {value}")


def aus():
    fake = Faker('en_AU')

    australian_states = [
        'New South Wales', 'Victoria', 'Queensland', 'Western Australia',
        'South Australia', 'Tasmania', 'Australian Capital Territory', 'Northern Territory'
    ]

    def generate_fake_data_australia(state):
        fake_data = {
            'Full Name': fake.name(),
            'Gender': random.choice(['Male', 'Female']),
            'Birthday': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            'Tax File Number': fake.random_int(min=100000000, max=999999999),
            'Street': fake.street_address(),
            'City/Town': fake.city(),
            'State': state,
            'Postal Code': fake.postcode(),
            'Phone Number': fake.phone_number(),
            'Country': 'Australia',
            'Latitude': fake.latitude(),
            'Longitude': fake.longitude(),
            'Credit card brand': fake.credit_card_provider(),
            'Credit card number': fake.credit_card_number(card_type=None),
            'Expire': fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"),
            'CVV': fake.credit_card_security_code(card_type=None),
        }
        return fake_data

    st.markdown(
        "<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Australia Fake Data "
        "Generator</h1></center>",
        unsafe_allow_html=True)

    state = st.selectbox('Select a state:', australian_states)

    if st.button('Generate'):
        fake_data = generate_fake_data_australia(state)

        for key, value in fake_data.items():
            st.write(f"{key}: {value}")


def nz():
    fake = Faker('en_NZ')

    new_zealand_regions = [
        'Northland', 'Auckland', 'Waikato', 'Bay of Plenty', 'Gisborne', 'Hawke\'s Bay',
        'Taranaki', 'Manawatu-Wanganui', 'Wellington', 'Tasman', 'Nelson', 'Marlborough',
        'West Coast', 'Canterbury', 'Otago', 'Southland'
    ]

    def generate_fake_data_new_zealand(region):
        fake_data = {
            'Full Name': fake.name(),
            'Gender': random.choice(['Male', 'Female']),
            'Birthday': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            'NHI': fake.random_int(min=1000000000, max=9999999999),
            'Street': fake.street_address(),
            'City/Town': fake.city(),
            'Region': region,
            'Postal Code': fake.postcode(),
            'Phone Number': fake.phone_number(),
            'Country': 'New Zealand',
            'Latitude': fake.latitude(),
            'Longitude': fake.longitude(),
            'Credit card brand': fake.credit_card_provider(),
            'Credit card number': fake.credit_card_number(card_type=None),
            'Expire': fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"),
            'CVV': fake.credit_card_security_code(card_type=None),
        }
        return fake_data

    st.markdown(
        "<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>New Zealand Fake Data "
        "Generator</h1></center>",
        unsafe_allow_html=True)

    region = st.selectbox('Select a region:', new_zealand_regions)

    if st.button('Generate'):
        fake_data = generate_fake_data_new_zealand(region)

        for key, value in fake_data.items():
            st.write(f"{key}: {value}")


def switch():
    fake = Faker('de_CH')

    swiss_cantons = [
        'Zürich', 'Bern', 'Lucerne', 'Uri', 'Schwyz', 'Obwalden', 'Nidwalden',
        'Glarus', 'Zug', 'Fribourg', 'Solothurn', 'Basel-Stadt', 'Basel-Landschaft',
        'Schaffhausen', 'Appenzell Ausserrhoden', 'Appenzell Innerrhoden', 'St. Gallen',
        'Graubünden', 'Aargau', 'Thurgau', 'Ticino', 'Vaud', 'Valais', 'Neuchâtel',
        'Geneva', 'Jura'
    ]

    def generate_fake_data_switzerland(canton):
        fake_data = {
            'Full Name': fake.name(),
            'Gender': random.choice(['Male', 'Female']),
            'Birthday': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            'Social Security Number': fake.random_int(min=1000000000000, max=9999999999999),
            'Street': fake.street_address(),
            'City/Town': fake.city(),
            'Canton': canton,
            'Postal Code': fake.postcode(),
            'Phone Number': fake.phone_number(),
            'Country': 'Switzerland',
            'Latitude': fake.latitude(),
            'Longitude': fake.longitude(),
            'Credit card brand': fake.credit_card_provider(),
            'Credit card number': fake.credit_card_number(card_type=None),
            'Expire': fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"),
            'CVV': fake.credit_card_security_code(card_type=None),
        }
        return fake_data

    st.markdown(
        "<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Switzerland Fake Data "
        "Generator</h1></center>",
        unsafe_allow_html=True)

    canton = st.selectbox('Select a canton:', swiss_cantons)

    if st.button('Generate'):
        fake_data = generate_fake_data_switzerland(canton)

        for key, value in fake_data.items():
            st.write(f"{key}: {value}")


def bd():
    fake = Faker('bn_BD')

    bd_divisions = {
        'Dhaka': ['Dhaka', 'Gazipur', 'Narayanganj', 'Narsingdi', 'Manikganj', 'Munshiganj'],
        'Chittagong': ['Chittagong', 'Cox\'s Bazar', 'Khagrachhari', 'Rangamati'],
        'Rajshahi': ['Rajshahi', 'Bogra', 'Pabna', 'Naogaon'],
        'Khulna': ['Khulna', 'Jessore', 'Satkhira', 'Bagerhat'],
        'Barisal': ['Barisal', 'Bhola', 'Pirojpur'],
        'Sylhet': ['Sylhet', 'Moulvibazar', 'Habiganj'],
        'Rangpur': ['Rangpur', 'Dinajpur', 'Thakurgaon'],
        'Mymensingh': ['Mymensingh', 'Jamalpur', 'Netrokona']
    }

    def generate_fake_data(city):
        fake_data = {
            'Full Name': fake.name(),
            'Gender': fake.random_element(elements=('Male', 'Female')),
            'Birthday': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            'National ID': fake.random_int(min=1000000000000, max=9999999999999),
            'Street': fake.street_address(),
            'City/Town': city,
            'Division': get_division_from_city(city),
            'Postal Code': fake.postcode(),
            'Phone Number': fake.phone_number(),
            'Country': 'Bangladesh',
            'Latitude': fake.latitude(),
            'Longitude': fake.longitude(),
            'Credit card brand': fake.credit_card_provider(),
            'Credit card number': fake.credit_card_number(card_type=None),
            'Expire': fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"),
            'CVV': fake.credit_card_security_code(card_type=None),
        }
        return fake_data

    def get_division_from_city(city):
        for division, cities in bd_divisions.items():
            if city in cities:
                return division

    st.markdown(
        "<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Bangladesh Fake Data "
        "Generator</h1></center>",
        unsafe_allow_html=True)

    division = st.selectbox('Select a division:', list(bd_divisions.keys()))

    city = st.selectbox('Select a city:', bd_divisions[division])

    if st.button('Generate'):
        fake_data = generate_fake_data(city)

        for key, value in fake_data.items():
            st.write(f"{key}: {value}")

def ind():
    fake = Faker('en_IN')

    indian_states = [
        'Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',
        'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Goa',
        'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka',
        'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
        'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
        'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
    ]

    def generate_fake_data_india(state):
        fake_data = {
            'Full Name': fake.name(),
            'Gender': random.choice(['Male', 'Female']),
            'Birthday': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            'Aadhaar Number': fake.random_int(min=100000000000, max=999999999999),
            'Pincode': fake.postcode(),
            'Street': fake.street_address(),
            'City/Town': fake.city(),
            'State/Province/Region': state,
            'Zip/Postal Code': fake.postcode(),
            'Phone Number': fake.phone_number(),
            'Country': 'India',
            'Latitude': fake.latitude(),
            'Longitude': fake.longitude(),
            'Credit card brand': fake.credit_card_provider(),
            'Credit card number': fake.credit_card_number(card_type=None),
            'Expire': fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"),
            'CVV': fake.credit_card_security_code(card_type=None),
        }
        return fake_data

    st.markdown(
        "<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>India Fake Data "
        "Generator</h1></center>",
        unsafe_allow_html=True)

    state = st.selectbox('Select a state:', indian_states)

    if st.button('Generate'):
        # Generate fake data
        fake_data = generate_fake_data_india(state)

        for key, value in fake_data.items():
            st.write(f"{key}: {value}")


def russia():
    fake = Faker('ru_RU')
    russian_regions = [
        'Алтайский край', 'Амурская область', 'Архангельская область', 'Астраханская область', 'Белгородская область',
        'Брянская область', 'Владимирская область', 'Волгоградская область', 'Вологодская область',
        'Воронежская область',
        'г. Москва', 'г. Санкт-Петербург', 'Еврейская автономная область', 'Забайкальский край', 'Ивановская область',
        'Иные территории, включая город и космодром Байконур', 'Иркутская область', 'Кабардино-Балкарская Республика',
        'Калининградская область', 'Калужская область', 'Камчатский край', 'Карачаево-Черкесская Республика',
        'Кемеровская область', 'Кировская область', 'Костромская область', 'Краснодарский край', 'Красноярский край',
        'Курганская область', 'Курская область', 'Ленинградская область', 'Липецкая область', 'Магаданская область',
        'Московская область', 'Мурманская область', 'Ненецкий автономный округ', 'Нижегородская область',
        'Новгородская область', 'Новосибирская область', 'Омская область', 'Оренбургская область',
        'Орловская область', 'Пензенская область', 'Пермский край', 'Приморский край', 'Псковская область',
        'Республика Адыгея (Адыгея)', 'Республика Алтай', 'Республика Башкортостан', 'Республика Бурятия',
        'Республика Дагестан', 'Республика Ингушетия', 'Республика Калмыкия', 'Республика Карелия', 'Республика Коми',
        'Республика Крым', 'Республика Марий Эл', 'Республика Мордовия', 'Республика Саха (Якутия)',
        'Республика Северная Осетия - Алания', 'Республика Татарстан (Татарстан)', 'Республика Тыва',
        'Республика Хакасия', 'Ростовская область', 'Рязанская область', 'Самарская область', 'Саратовская область',
        'Сахалинская область', 'Свердловская область', 'Севастополь', 'Смоленская область', 'Ставропольский край',
        'Тамбовская область', 'Тверская область', 'Томская область', 'Тульская область', 'Тюменская область',
        'Удмуртская Республика', 'Ульяновская область', 'Хабаровский край', 'Ханты-Мансийский автономный округ - Югра',
        'Челябинская область', 'Чеченская Республика', 'Чувашская Республика - Чувашия', 'Чукотский автономный округ',
        'Ямало-Ненецкий автономный округ', 'Ярославская область'
    ]

    def generate_fake_data_russia():
        fake_data = {
            'Full Name': fake.name(),
            'Gender': random.choice(['Мужчина', 'Женщина']),
            'Birthday': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            'Passport Number': fake.random_int(min=1000000000, max=9999999999),
            'Street Address': fake.street_address(),
            'City': fake.city_name(),
            'Postal Code': fake.postcode(),
            'Phone Number': fake.phone_number(),
            'Country': 'Russia',
            'Latitude': fake.latitude(),
            'Longitude': fake.longitude(),
            'Credit Card Brand': fake.credit_card_provider(),
            'Credit Card Number': fake.credit_card_number(card_type=None),
            'Expire': fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"),
            'CVV': fake.credit_card_security_code(card_type=None),
        }
        return fake_data


    st.markdown(
        "<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Russia Fake Data Generator</h1></center>",
        unsafe_allow_html=True)
    state = st.selectbox('Select a Regions:', russian_regions)
    if st.button('Generate'):
        fake_data = generate_fake_data_russia()

        # Display generated fake data
        for key, value in fake_data.items():
            st.write(f"{key}: {value}")


def main():
    st.sidebar.markdown("<h1 style='font-family: Comic Sans MS; font-weight: 600; font-size: 32px;'>Fake "
                        "Details</h1></center>", unsafe_allow_html=True)
    selected_sidebar = st.sidebar.radio("Please Select One",
                                        ["United States", "United Kingdom", "Canada", "Germany", "Spain", "Japan",
                                         "Australia", "New Zealand", "Switzerland", "Bangladesh", "India", "Russia"])

    if selected_sidebar == "United States":
        usa()
    elif selected_sidebar == "United Kingdom":
        uk()
    elif selected_sidebar == "Canada":
        ca()
    elif selected_sidebar == "Germany":
        de()
    elif selected_sidebar == "Spain":
        spain()
    elif selected_sidebar == "Japan":
        jap()
    elif selected_sidebar == "Australia":
        aus()
    elif selected_sidebar == "New Zealand":
        nz()
    elif selected_sidebar == "Switzerland":
        switch()
    elif selected_sidebar == "Bangladesh":
        bd()
    elif selected_sidebar == "India":
        ind()
    elif selected_sidebar == "Russia":
        russia()


if __name__ == "__main__":
    main()
