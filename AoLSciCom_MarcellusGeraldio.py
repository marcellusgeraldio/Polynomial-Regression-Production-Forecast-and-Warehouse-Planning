# Nama = Marcellus Geraldio Florenta
# NIM  = 2702262816
# THEORY: ASSURANCE OF LEARNING
# Scientific Computing

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from sklearn.metrics import mean_squared_error

data_path = 'aol_data(in).csv'
data = pd.read_csv(data_path)

produksi_tas = data.iloc [0, 1:] .values.astype(float)
time = np.arange(1, len(produksi_tas) + 1)

derajat = 4 # derajat yang digunakan

# fitting polinomial
kf = np.polyfit(time, produksi_tas, derajat)
polinomial_model = np.poly1d(kf)

# menghitung nilai prediksi menggunakan polinomial
Y = polinomial_model(time)

# RMSE
rmse = np.sqrt(mean_squared_error(produksi_tas, Y))

# mencari root untuk menentukan target gudang
def find_root(polinomial, target, start_time):
    def equation(t):
        return polinomial(t) - target
    return fsolve(equation, start_time)

# menghitung waktu yang diperlukan untuk gudang baru
maksimum = 25000
prediksi_maksimum = find_root(polinomial_model, maksimum, 145)[0]
prediksi_pembangunan = 13
waktu_bangun = prediksi_maksimum - prediksi_pembangunan

plt.figure(figsize=(12, 6))
plt.scatter(time, produksi_tas, label='Data Asli', color='yellow', s=7)
plt.plot(time, Y, label=f'Model Polinomial Derajat {derajat}', color='blue')
plt.axhline(y=maksimum, color='green', linestyle='--', label='Kapasitas Maksimum Gudang')
plt.axvline(x=waktu_bangun, color='purple', linestyle='--', label='Perkiraan Waktu Mencapai Maksimum')
plt.xlabel('Waktu/Bulan')
plt.ylabel('Bag')
plt.legend()
plt.title(f'Polinomial untuk produksi Bag EGIER dan Gudang Baru | RMSE: {rmse:.3f} ')
plt.show()



# DISPLAY DATA

print(f"Root Mean Squared Error (RMSE): {rmse:.3f}")
print(f"    [] Perkiraan waktu untuk mencapai kapasitas maksimum gudang = bulan ke-{prediksi_maksimum:.0f}")
print(f"    [] Waktu untuk memulai pembangunan gudang baru = bulan ke-{waktu_bangun:.0f}")
