from typing import List, Dict, Any
import asyncio
import pprint
import sys # Trigger re-check 2
from backend.database.mongodb import mongodb
from backend.core.config import settings

async def view_users():
    print("Connecting to database...")
    await mongodb.connect_to_database()
    
    print(f"Fetching patients from database: {settings.DATABASE_NAME}")
    # mongodb.db is now set
    if mongodb.db is None:
        print("Error: Database connection failed.")
        return

    patients_cursor = mongodb.db.patients.find({})
    patients: List[Dict[str, Any]] = await patients_cursor.to_list(length=100)
    
    if not patients:
        print("No patients found in the database.")
    else:
        print(f"Found {len(patients)} patient(s):")
        print("-" * 30)
        # Patients is already a list from to_list()
        for patient in patients:
            # Convert ObjectId to string for printing
            patient['_id'] = str(patient['_id'])
            pprint.pprint(patient)
            print("-" * 30)
    
    await mongodb.close_database_connection()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(view_users())

# IDE Refresher