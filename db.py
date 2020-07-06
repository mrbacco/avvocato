############## db SETUP START ##############
# using mongo db cloud version
# checking the connection to cloud ongodb and printing in the console the list of collections under the database

try:
    myclient = pymongo.MongoClient("mongodb://###################################################")
    mydb = myclient["lawyers"]
    mycol = mydb["feedback"]
    print("if connected to db, then these are the collections in mydb: ", mydb.list_collection_names()) #used to check if db is connected
except:
    logging.warning("Could not connect to MongoDB")

############## db SETUP END ##############
