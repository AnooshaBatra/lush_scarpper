from categories_scrapper import get_category_data,write_to_csv, get_soup
import os

#getting all hair data
hair_soup= get_soup("https://www.lushusa.com/hair/")
data_frame = get_category_data(hair_soup)

#here we are giving absolute path so that cron job save the file in directory where script is and does not get permission denied error.
write_to_csv(os.path.dirname(os.path.abspath(__file__))+"\\all_hair1.csv", data_frame=data_frame)



#getting conditioner data
conditioner_soup= get_soup("https://www.lushusa.com/hair/conditioners/")
df = get_category_data(conditioner_soup)

#path=os.path.dirname(os.path.abspath(__file__))+"conditioner.csv"
write_to_csv(os.path.dirname(os.path.abspath(__file__))+"\\conditioner1.csv", data_frame=df)