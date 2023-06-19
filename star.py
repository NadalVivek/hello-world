# Function to print star pattern
def print_star_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
num_rows = 5
print_star_pattern(num_rows)
