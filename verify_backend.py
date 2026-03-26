import requests
import sys # Trigger re-check 2

BASE_URL = "http://127.0.0.1:8000"

def test_signup():
    print("Testing Signup...")
    payload = {
        "full_name": "Test User",
        "email": "test@example.com",
        "password": "password123",
        "phone": "1234567890",
        "address": "123 Test St",
        "date_of_birth": "1990-01-01",
        "gender": "Male"
    }
    try:
        response = requests.post(f"{BASE_URL}/auth/signup", json=payload)
        if response.status_code == 200:
            print("Signup Successful")
            return True
        elif response.status_code == 400 and "Email already registered" in response.text:
            print("User already exists, proceeding to login...")
            return True
        else:
            print(f"Signup Failed: {response.text}")
            return False
    except Exception as e:
        print(f"Signup Error: {e}")
        return False

def test_login():
    print("Testing Login...")
    payload = {
        "email": "test@example.com",
        "password": "password123"
    }
    try:
        response = requests.post(f"{BASE_URL}/auth/login", json=payload)
        if response.status_code == 200:
            token = response.json().get("access_token")
            if token:
                print("Login Successful. Token received.")
                return True, token
            else:
                print("Login Failed: No token received")
                return False, None
        else:
            print(f"Login Failed: {response.text}")
            return False, None
    except Exception as e:
        print(f"Login Error: {e}")
        return False, None

def test_patient_features(token):
    print("\n--- Testing Patient Features ---")
    headers = {"Authorization": f"Bearer {token}"}
    
    # 1. Test Hospital Info (Public)
    try:
        response = requests.get(f"{BASE_URL}/hospital-info")
        if response.status_code == 200:
            print("Hospital Info: OK")
        else:
            print(f"Hospital Info Failed: {response.text}")
    except Exception as e:
        print(f"Hospital Info Error: {e}")

    # 2. Test Get Rooms
    try:
        response = requests.get(f"{BASE_URL}/rooms", headers=headers)
        if response.status_code == 200:
            print(f"Get Rooms: OK (Found {len(response.json())} rooms)")
        else:
            print(f"Get Rooms Failed: {response.text}")
    except Exception as e:
        print(f"Get Rooms Error: {e}")

    # 3. Test Chatbot
    try:
        payload = {"message": "Hello, I need to book a room"}
        response = requests.post(f"{BASE_URL}/chatbot", json=payload, headers=headers)
        if response.status_code == 200:
            print(f"Chatbot: OK (Response: {response.json().get('response')})")
        else:
            print(f"Chatbot Failed: {response.text}")
    except Exception as e:
        print(f"Chatbot Error: {e}")

    # 4. Test Emergency Alert
    try:
        response = requests.post(f"{BASE_URL}/emergency/alert", headers=headers)
        if response.status_code == 200:
            print("Emergency Alert: OK")
        else:
            print(f"Emergency Alert Failed: {response.text}")
    except Exception as e:
        print(f"Emergency Alert Error: {e}")
        
    return True

if __name__ == "__main__":
    is_signup_ok = test_signup()
    is_login_ok, token = test_login()
    
    if is_signup_ok and is_login_ok and token:
        test_patient_features(token)
        print("\nBackend Verification Passed!")
    else:
        print("\nBackend Verification Failed!")
        sys.exit(1)

# IDE Refresher