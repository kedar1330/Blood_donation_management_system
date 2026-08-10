from services.campaign_services import *

def campaign_menu():
    while True:
        print("Campaign Management")
        print("1.Add Campaign")
        print("2.View Campaign")
        print("3.Update Campaign")
        print("4.Delete Campaign")
        print("5.Search Campaign")
        print("6.View Registered Members")
        print("7.back")
        
        choice=int(input("Enter your choice:"))
        
        match choice:
            
            case 1:
                add_campaign()
            case 2:
                view_campaign()
            case 3:
                update_campaign()
            case 4:
                delete_campaign()
            case 5:
                search_campaign()
            case 6: 
                members = view_registered_members_for_campaign()
            
                if members:
            
                    print("\n========== REGISTERED MEMBERS ==========\n")
            
                    print(f"{'ID':<5}{'Campaign ID':<15}{'Donor Name':<25}{'Age':<6}{'Gender':<10}{'Blood Group':<15}{'Phone'}")
                    print("-" * 95)
            
                    for member in members:
                        print(f"{member[0]:<5}{member[1]:<15}{member[2]:<25}{member[3]:<6}{member[4]:<10}{member[5]:<15}{member[6]}")
            
                else:
                    print("No registered members found.")
            case 7:
                break