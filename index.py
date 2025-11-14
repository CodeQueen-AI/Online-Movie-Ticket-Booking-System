print('-----------Welcome to CineZone Online Booking System---------')
print('Now Showing:')
print('-------------------------------------------------------------')
print('1. Inside Out 2         | 12:30 PM')
print('2. Venom 3              | 03:00 PM')
print('3. Joker 2              | 06:30 PM')
print('4. Kung Fu Panda 4      | 09:00 PM')
print('-------------------------------------------------------------')

# Customer Name 
customer_name = input('Please Enter Your Name : ')

# Movie Number
movie_number = int(input('Enter the movie number you want to watch : '))

# Assign Movie Based On Choice
if movie_number == 1:
    movie_name = 'Inside Out 2'
    show_time = '12:30 PM'
elif movie_number == 2:
    movie_name = 'Venom 3'
    show_time = '03:00 PM'
elif movie_number == 3:
    movie_name = 'Joker 2'
    show_time = '06:30 PM'
elif movie_number == 4:
    movie_name = 'Kung Fu Panda 4'
    show_time = '09:00 PM'
else:
    print("\nInvalid choice! Please restart the program")
    quit()
    
# Ticket Count
tickets = int(input(f"How many tickets would you like to buy for {movie_name}? "))

ticket_price = 500  

# Snacks
snack_choice = input('Do you want to add a popcorn combo (Rs. 300 each)? Type yes or no: ')
snack_choice = snack_choice.lower()  

# Free Ticket Offer
free_tickets = tickets // 4
payable_tickets = tickets - free_tickets

# Calculations
ticket_total = payable_tickets * ticket_price

if snack_choice == 'yes':
    snack_total = tickets * 300
else:
    snack_total = 0
    
# Final Bill
final_bill = ticket_total + snack_total

# Receipt
print("\n-------------------------------------------------------------------")
print("                     CINEZONE CINEMA BOOKING")
print("-------------------------------------------------------------------")
print('Customer Name: ' , customer_name)
print('Movie Selected: ' , movie_name)
print('Showtime: ' , show_time)
print()
print('Tickets Purchased: ' , tickets)
print('Free Tickets: ' , free_tickets)
print('Tickets Charged: ' , payable_tickets)
print('Ticket Price (each): Rs.500')
print('Snack Combo: ' + ('Yes' if snack_choice == 'yes' else 'No'))
print('Snack Combo Total: Rs.' + str(snack_total))
print("-------------------------------------------------------------------")
print("Total Amount Payable: Rs." + str(final_bill))
print("-------------------------------------------------------------------")
print('Thank you for Booking with CineZone Cinema!')
print('Enjoy Your Movie!')
print("-------------------------------------------------------------------")