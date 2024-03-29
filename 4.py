from scipy.stats import norm

def WWW(z):
    return 1 - norm.cdf(z)

# Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см

print(WWW(1))  # 0.15865525393145707

# б). больше 190 см

print(WWW(2))  # 0.02275013194817921

# в). от 166 см до 190 см

print(WWW(1) * 2 + WWW(2))  # 0.34006063981109336

# г). от 166 см до 182 см

print(WWW(1) * 2)  # 0.31731050786291415

# д). от 158 см до 190 см

print(WWW(2) * 2)  # 0.04550026389635842

# е). не выше 150 см или не ниже 190 см

print(1 - (WWW(2) + WWW(3)))  # 0.9758999700201907

# ё). не выше 150 см или не ниже 198 см

print(1 - (WWW(3) * 2))  # 0.9973002039367398

# ж). ниже 166 см.

print(1 - WWW(1))  # 0.8413447460685429