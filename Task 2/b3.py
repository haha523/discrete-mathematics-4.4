# Shannon-Fano Encoding Implementation in Python

from collections import Counter

# Helper function to recursively build Shannon-Fano codes
def build_tree(symbols, prefix=""):
    if len(symbols) == 1:
        return {symbols[0][0]: prefix}

    # Calculate split point
    total = sum(freq for _, freq in symbols)
    cumulative = 0
    split_index = 0

    for i, (_, freq) in enumerate(symbols):
        cumulative += freq
        if cumulative >= total / 2:
            split_index = i + 1
            break

    # Recursively process left and right halves
    left = build_tree(symbols[:split_index], prefix + "0")
    right = build_tree(symbols[split_index:], prefix + "1")

    # Merge the results
    left.update(right)
    return left

# Function to generate Shannon-Fano codes for a given text
def shannon_fano(text):
    # Count the frequency of each symbol
    frequencies = Counter(text)

    # Sort symbols by frequency in descending order
    sorted_symbols = sorted(frequencies.items(), key=lambda x: -x[1])

    # Build the Shannon-Fano tree and return codes
    return build_tree(sorted_symbols)

# Main execution
if __name__ == "__main__":
    # Example input
    text = input("Введите текст для кодирования: ").strip()

    # Generate Shannon-Fano codes
    codes = shannon_fano(text)

    # Display results
    print("\nSymbol | Code")
    print("-------|------")
    for symbol, code in codes.items():
        print(f"  {symbol}    | {code}")

    # Encode the text using generated codes
    encoded_text = ''.join(codes[char] for char in text)
    print("\nEncoded Text:", encoded_text)
