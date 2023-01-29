import pandas as pd

def calculate_compound_interest(principal, rate, periods, monthly_deposit):
    # calculate compound interest
    savings = principal
    total_principal = principal
    df = pd.DataFrame(columns=['Year', 'Invested', 'Current Value'])

    for i in range(periods):
        interest = savings * (rate/12)
        savings += interest + monthly_deposit
        total_principal += monthly_deposit
        year = (i // 12) + 1
        df = pd.concat([df, pd.DataFrame({'Year': str(year) + ".", 'Month': [round(i)], 'Invested': [total_principal], 'Current Value': [savings]})])

    df.to_csv('compoundInterest.csv')
    return savings
