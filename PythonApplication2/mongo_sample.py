from pymongo import MongoClient
import calendar

client = MongoClient()
db = client['test-database']
captcha_mapping1 = {"1":"2"}
captcha_mapping2 = {"23":"23"}
captcha_mappings = db.captcha_mappings
captcha_mapping_id = captcha_mappings.insert_one(captcha_mapping2).inserted_id
#c = captcha_mappings.find_one()
for dic in captcha_mappings.find():
    print(dic)