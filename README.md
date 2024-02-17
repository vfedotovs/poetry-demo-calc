# Project Name

A brief description of what the project does.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

Clone the repository:

   ```bash
   git clone https://github.com/username/project.git
   cd project
   poetry install
   ```

## Usage:

    ```bash
    poetry shell
    python app.py
    ```
## Contributing:

   Contributions are welcome! Please see the Contributing Guidelines.

## License:

   This project is licensed under the MIT License.


### Python project checklist

- [X] Source code in separate folder  
- [x] Tests code in test folder
- [x] README file wich contains usefull information
- [ ] Code documentation in docs folder
- [ ] Makefile for more productive work:
    - [x] Target for setup and activate env using poetry  
        - poetry env use python3.9  # creates venv
        - poetry shell  # activate venv
        - poetry add package_name  # adds dependency
        - poetry install  # install dependencies in venv
        - simply type exit or press Ctrl + D.  # deactivates venv
    - [x] Target for running tests with pytest
    - [x] Target for running test coverage with pytest
    - [x] Target for code formating using black
    - [x] Target for linting code with pylint to get code quality assesment and error check
    - [ ] Target for building application from Dockerfile to containerize app
    - [ ] Target for running container locally
    - [ ] Traget for pushing container image to dockerhub
    - [ ] Target for post deployment tests Push docker container
    - [ ] Target for creating docs
    - [x] Target for cleanup after tests
- [ ] Contribute.md file for guidelines
- [ ] Github actions automation to trigger tests and formarating, continerization and push on commit
- [ ] Security to protect main branche that does not allow push to main branche without PR
