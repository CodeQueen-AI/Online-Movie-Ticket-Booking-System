# 🎬 CineZone Cinema — Online Movie Ticket Booking System

A simple Python console program that simulates an online movie ticket booking experience.

## 📌 **Project Overview**

This program allows a customer to:

* Choose a movie
* Select the number of tickets
* Decide whether to add a snack combo
* Get an automatic free-ticket promotion
* View a complete, neatly-formatted booking receipt

It provides an interactive and smooth booking experience using basic Python concepts


## 💡 **Features**

### ✔ Movie Selection

Shows a list of 4 movies with their showtimes and lets the user choose one by number.

### ✔ Customer Input

The user enters their name, movie number, number of tickets, and snack choice.

### ✔ Free Ticket Offer

For every **4 tickets**, the customer gets **1 free**.
Example:

* 4 tickets → pay for 3
* 8 tickets → pay for 6

### ✔ Snack Combo Option

Popcorn combo = **Rs. 300 per ticket**
If the customer selects “yes”, snack cost is added for each ticket.

### ✔ Final Receipt

A clean and clearly formatted receipt is displayed showing:

* Customer name
* Movie selected
* Showtime
* Tickets purchased
* Free tickets
* Payable tickets
* Snack details
* Total amount



## 🛠️ **How the Program Works**

1. Displays a welcome message and movie list
2. Asks for customer name
3. User selects a movie by number
4. Program assigns the correct movie name and showtime
5. User enters number of tickets
6. Program calculates:

   * Free tickets
   * Payable tickets
   * Ticket total (Rs. 500 each)
7. Program asks if snacks should be added
8. Calculates snack total
9. Adds everything to get the **final bill**
10. Prints a professional-styled movie booking receipt



## 🎯 **Skills Practiced**

* Input handling
* Conditional statements
* Nested if-statements
* Basic arithmetic operations
* Console formatting
* Realistic program flow
