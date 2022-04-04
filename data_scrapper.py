import os
import csv
import requests
import json
import datetime


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

    url_date = str(datetime.date.isoformat(datetime.date.today()))


    #Depricated, reads in date as a string.
    #url_date = input("Enter the date in the following format: YYYY-MM-DD\n")

    print("Welcome to the COVID-19 Information Tracker. Your searching options are as follows:\n"
              "1. Global Totals for Today\n"
              "2. Today's Case Totals by Country\n"
              "3. Totals for a specific Country\n"
              "8. Total Cases, Deaths, and Recoveries Worldwide per county in America\n"
              "9. Total Cases, Deaths, and Recoveries Worldwide per province/district/region Worldwide\n")
   

    #Creates a file for database use as well as later in the program.
    ###########################################################################
    url = ("https://api.covid19tracking.narrativa.com/api/"+url_date)
    myfile = requests.get(url)
    
    text = myfile.text

    data = json.loads(text)

    file = open(fileName, "w")
    json.dump(data,file)
    file.close()
    ###########################################################################

    choice = 1

    if(choice == 1):

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
        print("Yesterady's Data\n\n")

        print("Yesterday's Confirmed Cases: "+yesterday_confirmed+'\n')
        print("Yesterday's Deaths: "+yesterday_deaths+'\n')
        print("Yesterday's Open Cases: "+yesterday_open_cases+'\n')
        print("Yesterday's Recovered Cases: "+yesterday_recovered+'\n')
    
        print("\nAnalysis:\n\n")
    
        if(diff_open < 0):
            diff_open = diff_open * -1
            diff_open = str(diff_open)
            print("There has been a net gain of " + diff_open + " cases since yesterday\n")


        else:
            diff_open = str(diff_open)
            print("There has been a net decrease of " + diff_open + " cases since yesterday\n")

    if(choice == 2):
        key = data['dates']
        key2 = key[url_date]
        key3 = key2['countries']
        counter = 1
        while(counter < 196):
            country = countries_func(counter)
            try:
                key4 = key3[countries_func(counter)]
            except:
                counter += 1
            else:
                key5 = key4["today_confirmed"]
                key5 = str(key5)
                print("Confirmed cases for " + country + ": " + key5)
                counter += 1

    if(choice == 3):

        key = data['dates']
        key2 = key[url_date]
        key3 = key2['countries']
        country = input("Enter a country name to research\n")
        try:
            key4 = key3[country]

        except:
            country = input("Please enter a valid country name\n")
            key4 = key3[country]


        today_confirmed = key4['today_confirmed']
        today_deaths = key4['today_deaths']
        today_new_confirmed = key4['today_new_confirmed']
        today_new_deaths = key4['today_new_deaths']
        today_new_open_cases = key4['today_new_open_cases']
        today_new_recovered = key4['today_new_recovered']
        today_open_cases = key4['today_open_cases']
        today_recovered = key4['today_recovered']
        yesterday_confirmed = key4['yesterday_confirmed']
        yesterday_deaths = key4['yesterday_deaths']
        yesterday_open_cases = key4['yesterday_open_cases']
        yesterday_recovered = key4['yesterday_recovered']

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
        print("Yesterady's Data\n\n")

        print("Yesterday's Confirmed Cases: "+yesterday_confirmed+'\n')
        print("Yesterday's Deaths: "+yesterday_deaths+'\n')
        print("Yesterday's Open Cases: "+yesterday_open_cases+'\n')
        print("Yesterday's Recovered Cases: "+yesterday_recovered+'\n')
    
        print("\nAnalysis:\n\n")
    
        if(diff_open < 0):
            diff_open = diff_open * -1
            diff_open = str(diff_open)
            print("There has been a net gain of " + diff_open + " cases since yesterday\n")


        else:
            diff_open = str(diff_open)
            print("There has been a net decrease of " + diff_open + " cases since yesterday\n")

    if(choice == 8):
        key = data['dates']
        key2 = key[url_date]
        key3 = key2['countries']
        key4 = key3["US"]
        key5 = key4["regions"]
        counter = 0
        county_counter = 0
        while (counter < 56):
            key6 = key5[counter]
            state_name = key6['name']
            print("Information for " + state_name +":\n")

            print("Totals: \n")
            print("Today's New Case Count: " + str(key6['today_new_confirmed'])+ "\n")
            print("Today's Death Count: " + str(key6['today_deaths'])+ "\n" )
            #Fix for error in the API (missing entry)
            if(counter != 21 and counter != 42):
                print("Today's Recoveries: " + str(key6['today_new_recovered']) + "\n")

            print("Information by county:\n")
            try:
                key7 = key6['sub_regions']
            except:
                break;
            while(county_counter < 1000):
                try:
                    key8 = key7[county_counter]
                    print("     " + key8['name'] + " County:\n")
                    print("          Today's New Case Count: " + str(key8['today_new_confirmed'])+ "\n")
                    print("          Today's Death Count: " + str(key8['today_deaths'])+ "\n" )
                    print("          Today's Recoveries: " + str(key8['today_new_recovered']) + "\n\n\n")
                    county_counter += 1
                except:
                    break;
            county_counter = 0
            counter+=1
            
    if(choice == 9):
        key = data['dates']
        key2 = key[url_date]
        key3 = key2['countries']
        counter = 0
        county_counter = 0
        global_counter = 1
        while(global_counter < 196):
            country = countries_func(global_counter)
            try:
                key4 = key3[country]
            except:
                global_counter += 1
            else:
                 print(country + ": \n")
                 while (counter < 200):
                    key5 = key4["regions"]

                    try:
                        key6 = key5[counter]
                        state_name = key6['name']
                        print("     Information for " + state_name +":\n")

                        print("     Totals: \n")
                        print("          Today's New Case Count: " + str(key6['today_new_confirmed'])+ "\n")
                        print("          Today's Death Count: " + str(key6['today_deaths'])+ "\n" )
                        #Fix for error in the API (missing entry)
                        if(counter != 21 and counter != 42):
                            print("          Today's Recoveries: " + str(key6['today_new_recovered']) + "\n")

                        try:
                            key7 = key6['sub_regions']
                        except:
                            break;
                        while(county_counter < 1000):
                            try:
                                key8 = key7[county_counter]
                                print("          " + key8['name'] + "\n")
                                print("                   Today's New Case Count: " + str(key8['today_new_confirmed'])+ "\n")
                                print("                   Today's Death Count: " + str(key8['today_deaths'])+ "\n" )
                                print("                   Today's Recoveries: " + str(key8['today_new_recovered']) + "\n\n\n")
                                county_counter += 1
                            except:
                                break;
                    except:
                       break;
                    county_counter = 0
                    counter+=1
            global_counter += 1
            counter = 0
            county_counter = 0
                           
pullCovidData()


