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
        monthly_property_tax = (house_price * 0.0111) / 12
        monthly_property_insurance = (house_price * 0.005532) / 12
        monthly_utility_cost = 4800.00 / 12
        total_monthly_payments = payments_per_period + monthly_property_tax + monthly_property_insurance + monthly_utility_cost


        # print output
        print(f"\n{seperator}")
        print(f"\nTotal down payment : ${round(down_payment_total, 2)}")
        print(f"Total loan amount: ${round(loan_amount, 2)}")
        print(f"Total interest cost: ${round(interest_cost, 2)}")
        print(f"Total sum of payments: ${round(sum_of_payments, 2)}")
        
        print(f"\nEstimated monthly property tax: ${round(monthly_property_tax, 2)}")
        print(f"Estimated monthly property insurance: ${round(monthly_property_insurance, 2)}")
        print(f"Estimated monthly utility cost: ${monthly_utility_cost}\n")

        print(seperator)
        print(f"\nLoan monthly payments: ${round(payments_per_period, 2)}")
        print(f"\nTotal monthly payments (Loan + Property Tax + Insurance + Utilities): \n${round(total_monthly_payments, 2)}\n")
        print(seperator)

        return "\nEnd program"


app = Calculator()
app.mortgage_calculations()


