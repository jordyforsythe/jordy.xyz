# ============================================================
# Program 1: African Currency Exchange Rate Calculator
# Currencies: Nigerian Naira (NGN), Kenyan Shilling (KES),
#             South African Rand (ZAR)
# ============================================================

# --- Base exchange rates relative to 1 USD (approx. 2025 rates) ---
usd_to_ngn = 1580.00   # 1 USD = 1580 Nigerian Naira
usd_to_kes = 129.50    # 1 USD = 129.50 Kenyan Shilling
usd_to_zar = 18.30     # 1 USD = 18.30 South African Rand

# --- Derive cross rates ---
ngn_to_kes = usd_to_kes / usd_to_ngn   # 1 NGN = ? KES
ngn_to_zar = usd_to_zar / usd_to_ngn   # 1 NGN = ? ZAR
kes_to_ngn = usd_to_ngn / usd_to_kes   # 1 KES = ? NGN
kes_to_zar = usd_to_zar / usd_to_kes   # 1 KES = ? ZAR
zar_to_ngn = usd_to_ngn / usd_to_zar   # 1 ZAR = ? NGN
zar_to_kes = usd_to_kes / usd_to_zar   # 1 ZAR = ? KES

# --- Sample conversion amounts ---
amount_ngn = 10_000   # 10,000 Naira
amount_kes = 5_000    # 5,000 Kenyan Shillings
amount_zar = 500      # 500 Rand

print("=" * 55)
print("   AFRICAN CURRENCY EXCHANGE RATE CALCULATOR")
print("=" * 55)
print(f"\nReference Rates (against USD):")
print(f"  1 USD = {usd_to_ngn:,.2f} NGN (Nigerian Naira)")
print(f"  1 USD = {usd_to_kes:,.2f} KES (Kenyan Shilling)")
print(f"  1 USD = {usd_to_zar:,.2f} ZAR (South African Rand)")

print(f"\n{'─' * 55}")
print(f"Converting {amount_ngn:,} NGN:")
print(f"  → {amount_ngn * ngn_to_kes:,.4f} KES")
print(f"  → {amount_ngn * ngn_to_zar:,.4f} ZAR")

print(f"\nConverting {amount_kes:,} KES:")
print(f"  → {amount_kes * kes_to_ngn:,.2f} NGN")
print(f"  → {amount_kes * kes_to_zar:,.4f} ZAR")

print(f"\nConverting {amount_zar:,} ZAR:")
print(f"  → {amount_zar * zar_to_ngn:,.2f} NGN")
print(f"  → {amount_zar * zar_to_kes:,.2f} KES")
print("=" * 55)
