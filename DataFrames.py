
import pandas as pd
restaurant_info = pd.read_csv("FoodRatings.csv")

print(restaurant_info)
restaurant_info.at[0,"Rating"]=12

print(restaurant_info.query("Rating >= 10"))