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
📦frontend
 ┣ 📂app
 ┃ ┣ 📜favicon.ico
 ┃ ┣ 📜globals.css
 ┃ ┣ 📜layout.js
 ┃ ┗ 📜page.js
 ┣ 📂public
 ┃ ┣ 📜next.svg
 ┃ ┗ 📜vercel.svg
 ┣ 📜.eslintrc.json
 ┣ 📜.gitignore
 ┣ 📜README.md
 ┣ 📜jsconfig.json
 ┣ 📜next.config.js
 ┣ 📜package-lock.json
 ┣ 📜package.json
 ┣ 📜postcss.config.js
 ┗ 📜tailwind.config.js
📦backend
 ┣ 📂server
 ┃ ┣ 📂server
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜asgi.py
 ┃ ┃ ┣ 📜settings.py
 ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┗ 📜wsgi.py
 ┃ ┃ 📂website
 ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📂templates
 ┃ ┃ ┃ ┣ 📂website
 ┃ ┃ ┃ ┃ ┣ 📜contact.html
 ┃ ┃ ┃ ┃ ┣ 📜index.html
 ┃ ┃ ┃ ┃ ┣ 📜listings.html
 ┃ ┃ ┃ ┃ ┣ 📜newfoundland_cover.jpg
 ┃ ┃ ┃ ┃ ┣ 📜resources.html
 ┃ ┃ ┃ ┃ ┣ 📜scripts.js
 ┃ ┃ ┃ ┃ ┣ 📜styles.css
 ┃ ┃ ┃ ┃ ┗ 📜submit.html
 ┃ ┃ ┃ ┗ 📜base.html
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┣ 📜tests.py
 ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┗ 📜views.py
 ┃ ┃ 📜.DS_Store
 ┃ ┃ 📜manage.py
 ┃ ┃ 📜requirements.txt
 ┣ 📜.gitignore
📦document
 ┣ 📜.DS_Store
 ┣ 📜LostInNL(v0.1).pdf
 ┣ 📜LostInNL(v1.0).pdf
 ┗ 📜sys-arch.jpg
📜CONTRIBUTING.MD
📜LICENSE
📜readme.md
```
