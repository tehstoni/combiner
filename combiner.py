import argparse

def combine_words(input_file, output_file):
    with open(input_file, 'r') as f:
        words = f.read().splitlines()

    unique_combinations = set()

    with open(output_file, 'w') as f:
        for word1 in words:
            for word2 in words:
                if word1 != word2:
                    combined_word = word1 + word2
                    unique_combinations.add(combined_word)

        for combination in unique_combinations:
            f.write(combination + '\n')

def main():
    parser = argparse.ArgumentParser(description="Generate word combinations from an input wordlist and remove duplicates.")
    parser.add_argument("input_file", help="Input wordlist file")
    parser.add_argument("output_file", help="Output wordlist file")

    args = parser.parse_args()

    combine_words(args.input_file, args.output_file)
    print(f"Word combinations generated, duplicates removed, and saved to {args.output_file}")

if __name__ == "__main__":
    main()
