#!/usr/bin/env python
# coding: utf-8

import requests
api_address ='insert weather api in this place . its is unique id fpr every user '
city=input("enter the name of the city:")
url=api_address+city
json_data=requests.get(url).json()
print(json_data)

