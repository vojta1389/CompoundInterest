import pandas as pd

def calculate_compound_interest(principal, rate, periods, monthly_deposit):
    # calculate compound interest
    total_savings = 0
    total_principal = 0
    df = pd.DataFrame(columns=['Year', 'Invested', 'Current Value'])

    for i in range(periods):
        if i == 0:
            savings = principal
        else:
            interest = (savings + total_savings) * (rate/12)
            total_savings += interest
            total_savings += monthly_deposit
            total_principal += monthly_deposit
            savings = total_savings
            year = (i // 12) + 1
            df = pd.concat([df, pd.DataFrame({'Year': str(year) + ".", 'Month': [round(i)], 'Invested': [total_principal], 'Current Value': [savings]})])

    df.to_csv('compoundInterest.csv')
    return total_savings
