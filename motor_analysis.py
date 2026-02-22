"""
Motor Insurance Claim Frequency Risk Segmentation
Author: Nidhi Sharma
Description:
Exposure-adjusted claim frequency modelling and risk segmentation
using the freMTPL2 motor insurance dataset.
"""

import pandas as pd


# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    return df


# --------------------------------------------------
# 2. Portfolio-Level Frequency
# --------------------------------------------------

def compute_portfolio_frequency(df: pd.DataFrame) -> float:
    total_claims = df["ClaimNb"].sum()
    total_exposure = df["Exposure"].sum()
    return total_claims / total_exposure


# --------------------------------------------------
# 3. Age Band Segmentation
# --------------------------------------------------

def age_band_analysis(df: pd.DataFrame) -> pd.DataFrame:
    df["Age_Band"] = pd.cut(
        df["DrivAge"],
        bins=[17, 25, 35, 50, 100],
        labels=["18-25", "26-35", "36-50", "50+"]
    )

    summary = df.groupby("Age_Band").agg(
        Total_Claims=("ClaimNb", "sum"),
        Total_Exposure=("Exposure", "sum")
    )

    summary["Frequency"] = summary["Total_Claims"] / summary["Total_Exposure"]
    return summary


# --------------------------------------------------
# 4. Vehicle Age Segmentation
# --------------------------------------------------

def vehicle_age_analysis(df: pd.DataFrame) -> pd.DataFrame:
    df["Vehicle_Age_Band"] = pd.cut(
        df["VehAge"],
        bins=[-1, 2, 5, 100],
        labels=["0-2 years", "3-5 years", "5+ years"]
    )

    summary = df.groupby("Vehicle_Age_Band").agg(
        Total_Claims=("ClaimNb", "sum"),
        Total_Exposure=("Exposure", "sum")
    )

    summary["Frequency"] = summary["Total_Claims"] / summary["Total_Exposure"]
    return summary


# --------------------------------------------------
# 5. Bonus-Malus Segmentation
# --------------------------------------------------

def bonus_malus_analysis(df: pd.DataFrame) -> pd.DataFrame:
    df["BM_Band"] = pd.cut(
        df["BonusMalus"],
        bins=[0, 50, 60, 80, 200],
        labels=["Low (<=50)", "Medium (51-60)", "High (61-80)", "Very High (80+)"]
    )

    summary = df.groupby("BM_Band").agg(
        Total_Claims=("ClaimNb", "sum"),
        Total_Exposure=("Exposure", "sum")
    )

    summary["Frequency"] = summary["Total_Claims"] / summary["Total_Exposure"]
    return summary


# --------------------------------------------------
# 6. Export Results
# --------------------------------------------------

def export_to_excel(age_df, vehicle_df, bm_df):
    with pd.ExcelWriter("motor_summary.xlsx") as writer:
        age_df.to_excel(writer, sheet_name="Age_Band")
        vehicle_df.to_excel(writer, sheet_name="Vehicle_Age")
        bm_df.to_excel(writer, sheet_name="BM_Band")


# --------------------------------------------------
# Main Execution
# --------------------------------------------------

if __name__ == "__main__":
    df = load_data("data.csv")

    df["Claim_Frequency"] = df["ClaimNb"] / df["Exposure"]

    portfolio_freq = compute_portfolio_frequency(df)

    age_summary = age_band_analysis(df)
    vehicle_summary = vehicle_age_analysis(df)
    bm_summary = bonus_malus_analysis(df)

    export_to_excel(age_summary, vehicle_summary, bm_summary)

    print("Portfolio Claim Frequency:", round(portfolio_freq, 4))
    print("Analysis completed successfully.")