import csv

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

def add_week11_data(data, increment=2):
    """
    Adds a new column HeightW11 to the dataset where HeightW11 = HeightW10 + increment.

    Args:
        data (list): List of dictionaries containing plant growth data
        increment (float): Value to add to HeightW10 (default: 2)

    Returns:
        list: Updated list with HeightW11 column added
    """
    updated_data = []

    for record in data:
        # Create a copy of the record to avoid modifying original
        updated_record = record.copy()

        # Calculate HeightW11
        height_w10 = float(record['HeightW10'])
        height_w11 = height_w10 + increment

        # Add the new column
        updated_record['HeightW11'] = f"{height_w11:.2f}"

        updated_data.append(updated_record)

    return updated_data


def write_updated_data(data, filename):
    """
    Writes the updated plant growth data to a CSV file.

    Args:
        data (list): List of dictionaries containing plant growth data
        filename (str): Path to the output CSV file
    """
    if not data:
        print("No data to write!")
        return

    # Get all column names (including the new HeightW11)
    fieldnames = list(data[0].keys())

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write all rows
        writer.writerows(data)

    print(f"✓ Updated data successfully written to {filename}")


def display_sample_comparison(original_data, updated_data, num_samples=3):
    """
    Displays a comparison of original and updated data for the first few records.

    Args:
        original_data (list): Original dataset
        updated_data (list): Updated dataset with HeightW11
        num_samples (int): Number of samples to display
    """
    print("\n" + "=" * 80)
    print("COMPARISON: Original vs Updated Data")
    print("=" * 80)

    for i in range(min(num_samples, len(original_data))):
        print(f"\nRecord {i + 1}:")
        print(f"  Plant: {original_data[i]['Plant']}")
        print(f"  Student: {original_data[i]['Student']}")
        print(f"  HeightW10: {original_data[i]['HeightW10']} cm")
        print(f"  HeightW11: {updated_data[i]['HeightW11']} cm (NEW)")
        print(
            f"  Growth from W10 to W11: {float(updated_data[i]['HeightW11']) - float(original_data[i]['HeightW10']):.2f} cm")


# Main execution
if __name__ == "__main__":
    try:
        # File paths
        input_file = 'C:/Users/g_aja/Desktop/data/plant_growth_trials.csv'
        output_file = 'C:/Users/g_aja/Desktop/data/plant_growth_trials_updated.csv'

        print("=" * 80)
        print("CHALLENGE TASK: APPEND WEEK 11 DATA")
        print("=" * 80)

        # Step 1: Read the original data
        print("\n[Step 1] Reading plant_growth_trials.csv...")
        original_data = read_growth_data(input_file)
        print(f"✓ Successfully read {len(original_data)} records")

        # Option to get user input for increment
        print("\n[Step 2] Adding HeightW11 column...")
        user_choice = input("Do you want to use a custom increment? (y/n, default is +2): ").strip().lower()

        if user_choice == 'y':
            try:
                increment = float(input("Enter the height increment value: "))
                print(f"Using increment: +{increment} cm")
            except ValueError:
                print("Invalid input. Using default increment of +2 cm")
                increment = 2
        else:
            increment = 2
            print(f"Using default increment: +{increment} cm")

        # Step 2: Add Week 11 data
        updated_data = add_week11_data(original_data, increment)
        print(f"✓ Added HeightW11 column (HeightW10 + {increment})")

        # Step 3: Write updated data to file
        print("\n[Step 3] Saving updated dataset...")
        write_updated_data(updated_data, output_file)

        # Display comparison
        display_sample_comparison(original_data, updated_data, num_samples=3)

        # Summary statistics
        print("\n" + "=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"Total records processed: {len(updated_data)}")
        print(f"New column added: HeightW11")
        print(f"Formula used: HeightW11 = HeightW10 + {increment}")
        print(f"Output file: {output_file}")

        # Calculate average Week 11 height
        avg_w11 = sum(float(record['HeightW11']) for record in updated_data) / len(updated_data)
        print(f"\nAverage HeightW11 across all plants: {avg_w11:.2f} cm")

        print("\n" + "=" * 80)
        print("TASK COMPLETE!")
        print("=" * 80)

    except FileNotFoundError:
        print(f"\n❌ ERROR: Could not find the file '{input_file}'")
        print("Please make sure the file exists in the correct location.")
    except KeyError as e:
        print(f"\n❌ ERROR: Missing expected column in CSV: {e}")
        print("Please verify the CSV file has the 'HeightW10' column.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        import traceback

        traceback.print_exc()