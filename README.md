# Motor Insurance Claim Frequency Risk Segmentation

## Project Overview

This project analyses a motor insurance portfolio to compute exposure-adjusted claim frequency and identify key risk drivers.

## Project Structure

```
motor-insurance-frequency-analysis/
│
├── data/                # Dataset location (not included in repo)
│   └── README.md
│
├── notebooks/           # Exploratory analysis notebook
│   └── motor_insurance_frequency_analysis.ipynb
│
├── motor_analysis.py    # Script version of analysis
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset

- freMTPL2 Motor Insurance Dataset (public dataset)
- 678,013 policies
- 36,102 claims
- 358,499 exposure years

Claim Frequency = Total Claims / Total Exposure

## Methodology

- Portfolio-level frequency calculation
- Driver Age Band segmentation
- Vehicle Age Band segmentation
- Bonus-Malus risk band analysis

## Key Insights

- Young drivers (18–25) exhibit materially higher claim frequency.
- Newer vehicles show elevated frequency.
- Claim frequency increases monotonically across Bonus-Malus bands.

## Tools Used

- Python (Pandas, Matplotlib)
- Jupyter Notebook
- Excel (dashboard)

## How to Run This Project

### 1. Clone the repository
```bash
git clone https://github.com/Nidhi-analysis/motor-insurance-frequency-analysis.git
cd motor-insurance-frequency-analysis

## Future Improvements

- Poisson GLM frequency modelling
- Model validation
- Severity modelling extension
