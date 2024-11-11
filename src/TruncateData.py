import argparse
import ast


parser = argparse.ArgumentParser("Truncate a list or string based on the start position and length")
parser.add_argument("--data", help="The original list or string")
parser.add_argument("--start", type=int, help="The position index to start truncation")
parser.add_argument("--length", type=int, help="The length of expected truncated data")

def truncate(data, start, length):
    """
    Truncate a list or string based on the start position and length,
    keeping only lowercase alphabetic characters.
    Returns: A truncated list or string.
    """
    end_open_border = start + length
    if end_open_border > len(data):
        # return "Notice: out of range."
        end_open_border = len(data)
    truncated_data = data[start:start + end_open_border]
    filtered_data = [char for char in truncated_data if str(char).isalpha()]
    
    # Return filtered data in the original type
    return ''.join(filtered_data) if isinstance(data, str) else filtered_data

if __name__=="__main__":
    args = parser.parse_args()
    try:
        # Convert `data` from a string to a list if possible
        data = ast.literal_eval(args.data)
    except (ValueError, SyntaxError):
        data = args.data
    start = args.start
    length = args.length

    truncated = truncate(data, start, length)
    print(truncated)