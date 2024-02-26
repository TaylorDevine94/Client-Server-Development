from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, client, database, collection):
        
       
        self.client = MongoClient('mongodb://%s:%s@nv-desktop-services.apporto.com:30275' % ("aacuser", "SNHU1234"))
        self.database = self.client['AAC']
        self.collection = self.database['animals']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary
            if insert !=0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            

# Create method to implement the R in CRUD.
    def read(self, searchData):
        if searchData:
            data = self.database.animals.find(searchData, {"_id": False})
            
        else:
            data = self.database.animals.find( {}, {"_id": False})
        return data

# Create method to implement the U in CRUD
    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData, {"$set": updateData })
        else:
            return "{}"
        return result.raw_result
    
# Create method to implement the D in CRUD
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return "{}"
        return result.raw_result

    
    def read(self, query):
   
        cursor = self.collection.find(query)
        result = [document for document in cursor]
        return result