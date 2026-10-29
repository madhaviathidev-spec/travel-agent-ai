import streamlit as st


class TravelAgent:

    def search_train(self, destination):

        trains = {
            "mysore": "Mysore Express - Fare ₹500",
            "chennai": "Chennai Mail - Fare ₹600",
            "bangalore": "Shatabdi Express - Fare ₹400"
        }

        return trains.get(
            destination.lower(),
            "Train information unavailable"
        )

    def search_hotel(self, destination):

        hotels = {
            "mysore": "Royal Residency - ₹2000/night",
            "chennai": "Grand Chennai Hotel - ₹2500/night",
            "bangalore": "Tech Park Residency - ₹3000/night"
        }

        return hotels.get(
            destination.lower(),
            "Hotel information unavailable"
        )

    def calculate_budget(self, destination):

        budgets = {
            "mysore": 5500,
            "chennai": 6500,
            "bangalore": 7000
        }

        return budgets.get(
            destination.lower(),
            5000
        )

    def create_itinerary(self, destination):

        places = {
            "mysore": [
                "Mysore Palace",
                "Chamundi Hills",
                "Brindavan Gardens"
            ],

            "chennai": [
                "Marina Beach",
                "Kapaleeshwarar Temple",
                "Mahabalipuram"
            ],

            "bangalore": [
                "Lalbagh",
                "Cubbon Park",
                "Bangalore Palace"
            ]
        }

        return places.get(
            destination.lower(),
            ["Local Sightseeing"]
        )


agent = TravelAgent()

st.set_page_config(
    page_title="AI Travel Agent",
    page_icon="✈️"
)

st.title("✈️ AI Travel Agent")

st.write(
    "Plan your travel with AI Agent"
)

destination = st.text_input(
    "Enter Destination"
)

if st.button("Plan Trip"):

    train = agent.search_train(destination)

    hotel = agent.search_hotel(destination)

    budget = agent.calculate_budget(destination)

    places = agent.create_itinerary(destination)

    st.success("Trip Plan Generated")

    st.subheader("🚆 Train")

    st.write(train)

    st.subheader("🏨 Hotel")

    st.write(hotel)

    st.subheader("💰 Estimated Budget")

    st.write(f"₹{budget}")

    st.subheader("📍 Places To Visit")

    for place in places:
        st.write("✅", place)
