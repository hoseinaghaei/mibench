import os
import glob
import subprocess

def run_gem5_mcpat_parser():
    # Get the current directory name dynamically
    current_directory = os.path.basename(os.getcwd())
    
    # Define the base directory for the config and stats files
    base_dir = f"/home/user01/workspace/gem5/m5out-cortex-a15-{current_directory}"
    print(f"base dir: {base_dir}")
    # Get the path to the config.json file
    config_file = os.path.join(base_dir, 'config.json')
    
    # Find all stats-{number}.txt files
    stats_files = glob.glob(os.path.join(base_dir, 'stats-*.txt'))
    
    # Template file location (same for all runs)
    template_file = "/home/user01/workspace/Gem5McPatParser/templates/template_arm.xml"
    
    # Iterate over each stats file and generate the corresponding McPAT XML output
    for stats_file in stats_files:
        # Extract the number from the stats file name
        file_number = os.path.splitext(os.path.basename(stats_file))[0].split('-')[1]
        
        # Define the output file name for the McPAT XML
        output_file = f"mcpat-in-{file_number}.xml"
        
        # Run the Gem5McPATParser.py script with the appropriate arguments
        command = [
            'python3',
            '/home/user01/workspace/Gem5McPatParser/Gem5McPATParser.py',
            '-c', config_file,
            '-s', stats_file,
            '-t', template_file,
            '-o', output_file  # Optional: output argument for generated XML file
        ]
        
        print(f"Running: {' '.join(command)}")
        subprocess.run(command)

if __name__ == "__main__":
    run_gem5_mcpat_parser()

