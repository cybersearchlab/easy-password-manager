# easy-password-manager
A Python-based security tool that addresses the modern challenge of password management by generating a matrix of strong, unique passwords. Instead of remembering one complex master password, users only need to remember a simple reference (e.g., "M54") representing the row and column coordinates of their desired password within the generated matrix.

---

## Table of Contents
- [Context & Problem Statement](#context--problem-statement)
- [The Solution](#the-solution)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
- [Password Generation Rules](#password-generation-rules)
- [Security Considerations](#security-considerations)
- [File Structure](#file-structure)
- [Example Walkthrough](#example-walkthrough)
- [Limitations & Future Improvements](#limitations--future-improvements)
- [License](#license)

---

## Context & Problem Statement

In today's digital world, users are overwhelmed by the sheer number of online accounts they must manage. This proliferation often leads to dangerous habits:

- **Password Reuse** – Using the same password across multiple accounts for fear of forgetting them.
- **Weak Passwords** – Choosing simple, familiar, or easily guessable passwords.
- **Memory Overload** – Struggling to remember dozens of unique, complex passwords.

While **password managers** offer an excellent solution by storing all credentials in an encrypted vault, they introduce a new challenge: the **master password**. This single password must be:
- Extremely strong
- Memorized perfectly
- Changed regularly
- Never written down

For many users, this becomes a critical point of failure. If the master password is compromised, the attacker gains access to *every* stored credential—essentially stealing the user's entire digital identity.

---

## The Solution

This project proposes a novel approach to master password management: **the password matrix**.

Instead of remembering a long, complex master password like `Vgte59zYueas47erzd@esa21`, users only need to remember:
- The **row** and **column** coordinates of their chosen password within a matrix (e.g., `M54` for row 5, column 4).
- Optionally, a simple, easy-to-remember reference key.

This method offers several advantages:
- **Simplicity** – Coordinates are far easier to remember and change monthly.
- **Strong Passwords** – All generated passwords adhere to strict security standards.
- **No Storage** – The matrix can be regenerated as needed if you remember the coordinates and generation parameters.

---

## Features

- **Customizable Matrix Size** – Define the number of rows and columns.
- **Strong Password Generation** – Automatically generates passwords that meet industry-standard criteria.
- **Display & Save** – View the matrix in the terminal and save it to a text file.
- **Quick Retrieval** – Instantly retrieve a password by specifying its row and column indices.
- **Portable Output** – The saved matrix can be stored securely offline (e.g., on encrypted USB drive).

---

## How It Works

1. **User Inputs Matrix Dimensions** – Specify the number of rows and columns.
2. **Matrix Generation** – The program fills each cell with a randomly generated strong password.
3. **Display & Save** – The matrix is printed to the console and saved to `password_matrix.txt`.
4. **Password Retrieval** – Enter row/column indices (0-based) to retrieve the corresponding password.

---

## Installation

### Prerequisites
- Python 3.6 or higher
- No external libraries required (uses only Python standard library)

### Steps
1. Clone this repository or download the script.
   
         git clone https://github.com/cybersearchlab/easy-password-manager.git
         cd password-matrix-generator

## Usage Guide

### Step 1: Run the Script
    python password_matrix.py

### Step 2: Enter Matrix Size

You will be prompted to enter the number of rows and columns:

    Enter the number of rows: 5
    Enter the number of columns: 4

### Step 3: View Generated Matrix

The program displays the generated matrix:

Passwork Matrice:
<img width="1563" height="105" alt="image" src="https://github.com/user-attachments/assets/4a5eca04-f05c-4ec6-aaad-3489067eebb4" />

### Step 4: Retrieve a Password

Enter the row and column indices (starting from 0) for the password you want:

    Enter the row number (starting at 0): 4
    Enter the column number (starting at 0): 3
    Password at position (4, 3): 9ZL63Q?S8vl+awAXX#3HZ,tEU)tT5Y
<img width="1556" height="100" alt="image" src="https://github.com/user-attachments/assets/2fe5c4f6-0a34-4ef6-bb20-9c4973b1f8e3" />

### Step 5: Saved File

## Password Generation Rules

All generated passwords comply with strict security standards:

- **Length** – Between 12 and 50 characters (default 30).
- **Character Requirements:**
  - At least one uppercase letter (A-Z)
  - At least one lowercase letter (a-z)
  - At least one digit (0-9)
  - At least one special character from the allowed set: `-().&@?'#,/;+`
- **No Ambiguous Characters** – Only letters, digits, and allowed symbols are used to avoid confusion.

These criteria ensure each password is strong enough to resist brute-force and dictionary attacks.


## Security Considerations

### Important Notes

- **Local Storage Only** – The matrix is saved to a plain text file on your machine. It is not transmitted over the internet.
- **Encryption Recommended** – For maximum security, store `password_matrix.txt` on an encrypted volume or use disk encryption (e.g., BitLocker, FileVault, LUKS).
- **No Master Password** – This tool eliminates the need for a master password by using coordinates. However, protect access to the saved matrix file as it contains all passwords.
- **Memory-Based** – You can choose not to save the matrix and regenerate it each time (by modifying the script to skip the save step). This adds security but requires you to remember the exact matrix dimensions used.
<img width="364" height="158" alt="image" src="https://github.com/user-attachments/assets/88b98fab-42e3-4ac6-9603-9f1ca83c690a" />


## Best Practices

- Change your coordinates regularly (e.g., monthly).
- Never share your matrix file or coordinates.
- Use a trusted, secure environment when generating or viewing passwords.


## File Structure

    password-matrix-generator/
    │
    ├── password_matrix.py       # Main Python script
    ├── password_matrix.txt      # Generated output (created after first run)
    ├── README.md                # This file
    └── LICENSE                  # License information

### Example Walkthrough
Scenario: Alice wants to generate a 4×6 password matrix.

1. Run the script:

       $ python password_matrix.py

2. Input dimensions:
   
         Enter the number of rows: 4
         Enter the number of columns: 6

4. Matrix displayed:

       passwork Matrice :
       Vg5t&9zY uE8#sA2?w XpL4@mR7!q ...
       ...
    
5. Save file created: password_matrix.txt now contains the matrix.

6. Retrieve password:

       Enter the row number (starting at 0): 2
       Enter the column number (starting at 0): 5
       Password at position (2, 5): jK9#mN4$pL6

## Example Walkthrough

Scenario: Alice now remembers her coordinates (2,5) as "M25" and uses the strong password `jK9#mN4$pL6` for her password manager's master key.


## Limitations & Future Improvements

### Current Limitations
- **Plain Text Output** – The matrix is saved unencrypted.
- **No Password Hashing** – Passwords are generated and stored as-is.
- **No GUI** – Command-line interface only.

### Planned Improvements
- Add encryption option for saved matrix (AES-256).
- Implement a hashing mechanism to avoid storing passwords directly.
- Add GUI version for non-technical users.
- Support for exporting to encrypted formats (e.g., KeePass XML).
- Add configuration file to customize password length and allowed symbols.


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements, bug fixes, or documentation improvements.

## Contact

For questions or feedback, please open an issue on GitHub or contact the project maintainer.

- Website: [www.cybersearchlab.com](http://www.cybersearchlab.com)
- Email: [ulrich.ngueyep@cybersearchlab.com](mailto:ulrich.ngueyep@cybersearchlab.com)
- Phone: +237 694 556 542

---
