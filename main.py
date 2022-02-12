import pandas as pd

df = pd.read_csv("account_transactions.csv")
df = df.drop(["Account Number", "Transaction Type", "Balance"], axis=1)
df = df.sort_values(by="Transaction Date", ascending=False)
df = df[(df['Transaction Date'] >= '02/01/2022') & (df['Transaction Date'] <= '02/28/2022')]

bills_df = df[df["Transaction Description"].str.contains("TOGGLE|PROG UNIVERSAL")]
cc_df = df[df["Transaction Description"].str.contains(
    "WELLS FARGO|"
    "APPLECARD|"
    "CITI CARD|"
    "GenesisFS|"
    "TARGET CARD"
)]
loan_auto_df = df[df["Transaction Description"].str.contains("COLONIALTRANSFER")]
loan_student_df = df[df["Transaction Description"].str.contains(
    "FED LOAN|"
    "NELNET|"
    "FIRSTMARK|"
    "General Revenue|"
    "UAS"
)]
medical_df = df[df["Transaction Description"].str.contains("ONLINE VISIT PAY")]
mortgage_df = df[df["Transaction Description"].str.contains("Wimmer Brothers")]
utilities_df = df[df["Transaction Description"].str.contains("SPECTRUM|WE ENERGIES")]

misc_df = df[df["Transaction Description"].str.contains(
    "TOGGLE|"
    "PROG UNIVERSAL|"
    "WELLS FARGO|"
    "APPLECARD|"
    "CITI CARD|"
    "GenesisFS|"
    "TARGET CARD|"
    "COLONIALTRANSFER|"
    "FED LOAN|"
    "NELNET|"
    "FIRSTMARK|"
    "General Revenue|"
    "UAS|"
    "ONLINE VISIT PAY|"
    "Wimmer Brothers|"
    "SPECTRUM|"
    "WE ENERGIES") == False
]

bills_total = abs(round(bills_df["Transaction Amount"].sum(), 2))
cc_total = abs(round(cc_df["Transaction Amount"].sum(), 2))
loan_auto_total = abs(round(loan_auto_df["Transaction Amount"].sum(), 2))
loan_student_total = abs(round(loan_student_df["Transaction Amount"].sum(), 2))
medical_total = abs(round(medical_df["Transaction Amount"].sum(), 2))
mortgage_total = abs(round(mortgage_df["Transaction Amount"].sum(), 2))
utilities_total = abs(round(utilities_df["Transaction Amount"].sum(), 2))
misc_total = abs(round(misc_df['Transaction Amount'].sum(), 2))
gross_total = abs(bills_total + cc_total + loan_auto_total + loan_student_total + medical_total + mortgage_total + utilities_total)

bills_bdg = 562.10
cc_bdg = 236.78
loan_auto_bdg = 546.98
loan_student_bdg = 798.37
medical_bdg = 200.00
mortgage_bdg = 1048.50
utilities_bdg = 300.32
misc_bdg = 1280.00
gross_bdg = bills_bdg + cc_bdg + loan_auto_bdg + loan_student_bdg + medical_bdg + mortgage_bdg + utilities_bdg

print(df)
print('')
print('---')
print(f"Bills: ${bills_total}   Budget: ${bills_bdg}   Net: ${round(bills_bdg - bills_total, 2)}")
print(f"Credit: ${cc_total}   Budget: ${cc_bdg}   Net: ${round(cc_bdg - cc_total, 2)}")
print(f"Auto Loan: ${loan_auto_total}   Budget: ${loan_auto_bdg}   Net: ${round(loan_auto_bdg - loan_auto_total, 2)}")
print(f"Student Loans: ${loan_student_total}   Budget: ${loan_student_bdg}   Net: ${round(loan_student_bdg - loan_student_total, 2)}")
print(f"Medical: ${medical_total}   Budget: ${medical_bdg}   Net: ${round(medical_bdg - medical_total, 2)}")
print(f"Mortgage: ${mortgage_total}   Budget: ${mortgage_bdg}   Net: ${round(mortgage_bdg - mortgage_total, 2)}")
print(f"Utilities: ${utilities_total}   Budget: ${utilities_bdg}   Net: ${round(utilities_bdg - utilities_total, 2)}")
print('')
print('Misc budget to include Groceries($450.00) Shopping($150.00) Food($80.00) Fuel($100.00) and Savings($500.00)')
print(f"Misc Expenses: ${misc_total}   Budget: ${misc_bdg}   Net: ${round(misc_bdg - misc_total)}")
print('')
print("---")
print(f"Total: {round(gross_total, 2)}   Budget: ${gross_bdg}   Net: ${round(gross_bdg - (gross_total))}")