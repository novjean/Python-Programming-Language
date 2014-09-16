import json
import csv
from pprint import pprint


 
# Create a data structure
# data = [ { 'Hola':'Hello', 'Hoi':"Hello", 'noun':"hello" } ]


# print(data)

data = []

with open('yelp_academic_dataset_business.json') as f:
    for line in f:
        data.append(json.loads(line))
        
#print (cat)

f = csv.writer(open("yelp.csv", "wb+"))
  
# Write CSV Header, If you dont need that, remove this line
f.writerow(["business_id", "categories", "city", "full_address", 
            "latitude","longitude","name","neighborhoods","open",
            "review_count","stars","state","type"])
  
for data in data:
    f.writerow([data["business_id"],','.join(data["categories"]),data["city"],data["full_address"],
               data["latitude"],data["longitude"],data["name"],data["neighborhoods"],
               data["open"],data["review_count"],data["stars"], data["state"],data["type"]])
