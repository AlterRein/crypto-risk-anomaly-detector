import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta

# 1. GENERATE SIMULATED BLOCKCHAIN/EXCHANGE TRANSACTION DATA
print("Generating simulated transaction data stream...")
np.random.seed(42)
n_records = 5000

wallets = [f"0x{np.random.hex":06x}xyz" for _ in range(50)]
tokens = ['BNB', 'BTC', 'ETH', 'SOL']

start_time = datetime.now()
timestamps = [start_time + timedelta(seconds=int(np.random.randint(1, 600))) for _ in range(n_records)]
timestamps.sort()

data = {
    'timestamp': timestamps,
    'wallet_address': np.random.choice(wallets, n_records),
    'token': np.random.choice(tokens, n_records),
    'amount_usd': np.random.exponential(scale=5000, size=n_records) # Most are small, few are big
}

df = pd.DataFrame(data)

# Injecting some artificial anomalies (Whale transactions & High-frequency wash trading)
df.loc[100, 'amount_usd'] = 250000.0  # Massive Whale Transfer
df.loc[500:505, 'wallet_address'] = '0x111111xyz'  # High-frequency trading spam

print(f"Successfully generated {len(df)} transaction records.")

# 2. RISK ANALYSIS & ANOMALY DETECTION CRITERIA
print("\n🔍 Running Risk AI Detection Engines...")

# Rule 1: Whale Detection (Transactions > $50,000)
whale_threshold = 50000
whales_df = df[df['amount_usd'] > whale_threshold]

# Rule 2: High-Frequency Anomalies / Potential Wash Trading (Same wallet > 4 times within 10 seconds)
df['time_diff'] = df.groupby('wallet_address')['timestamp'].diff().dt.total_seconds()
hf_anomalies = df[(df['time_diff'] <= 2) & (df['time_diff'] > 0)]

# 3. CONSOLIDATE RISK REPORTS
print("\n=== BINANCE RISK DETECTOR REPORT ===")
print(f"Total Transactions Audited: {len(df)}")
print(f"Whale Alerts Detected (> ${whale_threshold}): {len(whales_df)} flags")
print(f"High-Frequency Wash Trading Red Flags: {len(hf_anomalies)} flags")

print("\nSample Whale Alerts Details:")
print(whales_df[['timestamp', 'wallet_address', 'token', 'amount_usd']].head(3).to_string(index=False))

print("\nSample High-Frequency Anomalies Details:")
print(hf_anomalies[['timestamp', 'wallet_address', 'token', 'amount_usd', 'time_diff']].head(3).to_string(index=False))

# Export clean reports for Dashboard/Security engineering team
whales_df.to_csv("whale_alerts_report.csv", index=False)
hf_anomalies.to_csv("high_frequency_anomalies_report.csv", index=False)
print("\nRisk reports successfully exported to CSV for the security response team.")
