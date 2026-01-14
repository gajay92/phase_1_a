import csv


# Remove this import - it causes circular import
# from growth_utils import average_improvement, write_summary

def read_growth_data(filename):
    """
    Reads plant growth data from a CSV file and returns a list of dictionaries.

    Args:
        filename (str): Path to the CSV file containing plant growth data

    Returns:
        list: A list of dictionaries, where each dictionary represents one row of data
    """
    records = []

    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(row)

    return records


# Test code
if __name__ == "__main__":
    # Import only when running as main script (avoids circular import)
    from growth_utils import average_improvement, write_summary

    # Test the function
    try:
        # Adjust the path based on your directory structure
        data = read_growth_data('C:/Users/g_aja/Desktop/data/plant_growth_trials.csv')

        print("Successfully read the data!")
        print(f"Total number of records: {len(data)}")
        print("\nFirst record:")
        print(data[0])

        print("\nAll column names:")
        if data:
            print(list(data[0].keys()))

        print("\n--- Sample of first 3 records ---")
        for i, record in enumerate(data[:3]):
            print(f"\nRecord {i + 1}:")
            print(f"  Student: {record['Student']}")
            print(f"  Greenhouse: {record['Greenhouse']}")
            print(f"  Plant: {record['Plant']}")
            print(f"  Nutrient: {record['Nutrient']}")
            print(f"  Week 1 Height: {record['HeightW1']} cm")
            print(f"  Week 10 Height: {record['HeightW10']} cm")

        # CP3: Calculate average improvements (moved outside the loop)
        print("\n" + "=" * 60)
        print("CALCULATING AVERAGE IMPROVEMENTS...")
        print("=" * 60)

        improvements = average_improvement(data)

        # CP4: Write summary to CSV file
        summary_file = 'C:/Users/g_aja/Desktop/data/growth_summary.csv'
        write_summary(improvements, summary_file)
        print(f"\n✓ Summary written to growth_summary.csv")

        # CP5: Display results neatly
        print("\nAverage Height Improvements:")
        print("-" * 60)
        for plant in sorted(improvements.keys()):
            avg_gain = improvements[plant]
            print(f"{plant}: {avg_gain:.2f} cm")

        print("\n" + "=" * 60)
        print("ANALYSIS COMPLETE")
        print("=" * 60)

    except FileNotFoundError:
        print("Error: Could not find the file 'plant_growth_trials.csv'")
        print("Please make sure the file exists in the Week11_lab/data directory")
        print("Please check that the file path is correct:")
        print("C:/Users/g_aja/Desktop/data/plant_growth_trials.csv")
    except KeyError as e:
        print(f"\n❌ ERROR: Missing expected column in CSV: {e}")
        print("Please verify the CSV file has all required columns.")
    except Exception as e:
        print(f"An error occurred: {e}")