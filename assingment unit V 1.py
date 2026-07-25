# Python Program for Bank Transaction System with Exception Handling

# User-defined Exception
class LowBalanceError(Exception):
    pass
balance = 5000

try:
    print("Current Balance: ₹", balance)

    
    amount = float(input("Enter withdrawal amount: ₹"))

  
    if amount < 0:
        raise ValueError("Withdrawal amount cannot be negative.")

    
    if amount > balance:
        raise LowBalanceError("Insufficient balance in account.")

    
    balance -= amount
    print("Withdrawal Successful!")
    print("Amount Withdrawn: ₹", amount)


except ValueError as ve:
    print("Invalid Input:", ve)


except LowBalanceError as le:
    print("Transaction Failed:", le)


except Exception as e:
    print("Error:", e)

finally:
    print("\n--- Transaction Summary ---")
    print("Available Balance: ₹", balance)
    print("Thank you for using our banking system.")
