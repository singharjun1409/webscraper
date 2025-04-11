import csv

# filepath: /Users/arjun/Desktop/Programs/webscraper/analysis.py
# Read and process the CSV file
def analyze_volume(file_path):
    above_avg_count = 0
    below_avg_count = 0

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        print(f"{'Symbol':<10} {'Name':<30} {'Volume':<15} {'Avg Vol (3M)':<15} {'Comparison':<15}")
        print("-" * 85)
        
        for row in reader:
            symbol = row['Symbol']
            name = row['Name']
            volume = parse_volume(row['Volume'])
            avg_volume = parse_volume(row['Avg Vol (3M)'])
            
            # Compare Volume vs Avg Volume
            if volume > avg_volume:
                comparison = "Above Avg"
                above_avg_count += 1
            elif volume < avg_volume:
                comparison = "Below Avg"
                below_avg_count += 1
            else:
                comparison = "Equal"
            
            # Print the analysis
            print(f"{symbol:<10} {name:<30} {volume:<15,.0f} {avg_volume:<15,.0f} {comparison:<15}")

    # Print summary
    print("\nSummary:")
    print(f"Companies Above Average Volume: {above_avg_count}")
    print(f"Companies Below Average Volume: {below_avg_count}")

# Helper function to parse volume (convert to numeric value)
def parse_volume(volume_str):
    if 'M' in volume_str:
        return float(volume_str.replace('M', '')) * 1_000_000
    elif 'B' in volume_str:
        return float(volume_str.replace('B', '')) * 1_000_000_000
    else:
        return float(volume_str)

# Filepath to the CSV file
file_path = '/Users/arjun/Desktop/Programs/webscraper/stocks.csv'

# Analyze the volume data
analyze_volume(file_path)