# Contributing to Zentri AI

We are thrilled that you're interested in contributing to Zentri AI! This guide will help you get started.

## How Can You Contribute?

There are many ways you can contribute to Zentri AI:

1. **Reporting Bugs**: Found a bug? Open an issue with details about the problem, steps to reproduce it, and suggestions for fixing it.
2. **Proposing Features**: Have an idea for an improvement? Let us know by opening a feature request issue.
3. **Improving Documentation**: Help us improve our documentation, including this guide, the README, or our code comments.
4. **Contributing Code**: Submit pull requests for new features, bug fixes, or optimizations.

## Getting Started

### Prerequisites

Before contributing, ensure you have the following installed:

- Python 3.9 or higher
- pip (Python package manager)
- Git

### Fork the Repository

1. Fork the repository on GitHub.
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/zentri-ai.git
   ```
3. Set the original repository as the upstream remote:
   ```bash
   git remote add upstream https://github.com/zentri-ai/zentri-ai.git
   ```

### Set Up the Environment

1. Navigate to the project directory:
   ```bash
   cd zentri-ai
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Making Changes

1. Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Add a meaningful commit message"
   ```
3. Push your changes to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

### Submitting a Pull Request

1. Navigate to your fork on GitHub and click the **New Pull Request** button.
2. Ensure your branch is up-to-date with the upstream `main` branch:
   ```bash
   git fetch upstream
   git merge upstream/main
   ```
3. Resolve any merge conflicts, then push your changes.
4. Add a descriptive title and summary for your pull request.
5. Submit your pull request and engage in the review process.

## Code of Conduct

Please read and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and collaborative environment for everyone.

## Style Guide

- **Python Code**: Follow [PEP 8](https://peps.python.org/pep-0008/) standards.
- **Commit Messages**: Write clear, concise, and descriptive commit messages.
- **Testing**: Ensure all new code is covered by unit tests.

## Feedback and Support

For questions, join our community on [Discord](#) or reach out via [email](mailto:support@zentri.ai).

---

**Thank you for helping us build Zentri AI!**
