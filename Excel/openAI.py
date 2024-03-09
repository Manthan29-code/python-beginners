import pandas as pd

# Your data
data = {
    'Credit Card Company Name': ['SBI Card', 'HDFC Bank', 'ICICI Bank', 'Axis Bank', 'Citibank', 'Standard Chartered',
                                  'Kotak Mahindra Bank', 'Bank of Baroda', 'IndusInd Bank', 'Yes Bank', 'American Express',
                                    'Punjab National Bank', 'Canara Bank', 'RBL Bank', 'Union Bank of India', 'Federal Bank', 
                                    'IDBI Bank', 'DBS Bank', 'Karur Vysya Bank', 'Dhanlaxmi Bank'],
    'Active Users': [1200000, 1000000, 900000, 500000, 700000, 600000, 400000, 350000, 300000, 150000, 200000, 250000, 180000, 
                     120000, 130000, 90000, 80000, 60000, 40000, 25000],
    'Market Share (%)': [20, 16.67, 15, 8.33, 11.67, 10, 6.67, 5.83, 5, 2.5, 3.33, 4.17, 3, 2, 2.17, 1.5, 1.33, 1, 0.67, 0.42]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Sort the DataFrame based on Market Share in descending order
df = df.sort_values(by='Market Share (%)', ascending=False)

# Write the DataFrame to an Excel file
df.to_excel('credit_card_data.xlsx', index=False)