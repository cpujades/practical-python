# bounce.py
#
# Exercise 1.5

height = 100
bounce_height = 0.6
bounce_count = 0

for bounce in range(10):
    bounce_count += 1
    height *= bounce_height
    print(bounce_count, round(height, 4))
