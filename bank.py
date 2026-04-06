balances = {"A": 5000, "B": 1000}

def parse(command):
    words = command.split()
    return {
        "amount": int(words[1]),
        "sender": words[3],
        "receiver": words[5],
        "min_balance": int(words[9])
    }
def interpret(transaction):
    amount = transaction["amount"]
    sender = transaction["sender"]
    receiver = transaction["receiver"]
    min_balance = transaction["min_balance"]
    
    if balances[sender] > min_balance:
        balances[sender] -= amount
        balances[receiver] += amount
        print(f"SUCCESS Transferred {amount}")
    else:
        print(f"FAILED Balance {balances[sender]} not > {min_balance}")
    
    print(f"Balances: {balances}")
    
print("Initial balances:", balances)
command = input("Enter command: ")
transaction = parse(command)
interpret(transaction)