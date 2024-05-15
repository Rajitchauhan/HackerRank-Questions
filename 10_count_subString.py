
def count_substring(string, substring):
    count = 0
    index = string.find(substring)
    while index != -1:
        count += 1
        index = string.find(substring, index + 1)
    return count

# Input
original_string = input().strip()
substring = input().strip()

# Output
print(count_substring(original_string, substring))
