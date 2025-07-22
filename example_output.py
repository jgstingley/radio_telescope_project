import numpy as np
import matplotlib.pyplot as plt

# Simulated time (minutes)
time = np.linspace(0, 60, 300)

# Simulated 21cm intensity with a spike
intensity = 0.2 + 0.05 * np.random.randn(len(time))
intensity[120:130] += 0.5  # fake hydrogen spike

plt.plot(time, intensity, label='Simulated 21cm Signal')
plt.xlabel('Time (minutes)')
plt.ylabel('Signal Intensity (arb. units)')
plt.title('Simulated 1420 MHz Detection')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('simulated_21cm_signal.png', dpi=200)
plt.show()
