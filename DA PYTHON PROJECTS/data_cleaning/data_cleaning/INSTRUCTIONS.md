
# Instructions for Running the Jupyter Notebook

Follow these steps to use the provided Jupyter Notebook for exploring data cleaning techniques with visualisations.

## Prerequisites
Before you begin, ensure you have the following:
- Python 3.7 or later installed on your system.
- Jupyter Notebook installed as part of Anaconda or as a standalone package.
- Required Python libraries: pandas, matplotlib, seaborn.

## Requirements

####  Virtual Environment and Pandas Setup Notebook
Create a virtual environment to keep project dependencies separate. 
In your terminal, navigate to your project folder and type: python -m venv .venv
``` bash
python -m venv .venv
```

To activate it:
Windows: .venv\Scripts\activate
macOS/Linux: source .venv/bin/activate

Once activated, you’ll see the environment name in your terminal prompt.

Make sure you have the following Python libraries installed:
- pandas
- matplotlib
- seaborn

You can install these using pip:
```bash
pip install pandas matplotlib seaborn ipykernel 
```
To select the Kernel:
Click the kernel dropdown (top-right of the notebook) and select the virtual environment `.venv.`

## Steps to Run the Notebook

### 1. Download the Files
- Save the `Data_Cleaning_Techniques.ipynb` file to your local machine.
- If applicable, download the dataset used in the notebook and place it in the same directory as the notebook file.

### 2. Open the Notebook in Visual Studio Code
1. Open Visual Studio Code.
2. Ensure the Python extension is installed (search for it in the Extensions marketplace).
3. Open the `.ipynb` file in Visual Studio Code.

### 3. Select a Python Environment
1. Ensure you have selected a Python environment that has the required libraries installed.
2. If no environment is available, create one and install the prerequisites.

### 4. Run the Notebook
- Execute each cell in order by clicking the "Run" button or pressing `Shift + Enter`.
- Follow the step-by-step instructions within the notebook to apply data cleaning techniques and observe the visualisations.

## Additional Notes
- Ensure that the dataset paths within the notebook match the location of your dataset.
- If you encounter errors related to missing libraries, ensure they are installed in your Python environment.