# ============================================================
# Program 4: African Countries & Capitals Dictionary Lookup
# Stores 10 African countries with their capitals.
# Allows the user to look up the capital of any country.
# ============================================================

# --- Dictionary: country -> capital ---
africa_capitals = {
    "Nigeria":       "Abuja",
    "South Africa":  "Pretoria",
    "Egypt":         "Cairo",
    "Kenya":         "Nairobi",
    "Ghana":         "Accra",
    "Ethiopia":      "Addis Ababa",
    "Tanzania":      "Dodoma",
    "Morocco":       "Rabat",
    "Senegal":       "Dakar",
    "Uganda":        "Kampala",
}

print("=" * 50)
print("   AFRICAN COUNTRIES & CAPITALS LOOKUP")
print("=" * 50)
print("\nAvailable countries:")
for i, country in enumerate(africa_capitals, start=1):
    print(f"  {i:>2}. {country}")
print("=" * 50)

# --- Interactive lookup loop ---
while True:
    print("\nEnter a country name to find its capital.")
    print("(Type 'quit' to exit)\n")
    user_input = input("Country: ").strip()

    if user_input.lower() == "quit":
        print("\nGoodbye! 🌍")
        break

    # Case-insensitive search
    match = None
    for country in africa_capitals:
        if country.lower() == user_input.lower():
            match = country
            break

    if match:
        print(f"\n✅ The capital of {match} is: {africa_capitals[match]}")
    else:
        print(f"\n❌ '{user_input}' was not found in the database.")
        print("   Please check the spelling or choose from the list above.")
