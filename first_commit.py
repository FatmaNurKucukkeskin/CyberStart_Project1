import math

# 1. Noktaların Tanımlanması
points = [(1, 2), (3, 4), (6, 8), (9, 12)]

# 2. Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    # Noktaların koordinatlarını ayırma
    x1, y1 = point1
    x2, y2 = point2
    # Öklid mesafesini hesaplama
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# 3. Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 4. Minimum Mesafenin Bulunması
min_distance = min(distances)
print("Minimum Öklid Mesafesi:", min_distance)
