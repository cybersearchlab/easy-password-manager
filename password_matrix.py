"""
=============================================================================================
Easy Passwork Manager – Password Matrix Generation Script
=============================================================================================

Author: Ngueyep Ulrich
Trigramme: UNG
Organization: CyberSearchLab
Profile: https://www.cybersearchlab.com
Date: 28/03/2026
Last Modified: 28/03/2026
License: MIT License

This script generates a secure password matrix based on user input and saves it to a file.
The matrix consists of randomly generated passwords following strict security standards. 

Generated passwords are used to facilitate secure password retrieval by remembering the 
coordinates (row, column) instead of the entire password.

---------------------------------------------------------------------------------------------
INPUTS
---------------------------------------------------------------------------------------------
User Inputs:
    - Number of rows (integer) for the password matrix.
    - Number of columns (integer) for the password matrix.
    - Row and column indices (integers, starting from 0) to retrieve a password from the matrix.

Expected Output:
    - A matrix of passwords saved to a file named `password_matrix.txt`.
    - The user can retrieve a password from the matrix using the specified row and column.

---------------------------------------------------------------------------------------------
OUTPUTS
---------------------------------------------------------------------------------------------
Saved to:
    - password_matrix.txt              : Contains the generated password matrix (plain text).

Files generated:
    - password_matrix.txt              : A file with the generated passwords saved in a matrix form.

---------------------------------------------------------------------------------------------
SECURITY CONSIDERATIONS
---------------------------------------------------------------------------------------------
• Passwords are generated using cryptographically secure random choices (`secrets.choice()`).
• Passwords must meet the following security requirements:
    - Length between 12 and 50 characters.
    - Contains at least one uppercase letter, one lowercase letter, one digit, and one special character.
• This script does not store any passwords in a hashed format. The passwords are stored as plain text in the matrix.
• It is recommended to store the password matrix in an encrypted volume or use disk encryption for maximum security.

---------------------------------------------------------------------------------------------
METHODOLOGY
---------------------------------------------------------------------------------------------
• Passwords are generated randomly with a secure method, ensuring cryptographic strength.
• The password matrix is displayed on the console for the user to view.
• The matrix is saved to a text file, where each line corresponds to a row of passwords.

---------------------------------------------------------------------------------------------
REPRODUCIBILITY
---------------------------------------------------------------------------------------------
• Fixed random seed for consistent behavior.
• Deterministic password generation using a predefined set of allowed characters.
• No external dependencies (other than Python standard libraries) are needed.

=============================================================================================
"""

import random
import string
import re
import secrets

# Allowed symbols - EXCLUDING spaces to avoid display issues
symbols_allowed = "-().&@?'#,/;+"

# Function to generate a valid password according to the specified security criteria
def generate_password(length=30):
    """
    Generates a password that meets the following security requirements:
    - Length between 12 and 50 characters.
    - Contains at least one uppercase letter, one lowercase letter, one digit, and one special character.
    
    This function uses cryptographically secure random choices for password generation.

    Args:
        length (int): The length of the generated password (default is 30).

    Returns:
        str: A valid password string that satisfies the defined security criteria.

    """
    # Generating password securely using secrets
    characters = string.ascii_letters + string.digits + symbols_allowed
    
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        
        # Ensure the generated password follows the criteria
        if (12 <= len(password) <= 50 and 
            re.search(r"\d", password) and         # Must contain at least one digit
            re.search(r"[a-z]", password) and       # Must contain at least one lowercase letter
            re.search(r"[A-Z]", password) and       # Must contain at least one uppercase letter
            re.search(r"[" + re.escape(symbols_allowed) + r"]", password)):  # Must contain at least one special character
            return password

# Function to create a password matrix of given rows and columns
def create_password_matrix(rows, cols):
    """
    Creates a matrix of passwords by generating a password for each cell.

    Args:
        rows (int): The number of rows in the matrix.
        cols (int): The number of columns in the matrix.

    Returns:
        list: A matrix (list of lists) containing the generated passwords.

    """
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            password = generate_password()
            row.append(password)
            # Optional: Show progress for large matrices
            print(f"Generating password [{i+1},{j+1}]...", end="\r")
        matrix.append(row)
    print("\n✓ Password matrix generated successfully!   ")  # Clear the progress line
    return matrix

