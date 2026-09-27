# Crypto Transaction Risk & Anomaly Detector

An open-source Python-based data pipeline designed to monitor blockchain/crypto exchange transaction streams, detect market manipulation patterns, flag high-value "whale" movements, and uncover high-frequency anomalies (potential wash trading). 

*This portfolio project is tailored to align with the technical requirements of the Binance Risk AI Data Science & Analytics Team.*

## Key Features
- **Data Generation Pipeline:** Simulates large-scale real-time user behavior, fund-flow, and digital asset transactions.
- **Whale Alert System:** Automatically flags high-volume transaction spikes exceeding designated thresholds to mitigate liquidity risks.
- **High-Frequency Anomaly Detection:** Leverages time-series parsing with `pandas` to isolate rapid-fire transaction patterns (same wallet transacting within ≤ 2 seconds).
- **Automated Fraud Exporting:** Outputs clean anomalies matrices data structure for security engineering teams and forensic analysis.

## Tech Stack & Tools
- **Language:** Python 3.x
- **Data Processing:** Pandas, NumPy
- **Development Tooling:** Enhanced using advanced prompting workflows in AI Coding Agents (Cursor / Claude).

## How to Run the Script
1. Clone the repository:
   ```bash
   git clone https://github.com/AlterRein/crypto-risk-anomaly-detector
   ```
2. Run the script:
   ```bash
   python detector.py
   ```

## Industry Relevance (Alignment with Binance Risk AI)
This framework directly mirrors real-world objectives handled by cryptocurrency exchange security teams: protecting investors from market manipulation, parsing through millions of data points rapidly, and translating algorithmic detection signals into actionable business metrics.
# crypto-risk-anomaly-detector
