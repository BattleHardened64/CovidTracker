import os
import csv
import requests
import datetime
import sqlite3



def countries_func(counter):
     country_list = {
        1:"Afghanistan",
        2:"Albania",
        3:"Algeria",
        4:"Andorra",
        5:"Angola",
        6:"Antigua and Barbuda",
        7:"Argentina",
        8:"Armenia",
        9:"Australia",
        10:"Austria",
        11:"Azerbaijan",
        12:"Bahamas",
        13:"Bahrain",
        14:"Bangladesh",
        15:"Barbados",
        16:"Belarus",
        17:"Belgium",
        18:"Belize",
        19:"Benin",
        20:"Bhutan",
        21:"Bolivia",
        22:"Bosnia and Herzegovina",
        23:"Botswana",
        24:"Brazil",
        25:"Brunei",
        26:"Bulgaria",
        27:"Burkina Faso",
        28:"Burma",
        29:"Burundi",
        30:"Cabo Verde",
        31:"Cambodia",
        32:"Cameroon",
        33:"Canada",
        34:"Central African Republic",
        35:"Chad",
        36:"Chile",
        37:"China",
        38:"Colombia",
        39:"Comoros",
        40:"Congo (Brazzaville)",
        41:"Congo (Kinshasa)",
        42:"Costa Rica",
        43:"Cote d'Ivoire",
        44:"Croatia",
        45:"Cuba",
        46:"Cyprus",
        47:"Czechia",
        48:"Denmark",
        49:"Diamond Princess",
        50:"Djibouti",
        51:"Dominica",
        52:"Dominican Republic",
        53:"East Timor",
        54:"Ecuador",
        55:"Egypt",
        56:"El Salvador",
        57:"Equatorial Guinea",
        58:"Eritrea",
        59:"Estonia",
        60:"Eswatini",
        61:"Ethiopia",
        62:"Fiji",
        63:"Finland",
        64:"France",
        65:"Gabon",
        66:"Gambia",
        67:"Georgia",
        68:"Germany",
        69:"Ghana",
        70:"Greece",
        71:"Grenada",
        72:"Guatemala",
        73:"Guernsey",
        74:"Guinea",
        75:"Guinea-Bissau",
        76:"Guyana",
        77:"Haiti",
        78:"Holy See",
        79:"Honduras",
        80:"Hungary",
        81:"Iceland",
        82:"India",
        83:"Indonesia",
        84:"Iran",
        85:"Iraq",
        86:"Ireland",
        87:"Israel",
        88:"Italy",
        89:"Jamaica",
        90:"Japan",
        91:"Jersey",
        92:"Jordan",
        93:"Kazakhstan",
        94:"Kenya",
        95:"Kiribati",
        96:"Korea, South",
        97:"Kosovo",
        98:"Kuwait",
        99:"Kyrgyzstan",
        100:"Laos",
        101:"Latvia",
        102:"Lebanon",
        103:"Lesotho",
        104:"Liberia",
        105:"Libya",
        106:"Liechtenstein",
        107:"Lithuania",
        108:"Luxembourg",
        109:"MS Zaandam",
        110:"Madagascar",
        111:"Malawi",
        112:"Malaysia",
        113:"Maldives",
        114:"Mali",
        115:"Malta",
        116:"Mauritania",
        117:"Mauritius",
        118:"Mexico",
        119:"Micronesia",
        120:"Moldova",
        121:"Monaco",
        122:"Mongolia",
        123:"Montenegro",
        124:"Morocco",
        125:"Mozambique",
        126:"Namibia",
        127:"Nepal",
        128:"Netherlands",
        129:"New Zealand",
        130:"Nicaragua",
        131:"Niger",
        132:"Nigeria",
        133:"North Macedonia",
        134:"Norway",
        135:"Oman",
        136:"Pakistan",
        137:"Panama",
        138:"Papua New Guinea",
        139:"Paraguay",
        140:"Peru",
        141:"Philippines",
        142:"Poland",
        143:"Portugal",
        144:"Qatar",
        145:"Romania",
        146:"Russia",
        147:"Rwanda",
        148:"Saint Kitts and Nevis",
        149:"Saint Lucia",
        150:"Saint Vincent and the Grenadines",
        151:"Samoa",
        152:"San Marino",
        153:"Sao Tome and Principe",
        154:"Saudi Arabia",
        155:"Senegal",
        156:"Serbia",
        157:"Seychelles",
        158:"Sierra Leone",
        159:"Singapore",
        160:"Slovakia",
        161:"Slovenia",
        162:"Somalia",
        163:"South Africa",
        164:"South Sudan",
        165:"Spain",
        166:"Sri Lanka",
        167:"Sudan",
        168:"Suriname",
        169:"Sweden",
        170:"Switzerland",
        171:"Syria",
        172:"Taiwan*",
        173:"Tajikistan",
        174:"Tanzania",
        175:"Thailand",
        176:"Timor-Leste",
        177:"Togo",
        178:"Trinidad and Tobago",
        179:"Tunisia",
        180:"Turkey",
        181:"US",
        182:"Uganda",
        183:"Ukraine",
        184:"United Arab Emirates",
        185:"United Kingdom",
        186:"Uruguay",
        187:"Uzbekistan",
        188:"Vanuatu",
        189:"Venezuela",
        190:"Vietnam",
        191:"West Bank and Gaza",
        192:"Western Sahara",
        193:"Yemen",
        194:"Zambia",
        195:"Zimbabwe",
                }

     return country_list[counter]

def pullCovidData():

    url_date = str(datetime.date.isoformat(datetime.date.today()))
    url_date = "04-10-2022"

    connection = sqlite3.connect("coviddata.db")
    cursor = connection.cursor()



    url = ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"+url_date+".csv")

    with requests.Session() as s:
        download = s.get(url)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            insert = """
            INSERT INTO coviddata (FIPS, County, State_Province, Country_Region, Last_updated, Latitude, Longitude, Confirmed_Cases, Deaths, Recovered, Active_Cases, Location, Incident_rate, Fatality_Rate)
            """

            cursor.execute(insert)
            
        connection.close()
                           
pullCovidData()

