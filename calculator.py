import sys
import pandas as pd


class Calculator:


    def mortgage_calculations(self):

        seperator = "==============================================================================="
        
        # user input
        print(f"\n{seperator}")
        house_price = int(input("\nWhat is the House Price? "))
        down_payment = float(input("What percent Down Payment will you put down? (Ex: 20%, enter 0.2) "))
        annual_interest_rate = float(input("What is the Annual Interest Rate of the loan? (Ex: 5%, enter 0.05) "))
        life_of_loan = int(input("What is the loan term (in years) "))

        # calculations
        down_payment_total = house_price * down_payment
        loan_amount = house_price - down_payment_total
        payments_per_year = 12
        periodic_interest_rate = annual_interest_rate / payments_per_year
        payments_per_period = (periodic_interest_rate * (1 + periodic_interest_rate) ** (life_of_loan * payments_per_year))\
            / ((1 + periodic_interest_rate) ** (life_of_loan * payments_per_year) - 1) * loan_amount
        sum_of_payments = payments_per_period * payments_per_year * life_of_loan
        interest_cost = sum_of_payments - loan_amount
        property_tax = house_price * 0.0111
        property_insurance = house_price * 0.005532
        total_monthly_payments = payments_per_period + (property_tax / 12) + (property_insurance / 12)


        # print output
        print(f"\n{seperator}")
        print(f"\nTotal down payment : ${round(down_payment_total, 2)}")
        print(f"Total loan amount: ${round(loan_amount, 2)}")
        print(f"Total interest cost: ${round(interest_cost, 2)}")
        # print(f"Loan monthly payments: ${round(payments_per_period, 2)}")
        print(f"Total sum of payments: ${round(sum_of_payments, 2)}")
        
        print(f"\nAnnual property tax: ${round(property_tax, 2)}")
        print(f"Annual property insurance: ${round(property_insurance, 2)} \n")

        print(seperator)
        print(f"\nTotal monthly payments (Mortgage + Property Tax + Insurance + HOA): \n${round(total_monthly_payments, 2)}\n")
        print(seperator)

        return "\nEnd program"


app = Calculator()
app.mortgage_calculations()


