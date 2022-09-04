import sys
take_after_taxes = 0.68


def salary_calculator():

    hourly_wage = int(input("What is your hourly wage? "))
    tax_salary = input("Do you want (pre) or (post) tax salary? ")
    frequency_salary = input("Do you want (weekly), (biweekly), (monthly), or (annual) salary calculated? ")

# Pre-Tax Salary (weekly, biweekly, monthly, annual)
    if tax_salary.lower() == 'pre' and frequency_salary.lower() =='weekly':
        weekly_pre_tax_wage = hourly_wage * 40
        return f"Your Weekly Pre-Taxed Wage is: ${round(weekly_pre_tax_wage)}"
    elif tax_salary.lower() == 'pre' and frequency_salary.lower() == 'biweekly':
        bi_weekly_pre_tax_wage = hourly_wage * 80
        return f"Your Bi-Weekly Pre-Taxed Wage is: ${round(bi_weekly_pre_tax_wage)}"
    elif tax_salary.lower() == 'pre' and frequency_salary.lower() == 'monthly':
        monthly_pre_tax_wage = hourly_wage * 173.3
        return f"Your Monthly Pre-Taxed Wage is: ${round(monthly_pre_tax_wage)}"
    elif tax_salary.lower() == 'pre' and frequency_salary.lower() == 'annual':
        annual_pre_tax_wage = hourly_wage * 2080
        return f"Your Annual Pre-Taxed Wage is: ${round(annual_pre_tax_wage)}"

# Post Tax Salary (weekly, biweekly, monthly, annual)
    elif tax_salary.lower() == 'post' and frequency_salary.lower() == 'weekly':
        weekly_pre_tax_wage = hourly_wage * 40
        weekly_post_tax_wage = weekly_pre_tax_wage * take_after_taxes
        return f"Your Weekly Post-Taxed Wage is: ${round(weekly_post_tax_wage)}"
    elif tax_salary.lower() == 'post' and frequency_salary.lower() == 'biweekly':
        bi_weekly_pre_tax_wage = hourly_wage * 80
        bi_weekly_post_tax_wage = bi_weekly_pre_tax_wage * take_after_taxes
        return f"Your Bi-Weekly Post-Taxed Wage is: ${round(bi_weekly_post_tax_wage)}"
    elif tax_salary.lower() == 'post' and frequency_salary.lower() == 'monthly':
        monthly_pre_tax_wage = hourly_wage * 173.3
        monthly_post_tax_wage = monthly_pre_tax_wage * take_after_taxes
        return f"Your Monthly Post-Taxed Wage is: ${round(monthly_post_tax_wage)}"
    elif tax_salary.lower() == 'post' and frequency_salary.lower() == 'annual':
        annual_pre_tax_wage = hourly_wage * 2080
        annual_post_tax_wage = annual_pre_tax_wage * take_after_taxes
        return f"Your Annual Post-Taxed Wage is: ${round(annual_post_tax_wage)}"
        
    else:
        return "invalid entry"


def mortgage_calculator():
    house_price = int(input("What is the House Price? "))
    down_payment = float(input("What percent Down Payment will you put down? (Ex: 20%, enter 0.2) "))
    down_payment_total = house_price * down_payment
    loan_amount = house_price - down_payment_total
    annual_interest_rate = float(input("What is the Annual Interest Rate of the loan? "))
    life_of_loan = int(input("What is the loan term (in years) "))
    payments_per_year = 12
    periodic_interest_rate = annual_interest_rate / payments_per_year
    payments_per_period = (periodic_interest_rate * (1 + periodic_interest_rate) ** (life_of_loan * payments_per_year))\
        / ((1 + periodic_interest_rate) ** (life_of_loan * payments_per_year) - 1) * loan_amount
    sum_of_payments = payments_per_period * payments_per_year * life_of_loan
    interest_cost = sum_of_payments - loan_amount
    return down_payment_total, loan_amount, payments_per_period, sum_of_payments, interest_cost
