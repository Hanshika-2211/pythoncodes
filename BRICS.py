# write a program that defines a list of countries that are a member of BRICS. Check whether a country is memeber of brics or not
BRICS_list=['Brazil', 'Russia', 'India', 'China', 'South Africa']
countryInput = input("Enter a country to check if it's a member of BRICS: ")# n=str(input("Enter the number of countries :"))

member_BRICS = False
for country in BRICS_list:
    if country.lower() == countryInput.lower():
        member_BRICS = True
        break

if member_BRICS:
    print(countryInput ,"is a member of BRICS.")
else:
    print(countryInput ,"is not a member of BRICS.")