# Real scenario
# Store all 60 rice bags in our home or bring 1 bag every month. Obviously 2nd approach is better.

# following lines of code will execute smoothly.
l = [x*x for x in range (10000)]
print(l)

# following lines of code will throw memory error.
l = [x*x for x in range (10000000000000000000000000000000000000000000000000000000000000)]
print(l)