import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("NVDA", start="2025-01-01", end="2025-12-01", auto_adjust=True)
close = df[("Close", "NVDA")]
volume = df[("Volume", "NVDA")]
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(12, 8),gridspec_kw={"height_ratios":[3,1]})

ax1.plot(df.index, close,color = "blue",label = "Close Price", linewidth=1.5)
ax1.set_title("NVDA Price and Volume")
ax1.set_ylabel("Price (USD)")
ax1.grid(True)
ax1.legend()

ax2.bar(df.index, volume)
ax2.set_ylabel("Volume")
ax2.set_xlabel("Date")
ax2.grid(True)

plt.tight_layout()
plt.show()
