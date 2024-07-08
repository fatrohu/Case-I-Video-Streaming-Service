# Import module
from tabulate import tabulate
from datetime import date, datetime
import csv


class User:
    """
    A class representing a user with subscription management functionalities

    Attributes
    ----------
        DISCOUNT (float): A class attribute representing the discount rate for subscription more than 12 months
    """

    DISCOUNT = 0.05
        
    def __init__(self, username: str):
        """
        Initializes a User object with a username and retrieves user data from user_database.csv

        Parameters
        ----------
            username (str): The username of the user
        """

        self.username = username.lower()
        self.current_plan, self.referral_code, self.subs_date = self.read_user_data()
        self.subs_duration = self.check_duration()
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


    def read_user_data(self):
        """
        Reads user data from user_database.csv based on the username

        Returns
        -------
            tuple: A tuple containing the user's current plan, referral code, and subscription start date
        """

        with open("user_database.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.username:
                    current_plan = row[2].title()
                    referral_code = row[3]
                    subs_date = datetime.strptime(row[1], '%Y-%m-%d').date()
                    return current_plan, referral_code, subs_date
        return None, None, None
    
    
    def check_all_plan(self): 
        """ Display all available subscription plans and their benefits """

        print("\nSee how our products can benefit you.\n")
        print(tabulate(self.benefit_plan, headers="firstrow", tablefmt='simple'))


    def benefit_current_plan(self):
        """ Displays the benefits of the current subscription plan """

        index_plan = self.benefit_plan[0].index(self.current_plan)  # Find the index of the current plan in the benefit plan list
        headers = [self.benefit_plan[0][0], self.benefit_plan[0][index_plan]]
        rows = self.benefit_plan[1:]
        filtered_rows = [[row[0], row[index_plan]] for row in rows]

        table = tabulate(filtered_rows, headers=headers, tablefmt="simple")
        print("\nHere are your subscription plan and benefits.\n")
        print(table)


    def check_subs_status(self):
        """
        Checks if the user is currently subscribed

        Returns
        -------
            bool: True if the user is subscribed, False otherwise
        """

        with open("user_database.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.username:
                    return True
            return False

    
    def check_duration(self):
        """
        Calculates and returns the duration of the user's subscription in months

        Returns
        -------
            int: The number of months the user has been subscribed
        """
        if self.subs_date is None:
            return 0

        today_date = date.today()
        subs_duration = (today_date.year * 12 + today_date.month) - (self.subs_date.year * 12 + self.subs_date.month)
        return subs_duration
                

    def calculate_price(self, new_plan):
        """
        Calculates the total price for upgrading or downgrading to a new subscription plan

        Parameters
        ----------
            new_plan (str): The new subscription plan to calculate the price for

        Returns
        -------
            int: The total price for the new subscription plan
        """

        index_plan = self.benefit_plan[0].index(new_plan) # Find the index of the current plan in the benefit plan list
        plan_price = int(self.benefit_plan[8][index_plan].replace('Rp','').replace('.',''))

        if self.subs_duration > 12:
            total_price = plan_price - self.DISCOUNT * plan_price
        else:
            total_price = plan_price
        return total_price
    
    
    def confirm_payment(self):
        """
        Prompts the user to confirm if they want to proceed with the payment.

        Returns
        -------
            bool: True if the user confirms the payment, False otherwise.
        """

        deal = input("\nWould you like to proceed with the payment? (y/n) ")
        return deal.lower() == 'y'
    

    def update_user_data(self):
        """ Updates user data in user_database.csv after subscribing to a new plan """

        new_data = [self.username, self.subs_date, self.new_plan, self.referral_code]
        lines = []

        with open('user_database.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.username:
                    row = new_data
                lines.append(row)

        with open('user_database.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lines)
        print(f"\n{self.username} has been change to {self.new_plan}.")

        self.current_plan = self.new_plan


    def upgrade_plan(self, new_plan: str):
        """
        Allows the user to upgrade to a new subscription plan if eligible

        Parameters
        ----------
            new_plan (str): The new subscription plan to upgrade to
        """

        self.new_plan = new_plan.title()
        
        if self.current_plan == "Premium Plan":
            print("\nYour current plan is our most premium choice available.")
        elif self.current_plan == self.new_plan:
            print("\nYour new plan is the same as your current plan.")
            return
        
        # Check eligibility based on current plan
        change_plan = False    
        if self.current_plan == "Basic Plan":         
            if self.new_plan == "Standard Plan" or self.new_plan == "Premium Plan":
                change_plan = True
                total_price = self.calculate_price(self.new_plan)
                print("\n-----------------------------------------------")
                print(f"\nTotal Price for {self.new_plan}: Rp {int(total_price)},-")

        elif self.current_plan == "Standard Plan":                
            if self.new_plan == "Basic Plan":
                print(f"\nYou cannot upgrade from {self.current_plan} to {self.new_plan}, choose DOWNGRADE instead.")                    
            elif self.new_plan == "Premium Plan":
                change_plan = True
                total_price = self.calculate_price(self.new_plan)
                print("\n-----------------------------------------------")
                print(f"\nTotal Price for {self.new_plan}: Rp {int(total_price)},-")

        # If eligible and user confirms, update user data
        if change_plan:
            if self.confirm_payment():
                self.update_user_data()


    def downgrade_plan(self, new_plan: str):
        """
        Allows the user to downgrade to a new subscription plan if eligible

        Parameters
        ----------
            new_plan (str): The new subscription plan to downgrade to
        """

        self.new_plan = new_plan.title()

        if self.current_plan == "Basic Plan":
            print("\nYour current plan is our most basic plan available.")
        elif self.current_plan == self.new_plan:
            print("\nYour new plan is the same as your current plan.")
            return

        # Check eligibility based on current plan
        change_plan = False
        if self.current_plan == "Standard Plan":
            if self.new_plan == "Basic Plan":
                change_plan = True
                total_price = self.calculate_price(self.new_plan)
                print("\n-----------------------------------------------")
                print(f"\nTotal Price for {self.new_plan}: Rp {int(total_price)},-")

        elif self.new_plan == "Premium Plan":
            print(f"\nYou cannot downgrade from {self.current_plan} to {self.new_plan}, choose UPGRADE instead.")
                   
        if self.current_plan == "Premium Plan":
            if self.new_plan == "Basic Plan" or self.new_plan == "Standard Plan":
                change_plan = True
                total_price = self.calculate_price(self.new_plan)
                print("\n-----------------------------------------------")
                print(f"\nTotal Price for {self.new_plan}: Rp {int(total_price)},-")
        
        # If eligible and user confirms, update user data
        if change_plan:
            if self.confirm_payment():
                self.update_user_data()


    def check_referral(self):
        """
        Checks and returns the referral code associated with the user, if any.

        Returns
        -------
            str: The referral code associated with the user, or None if not found.
        """

        with open("user_database.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.username:
                    return row[3]


    def view_special_offers(self):      
        """ Displays special offers based on the user's subscription duration """

        if self.subs_duration > 12:
            print("\nTake your plan to the next level and enjoy a special 5% discount!")
        else:
            print("\nSorry, you haven't unlocked the special offer yet.")
            

    def unsubscribe(self):
        """ Unsubscribes the user by removing their data from user_database.csv """

        lines = []
        account_exists = False
        with open("user_database.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != self.username:
                    lines.append(row)
                else:
                    account_exists = True

        # Delete account
        if account_exists:
            with open("user_database.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(lines)
            print(f"\n{self.username.upper()} has been unsubscribed.")
        else:
            print(f"\n{self.username.upper()} not subscribed yet.")