from trip_agent import interpret_trip_request
from browser_agent import search_hotels

def main():
    print("🌍 Trip Planning Assistant")
    user_prompt = input("🗨️  Where do you want to go? ➜ ")

    trip_info = interpret_trip_request(user_prompt)
    if not trip_info:
        print("❌ Failed to understand the trip request.")
        return

    print("\n🧳 Trip Details:")
    print(f"Destination: {trip_info['destination']}")
    print(f"Duration: {trip_info['duration_days']} days")
    print(f"Budget: LKR {trip_info['budget_lkr']:,}")

    print("\n🔍 Searching for hotels...")
    hotels = search_hotels(trip_info['destination'], trip_info['duration_days'], trip_info['budget_lkr'])

    if not hotels:
        print("⚠️ No hotels found.")
        return

    print("\n🏨 Suggested Hotels:")
    for i, hotel in enumerate(hotels, 1):
        print(f"{i}. {hotel['name']}\n   ↪ {hotel['url']}")

if __name__ == "__main__":
    main()
