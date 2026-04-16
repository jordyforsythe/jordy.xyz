# ============================================================
# Program 2: African Country Income Classifier by GDP per Capita
# Categories (World Bank thresholds, USD):
#   Low income    : < $1,136
#   Middle income : $1,136 – $13,845
#   High income   : > $13,845
# ============================================================

# --- Dataset: (Country, GDP per capita in USD, approx. 2024) ---
countries = [
    ("Nigeria",       2_085),
    ("South Africa",  6_180),
    ("Egypt",         3_790),
    ("Ethiopia",        925),
    ("Kenya",         2_010),
    ("Morocco",       3_680),
    ("Mauritius",    11_360),
    ("Seychelles",   17_740),
    ("Burundi",         270),
    ("Tanzania",      1_200),
]

LOW_UPPER    = 1_136
MIDDLE_UPPER = 13_845

def classify_income(gdp_per_capita):
    """Classify a country by GDP per capita."""
    if gdp_per_capita < LOW_UPPER:
        return "🔴 Low Income"
    elif gdp_per_capita <= MIDDLE_UPPER:
        return "🟡 Middle Income"
    else:
        return "🟢 High Income"

print("=" * 58)
print("   AFRICAN COUNTRIES — GDP PER CAPITA INCOME CLASSIFIER")
print("=" * 58)
print(f"{'Country':<18} {'GDP/capita (USD)':>18}   {'Category'}")
print("─" * 58)

for country, gdp in countries:
    category = classify_income(gdp)
    print(f"{country:<18} ${gdp:>15,.0f}   {category}")

print("=" * 58)

# --- Summary counts ---
low    = sum(1 for _, gdp in countries if gdp < LOW_UPPER)
middle = sum(1 for _, gdp in countries if LOW_UPPER <= gdp <= MIDDLE_UPPER)
high   = sum(1 for _, gdp in countries if gdp > MIDDLE_UPPER)

print(f"\nSummary:")
print(f"  🔴 Low Income countries    : {low}")
print(f"  🟡 Middle Income countries : {middle}")
print(f"  🟢 High Income countries   : {high}")
print("=" * 58)
