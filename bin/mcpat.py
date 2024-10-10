import os
import glob
import subprocess

def run_mcpat_for_each_xml():
    # Get the current directory name dynamically
    current_directory = os.path.basename(os.getcwd())
    
    # Find all mcpat-in-{number}.xml files in the current directory
    mcpat_input_files = glob.glob('mcpat-in-*.xml')
    
    # Sort the files based on the number extracted from the filename
    mcpat_input_files.sort(key=lambda f: int(os.path.splitext(os.path.basename(f))[0].split('-')[2]))
    
    # Base path to the mcpat executable
    mcpat_executable = "/home/user01/workspace/mcpat/build/mcpat"
    
    # Iterate over each mcpat-in-{number}.xml file in ascending order
    for input_file in mcpat_input_files:
        # Extract the number from the input file name
        file_number = os.path.splitext(os.path.basename(input_file))[0].split('-')[2]
        
        # Define the output file name for the result
        output_file = f"mcpat/mcpat-{current_directory}-{file_number}.txt"
        
        # Construct the mcpat command
        command = [
            mcpat_executable,
            '-i', input_file,
            '-p', '5',
            '--opt_for_clk', '1'
        ]
        
        # Open the output file to write mcpat's output
        with open(output_file, 'w') as outfile:
            print(f"Running: {' '.join(command)}")
            subprocess.run(command, stdout=outfile)
        
        print(f"Output written to: {output_file}")

if __name__ == "__main__":
    run_mcpat_for_each_xml()

