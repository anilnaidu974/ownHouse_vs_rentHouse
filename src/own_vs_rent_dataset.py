import pandas as pd 
import numpy as np 


property_cost = [100000, 500000, 1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000,15000000,20000000,25000000,40000000,35000000,30000000,45000000,50000000]

loans = [0, 0.1,0.2, 0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

interest_rates = [1,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,12,13,14,15,15.5,16,16.5,17,17.5,18,18.5]

no_of_years = [1,2,3,4,5,6,7,8,9,10,12,14,16,18,20,23,25,27,30,35,40,45,50,55,60,65,70]

in_aparment = [True, False]

rent_pays = [2000,4000,6000,8000,10000,15000,20000,25000,30000,35000,40000,45000,50000,60000,70000,80000,90000,100000]

savings_interest = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,26,28,30,35,40,45,50]


# temp_property_cost  = 0
# temp_loan  = 0
# temp_interest_rate  = 0
# temp_no_of_years  = 0
# temp_growth  = 0
# temp_rent_pay  = 0
# temp_savings_interest  = 0

def emi_calculate(temp_loan,temp_interest_rate,temp_no_of_years):
    P = temp_loan
    R = temp_interest_rate/(12*100)
    N = temp_no_of_years*12
    emi = (P * R * (1+R)**N)/((1+R)**N-1)
    return emi

def total_rent_saved(temp_rent_pay,temp_no_of_years):
    P = temp_rent_pay*12
    # increase in rent every year
    R = 5/100 
    N = temp_no_of_years
    rest_savings = P * ((1 + R)**N - 1) / R
    return rest_savings

def propety_value_after_loan(temp_property_cost, temp_no_of_years, temp_in_aparment):
    P = temp_property_cost
    if temp_in_aparment:
        R = 6/100
    else:
        R = 7/100
    N = temp_no_of_years
    property_asset = P * (1+R)**N
    return property_asset

loans_excel = []
property_cost_excel = []
interest_rates_excel = []
no_of_years_excel = []
house_type_excel = []
rent_pays_excel = []
savings_interest_excel = []
own_house_asset = []
rent_house_asset = []




for p_cost in property_cost:
    for loan_per in loans:
        for i_rate in interest_rates:
            for year in no_of_years:
                for boolean in in_aparment:
                    for rent in rent_pays:
                        for s_rate in savings_interest:
                            loan = p_cost*loan_per
                            emi = emi_calculate(loan,i_rate,year)
                            rest_savings = total_rent_saved(rent,year)
                            property_asset = propety_value_after_loan(p_cost, year,boolean)
                            registration_cost = p_cost * 0.07
                            emi_year = emi*12
                            tax_benefit = (emi_year*0.8)*0.2*year
                            interest_paid_to_bank = emi*12*year- loan

                            own_house_value = property_asset + tax_benefit + rest_savings - registration_cost - interest_paid_to_bank

                            down_payment = p_cost - loan
                            property_tax = 3000
                            rent_saved = emi - rent
                            rest_save_investments = rent_saved if rent_saved > 0 else 0

                            s_rate = s_rate/100
                            rent_house_value = ((down_payment+registration_cost) * (1+s_rate/12)**(year*12)) + ((rest_save_investments+property_tax/12)*((1 + s_rate/12)**(year*12) - 1) / (s_rate/12))

                            house_type = 1 if boolean else 0
                            loans_excel.append(loan)
                            property_cost_excel.append(p_cost)
                            interest_rates_excel.append(i_rate)
                            no_of_years_excel.append(year)
                            house_type_excel.append(house_type)
                            rent_pays_excel.append(rent)
                            savings_interest_excel.append(s_rate)
                            own_house_asset.append(own_house_value)
                            rent_house_asset.append(rent_house_value)


dataset = pd.DataFrame()
dataset['Property_Cost'] = property_cost_excel
dataset['Loan'] = loans_excel
dataset['Loan_Interest'] = interest_rates_excel
dataset['Loan_Years'] = no_of_years_excel
dataset['House_Type'] = house_type_excel
dataset['Monthly_Rent'] = rent_pays_excel
dataset['Investment_Interest'] = savings_interest_excel
dataset['Own_House_Asset'] = own_house_asset
dataset['Rent_House_Asset'] = rent_house_asset
dataset.to_csv('./Downloads/own_vs_rent.csv', index = False)