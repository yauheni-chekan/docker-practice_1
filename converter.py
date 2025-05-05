#!/usr/bin/env python3

import argparse
import pandas as pd
import os
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert a CSV file to JSON using pandas.")
    parser.add_argument('--input-file', '-i', required=True, help='Path to the input CSV file.')
    parser.add_argument('--output-file', '-o', required=True, help='Path to the output JSON file.')
    return parser.parse_args()

def convert_csv_to_json(input_path, output_path):
    print(f"[INFO] Reading CSV from: {input_path}")
    try:
        df = pd.read_csv(input_path)
        print(f"[INFO] Successfully read CSV. Rows: {len(df)}")
    except Exception as e:
        print(f"[ERROR] Failed to read CSV: {e}")
        sys.exit(1)

    print(f"[INFO] Converting CSV to JSON...")
    try:
        df.to_json(output_path, orient='records', lines=True)
        print(f"[SUCCESS] JSON saved to: {output_path}")
    except Exception as e:
        print(f"[ERROR] Failed to write JSON: {e}")
        sys.exit(1)

def main():
    args = parse_arguments()
    print(f"[INFO] Input file: {args.input_file}")
    print(f"[INFO] Output file: {args.output_file}")

    if not os.path.exists(args.input_file):
        print(f"[ERROR] Input file does not exist: {args.input_file}")
        sys.exit(1)

    convert_csv_to_json(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
