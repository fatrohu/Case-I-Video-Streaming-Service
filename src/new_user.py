# Import module
from tabulate import tabulate
from datetime import date
import csv
import random
import string


class NewUser:
    """ 
    Class representing a new user subscribing to a service
    
    Attributes
    ----------
        DISCOUNT (float): A class attribute representing the discount rate for new users with referral code
    """

    DISCOUNT = 0.04 

    def __init__(self, username: str):
        """
        Initialize a NewUser instance

        Parameters
        ----------
            username (str): The username of the new user
        """

        self.username = username
        self.account_exists = self.check_account_exists()
        self.benefit_plan = [
                        ['Services', 'Basic Plan', 'Standard Plan', 'Premium Plan'],
                        ['Can Stream', '✓', '✓', '✓'],
                        ['Can Download', '✓', '✓', '✓'],
                        ['Has SD', '✓', '✓', '✓'],
                        ['Has HD', ' ', '✓', '✓'],
                        ['Has UHD', ' ', ' ', '✓'],
                        ['Num of Devices', 1, 2, 4],
                        ['Content', '3rd party movie only', 
                                    'Basic Plan Content + \nSports Content', 
                                    'Basic Plan + Standard Plan + \nPacFlix Original Series or Movie'],
                        ['Price', 'Rp120.000', 'Rp160000', 'Rp200.000']
        ]
    
    
    def check_all_plan(self):
        """ Display all available subscription plans and their benefits """
        
        print("\nSee how our products can benefit you.")
        print(tabulate(self.benefit_plan, headers="firstrow", tablefmt='simple'))

        
    def check_account_exists(self):
        """
        Check if the user's account already exists in the user database.

        Returns
        -------
            bool: True if the account exists, False otherwise.
        """

        try:
            with open("user_database.csv", "r") as file:
                reader = csv.reader(file)
                return any(row[0] == self.username for row in reader)
                    
        except FileNotFoundError:
            return False
    

    def pick_plan(self, new_plan: str, referral_code: str):

        """
        Pick a subscription plan and process payment for the new user.

        Parameters
        ----------
            new_plan (str): The new plan chosen by the user.
            referral_code (str): The referral code entered by the user.
        """

        self.new_plan = new_plan
        self.referral_code = referral_code

        index_plan = self.benefit_plan[0].index(new_plan)  # Find the index of the chosen plan in the benefit plan list
        plan_price = int(self.benefit_plan[8][index_plan].replace('Rp','').replace('.','')) # Get the price of the chosen plan

        referral_exist = False
        try:
            # Check ff referral code is exist
            with open("user_database.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[3] == self.referral_code:
                        referral_exist = True
                        print("\nReferral code is VALID")
                        final_price = plan_price - (plan_price * self.DISCOUNT)
                        print(f"Total Price for {self.new_plan} with Referral Code '{self.referral_code}': Rp {int(final_price)},-")
                        break

                if not referral_exist:
                        print("\nreferral code is INVALID")
                        print(f"Total Price for {self.new_plan}: Rp {int(plan_price)},-")

                deal = input("\nWould you like to proceed with the payment? (y/n) ")

                # Proceed with payment if user confirms
                if deal.lower() == 'y':
                    random_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) # Generate referral code for user
                    
                    # Append user's subscription details to user_database.csv
                    with open("user_database.csv", "a", newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([self.username, date.today(), self.new_plan, random_code])
                    print(f"\n{self.username.upper()} has subscribed to {self.new_plan}.")
                    print(f"Your referral code is: {random_code}")
        
        except FileNotFoundError:
            print("Error: user_database.csv not found. Please check your file path.")