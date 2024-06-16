# HexByte Comparator

A simple Python program to compare Array of Bytes (AOB) patterns, allowing you to add new AOBs, compare them, and update existing patterns with wildcards for differing bytes.

## Features

- **Hex String to List Conversion**: Converts a hex string into a list of integers, with support for unknown bytes.
- **AOB Comparison**: Compares two AOBs, updating the first AOB with wildcards where bytes differ.
- **Interactive Command Line Interface**: Allows users to interactively add AOBs and see comparisons in real-time.

## How It Works

1. **Convert Hex to List**: The `hex_to_list` function converts a space-separated hex string into a list of integers, using `None` for unknown bytes (`??`).

2. **Compare AOBs**: The `aobs_are_identical` function checks if two AOBs are identical, ignoring positions with `None`.

3. **Add and Compare AOBs**: The `add_aob` function:

   - Prompts the user to input a new AOB.
   - Converts the input into a list.
   - Compares the new AOB with the existing one, updating the existing AOB with `None` where bytes differ.
   - Prints the updated AOB and indicates if the AOBs are identical.

4. **Main Loop**: The `main` function provides a simple menu for adding AOBs and exiting the program.

## Usage

1. **Run the Program**: Execute the script to start the program.

   ```sh
   python hexbyte_comparator.py
   ```

2. **Select an Option**:

   - **Add an AOB**: Enter `1` to input a new AOB. Use space-separated hex values, with `??` for unknown bytes.
   - **Exit**: Enter `2` to exit the program.

3. **View Results**: The program will display the updated AOB and indicate if the new AOB is identical to the existing one.

## Example

```sh
$ python aob_comparator.py
Select an option:
1. Add an AOB
2. Exit
Enter your choice: 1
Enter the AOB (space-separated hex values, use ?? for unknown bytes): 1A 2B 3C ?? 5E
AOB added: 1A 2B 3C ?? 5E
Current AOB1 after comparison:
1A 2B 3C ?? 5E

Select an option:
1. Add an AOB
2. Exit
Enter your choice: 1
Enter the AOB (space-separated hex values, use ?? for unknown bytes): 1A ?? 3C 4D 5E
AOB added: 1A ?? 3C 4D 5E
Current AOB1 after comparison:
1A ?? 3C ?? 5E

Select an option:
1. Add an AOB
2. Exit
Enter your choice: 2
```
