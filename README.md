# LEGO® Set Inventory Management System

## Overview

This is a Python-based inventory management system for LEGO® sets. It allows users to view, add, and search for LEGO® sets using data stored in a file. The system is designed to be modular, reusable, and maintainable, following best practices in function usage and version control.

This project is developed as part of the SOFT6017 and SOFT6018 modules and adheres to their constraints and learning content.

---

## Features

- Load LEGO® set data from a file into Python data structures.
- Display the inventory in a well-formatted table.
- Add new LEGO® sets with full input validation.
- Search for LEGO® sets by set number prefix.
- Save data back to the file on exit.
- Designed to allow easy expansion with additional menu options.

---

## Menu Options

1. **Display Inventory** – Shows all sets with details, using ✅ / ❌ indicators and a retired set marker.  
2. **Add New LEGO® Set** – Allows users to input a new set with full validation.  
3. **Search by Code Prefix** – Lets users filter sets by starting digits of the set number.  
4. **(Placeholder)** – To be implemented during in-lab project work.  
5. **(Placeholder)** – To be implemented during in-lab project work.  
6. **(Placeholder)** – To be implemented during in-lab project work.  
7. **Quit** – Saves all current data back to the file.

---

## Data Format

The inventory data is stored in a CSV file with the following format:

SetNumber,Title,NumberOfPieces,RRP,StockStatus
Example:
10307,Eiffel Tower,10001,629.99,1 42177,Mercedes-Benz 500,2891,249.99,0


- **SetNumber**: A unique 5–7 digit number.
- **RRP**: Recommended Retail Price, with `0.00` indicating a retired product.
- **StockStatus**: `1` for in stock, `0` for out of stock.

---

## Requirements

- Python 3.x
- Only standard Python libraries covered in SOFT6017 and SOFT6018 may be used.
- The `validation.py` module is provided and should be used for input validation where applicable.

---

## Development & Submission

- Development must be tracked using Git, with regular commits showing project progress.
- Two files must be submitted:
  - **File 1**: Core implementation with Git log images.
  - **File 2**: Same file with additional in-lab functionality for menu options 4, 5, and 6.

---

## Notes

- A `main()` function is required as the main driver of the application.
- Global variables are **not allowed**.
- Dictionaries may be used, although considered optional content.
- Handle file errors and corrupt data gracefully by terminating the application with a proper message.

---

© This project is for educational use only and is not affiliated with the LEGO Group.
