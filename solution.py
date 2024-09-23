def longest_substring_k_unique(s: str, k: int) -> int:
    if k == 0:  # If K is 0, no valid substring exists
        return 0

    i = 0  # Left pointer
    max_length = 0  # Variable to store the maximum length of the substring
    letter_map = {}  # Dictionary to count the frequency of characters

    for j in range(len(s)):  # Right pointer iterating through the string
        # Add the current character to the letter_map
        letter_map[s[j]] = letter_map.get(s[j], 0) + 1

        # If we have more than K unique characters, move the left pointer
        while len(letter_map) > k:
            letter_map[s[i]] -= 1  # Decrease the count of the left character
            if letter_map[s[i]] == 0:  # Remove it if its count is 0
                del letter_map[s[i]]
            i += 1  # Move the left pointer to the right

        # Calculate the length of the current valid window
        max_length = max(max_length, j - i + 1)

    return max_length

print(longest_substring_k_unique("deepinthere", 4))
