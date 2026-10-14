import requests

# Put your real API key here
API_KEY = "YOUR_API_KEY"

# Put your flight API URL here
API_URL = "YOUR_FLIGHT_API_URL"


headers = {
    "x-api-key": API_KEY
}

try:
    response = requests.get(API_URL, headers=headers)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()

        print("API Response:")
        print(data)

        if not data:
            print("\nNo flight data returned.")
    else:
        print("API Error:")
        print(response.text)

except Exception as e:
    print("Error:", e)