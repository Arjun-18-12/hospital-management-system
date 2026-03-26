import requests # Pyre trigger 2
import json
import time

BASE_URL = "http://127.0.0.1:8000/auth"

def test_signup():
    print("Testing Signup...")
    payload = {
        "full_name": "Verify Patient",
        "email": "verify@example.com",
        "password": "Password123!",
        "phone": "1234567890",
        "address": "123 Verify St",
        "date_of_birth": "1990-01-01",
        "gender": "Male"
    }
    response = requests.post(f"{BASE_URL}/signup", json=payload)
    print(f"Signup Response Code: {response.status_code}")
    print(f"Signup Response Body: {response.json()}")
    return response.status_code == 200 or response.status_code == 400 # 400 if already exists

def test_login():
    print("\nTesting Login...")
    payload = {
        "email": "verify@example.com",
        "password": "Password123!"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    print(f"Login Response Code: {response.status_code}")
    print(f"Login Response Body: {response.json()}")
    return response.status_code == 200

if __name__ == "__main__":
    # Give server a moment
    time.sleep(1)
    signup_ok = test_signup()
    login_ok = test_login()
    
    if signup_ok and login_ok:
        print("\nBackend API verification SUCCESSFUL!")
    else:
        print("\nBackend API verification FAILED!")

# IDE Refresher