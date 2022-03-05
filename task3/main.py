import re
from categories_scrapper import get_category_data,write_to_csv, get_soup
import requests
import pandas as pd

#creating session for getting pagination data
req_session = requests.session()

#in starting the url is this
base_url= "https://www.lushusa.com/hair/"
num=0

#to get pagination data url
updated_url= f"https://www.lushusa.com/on/demandware.store/Sites-Lush-Site/default/Search-UpdateGrid?cgid=all-hair&start={num}&sz=14"

#getting data from baseurl
hair_soup= get_soup(base_url, req_session)


data_frame = pd.DataFrame()

while True:
    #extracting required info from soup
    data_frame= get_category_data(hair_soup)
    write_to_csv(data_frame)
    if hair_soup.select("div.show-more button.btn"):
        num+=14
        updated_url= f"https://www.lushusa.com/on/demandware.store/Sites-Lush-Site/default/Search-UpdateGrid?cgid=all-hair&start={num}&sz=14"
        hair_soup= get_soup(updated_url, req_session)
    else:
        break 





