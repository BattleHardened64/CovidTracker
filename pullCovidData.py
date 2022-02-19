import os
import csv
import requests
from datetime import timedelta, date
from contextlib import closing
import json



def pullCovidData_old():
        #Source: https://github.com/CSSEGISandData/COVID-19

        #go through each date sequentially from start to end date
        def daterange(start_date, end_date):
            for n in range(int ((end_date - start_date).days)):
                yield start_date + timedelta(n)


        #Code for testing date ranges:
        #print("Enter the date you wish to start at in the following format: YYYY MM DD")
        #date = input()
        #start_date_y = int(date[0:4])
        #start_date_m = int(date[5:8])
        #start_date_d = int(date[8:10])

        #date = (start_date_y, start_date_m, start_date_d)
        

        #YYYY MM DD
        #hard code start date that data began being recorded. date(2020, 1, 22)
        start_date = date(2022, 2, 13) #date(2022, 2, 2) #temporary date for testing
        end_date = date.today()

        #loop through every date until we get to todays date
        for single_date in daterange(start_date, end_date):
            datestr=single_date.strftime("%m-%d-%Y")
            #This is the url to pull data from the github
            url = r'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+datestr+'.csv' 
    
            #Here is where you would store the data to sql
            print(url)
    
            #downloads data as csv
            with open(os.path.split(url)[1], 'wb') as f, \
                    requests.get(url, stream=True) as r:
                for line in r.iter_lines():
                    f.write(line+'\n'.encode())
            """ 
            #use this code if you want csv in variable
            with requests.get(url, stream=True) as r:
                lines = (line.decode('utf-8') for line in r.iter_lines())
                for row in csv.reader(lines):
                    print(row)
            """
   


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
    
    fileName = "covid-data.json"

    url_date = input("Enter the date in the following format: YYYY-MM-DD\n")

    url = ("https://api.covid19tracking.narrativa.com/api/"+url_date)
    myfile = requests.get(url)
    
    text = myfile.text

    data = json.loads(text)

    #key = data['dates']
    #key2 = key[url_date]
    #key3 = key2['countries']
    #key4 = key3['Poland']
    #print(key4['today_new_open_cases'])

    date = url_date
    key = data['total']
    today_confirmed = key['today_confirmed']
    today_deaths = key['today_deaths']
    today_new_confirmed = key['today_new_confirmed']
    today_new_deaths = key['today_new_deaths']
    today_new_open_cases = key['today_new_open_cases']
    today_new_recovered = key['today_new_recovered']
    today_open_cases = key['today_open_cases']
    today_recovered = key['today_recovered']
    yesterday_confirmed = key['yesterday_confirmed']
    yesterday_deaths = key['yesterday_deaths']
    yesterday_open_cases = key['yesterday_open_cases']
    yesterday_recovered = key['yesterday_recovered']

    diff_open = ( today_open_cases - yesterday_open_cases)


    today_confirmed = str(today_confirmed)
    today_deaths =str(today_deaths)
    today_new_confirmed = str(today_new_confirmed)
    today_new_deaths = str(today_new_deaths)
    today_new_open_cases =str(today_new_open_cases)
    today_new_recovered = str(today_new_recovered)
    today_open_cases = str(today_open_cases)
    today_recovered = str(today_recovered)
    yesterday_confirmed = str(yesterday_confirmed)
    yesterday_deaths =str(yesterday_deaths)
    yesterday_open_cases =str(yesterday_open_cases)
    yesterday_recovered =str(yesterday_recovered)

   

    print("Today's World Total Information:\n")
    print("Date: " + url_date +'\n')
    print("Total Confirmed Cases:"+ today_confirmed +'\n')
    print("Today's New Confirmmed Cases: "+today_new_confirmed+'\n')
    print("Total Deaths: "+today_deaths+'\n')
    print("Today's Death Count: "+today_new_deaths+'\n')
    print("Total Current Cases: "+today_open_cases+'\n')
    print("Today's Current Cases: "+today_new_open_cases+'\n')
    print("Total Recovered Cases: "+today_recovered+'\n')
    print("Today's Recovered Cases: "+today_new_recovered+'\n')
    print("\Yesterady's Data\n\n")

    print("Yesterday's Confirmed Cases: "+yesterday_confirmed+'\n')
    print("Yesterday's Deaths: "+yesterday_deaths+'\n')
    print("Yesterday's Open Cases: "+yesterday_open_cases+'\n')
    print("Yesterday's Recovered Cases: "+yesterday_recovered+'\n')
    
    print("\nAnalysis:\n\n")
    
    if(diff_open < 0):
        diff_open = diff_open * -1
        diff_open = str(diff_open)
        print("There has been a net gain of " + diff_open + " cases\n")


    else:
        diff_open = str(diff_open)
        print("There has been a net decrease of " + diff_open + " cases\n")



    key = data['dates']
    key2 = key[url_date]
    key3 = key2['countries']
    counter = 1
    while(counter < 196):
        country = countries_func(counter)
        key4 = key3[countries_func(counter)]
        key5 = key4["today_confirmed"]
        key5 = str(key5)
        print("Confirmed cases for " + country + ": " + key5)
        counter += 1

    '''file = open(fileName, "w")
    json.dump(data,file)
    file.close()'''
   
    
    



pullCovidData()



