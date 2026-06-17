# ---------- Stage 1: Log a single expense ----------
# Lesson: Every program starts tiny. Grab a description (a string) and an
#         amount (a number), then print them back nicely. Remember: input()
#         ALWAYS hands you a string, so convert the amount with float().
# Task:   Ask for a description and an amount, store each in a variable, then
#         print a tidy line like:  Logged: Coffee for £3.50
#    Use an f-string, and format the amount to 2 decimals with {amount:.2f}.
# 💾 COMMIT:  "Stage 1: log a single expense"


description = input("Name the purchased item: \n")
amount = float(input("How much did it cost? \n"))
print(f"Logged: {description} for £{amount:.2f}")


# ---------- Stage 2: Functions & decisions ----------
# Lesson: Right now your code runs once, top to bottom. Functions let you name
#         a chunk of work and reuse it. if/elif/else lets the program make
#         decisions. We'll size each expense: small / medium / large.
# Task:   1) Write a function categorise(amount) that returns:
#              "small"  if amount < 10
#              "medium" if amount < 50
#              "large"  otherwise
#         2) Test it by printing categorise(3.5) and categorise(80).
# 💡 Tip: A simple `if amount > 0` check beats a crash. We'll do proper
#    error handling later (it's optional), so don't reach for try/except yet.
# 💾 COMMIT:  "Stage 2: categorise expenses with a function"


def categorise(amount):
    if amount < 10:
        return "small"
    elif amount < 50:
        return "medium"
    else:
        return "large"


print(categorise(3.5))
print(categorise(80))

# ---------- Stage 3: Make it run (the menu loop) ----------
# Lesson: A real program waits for you and keeps going until you quit. A
#         `while True:` loop with a menu does exactly that.
#         `break` exits the loop.
# Task:   Build a menu loop that prints options and reads a choice:
#              1) Add an expense   2) Quit
#         For now, option 1 can just print "TODO: add". Option 2 should break.
#         Anything else: print "Not a valid choice" and loop again.
# 💾 COMMIT:  "Stage 3: interactive menu loop"

while True:
    print("1) Add an expense  2) Quit")
    choice = input("Choose an option: \n")
    if choice == "1":
        print("TODO: add expense")
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Not a valid choice")
        continue

    # ---------- Stage 4: Remember many expenses (lists) ----------
# Lesson: One expense is no use. A list holds many. .append() adds to it, and a
#         for loop walks through it. len() tells you how many you have.
# Task:   1) Make an empty list `expenses = []` before the loop.
#         2) When the user adds an expense, append the amount to the list.
#         3) Add a menu option "View all" that loops over the list and prints
#            each amount, plus the running total (add them up in a loop).
# 💾 COMMIT:  "Stage 4: store and total expenses"

expenses = []

while True:
    print("1) Add an expense  2) View all  3) Quit")
    choice = input("Choose an option: \n")
    if choice == "1":
        amount = float(input("How much did it cost? \n"))
        expenses.append(amount)
        print(f"Logged: £{amount:.2f}")
    elif choice == "2":
        total = 0
        print("Expenses:")
        for expense in expenses:
            print(f"£{expense:.2f}")
            total += expense
        print(f"Total: £{total:.2f}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Not a valid choice")
