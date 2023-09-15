# Contribution Guidelines for Newfoundland Missing Persons App

Thank you for your interest in contributing to the Newfoundland Missing Persons App! This document provides guidelines and instructions to ensure a smooth contribution process.

## Code of Conduct

Always maintain respect and understanding towards other contributors. Open source is about collaboration, and we want to foster a welcoming and inclusive environment.

## Getting Started

1. **Fork the Repository:** Start by forking the repository on GitHub. This allows you to have your own version of the repository to work with.

2. **Clone Your Fork Locally:**
```
git clone https://github.com/PrinceDisant/LostInNL.git
```

3. **Set Upstream Remote:** This helps to sync your fork with the original repository.
```
git remote add upstream https://github.com/PrinceDisant/LostInNL.git
```

4. **Sync and Update Your Fork:** Before you start working, always pull the latest changes from the main repository to avoid conflicts later.
```
git pull upstream main
```

5. **Create a New Branch:** Always create a new branch for your changes.
```
git checkout -b [branch-name]
```
Use meaningful branch names like `feature/add-search` or `fix/header-bug`.

## Development Guidelines

- **Code Style:** Adhere to the coding style and standards used throughout the project.
- **Commit Messages:** Write clear and concise commit messages describing the changes.
- **Atomic Commits:** Make small, focused commits. This makes it easier to review and track changes.
- **Update & Sync:** Regularly sync your branch with the main repository to get the latest updates.

## Submitting Changes

1. **Push Changes to Your Fork:**
```
git push origin [branch-name]
```

2. **Open a Pull Request (PR):** Go to your fork on GitHub and create a PR against the `development` branch of the original repository.

3. **Describe Your Changes:** In the PR, explain the changes, why you made them, and any other relevant details.

4. **Wait for Review:** Maintainers will review your PR. Address any feedback or changes they request.

## Staying Updated

Regularly fetch and merge changes from the main repository to stay updated:

```
git pull upstream main
git push origin main
```

## Asking Questions

If you're unsure about something, open an issue in the main repository or reach out to the maintainers. It's always better to clarify doubts early on.

## Conclusion

Thank you for considering contributing to the Newfoundland Missing Persons App. Your contributions, big or small, significantly impact the community and further the project's mission.