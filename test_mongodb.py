import asyncio
from motor.motor_asyncio import AsyncIOMotorClient # Pyre trigger 2
import pprint

async def test_connection():
    try:
        client = AsyncIOMotorClient("mongodb://127.0.0.1:27017")
        database = client.hospital_management_system
        patients_collection = database.patients
        
        # Test insertion
        test_doc = {"test": "connection", "timestamp": "now"}
        result = await patients_collection.insert_one(test_doc)
        print(f"Successfully inserted test document with id: {result.inserted_id}")
        
        # Test retrieval
        found = await patients_collection.find_one({"_id": result.inserted_id})
        print(f"Successfully retrieved test document: {found}")
        
        # Clean up
        await patients_collection.delete_one({"_id": result.inserted_id})
        print("Cleaned up test document")
        
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(test_connection())

# IDE Refresher