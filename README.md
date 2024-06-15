# CSV Analyzer

CSV Analyzer is a Django-based web application that allows users to upload CSV files, performs data analysis using pandas and numpy, and displays the results and visualizations on the web interface.

## Features

- **File Upload**: Upload CSV files for analysis.
- **Data Processing**: 
  - Display the first few rows of the data.
  - Calculate summary statistics (mean, median, standard deviation) for numerical columns.
  - Identify and handle missing values.
- **Data Visualization**: Generate and display histograms for numerical columns.

## Technologies Used

- Django
- pandas
- numpy
- matplotlib
- seaborn

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/csv_analyzer.git
   cd csv_analyzer
2. **Create a virtual environment and activate it:**:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
3. **Install the dependencies from the requirements.txt file:**:

   ```bash
   pip install -r requirements.txt
4. **Apply Migrations**:

   ```bash
   python manage.py migrate
5.  **Run the Development Server**:

   ```bash
   python manage.py runserver

   Open your web browser and go to http://127.0.0.1:8000/ to use the application.
