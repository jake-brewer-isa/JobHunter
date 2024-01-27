# LinkedIn Automation Project

This README provides clear instructions for the initial setup of your project, including how to use the `setup.bat` script, how to work within the Poetry environment, and additional notes for development. This should guide new users or collaborators on your project through the necessary steps to get started.

# Project Setup Instructions

To set up and run this project on a new machine, follow these steps:

1. **Clone the repository to your local machine.**

2. **Install Poetry:**
   - Poetry is a tool for dependency management and packaging in Python. 
   - To install Poetry, follow the instructions on the [official Poetry website](https://python-poetry.org/docs/).

3. **Install Dependencies:**
   - Once Poetry is installed, navigate to the project directory and run the following command to install the project dependencies:
     ```
     poetry install
     ```

4. **Activate the Virtual Environment:**
   - To activate the Poetry-created virtual environment, run:
     ```
     poetry shell
     ```

5. **Environment Variables:**
   - Set the following environment variables:
     - `LINKEDIN_USERNAME`: Your LinkedIn username.
     - `LINKEDIN_PASSWORD`: Your LinkedIn password.

## Running the Code
To run the code, execute the `main.py` script in the root directory.



## Initial Setup

To set up the project environment and dependencies, follow these steps:

1. **Install Poetry**:
   Ensure that [Poetry](https://python-poetry.org/docs/) is installed on your system.

2. **Run the Setup Script**:
   Execute the `setup.bat` script located in the project root. This script will install all necessary Python dependencies, download the correct version of ChromeDriver, and activate the virtual environment.

   ```bash
   ./setup.bat
