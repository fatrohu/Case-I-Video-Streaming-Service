# 🎬 WATCHLAH - Video Streaming Service 🎬
Video Demo: https://youtu.be/rT2ShlH4yNE?si=qn36BwhWdxC5Qjil

Presentation: https://www.canva.com/design/DAGIUaArq0U/x7G4dUGyMujoo0NeRNr6HQ/edit

**Watchlah** Video Streaming Service is a simple program designed to register new users and manage user subscriptions on the Watchlah platform. This program allows users to perform basic operations such as checking, modifying, and canceling subscriptions, as well as obtaining information about products, special offers, and referral codes.

## Case Description ❓
Watchlah offers 3 service plans:
- Basic Plan
- Standard Plan
- Premium Plan

Here are the benefits and prices for each plan:
| **Services**   | **Basic Plan**       | **Standard Plan**                                       | **Premium Plan**                                               |
|----------------------|---------------------------------------------------------|----------------------------------------------------------------|----------------|
| Can stream     | ✓                    | ✓                                                       | ✓                                                              |
| Can Download  | ✓                    | ✓                                                       | ✓                                                              |
| Has SD         | ✓                    | ✓                                                       | ✓                                                              |
| Has HD         |                      | ✓                                                       | ✓                                                              |
| Has UHD        |                      |                                                         | ✓                                                              |
| Num of Devices | 1                    | 2                                                       | 4                                                               |
| Content        | 3rd party movie only | Basic Plan Content + Sports Content | Basic Plan + Standard Plan +  PacFlix Original Series or Movie |
| Price          | Rp 120.000,-         | Rp 160.000,-                                            | Rp 200.000,-                                                    |

## Features 🎯
The system provides several key features:

- **View Products**: Users can see all available subscription products along with their benefits.
- **Current Plan Check**: Users can check their current subscription plan and its benefits.
- **Subscription Status**: Users can check whether their subscription is active.
- **Subscription Duration**: Users can see how long they have been subscribed.
- **Special Offers**: Users can view special offers based on their subscription duration.
- **Referral Code**: Users can view and use a referral code for additional discounts.
- **Upgrade and Downgrade Plans**: Users can upgrade or downgrade their subscription plans, considering eligibility criteria and applicable prices.
- **Unsubscribe**: Users can cancel their subscription through the menu.

## Data Management 📚

- **Data Storage**: User subscription data is stored in `user_database.csv`.
- **CSV Format**: The CSV file contains columns for username, subscription start date, current plan, and referral code.

## Instructions 📝
### Installation
To run the application:
    
- Ensure you have Python 3 installed on your system.
- Install the necessary dependencies using the command:
  ```
  'pip install -r requirements.txt'
  ```

### Running the Program
- Open a terminal or command prompt.
- Navigate to the directory where you cloned the repository.
- Run the program using the command:

     ```
     python main.py
     ```

### Using the Program
Follow the prompts displayed on the terminal to interact with the program:

* Login with your username. Choose from options to check, modify, or cancel.

* For new users, select a subscription plan and enter a referral code if available.
