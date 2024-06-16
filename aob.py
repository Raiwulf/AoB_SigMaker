def hex_to_list(hex_string):
    return [int(byte, 16) if byte != '??' else None for byte in hex_string.split()]

def aobs_are_identical(aob1, aob2):
    if len(aob1) != len(aob2):
        return False
    for byte1, byte2 in zip(aob1, aob2):
        if byte1 is None or byte2 is None:
            continue
        if byte1 != byte2:
            return False
    return True

def add_aob(aob1):
    hex_string = input("Enter the AOB (space-separated hex values, use ?? for unknown bytes): ")
    aob2 = hex_to_list(hex_string)
    print(f"AOB added: {hex_string}")

    if not aob1:
        aob1.extend(aob2)
        return

    identical = aobs_are_identical(aob1, aob2)

    for i in range(len(aob1)):
        if aob1[i] is None:
            continue
        if aob1[i] != aob2[i]:
            aob1[i] = None

    print("Current AOB1 after comparison:")
    print(" ".join([f'{byte:02X}' if byte is not None else '??' for byte in aob1]))
    if identical:
        print("AOBs are identical.")
    print()

def main():
    aob1 = []
    while True:
        print("Select an option:")
        print("1. Add an AOB")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_aob(aob1)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