# Function to display the password matrix with indices for clarity
def display_matrix(matrix):
    """
    Displays the password matrix on the console with row and column indices.

    Args:
        matrix (list): The matrix containing the passwords to be displayed.

    """
    if not matrix:
        return
    
    # Calculate column widths for better alignment
    col_widths = []
    for col in range(len(matrix[0])):
        max_width = max(len(matrix[row][col]) for row in range(len(matrix)))
        col_widths.append(max_width + 2)  # Add padding
    
    # Print header with column indices
    header = "Row\\Col"
    for col in range(len(matrix[0])):
        header += f" | {col:^{col_widths[col]-2}}"
    print("\n" + header)
    print("-" * len(header))
    
    # Print each row with row index
    for row_idx, row in enumerate(matrix):
        row_str = f"  {row_idx:2d}  "
        for col_idx, password in enumerate(row):
            row_str += f"| {password:<{col_widths[col_idx]-2}} "
        print(row_str)
    
    # Simple alternative display (uncomment if you prefer simpler view)
    # print("\nPassword Matrix (simple view):")
    # for i, row in enumerate(matrix):
    #     print(f"Row {i}:", " | ".join(row))

# Function to retrieve a password from the matrix based on row and column indices
def get_password_from_matrix(matrix, row, col):
    """
    Retrieves a password from the matrix given its row and column indices.

    Args:
        matrix (list): The matrix containing the passwords.
        row (int): The row index for the password.
        col (int): The column index for the password.

    Returns:
        str: The password found at the specified indices.

    """
    try:
        return matrix[row][col]
    except IndexError:
        return None

# Function to save the password matrix to a file with clear formatting
def save_matrix_to_file(matrix, filename="password_matrix.txt"):
    """
    Saves the password matrix to a text file with clear formatting.

    Args:
        matrix (list): The matrix containing the passwords to be saved.
        filename (str): The name of the file where the matrix will be saved. Default is "password_matrix.txt".

    """
    with open(filename, 'w') as f:
        # Write header with matrix dimensions
        f.write(f"Password Matrix - {len(matrix)} rows × {len(matrix[0])} columns\n")
        f.write("=" * 50 + "\n\n")
        
        # Write each row with clear separation
        for i, row in enumerate(matrix):
            f.write(f"Row {i:2d}: ")
            f.write(" | ".join(row))
            f.write("\n")
        
        f.write("\n" + "=" * 50 + "\n")
        f.write("Usage: Remember coordinates (row, column) to retrieve your password.\n")
    
    print(f"\n✓ Matrix saved to '{filename}'")

# Function to verify matrix integrity
def verify_matrix_index(matrix, row, col):
    """
    Verifies if the given indices are within the matrix bounds.

    Args:
        matrix (list): The password matrix.
        row (int): Row index to verify.
        col (int): Column index to verify.

    Returns:
        bool: True if indices are valid, False otherwise.
    """
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        return True
    return False

# Main function
if __name__ == "__main__":
    print("\n" + "="*60)
    print("EASY PASSWORK MANAGER - Password Matrix Generator")
    print("="*60 + "\n")
    
    # Request user input for the matrix size
    try:
        rows = int(input("Enter the number of rows for the matrix: "))
        cols = int(input("Enter the number of columns for the matrix: "))
        
        if rows <= 0 or cols <= 0:
            print("Error: Rows and columns must be positive integers.")
            exit(1)
            
    except ValueError:
        print("Error: Please enter valid integers.")
        exit(1)
    
    # Generate the password matrix
    print("\n⏳ Generating password matrix...")
    matrix = create_password_matrix(rows, cols)
    
    # Display the matrix with indices
    display_matrix(matrix)
    
    # Save the matrix to a file
    save_matrix_to_file(matrix)
    
    # Request user input for row and column to retrieve a password
    print("\n" + "-"*60)
    print("🔍 RETRIEVE A PASSWORD")
    print("-"*60)
    
    while True:
        try:
            row_index = int(input("Enter the row number (starting at 0): "))
            col_index = int(input("Enter the column number (starting at 0): "))
            
            if verify_matrix_index(matrix, row_index, col_index):
                break
            else:
                print(f"Invalid indices! Please enter row between 0-{len(matrix)-1} and column between 0-{len(matrix[0])-1}")
        except ValueError:
            print("Please enter valid integers.")
    
    # Retrieve and display the password at the specified position
    password = get_password_from_matrix(matrix, row_index, col_index)
    print(f"\n Password at position ({row_index}, {col_index}):")
    print(f"   {password}")
    print("\n💡 Tip: Remember your coordinates instead of the full password!")
    
    # Optional: Show all coordinates for reference
    print("\n All available coordinates:")
    print(f"   Rows: 0 to {len(matrix)-1}")
    print(f"   Columns: 0 to {len(matrix[0])-1}")
