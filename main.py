# Import module
from src.registered_user import User
from src.new_user import NewUser
import csv

try:
    with open("user_database.csv", "r") as file:
        reader = csv.reader(file)

except FileNotFoundError:
    with open("user_database.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "subs_start_date", "current_plant","referral_code"])

def main():
    print("===============================================")
    print("            WELCOME TO WATCHLAH                ")
    print("===============================================")
    print("\nPlease login to your account")
    username = input("Username: ")
    print("\n-----------------------------------------------")

    user = User(username)
    account_exists = user.check_subs_status()

    if account_exists:
        print(f"\nWelcome back, {username.upper()}!")
        print(f"You are currently subscribed as a member")
    else:
        print(f"\nSorry, {username.upper()}, you're not subscribed yet")
        print("\n-----------------------------------------------")
        user.check_all_plan()

    while True:
        if account_exists:
            print("\n-----------------------------------------------")
            print("\nWhat would you like to do?\n")
            print("1. Check our products and exclusive benefits")
            print("2. Check current plan and benefits")
            print("3. Check subscription status")
            print("4. Check subscription duration")
            print("5. Check special offers")
            print("6. Check referral code")
            print("7. Upgrade plan")
            print("8. Downgrade plan")
            print("9. Unsubscribe")
            print("0. Exit")
            choice = input("\nEnter your choice (1/2/3/4/5/6/7/8/9/0): ")
            print("\n-----------------------------------------------")

            if choice == '1':
                user.check_all_plan()
            elif choice == '2':
                user.benefit_current_plan()
            elif choice == '3':
                status = user.check_subs_status()
                print("\nYour subscription is active") if status else print("\nYou're not subscribed yet")
            elif choice == '4':
                print(f"\nYou've been subscribed for {user.check_duration()} months now.")
            elif choice == '5':
                user.view_special_offers()
            elif choice == '6':
                print(f"\nYour referral code: {user.check_referral()}")
            elif choice == '7':
                if user.current_plan == 'Premium Plan':
                        print("\nYour current plan is our most premium choice available.")
                else:
                    if user.subs_duration > 12:
                        print("\nAs a loyal long-term subscriber, enjoy a 5% discount on your next subscription. Thank you for your loyalty!")
                    new_plan = input("\nWhich plan would you like to upgrade? (Basic Plan/Standard Plan/Premium Plan) ").title()
                    
                    user.upgrade_plan(new_plan) if new_plan in ('Basic Plan', 'Standard Plan', 'Premium Plan') else print("\nInvalid choice")                        
            elif choice == '8':
                if user.current_plan == 'Basic Plan':
                    print("\nYour current plan is our most basic choice available.")
                else:
                    if user.subs_duration > 12:
                        print("\nAs a loyal long-term subscriber, enjoy a 5% discount on your next subscription. Thank you for your loyalty!")
                    new_plan = input("\nWhich plan would you like to downgrade? (Basic Plan/Standard Plan/Premium Plan) ").strip().title()
                    
                    user.downgrade_plan(new_plan) if new_plan in ('Basic Plan', 'Standard Plan', 'Premium Plan') else print("Invalid choice")
            elif choice == '9':
                user.unsubscribe()
                print("\nPlease refresh and login back!\n")
                break
            elif choice == '0':
                print("===============================================")
                print("         Thank you for using Watchlah.         ")
                print("===============================================")
                break    
            else:
                print("\nInvalid choice")

        else:
            print("\n==============================================================================================")
            subscribe = input("\nWould you like to subscribe? (y/n): ")
            if subscribe.lower() == 'y':
                new_user = NewUser(username)
                new_plan = input("\nPlease pick a plan (Basic Plan/Standard Plan/Premium Plan): ").strip().title()
                referral_code = input("\nDo you have a referral code? Please enter: ")
                new_user.pick_plan(new_plan, referral_code)
                account_exists = True
                user = User(username)
            else:
                print("\n===============================================")
                print("         Thank you for using Watchlah.         ")
                print("           Join now and gain access!           ")
                print("===============================================")
                break

        print("\n==============================================================================================")
        another_action = input("\nDo you want to perform another action? (y/n): ")
        if another_action.lower() != 'y':
            print("\n===============================================")
            print("         Thank you for using Watchlah.         ")
            print("===============================================")
            break

if __name__ == "__main__":
    main()