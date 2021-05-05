import requests
import json
import time
from datetime import date, timedelta
import sys


state_with_state_id={
  "Andaman and Nicobar Islands": 1,
  "Andhra Pradesh": 2,
  "Arunachal Pradesh": 3,
  "Assam": 4,
  "Bihar": 5,
  "Chandigarh": 6,
  "Chhattisgarh": 7,
  "Dadra and Nagar Haveli": 8,
  "Delhi": 9,
  "Goa": 10,
  "Gujarat": 11,
  "Haryana": 12,
  "Himachal Pradesh": 13,
  "Jammu and Kashmir": 14,
  "Jharkhand": 15,
  "Karnataka": 16,
  "Kerala": 17,
  "Ladakh": 18,
  "Lakshadweep": 19,
  "Madhya Pradesh": 20,
  "Maharashtra": 21,
  "Manipur": 22,
  "Meghalaya": 23,
  "Mizoram": 24,
  "Nagaland": 25,
  "Odisha": 26,
  "Puducherry": 27,
  "Punjab": 28,
  "Rajasthan": 29,
  "Sikkim": 30,
  "Tamil Nadu": 31,
  "Telangana": 32,
  "Tripura": 33,
  "Uttar Pradesh": 34,
  "Uttarakhand": 35,
  "West Bengal": 36,
  "Daman and Diu": 37
}




def get_state_id(state):
    if state in state_with_state_id:
        return state_with_state_id[state]
    else:
        return None


def get_state_district_ids(StateID):
    url = f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{StateID}"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Host": "cdn-api.co-vin.in",
        "If-None-Match": 'W/"257f1-NjCxF6oyBg9C21YdV2Uxt6W7NPQ"',
        "Origin": 'https://www.cowin.gov.in',
        'Referer': 'https://www.cowin.gov.in/',
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
        "sec-ch-ua-mobile": '?0',
        "Sec-Fetch-Dest": 'empty',
        "Sec-Fetch-Mode": 'cors',
        'Sec-Fetch-Site': 'cross-site',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51",
    }
    response = requests.get(url, headers=headers)
    district_id_mapper = {}
    if response.status_code==200:
        print(response.json())
        for i in response.json()["districts"]:
            district_id_mapper[i['district_name']] = i["district_id"]
            print(f'{i["district_name"]}: {i["district_id"]}')
        return district_id_mapper
    else:
        print("Cloudflare error encountered")
        return None

def getListOfCenters(district_id,today):
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={district_id}&date={today}"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Host": "cdn-api.co-vin.in",
        "If-None-Match": 'W/"257f1-NjCxF6oyBg9C21YdV2Uxt6W7NPQ"',
        "Origin": 'https://www.cowin.gov.in',
        'Referer': 'https://www.cowin.gov.in/',
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
        "sec-ch-ua-mobile": '?0',
        "Sec-Fetch-Dest": 'empty',
        "Sec-Fetch-Mode": 'cors',
        'Sec-Fetch-Site': 'cross-site',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51",
    }
    response = requests.get(url, headers=headers)
    # print(response.text)
    return response


def getAgeBasedCentersPaid(response,age):
    response=response.json()
    listofCenters=[]
    centers=response["centers"]
    dateCenterdict={}
    for center in centers:
        if center["fee_type"]=="Paid":
            for session in center["sessions"]:
                if session["min_age_limit"]==age and session["available_capacity"]!=0:
                    if session["date"] in dateCenterdict:
                        dateCenterdict[session["date"]].append([center["name"],session["vaccine"],session["available_capacity"]])
                    else:
                        dateCenterdict[session["date"]]=[[center["name"],session["vaccine"],session["available_capacity"]]]
    return(dateCenterdict)

def getAllCentersPaid(response,age):
    response=response.json()
    listofCenters=[]
    centers=response["centers"]
    dateCenterdict={}
    for center in centers:
        if center["fee_type"]=="Paid":
            for session in center["sessions"]:
                if session["available_capacity"]!=0:
                    if session["date"] in dateCenterdict:
                        dateCenterdict[session["date"]].append([center["name"],session["vaccine"],session["available_capacity"]])
                    else:
                        dateCenterdict[session["date"]]=[[center["name"],session["vaccine"],session["available_capacity"]]]
    return(dateCenterdict)

def getAllCentersUnpaid(response,age):
    response=response.json()
    listofCenters=[]
    centers=response["centers"]
    dateCenterdict={}
    for center in centers:
        if center["fee_type"]=="Free":
            for session in center["sessions"]:
                if session["available_capacity"]!=0:
                    if session["date"] in dateCenterdict:
                        dateCenterdict[session["date"]].append([center["name"],session["vaccine"],session["available_capacity"]])
                    else:
                        dateCenterdict[session["date"]]=[[center["name"],session["vaccine"],session["available_capacity"]]]
    return(dateCenterdict)

