📊 CSV Dashboard Customizer
A Python-based Streamlit web app that allows users to upload any CSV file, automatically clean the data, and generate custom interactive visualizations using Plotly. Ideal for quick data analysis and visual storytelling without writing any code!

🔧 Features
✅ CSV Upload: Upload any .csv file and view the raw and cleaned dataset.

🧹 Data Cleaning:

Removes completely empty rows/columns

Strips column name whitespaces

Removes duplicate rows

Detects and removes numeric outliers using Z-score

📈 Graph Customization:

Choose chart type: Line, Bar, Scatter, or Pie

Pick any two columns as X and Y axes

Add a custom graph title

📥 Download Option: Export the cleaned data as a CSV file.

📁 Project Structure
graphql
Copy
Edit
📦csv_dashboard_customizer/
├── app.py                 # Main Streamlit web app
├── data_cleaner.py        # Data cleaning logic
├── graph_generator.py     # Plot creation logic using Plotly
├── utils.py               # Utility function for outlier removal
├── requirements.txt       # Python dependencies (optional)
└── *.csv                  # Sample CSV files for testing
🛠️ How It Works
Step-by-Step
Launch the App

bash
Copy
Edit
streamlit run app.py
Upload a CSV

Use the upload widget to load any CSV file.

View the raw data.

Cleaned Output

Automatically processes the file to clean and prepare it for visualization.

Customize Plot

Select:

X-axis and Y-axis columns

Chart type

Title for your graph

Click Generate Graph to visualize the data.

Export Cleaned Data

Download the cleaned version of your dataset.

📚 Libraries Used
Library	Purpose
streamlit	Web UI framework for fast dashboard creation
pandas	CSV file handling, data manipulation
numpy	Numeric processing (for outlier detection)
plotly.express	Interactive graph generation
matplotlib	(Imported but not used - optional)
scipy.stats	Z-score calculation for outlier removal

📉 Outlier Removal Logic
Outliers are removed using Z-score with a default threshold of 3:

python
Copy
Edit
from scipy.stats import zscore
z_scores = np.abs(zscore(numeric_columns))
filtered_df = df[(z_scores < 3).all(axis=1)]
This ensures more accurate visualizations and analysis.

💡 Example Use Cases
Quick visualization of student performance or salary datasets

Cleaning messy CSV files before exporting

Rapid exploratory data analysis (EDA) with just a few clicks

📝 To-Do / Future Improvements
Add support for multi-column plotting

Enable filtering and sorting in the dashboard

Include non-numeric data encoding for more flexible plotting

📄 License
Open-source project for personal and academic use.
