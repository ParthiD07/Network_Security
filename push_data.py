import os
import sys
import json
import certifi
import pandas as pd
import pymongo
from dotenv import load_dotenv

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logger

# Load environment variables
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
ca=certifi.where()

class NetworkDataExtrack:
    def __init__(self):
        """Initializer (currently not used, but reserved for future configs)"""
        pass

    def csv_to_json(self,file_path:str):
        """Convert CSV file into list of JSON-like dict records"""
        try:
            logger.info(f"Reading CSV file: {file_path}")
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=data.to_dict(orient=records)
            logger.info(f"Successfully converted {len(records)} rows to JSON records")
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_data_to_mongodb(self,records,database:str,collection:str):
        """Insert list of records into MongoDB collection"""
        try:
            logger.info(f"Connecting to MongoDB: {database}.{collection}")
            with pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca) as client:
                db=client[database]
                collection_obj=db[collection]
                result = collection_obj.insert_many(records)
                logger.info(f"Inserted {len(result.inserted_ids)} records into {database}.{collection}")
                return len(result.inserted_ids)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=="__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="Network_DB"
    COLLECTION="NetworkData"

    network_obj=NetworkDataExtrack()
    records=network_obj.csv_to_json(FILE_PATH)
    print(records[:5])
    no_of_records=network_obj.insert_data_to_mongodb(records,DATABASE,COLLECTION)
    print(f"Total inserted records: {no_of_records}")

        
