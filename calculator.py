import sys
from turtle import down
take_after_taxes = 0.68
seperator = "==============================================================================="


class Calculator:


    def mortgage_calculations(self):


        
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
        print(f"{seperator}\n")

        # return "\nEnd program"


    def salary_calculator(self):
        print(f"\n{seperator}\n")
        hourly_wage = int(input("What is your hourly wage? "))
        tax_salary = input("Do you want (pre) or (post) tax salary? ")
        frequency_salary = input("Do you want (weekly), (biweekly), (monthly), or (annual) salary calculated? ")
        print(f"\n{seperator}\n")
        

    # Pre-Tax Salary (weekly, biweekly, monthly, annual)
        if tax_salary.lower() == 'pre' and frequency_salary.lower() =='weekly':
            weekly_pre_tax_wage = hourly_wage * 40
            print(f"Your Weekly Pre-Taxed Wage is: ${round(weekly_pre_tax_wage, 2)}")
            print(f"\n{seperator}\n")
        elif tax_salary.lower() == 'pre' and frequency_salary.lower() == 'biweekly':
            bi_weekly_pre_tax_wage = hourly_wage * 80
            print(f"Your Bi-Weekly Pre-Taxed Wage is: ${round(bi_weekly_pre_tax_wage, 2)}")
            print(f"\n{seperator}\n")
        elif tax_salary.lower() == 'pre' and frequency_salary.lower() == 'monthly':
            monthly_pre_tax_wage = hourly_wage * 173.3333333333333
            print(f"Your Monthly Pre-Taxed Wage is: ${round(monthly_pre_tax_wage, 2)}")
            print(f"\n{seperator}\n")
        elif tax_salary.lower() == 'pre' and frequency_salary.lower() == 'annual':
            annual_pre_tax_wage = hourly_wage * 2080
            print(f"Your Annual Pre-Taxed Wage is: ${round(annual_pre_tax_wage, 2)}")
            print(f"\n{seperator}\n")

    # Post Tax Salary (weekly, biweekly, monthly, annual)
        elif tax_salary.lower() == 'post' and frequency_salary.lower() == 'weekly':
            weekly_pre_tax_wage = hourly_wage * 40
            weekly_post_tax_wage = weekly_pre_tax_wage * take_after_taxes
            print(f"Your Weekly Post-Taxed Wage is: ${round(weekly_post_tax_wage, 2)}")
            print(f"\n{seperator}\n")
        elif tax_salary.lower() == 'post' and frequency_salary.lower() == 'biweekly':
            bi_weekly_pre_tax_wage = hourly_wage * 80
            bi_weekly_post_tax_wage = bi_weekly_pre_tax_wage * take_after_taxes
            print(f"Your Bi-Weekly Post-Taxed Wage is: ${round(bi_weekly_post_tax_wage, 2)}")
            print(f"\n{seperator}\n")
        elif tax_salary.lower() == 'post' and frequency_salary.lower() == 'monthly':
            monthly_pre_tax_wage = hourly_wage * 173.3333333333333
            monthly_post_tax_wage = monthly_pre_tax_wage * take_after_taxes
            print(f"Your Monthly Post-Taxed Wage is: ${round(monthly_post_tax_wage, 2)}")
            print(f"\n{seperator}\n")
        elif tax_salary.lower() == 'post' and frequency_salary.lower() == 'annual':
            annual_pre_tax_wage = hourly_wage * 2080
            annual_post_tax_wage = annual_pre_tax_wage * take_after_taxes
            print(f"Your Annual Post-Taxed Wage is: ${round(annual_post_tax_wage, 2)}")
            print(f"\n{seperator}\n")
            
        else:
            print("invalid entry")
            print(f"\n{seperator}\n")


app = Calculator()
app.mortgage_calculations()
app.salary_calculator()


