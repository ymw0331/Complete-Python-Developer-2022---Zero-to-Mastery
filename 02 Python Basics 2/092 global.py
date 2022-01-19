# Global
total = 0


def count(total):
    total += 1
    return total

print(count(count(total)))

# 1 - start with local
# 2 - parent local?
# 3 - global
# 4 - built-in python functions
