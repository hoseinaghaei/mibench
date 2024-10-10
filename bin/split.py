import os
current_directory = os.path.basename(os.getcwd())
base_dir = f"/home/user01/workspace/gem5/m5out-cortex-a15-{current_directory}"

def split_stats_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    index = 0
    in_block = False
    current_block = []

    for line in lines:
        if "---------- Begin Simulation Statistics ----------" in line:
            in_block = True
            current_block = [line]  # Start a new block with the "Begin" line
        elif "---------- End Simulation Statistics   ----------" in line and in_block:
            current_block.append(line)  # Add the "End" line
            # Write the block to a new file
            with open(f'{base_dir}/stats-{index}.txt', 'w') as output_file:
                output_file.writelines(current_block)
            print(f'Created stats-{index}.txt')
            index += 1
            in_block = False
        elif in_block:
            current_block.append(line)  # Add lines between Begin and End

if __name__ == "__main__":
    # Get the current directory name dynamically using os.getcwd() and basename
   # current_directory = os.path.basename(os.getcwd())

    # Construct the input file path
    input_file = f"{base_dir}/stats.txt"
    print(input_file)
    if os.path.exists(input_file):
        split_stats_file(input_file)
    else:
        print(f"Error: The file {input_file} does not exist.")

