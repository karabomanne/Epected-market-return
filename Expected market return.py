#Epected market return when the beta is known

b = 0.6  #Beta of the portfolio
i = 0.04 #Risk-free interest rate
m = 0.2  #Return on the market
ARp = 0.3 #Actual expected return 
erPm = i + b * (m - i) #Expected return on a portfolio in relation to the market

#Test market return vs. actual market return to observe if the return is superior to the amount of systematic risk taken
if testinv = ARp > erPm
    Print ("The expected return on our portfolio is suitable for the amount of systematic risk taken")
else 
    Print ("The expected return on our portfolio is not suitable for the amount of systematic risk taken")
#add A, B, C and so on to the variables (b, i, m, etc) to create multiple expected returns