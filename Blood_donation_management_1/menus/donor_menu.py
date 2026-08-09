from services.donor_services import search_campaign,user_registration_campaigns

def donor_menu():
    while True:
        print("\n===== Booking Menu =====")
        print("1. Search_campaign")
        print("2. user registration for campaigns")
        print("3. exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            search_campaign()
        elif choice==2:
            user_registration_campaigns()
        elif choice==3:
            break    
        else:
            print("Invalid Choice")
