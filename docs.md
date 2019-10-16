# MVP:

Author: Lucky Adogun
Date: 15-10-2019
---
The MVP Version of the application is built for the following purpose:

### Users:
f_name
l_name
email
password
temporary_pass
1. User model

### Customers:
user => User
account_type:
1. Free
2. Paid

### Payment:
1. How do we process payment?
2. How to process people that have paid and are on trial from ppl that haven't

### Actions:
1. User signs up for free trial using email only
    - user account is created with temporary_password
    - password is sent to the user's email address with a link to dashboard
    - user is automatically set to trial_plan as their plan
    - every plan has a request count. Trial is 1 which gets updated when user sends
        a request for a design to -1
    - user logs in 
    - user is redirected to dashboard
    - user clicks on request design - current plan is displayed and quota too
    - user sends a request: if they have 1 or more quota left. Else redirects them to payment page
2. User uses dashboard to request for design


current_plan: free, mono, duo, trio

1. To allow users sign up for free trial which has an expiry date.
    when met, the user is unable to access the dashboard to make an order
    until they have paid.

2. 


----
1. clicks sign-in (no email or password)
2. clicks signup (redirects to dashboard)
    - current_plan=free
3. Create task: permission or decorator
    - on send: signal fires to get user plan
    - if plan less than 1 => subscribe to a paid plan
    - if plan == 1 or more => subtract one from the user quota


-------------------
1. Enter email for free offer or click on any payment plan
2. Redirects to signup view - and signup: account is created
3. Account activation email is sent 
4. Activates account - and customer model is created - redirects to login
5. Redirects to dashboard or payment page: check if customer has active paid plan or free plan
    if doesnt:
        1. Lands on payment page
            If select any paid plan:
                1. Redirects to dynamic checkout page
                2. Account is credited based on selected plan
                3. Redirects to dashboard
                4. Every request reduces plan by 1
                5. Request has several status: pending, on-going, under-review, done
    
    else:
        1. Lands on dashboard
        2. Every request reduces plan by 1
