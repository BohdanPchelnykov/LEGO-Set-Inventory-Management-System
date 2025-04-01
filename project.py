class LegoSet:
    def __init__(self, set_number, title, num_pieces, rrp, in_stock):
        self.set_number = set_number
        self.title = title
        self.num_pieces = num_pieces
        self.rrp = rrp
        self.in_stock = in_stock

    def __repr__(self):
        return f"{self.set_number} - {self.title} ({self.num_pieces} pcs) €{self.rrp} - {'In stock' if self.in_stock else 'Out of stock'}"


def load_lego_data(filename):
    lego_sets = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")

                if len(parts) != 5:
                    raise ValueError(f"Line {i + 1} is malformed: {line}")

                set_number = parts[0].strip()
                title = parts[1].strip()
                num_pieces = int(parts[2].strip())
                rrp = float(parts[3].strip())
                in_stock = int(parts[4].strip())

                if in_stock not in (0, 1):
                    raise ValueError(f"Invalid stock value on line {i + 1}: {line}")

                lego_sets.append(LegoSet(set_number, title, num_pieces, rrp, bool(in_stock)))

    except FileNotFoundError:
        print("Error: File not found.")
        exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

    return lego_sets


def main():
    filename = "SampleData.txt"
    lego_sets = load_lego_data(filename)
    print(f"\nLoaded {len(lego_sets)} LEGO® sets:\n")
    for lego in lego_sets:
        print(lego)


if __name__ == '__main__':
    main()
