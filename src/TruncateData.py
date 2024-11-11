import argparse
import ast


parser = argparse.ArgumentParser()
parser.add_argument("--data", help="The original list")
parser.add_argument("--start", type=int, help="The position index to start truncation")
parser.add_argument("--length", type=int, help="The length of expected truncated data")

def truncate(data, start, length):
    """
    Truncate a list based on the start position and length,
    keeping only lowercase alphabetic characters.
    Returns: A truncated list.
    """
    truncated_data = data[start:start + length]
    filtered_data = [char for char in truncated_data if str(char).isalpha()]
    return filtered_data

if __name__=="__main__":
    args = parser.parse_args()
    data = ast.literal_eval(args.data)
    start = args.start
    length = args.length

    truncated = truncate(data, start, length)
    print(truncated)