customers = [
    {
        "name": "Omotola Fashola",
        "acctNumber": "001",
        "age": 19,
        "balance": 1_000,
        "accountType": "savings",
        "gender": "female",
        "is_married": True
    },

    {
        "name": "John Shibuzo",
        "acctNumber": "002",
        "age": 27,
        "balance": 25_000,
        "accountType": "current",
        "gender": "male",
        "is_married": False
    },

    {
        "name": "Emmanuel Obsession",
        "acctNumber": "003",
        "age": 79,
        "balance": 58_100,
        "accountType": "savings",
        "gender": "male",
        "is_married": True
    },

    {
        "name": "Idiot Olamide",
        "acctNumber": "004",
        "age": 29,
        "balance": 10,
        "accountType": "savings",
        "gender": "male",
        "is_married": True
    },

    {
        "name": "Odogwu Buga",
        "acctNumber": "005",
        "age": 19,
        "balance": 1_000,
        "accountType": "savings",
        "gender": "male",
        "is_married": True
    },
]

# names = [customer["name"] for customer in customers]
# avg_age = sum(customer["age"] for customer in customers) / len(customers)
# savings_acct_holders = [customer for customer in customers if customer["type"]== "savings"]
# print(names)
# print(avg_age)
# print(savings_acct_holders)
# savings_acct_holders = [dict(name=c["name"], balance=c["balance"])
#                         for c in customers if c["type"] == "savings"]
#
# print(savings_acct_holders)


def get_balance(dict_: dict) -> int:
    return dict_["balance"]

# print(sorted(customers, key=get_balance, reverse=True))
print(max(customers, key=get_balance))
print(customers)