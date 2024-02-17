# Project Name

A brief description of what the project does.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/username/project.git
   cd project
   poetry install
   ```

2. Usage:

    ```bash
    poetry shell
    python app.py
    ```
3. Contributing:

Contributions are welcome! Please see the Contributing Guidelines.

4. License:

This project is licensed under the MIT License.


### Python project checklist

[x] 1. Source code in separate folder
[x] 2. Tests code in test folder
[X] 3. README file wich contains usefull information
[ ] 4. Code documentation in docs folder
[ ] 5. Makefile :
    - for setup and activate env using poetry  
        - poetry env use python3.9  # creates venv
        - poetry shell  # activate venv
        - poetry add package_name  # adds dependency
        - poetry install  # install dependencies in venv
        - simply type exit or press Ctrl + D.  # deactivates venv


    - install dependencies from requirements.txt
    - run tests
    - run coverage
    - black - formating
    - pylint code quality and error check
    - Dockerfile to dockerize app
    - Run docker container locally
    - Push docker container
    - create docs
    - cleanup 
[ ] 6. How to contribute md file
[ ] 7. Automate tests and formarating, continerization and push
