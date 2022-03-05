from operator import index
from urllib import response
from bs4 import BeautifulSoup
import requests
import pandas as pd


#this function return the html data of the url that goes into argument and return that response into presantable form  
def get_soup(url, req_session):

    #sending the request to specified url
    response= req_session.get(url=url)
    #converting the response into presantable form 
    soup= BeautifulSoup(response.text, "html.parser")
    return soup

#extracting the required data and storing into panadaframe
def get_category_data(soup):
    #data frame which will hold data
    data_frame = pd.DataFrame()
    i=0
    #getting all product names
    product_name_list= soup.select("a.link")
    #the required data is stored in common div, so first we are extracting that common div and looping  through it
    for info in soup.select("div.d-flex  div.tile-price-size"):
        #extracting name one by one 
        product_name= product_name_list[i].text.strip()

        #extracting the product price from common div
        product_price= info.select_one("span.tile-price").text.strip()
       #extracting the product size from common div
        product_size= info.select_one("span.tile-size").text.replace('/ ', "")
        #a dict to hold data to be isnerted to data frame
        data_dict = {
        "name":product_name,
        "price":product_price,
        "size":product_size
    }

        i+=1
        
        #dict data will be appended into frame
        data_frame = data_frame.append(data_dict, ignore_index=True)
    return data_frame
      



#writing the datframe to csv file by taking data to write and path for file 
def write_to_csv( data_frame): 
    data_frame.to_csv("hair_paginations1.csv",mode='a', header=False, index= False)   