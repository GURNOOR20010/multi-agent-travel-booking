import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")


def search_flights(query=None):
    url = "https://api.aviationstack.com/v1/flights"

    params = {
        "access_key": API_KEY,
        "limit": 5
    }

    response = requests.get(url, params=params)

    print("Status Code:", response.status_code)

    data = response.json()

    print("API Response:")
    print(data)

    flights = []

    if "error" in data:
        return str(data["error"])

    if "data" in data:
        for flight in data["data"][:5]:
            airline = flight.get("airline", {}).get("name", "Unknown")
            departure = flight.get("departure", {}).get("airport", "Unknown")
            arrival = flight.get("arrival", {}).get("airport", "Unknown")
            status = flight.get("flight_status", "Unknown")

            flights.append(
                f"""
Airline   : {airline}
Departure : {departure}
Arrival   : {arrival}
Status    : {status}
"""
            )

    return "\n".join(flights) if flights else "No flights found."


if __name__ == "__main__":
    print(search_flights())