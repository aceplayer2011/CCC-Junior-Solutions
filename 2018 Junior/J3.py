distances = list(map(int, input().split()))
city_positions = [0] * 5

for i in range(1, 5):
    city_positions[i] = city_positions[i-1] + distances[i-1]

for i in range(5):
    for j in range(5):
        distance = city_positions[j] - city_positions[i]
        if distance < 0:  # Ensuring result is positive
            distance = distance * -1
        print(distance, end=" ")
    print()