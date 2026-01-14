"""
week11_lab.py
Main file for plant growth data analysis
Integrates CP1 (reading data) and CP3 (analyzing improvements)
"""
import csv

# Import only read_growth_data from the helper module
from week11_lab import read_growth_data


def average_improvement(records):
    """
    Calculates the average height improvement (HeightW10 - HeightW1) for each plant type.

    Args:
        records (list): List of dictionaries containing plant growth data

    Returns:
        dict: Dictionary with plant types as keys and average improvements as values
    """
    # Step 1: Create empty dictionary improvements
    improvements = {}

    # Step 2: For each row in records
    for row in records:
        # Get the plant type
        plant = row["Plant"]

        # Calculate gain (HeightW10 - HeightW1)
        gain = float(row["HeightW10"]) - float(row["HeightW1"])

        # Step 3: If plant not in improvements, create empty list
        if plant not in improvements:
            improvements[plant] = []

        # Step 4: Append gain to improvements[plant]
        improvements[plant].append(gain)

    # Step 5: For each plant, compute average of its list
    results = {}
    for plant in improvements:
        # Calculate average: sum of all gains / number of gains
        average = sum(improvements[plant]) / len(improvements[plant])
        results[plant] = average

    return results


def write_summary(results, filename):
    """
    Writes the average improvements to a summary CSV file.

    Args:
        results (dict): Dictionary with plant types as keys and average gains as values
        filename (str): Path to the output CSV file
    """
    # Open file for writing
    with open(filename, 'w', newline='') as file:
        # Define column names
        fieldnames = ['Plant', 'AverageGain']

        # Create DictWriter object
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header row
        writer.writeheader()

        # Write data rows
        for plant, gain in results.items():
            writer.writerow({'Plant': plant, 'AverageGain': f'{gain:.2f}'})


def main():
    """
    Main function that:
    1. Reads the plant growth data (CP1)
    2. Displays sample records
    3. Calculates and displays average improvements (CP3)
    """
    try:
        # CP1: Read the data
        print("=" * 60)
        print("PLANT GROWTH DATA ANALYSIS")
        print("=" * 60)

        data = read_growth_data('C:/Users/g_aja/Desktop/data/plant_growth_trials.csv')

        print("\n✓ Successfully read the data!")
        print(f"✓ Total records: {len(data)}")

        # Display first record
        print("\n" + "-" * 60)
        print("FIRST RECORD:")
        print("-" * 60)
        print(data[0])

        # Display all column names
        print("\n" + "-" * 60)
        print("ALL COLUMN NAMES:")
        print("-" * 60)
        if data:
            print(list(data[0].keys()))

        # Display sample of first 3 records
        print("\n" + "-" * 60)
        print("SAMPLE OF FIRST 3 RECORDS:")
        print("-" * 60)
        for i, record in enumerate(data[:3]):
            print(f"\nRecord {i + 1}:")
            print(f"  Student:    {record['Student']}")
            print(f"  Greenhouse: {record['Greenhouse']}")
            print(f"  Plant:      {record['Plant']}")
            print(f"  Nutrient:   {record['Nutrient']}")
            print(f"  Week 1:     {record['HeightW1']} cm")
            print(f"  Week 10:    {record['HeightW10']} cm")

        # CP3: Calculate and display average improvements
        print("\n" + "=" * 60)
        print("AVERAGE HEIGHT IMPROVEMENTS (Week 10 - Week 1)")
        print("=" * 60)

        improvements = average_improvement(data)

        # Display results sorted by plant name
        for plant in sorted(improvements.keys()):
            avg_gain = improvements[plant]
            print(f"{plant:12s}: {avg_gain:.2f} cm")

        # CP4: Write summary to CSV file
        print("\n" + "-" * 60)
        summary_file = 'C:/Users/g_aja/Desktop/data/growth_summary.csv'
        write_summary(improvements, summary_file)
        print(f"✓ growth_summary.csv created successfully at:")
        print(f"  {summary_file}")
        print("-" * 60)

        print("\n" + "=" * 60)
        print("ANALYSIS COMPLETE")
        print("=" * 60)

    except FileNotFoundError:
        print("\n❌ ERROR: Could not find the file 'plant_growth_trials.csv'")
        print("Please check that the file path is correct:")
        print("C:/Users/g_aja/Desktop/data/plant_growth_trials.csv")
    except KeyError as e:
        print(f"\n❌ ERROR: Missing expected column in CSV: {e}")
        print("Please verify the CSV file has all required columns.")
    except Exception as e:
        print(f"\n❌ ERROR: An unexpected error occurred: {e}")


# Run the main function
if __name__ == "__main__":
    main()