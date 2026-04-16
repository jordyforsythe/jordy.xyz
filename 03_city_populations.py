# ============================================================
# Program 3: African City Population Processor
# Uses a for loop to find the Top 3 largest cities by population
# ============================================================

# --- Dataset: (City, Country, Population approx. 2024) ---
african_cities = [
    ("Lagos",         "Nigeria",      15_946_000),
    ("Cairo",         "Egypt",        21_323_000),
    ("Kinshasa",      "DR Congo",     17_071_000),
    ("Johannesburg",  "South Africa",  6_065_000),
    ("Luanda",        "Angola",        9_292_000),
    ("Dar es Salaam", "Tanzania",      7_776_000),
    ("Khartoum",      "Sudan",         6_160_000),
    ("Abidjan",       "Côte d'Ivoire", 5_516_000),
    ("Nairobi",       "Kenya",         5_118_000),
    ("Accra",         "Ghana",         3_630_000),
    ("Addis Ababa",   "Ethiopia",      5_461_000),
    ("Casablanca",    "Morocco",       4_370_000),
]

print("=" * 58)
print("       AFRICAN CITY POPULATION PROCESSOR")
print("=" * 58)
print(f"\n{'#':<4} {'City':<18} {'Country':<16} {'Population':>12}")
print("─" * 58)

# Print all cities using a for loop
for i, (city, country, pop) in enumerate(african_cities, start=1):
    print(f"{i:<4} {city:<18} {country:<16} {pop:>12,}")

# --- Find Top 3 using a for loop (no sorting built-ins) ---
top3 = []

for city_data in african_cities:
    top3.append(city_data)
    # Keep only the 3 largest by population
    top3.sort(key=lambda x: x[2], reverse=True)
    if len(top3) > 3:
        top3.pop()   # remove the smallest of the 4

print("\n" + "=" * 58)
print("   🏆 TOP 3 LARGEST AFRICAN CITIES BY POPULATION")
print("=" * 58)
medals = ["🥇", "🥈", "🥉"]
for rank, (city, country, pop) in enumerate(top3):
    print(f"  {medals[rank]}  {city}, {country:<16} — {pop:,} people")
print("=" * 58)
