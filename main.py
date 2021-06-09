import urllib.request, urllib.parse, urllib.error
import json
import ssl
import datetime

x = datetime.datetime.now()
x=str(x.strftime("%c"))
x1=x.split()
date=x1[0]+" "+x1[1]+" "+x1[2]+" "+x1[4]
global first
first=1
def answer(loc):
    global first
    ans=[]
    print(loc)
    print(first)
    # if (first==1): loc = "howrah"
    api_key = False
    # If you have a Google Places API key, enter it here
    # api_key = 'AIzaSy___IDByT70'
    # https://developers.google.com/maps/documentation/geocoding/intro

    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else :
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    address = loc
    #if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    #print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    #print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
    
    for i in range(len(js['results'][0]['address_components'])):
        if js['results'][0]['address_components'][i]['types'][0]=="administrative_area_level_1":
            state_name=js['results'][0]['address_components'][i]['long_name']
            break
    
    

    try :

        for i in range(len(js['results'][0]['address_components'])):
            if js['results'][0]['address_components'][i]['types'][0]=="administrative_area_level_2":
                district_name=js['results'][0]['address_components'][i]['long_name'] #getting the district name of the entered place
                break
    except:
        district_name=js['results'][0]['address_components'][0]["long_name"]
    print(district_name)
    if district_name=="Bangalore Urban": district_name="Bengaluru Urban"
    if district_name=="Gulbarga":district_name="Kalaburagi"
    full_name=js['results'][0]['formatted_address']  #getting the proper address of the entered place
            
    #print(district_name)
    print(full_name)

    covidurl="https://api.covid19india.org/state_district_wise.json"

    uh1=urllib.request.urlopen(covidurl, context=ctx)
    data1=uh1.read().decode()
    try:
        js1 = json.loads(data1)
    except:
        js1 = None

    if not js1:
        print('==== Failure To Retrieve ====')
        print(data1)

    #print(json.dumps(js1, indent=4))

    #print(state_name)

    total_cases_district=js1[state_name]["districtData"][district_name]["confirmed"]
    active_cases_district=js1[state_name]["districtData"][district_name]["active"]
    recovered_cases_district=js1[state_name]["districtData"][district_name]["recovered"]
    death_cases_district=js1[state_name]["districtData"][district_name]["deceased"]


    print("Date :"+str(date))
    print("District : " + district_name)
    print("Total cases confirmed : " + str(total_cases_district))
    print("Cases active : " +str(active_cases_district))
    print("Recovered : " +str(recovered_cases_district))
    print("Deaths : " +str(death_cases_district))
    ans.append(full_name)
    ans.append(district_name)
    ans.append(total_cases_district)
    ans.append(active_cases_district)
    ans.append(recovered_cases_district)
    ans.append(death_cases_district)
    first=0
    return ans
    
