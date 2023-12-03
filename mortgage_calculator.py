# 参考资料
# 知乎 https://zhuanlan.zhihu.com/p/617706691
# 李永乐 https://www.youtube.com/watch?v=T6FBfNpiBYw&t=431s
# The next three websites are for verification of correctness
# https://www.mortgagecalculator.org/calculators/what-if-i-pay-more-calculator.php#top
# https://www.bankrate.com/mortgages/additional-mortgage-payment-calculator/
# https://www.calculator.net/mortgage-payoff-calculator.html?cloanamount=490%2C000&cloanterm=30&cinterestrate=6.9&cremainingyear=30&cremainingmonth=0&cpayoffoption=extra&cadditionalmonth=500&cadditionalyear=0&cadditionalonetime=0&type=1&x=Calculate#loanterm


# Initial Setup
LOAN = 490000
LOAN_TERM = 30 # years
ANNUAL_INTEREST_RATE = 0.069
EXTRA_PAYMENT_MONTHLY = 500

# calculate helper variables
loan_term_in_month = LOAN_TERM * 12
monthly_interest_rate = ANNUAL_INTEREST_RATE / 12

# calculate monthly payment
x = (1 + monthly_interest_rate)**loan_term_in_month
monthly_payment = (LOAN * x *  monthly_interest_rate) / (x - 1)

print("Monthly payment = " + str(monthly_payment))

# calculate interest paid
monthly_interest_paid = monthly_payment - LOAN / loan_term_in_month
total_interest_paid = monthly_payment * loan_term_in_month - LOAN
# total_interest_paid = monthly_interest_paid * loan_term_in_month

print("Monthly interest paid without extra payment = " + str(monthly_interest_paid))
print("Total interest paid without extra payemnt = " + str(total_interest_paid))

# calculate mortgage with extra payments

P = LOAN
total_payment_w_extra_pay = 0
total_months = 0
while P > 0:
    monthly_payment_w_extra_pay = monthly_payment + EXTRA_PAYMENT_MONTHLY
    P = P * (1 + monthly_interest_rate)
    if P > monthly_payment_w_extra_pay:
        total_payment_w_extra_pay += monthly_payment_w_extra_pay
        P -= monthly_payment_w_extra_pay
    else:
        total_payment_w_extra_pay += P
        P = 0
    total_months += 1

total_interest_paid_w_extra_pay = total_payment_w_extra_pay - LOAN
monthly_interest_paid_w_extra_pay = total_interest_paid_w_extra_pay / loan_term_in_month
monthly_interest_savings = monthly_interest_paid - monthly_interest_paid_w_extra_pay
total_interest_savings = total_interest_paid - total_interest_paid_w_extra_pay
diff_num_month_total = loan_term_in_month - total_months
diff_num_year = diff_num_month_total // 12
diff_num_month = diff_num_month_total - diff_num_year * 12

print("---------------------------------------------------")
print("Total interest paid with extra pay = " + str(total_interest_paid_w_extra_pay))
print("Monthly interest paid with extra pay = " + str(monthly_interest_paid_w_extra_pay))
print("Monthly interest paid savings = " + str(monthly_interest_savings))
print("Total interest savings = " + str(total_interest_savings))
print("Paid off " + str(diff_num_month_total) + " months early")
print("Paid off " + str(diff_num_year) + " years and " + str(diff_num_month) + " months early")




