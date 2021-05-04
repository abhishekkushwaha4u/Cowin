# **Gettin Started**

Hi!
So I created this project because I was tired of logging in via Cowin using an OTP to check for availability of vaccines in my area.

Please feel free to clone this code and use for your own friends and family

Stay safe!!

## **Requirements**
* One python developer who works in Python 3.x. If you can't find one, feel free to contact me.
* A working internet connection

## **How it works?**

So the program gets the vaccines available in an entire district using a district key- which depends on the state. 


You can get the your district key by running **getDistrictIDs.py**, and **replace** the value of StateID with your state ID from the table given below.

| State name                  | State id |
| --------------------------- | -------- |
| Andaman and Nicobar Islands | 1        |
| Andhra Pradesh              | 2        |
| Arunachal Pradesh           | 3        |
| Assam                       | 4        |
| Bihar                       | 5        |
| Chandigarh                  | 6        |
| Chhattisgarh                | 7        |
| Dadra and Nagar Haveli      | 8        |
| Daman and Diu               | 37       |
| Delhi                       | 9        |
| Goa                         | 10       |
| Gujarat                     | 11       |
| Haryana                     | 12       |
| Himachal Pradesh            | 13       |
| Jammu and Kashmir           | 14       |
| Jharkhand                   | 15       |
| Karnataka                   | 16       |
| Kerala                      | 17       |
| Ladakh                      | 18       |
| Lakshadweep                 | 19       |
| Madhya Pradesh              | 20       |
| Maharashtra                 | 21       |
| Manipur                     | 22       |
| Meghalaya                   | 23       |
| Mizoram                     | 24       |
| Nagaland                    | 25       |
| Odisha                      | 26       |
| Puducherry                  | 27       |
| Punjab                      | 28       |
| Rajasthan                   | 29       |
| Sikkim                      | 30       |
| Tamil Nadu                  | 31       |
| Telangana                   | 32       |
| Tripura                     | 33       |
| Uttar Pradesh               | 34       |
| Uttarakhand                 | 35       |
| West Bengal                 | 36       |


For example, if my district lies in Delhi, I will run getDistrictIDs.py with the StateID value as 9
Upon running, you will recieve a table of the format below

```
$ python getDistrictIDs.py


Central Delhi                    141
East Delhi                       145
New Delhi                        140
North Delhi                      146
North East Delhi                 147
North West Delhi                 143
Shahdara                         148
South Delhi                      149
South East Delhi                 144
South West Delhi                 150
West Delhi                       142
```

Now take the ID to your respective district, and edit line 13 in Main.py to get vaccines for your district.
Run Main.py to get vaccine details in your district till the next five weeks.

## Default values
* number of weeks to search forward- 5
* district ID- 144 (South East Delhi)
* selected age- 21
* paid necessary- 0

Now you might say that your filter isn't the one above, you can change the values given below to filter centers as per your need


### **Some variables you can edit to get different results in Main.py**

| Variable name | Description |
| ------------- | ----------- |
|num_weeks| Looks through certain number of weeks forward, minimum value is 1. Default is 5.|
|district_id| Enter the district_id of the district you want to get vaccination details of. Default is Gurgaon (188) |
|age| Enter age of person to be vaccinated. Works only when select_age_flag is 1|
|select_age_flag|Flag to displays center list based on all ages or specific age group, select 0 for all vaccine slots, 1 for selected age vaccine slots. Default is 1|
|paid_necessary| Enter one if only want to see paid centers, else enter 0, default is 0|

