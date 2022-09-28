# Compulsory Task 1

# Designing a program for a courier company to calculate the cost of goods that it needs to deliver

cost_of_package = float(input("Please enter the price of the package you would like to purchase"))
distance_in_kilometres = float(input("Please enter the total distance of the delivery in kilometres(km)"))

cost_of_delivery_air = 0.36
cost_of_freight_delivery = 0.25
full_insurance_cost = 50
limited_insurance_cost = 25
gift_cost = 15
no_gift = 0
priority_customer = 100
standard_delivery = 20
freight_delivery = 1 * (cost_of_package + (distance_in_kilometres * cost_of_freight_delivery))
delivery_air_cost = float(cost_of_package + (distance_in_kilometres * cost_of_delivery_air))
comp_insurance_cost = float(delivery_air_cost + full_insurance_cost)
limit_insurance_cost = float(freight_delivery + limited_insurance_cost)
no_gift_inclusion = float(limit_insurance_cost + 0)
gift_inclusion = float(comp_insurance_cost + gift_cost)
express_priority_cost = float(gift_inclusion + priority_customer)
standard_customer_cost = float(no_gift_inclusion + standard_delivery)

print("\n")

# The customer gets to decide on the method of delivery and any other extras

print("There are choices of delivery between Air travel of R0.36 per km or by freight of R0.25 per km")
choice_of_travel_method = input("Type in 'Air' for Air travel OR type in 'Freight' for Freight to select your option")


print("\n")

if len(choice_of_travel_method) <= 3:
    print("You have selected Air service. R0.36 per km will be added to your delivery cost", "\n")
    print("Your total cost of delivery so far is R{}".format(delivery_air_cost), "\n")

else:
    print("You have selected Freight service. R0.25 per km will be added to your delivery cost", "\n")
    print("Your total cost of delivery so far is R{}".format(freight_delivery), "\n")

print("There is an option to pay for comprehensive insurance at R50 or limited insurance on your delivery at R25.")
insurance_choice = input("Type in 'comprehensive' for comprehensive cover OR Type in 'limit' for limited coverage to "
                         "select your option")

print("\n")

if len(insurance_choice) >= 6:
    print("You have selected comprehensive cover. R50 will be added to your delivery cost")
    print("Your total cost of delivery so far is R{}".format(comp_insurance_cost), "\n")

else:
    print("You have selected limited insurance. R25 will be added to your delivery cost")
    print("Your total cost of delivery so far is R{}".format(limit_insurance_cost), "\n")

print("There is an option to add a gift at R15")
gift_selection = input("Type in 'gift' for a gift OR Type in 'no gift' for no gift option")
print("\n")

if len(gift_selection) <= 4:
    print("You have selected to add a gift and R15 will be added to your delivery cost")
    print("Your total cost of delivery so far is R{}".format(gift_inclusion), "\n")

else:
    print("You have not selected to add a gift to your delivery")
    print("Your total cost of delivery so far is R{}".format(no_gift_inclusion), "\n")

print("Priority delivery is R100 and standard delivery is R20")
selection_of_customer = input("Type in 'exp' for priority delivery OR Type in 'standard' for standard delivery ")

print("\n")
if len(selection_of_customer) <= 3:
    print("You have selected priority delivery", "\n")
    print("Your total cost of delivery will be R{}".format(express_priority_cost))

else:
    print("You have selected standard delivery", "\n")
    print("Your total cost of delivery will be R{}".format(standard_customer_cost))
