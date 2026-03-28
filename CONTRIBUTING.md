# Contributing to Easy-password-manager

Thank you for your interest in contributing to **Passwork Matrice**! Here’s how you can help:

## Reporting Bugs

If you’ve found a bug, please open an issue on GitHub with the following details:
- **Steps to reproduce** the bug
- **Expected vs actual behavior**
- **Screenshots** (if applicable)
- **Environment** (Python version, OS)

## Suggesting Enhancements

If you have an idea for improving the project, feel free to open an issue with your suggestions. Be clear and specific about the enhancement you would like to see.

## How to Submit Code

If you want to contribute code, please follow these steps:
1. **Fork** the repository to your GitHub account.
2. **Clone** your forked repository to your local machine.(`git clone https://github.com/your-username/password-matrix-generator.git`).
3. Create a new branch for your changes (`git checkout -b feature-branch/your-feature-name`).
4. Make your changes and commit them with a clear message: (`git commit -m "feat: add encryption support for saved matrix"`).
5. Push your changes to your forked repository (`git push origin feature-branch/your-feature-name`).
6. Open a Pull Request (PR) on GitHub with a description of your changes.

## Coding Guidelines

- Please write clean, readable code.
- Follow the PEP 8 style guide for Python code.
- Add docstrings to functions and classes.
- Use type hints where possible.
- Keep commits atomic (one logical change per commit).
- Write meaningful, descriptive commit messages.

We welcome all contributions and appreciate your help to improve **Passwork Matrice**!

## Testing

Before submitting, please test your changes:
- Run the script with various matrix sizes (e.g., 3×3, 5×10).
- Verify that generated passwords meet all security criteria.
- Ensure the matrix saves correctly to password_matrix.txt.
- Check that password retrieval works with valid indices.

## Security Considerations

Since this project handles password generation:
- Never hardcode sensitive data (passwords, keys).
- Never submit password_matrix.txt files in pull requests.
- Be mindful of randomness quality – use Python's secrets module for cryptographic randomness.
- If adding encryption features, use well-established libraries (e.g., cryptography).

## Code of Conduct
Please be respectful and constructive in all interactions. We welcome contributors of all experience levels!

## License
By contributing, you agree that your contributions will be licensed under the MIT License.
