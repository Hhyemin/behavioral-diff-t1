import argparse
import ast


parser = argparse.ArgumentParser()
parser.add_argument("--data", help="The original list or string")
parser.add_argument("--filter", type=str, help="To filter out 'num' or 'letter'")

   
if __name__=="__main__":
    args = parser.parse_args()
    try:
        # Convert `data` from a string to a list if possible
        data = ast.literal_eval(args.data)
    except (ValueError, SyntaxError):
        data = args.data
    filter = args.filter

    filtered = None
    if filter == "num":
        filtered = [char for char in data if not str(char).isdigit()]
    elif filter == "letter":
        filtered = [char for char in data if not str(char).isalpha()]
    else:
        print("The filter is not supported.")
        exit()
    
    # Print filtered data in the original type
    reformatted_filtered = ''.join(filtered) if isinstance(data, str) else filtered
    print(reformatted_filtered)