def getAgeBasedCentersUnpaid(response,age):
    response=response.json()
    listofCenters=[]
    centers=response["centers"]
    dateCenterdict={}
    for center in centers:
        if center["fee_type"]=="Free":
            for session in center["sessions"]:
                if session["min_age_limit"]==age and session["available_capacity"]!=0:
                    if session["date"] in dateCenterdict:
                        dateCenterdict[session["date"]].append([center["name"],session["vaccine"],session["available_capacity"]])
                    else:
                        dateCenterdict[session["date"]]=[[center["name"],session["vaccine"],session["available_capacity"]]]
    return(dateCenterdict)

def prettyprint(availableDates):
    for date in availableDates:
        print(f"\t------------------------Date: {date}-----------------------------\n")
        print("\tName \t \t \t Vaccine type \t \t Available vaccines\n")
        for centerDetails in availableDates[date]:
            print(f"\t{centerDetails[0]}\t \t{centerDetails[1]}\t \t{centerDetails[2]}")
        print(f"\t---------------------------------------------------------------------\n")

def getDate(date):
    FormattedDate = date.strftime("%d-%m-%Y")
    return FormattedDate

def getAgeGroup(age):
    if age>=45:
        return 45
    else:
        return 18

def getPaid(select_age_flag,num_weeks,today,district_id,age):
    if select_age_flag == 1:
        print(
            f"\n\n\n----------------------Paid centers for minimum Age {age}------------------------------\n")
        for i in range(num_weeks):  # searching for 3 weeks
            getDateFormatted = getDate(today)
            response = getListOfCenters(
                district_id, getDateFormatted)
            if response.status_code == 200:
                availableDates = getAgeBasedCentersPaid(response, age)
                if availableDates=={}:
                    print(f"\tNone showing from {getDateFormatted} till  {getDate(today+timedelta(weeks=1))}\n")            
                else:
                    prettyprint(availableDates)
            else:
                print(response.text)
                print(f"\tError accessing data from Cowin for dates from date {getDateFormatted} till  {getDate(today+timedelta(weeks=1))}, try again\n")
            today = today+timedelta(weeks=1)

    else:
        print(f"----------------------Paid-> All ages------------------------------------")
        for i in range(num_weeks):  # searching for 3 weeks
            getDateFormatted = getDate(today)
            response = getListOfCenters(
                district_id, getDateFormatted)
            if response.status_code == 200:
                availableDates = getAllCentersPaid(response, age)
                if availableDates=={}:
                    print(f"\tNone showing from {getDateFormatted} till  {getDate(today+timedelta(weeks=1))}\n")            
                else:
                    prettyprint(availableDates)
            else:
                print(f"\tError accessing data from Cowin for date{getDateFormatted}, try again\n")
            today = today+timedelta(weeks=1)



def getUnpaid(select_age_flag,num_weeks,today,district_id,age):
    if select_age_flag == 1:
        print(
            f"\n\n\n----------------------Unpaid centers for minimum Age {age}------------------------------\n")
        for i in range(num_weeks):  # searching for 3 weeks
            getDateFormatted = getDate(today)
            response = getListOfCenters(
                district_id, getDateFormatted)
            if response.status_code == 200:
                availableDates = getAgeBasedCentersUnpaid(response, age)
                if availableDates=={}:
                    print(f"\tNone showing from {getDateFormatted} till  {getDate(today+timedelta(weeks=1))}\n")            
                else:
                    prettyprint(availableDates)
            else:
                print(f"\tError accessing data from Cowin for dates from date {getDateFormatted} till  {getDate(today+timedelta(weeks=1))}, try again\n")
            today = today+timedelta(weeks=1)

    else:
        print(f"----------------------Unpaid-> All ages------------------------------------")
        for i in range(num_weeks):  # searching for 3 weeks
            getDateFormatted = getDate(today)
            response = getListOfCenters(
                district_id, getDateFormatted)
            if response.status_code == 200:
                availableDates = getAllCentersUnpaid(response, age)
                if availableDates=={}:
                    print(f"\tNone showing from {getDateFormatted} till  {getDate(today+timedelta(weeks=1))}\n")            
                else:
                    prettyprint(availableDates)
            else:
                print(f"\tError accessing data from Cowin for date{getDateFormatted}, try again\n")
            today = today+timedelta(weeks=1)



today = date.today()
num_weeks = 5        # number of weeks to search through for
print("List of States available:\n")
for i in state_with_state_id:
    print(f'•) {i}')
print()
print()
print()
x = input("Please enter your state preference: ")
if x not in state_with_state_id:
    print("No state exists by that name...exitting, bye")
    sys.exit(0)
else:
    print(state_with_state_id[x])
    state_id = state_with_state_id[x]
    district_ids = get_state_district_ids(state_id)
    if district_ids == None:
        print("Request blocked by government.....Qutting....byeeee")
        sys.exit(0)
    district_id = int(input("Enter district id: "))


select_age_flag = 1
age = int(input("Enter age: "))    
paid_necessary=0
age=getAgeGroup(age)
getPaid(select_age_flag,num_weeks,today,district_id,age)
if paid_necessary==0:
    getUnpaid(select_age_flag,num_weeks,today,district_id,age)

