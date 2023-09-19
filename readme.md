# Newfoundland Missing Persons App

A dedicated platform to store and disseminate information about individuals who go missing in Newfoundland, offering supplementary features to assist in the search and awareness efforts.

## Table of Contents

- [Project Overview](#project-overview)
- [Setup & Installation](#setup--installation)
- [Features](#features)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Overview

Every year, numerous individuals go missing in Newfoundland. The primary objective of this application is to serve as a central hub where information about these individuals can be stored, accessed, and disseminated; assisting in the search and creating awareness in the community.

## Setup & Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/PrinceDisant/LostInNL.git
    ```

2. Navigate to the project directory and set up the virtual environment (if necessary):

    ```bash
    cd LostInNL
    source virt/bin/activate  # For Unix-based systems
    ```

3. Navigate to the server directory and install the required dependencies:

    ```bash
    cd server
    pip install -r requirements.txt
    ```

4. Provide additional setup steps, such as database configurations, environment variable setup, etc.

5. Run the application:

    ```bash
    python manage.py runserver
    ```

## Features

- **Central Repository**: Store detailed information about missing individuals.
- **Search Functionality**: Search for individuals based on various criteria.
- Additional features you plan to implement.

## Contribution Guidelines

We welcome contributions! If you're interested in contributing, please read our [Contribution Guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the BSD 3-Clause License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thank any collaborators, third-party resources/libraries, or others who have influenced the project.

---

## Directory structure

```bash
/LostInNL/
|-- CONTRIBUTING.MD
|-- LICENSE
|-- readme.md
|-- /server/
| |-- manage.py
| |-- requirements.txt
| |-- /website/
| | |-- init.py
| | |-- admin.py
| | |-- apps.py
| | |-- models.py
| | |-- urls.py
| | |-- views.py
| | |-- /templates/
| | | |-- base.html
| | | |-- /website/
| | | | |-- contact.html
| | | | |-- index.html
| | | | |-- listings.html
| | | | |-- resources.html
| | | | |-- submit.html
| | | | |-- styles.css
| | | | |-- scripts.js
| | | | |-- newfoundland_cover.jpg
|-- /document/
|-- .gitignore
```
