userName = input("Enter your name -> ")
alertz = int(input("What is your Alertz mobile Number? -> "))

def main_menu():
    user_input= int(input(f"""
            Hello  {userName}, Welcome back. How can I assist you today?
            1. Account Opening
            2. Account Reactivation
            3. Account Restriction
            4. Balance Enquiry
            5. Money Transfer
            6. Airtime
            7. Data Purchase
            8. Bills Payment
            9. Block Card
            10. Account Statement
            11. Log Complaints
            12. ATM/Branch Locator
            13. Agent Locator
            14. Reset PIN
            15. Loan Request
            0. Exit
    """))
    match user_input:
        case 1:
            response = int(input(f"""
            Before I open a new Zenith account for you  {userName}, do you have a Bank Verification Number (BVN)?
            1. Yes
            2. No
            """))
            if response == 1:
                userInput = int(input(f"""
            Visit a nearest branch to open an account {userName}
            0.Press 0 to exit.
            Press 11 to go back to main menu
            """))
                if userInput == 11:
                    main_menu()

            else:
                response = int(input("""
            Visit a nearest branch to get your BVN
            Press 0 to exit
            Press 1 to go back to main menu
            """))
                if response == 1:
                    main_menu()

        case 2:
            response = int(input("""
            You do not have a dormant account.
            Press 0 to exit
            Press 1 to go back to main menu
            """))
            if response == 1:
                main_menu()

        case 3:
            response = int(input("""
            1.Enter 1 if you want your account restricted?
            11.Main menu
            0.Exit
            """))
            if response == 1:
                print("Account Restriction successful")

            else:
                main_menu()

        case 4:
            response = int(input("""
            Your available balance is 690,850.95.
            Press 0 to exit.
            Press 1 to go back to main menu
            """))
            if response == 1:
                main_menu()

        case 5:
            response = int(input("""
            Who do you want to send to?
            1. Transfer to Self
            2. Transfer to Third Party
            3. My Saved Beneficiaries
            4. Transfer to Prepaid Card
            Press 0 to exit.
            Press 1 to go back to main menu
            """))
            if response == 1:
                main_menu()

        case 6:
            response = int(input("""
            Who do you want to recharge for?
            1. Self Topup
            2. Third Party Topup
            Press 0 to exit.
            Press 1 to go back to main menu
            """))
            if response == 1:
                main_menu()

        case 7:
            response = int(input("""
            Who do you want to topup for?
            1.Self Topup
            2.Third Party Topup
            Press 0 to exit.
            Press 1 to go back to main menu
            """))
            if response == 1:
                main_menu()

        case 8:
            response = int(input("""
            These are the bills I can help you pay; please make a selection.
            1. Airlines
            2. Cable Tv
            3. Charities
            4. Churches
            5. Electricity/Power
            6. Fashion
            7. Fastfood & Restaurants
            8. Fintech
            9. FMCG
            10. FUEL SERVICE STATION
            11. Gaming/ Lottery
            12. Hotels
            13. Insurance
            14. Internet Service Providers
            15. Investment
            16. Microfinance
            17. MOBILE WALLET
            18. Multinationals
            19. NGOs
            20. Schools
            21. Shipping
            22. Taxes and Levies
            23. Telecommunications
            24. Transportation
            25. Zenith Mutual Fund
            Press 0 to exit.
            Press 1 to go back to main menu
            """))
            if response == 1:
                main_menu()

        case 9:
            response = int(input("""
            Please select a card to continue
            1.539941******879
            2.506109******909
            Press 0 to exit.
            Press 1 to go back to main menu
            """))
            if response == 1:
                main_menu()

        case 10:
            response = int(input(f"""
            What statement type do you need  {userName}?
            1.Mini Statement
            2.Full Statement
            Press 0 to exit.
            Press 1 to go back to main menu
            """))
            if response == 1:
                main_menu()

        case 11:
            response = int(input("""
            What do you want to complain about on your account? Please provide full details.
            Press 0 to exit.
            Press 1 to go back to main menu
            """))
            if response == 1:
                main_menu()

        case 12:
            response = int(input("""
            Enter your location below, e.g Victoria Island or send your location from your device menu
            Press 0 to exit.
            Press 1 to go back to main menu
            """))
            if response == 1:
                main_menu()

        case 13:
            response = int(input("""
            Enter your location below, e.g Victoria Island or send your location from your device menu
            Press 0 to exit.
            Press 1 to go back to main menu
            """))
            if response == 1:
                main_menu()

        case 14:
            response = int(input("""
            Please select an authorization method:
            1.Token
            2.ATM Card
            Press 0 to exit.
            Press 1 to go back to main menu
            """))
            if response == 1:
                main_menu()

        case 15:
            response = int(input(f"""
            This is coming soon.
            Press 0 to exit.
            Press 1 to go back to main menu
            """))
            if response == 1:
                main_menu()


main_menu()
