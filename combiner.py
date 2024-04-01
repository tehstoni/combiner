import argparse
import concurrent.futures

def generate_combinations(words, start, end):
    unique_combinations = set()
    for i in range(start, end):
        for j in range(len(words)):
            if i != j:
                combined_word = words[i] + words[j]
                unique_combinations.add(combined_word)
    return unique_combinations

def combine_words(input_file, output_file, workers=4):
    with open(input_file, 'r', encoding='utf-8') as f:
        words = f.read().splitlines()

    total_words = len(words)
    chunk_size = total_words // workers
    futures = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        for i in range(workers):
            start = i * chunk_size
            end = (i + 1) * chunk_size if i < workers - 1 else total_words
            futures.append(executor.submit(generate_combinations, words, start, end))

        unique_combinations = set()
        for future in concurrent.futures.as_completed(futures):
            unique_combinations.update(future.result())

    with open(output_file, 'w', encoding='utf-8') as f:
        for combination in unique_combinations:
            f.write(combination + '\n')

def main():
    parser = argparse.ArgumentParser(description="Generate word combinations from an input wordlist and remove duplicates, using multiprocessing.")
    parser.add_argument("input_file", help="Input wordlist file")
    parser.add_argument("output_file", help="Output wordlist file")
    parser.add_argument("--workers", type=int, default=4, help="Number of worker processes to use")

    args = parser.parse_args()

    combine_words(args.input_file, args.output_file, args.workers)
    print(f"Word combinations generated, duplicates removed, and saved to {args.output_file}")

if __name__ == "__main__":
    main()
