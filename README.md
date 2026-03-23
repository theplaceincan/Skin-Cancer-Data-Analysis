# Skin Cancer Data Analysis

This project analyzes a skin lesion metadata dataset to explore relationships between clinical features and diagnostic outcomes.

## Technologies
- Python
- Pandas
- NumPy

## Dataset
The dataset contains patient and lesion metadata including:
- Age
- Gender
- Lesion characteristics (itch, bleed, elevation, etc.)
- Diagnostic labels

## Analysis Performed
- Data cleaning and preprocessing
- Grouped statistical analysis by diagnostic class
- Correlation analysis between clinical features

## Example Insights
- Certain lesion features (e.g., bleed, elevation) show higher prevalence in specific diagnostic groups
- Age and lesion characteristics demonstrate measurable correlations with diagnostic outcomes

## How to Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/analysis.py