# Motor Insurance Claim Frequency Risk Segmentation

## Project Overview

This project analyses a motor insurance portfolio to compute exposure-adjusted claim frequency and identify key risk drivers.

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

## Future Improvements

- Poisson GLM frequency modelling
- Model validation
- Severity modelling extension