# Polar Ltd

Polar is a small eccomerce website that sells Computer components, keyboards, cases etc, This website has/is being built for the purpose of Code Institute 4th milestone project
"Full-Stack Frameworks" the website will include a few different apps which will bring together the overaly userbility and function of the website.

This Website will benifit users by providing them with a service to purchase computer parts easily, it will also keep track of their delivery info and past orders.

#### Test Admin:
User - Test
Password - Polar2020


#### Stripe Cards:

- Authed Number - 4242 4242 4242 4242 - Any 3 Digits - Any future date

- Requires Auth Number - 4000 0025 0000 3155 - Any 3 Digits - Any future date

##### Stripe international cards:

- Ireland - 4000 0037 2000 0005

- U.S.A - 4242 4242 4242 4242

- UK Visa - 4000 0082 6000 0000

- UK Visa(Debit) - 4000 0582 6000 0005

## UX
### Main Requirements
The requirements for this Website is to give the user the ability to Purchase items, create accounts and see past orders while also offering the Owner the ability to easily manage the store via
their account and to easily satisfy all CRUD (Create, Read, Update & Delete) functions for both reviews and products.

### Wireframes

![Home (All sizes)](https://user-images.githubusercontent.com/55837085/98591609-60eed300-22c8-11eb-857d-c556e6baadd7.png)

![Products (All Sizes)](https://user-images.githubusercontent.com/55837085/98591769-9d223380-22c8-11eb-9213-ff2a153204af.png)

![Bag (All Sizes)](https://user-images.githubusercontent.com/55837085/98591800-ab704f80-22c8-11eb-8926-2d4b6c16ab3b.png)

![Account(All Sizes)](https://user-images.githubusercontent.com/55837085/98591842-bd51f280-22c8-11eb-85c3-2c9fc09a5b86.png)

### User Stories

| Who | Wanting to Achieve | Reason | Ticked |
| - | - | - | - |
| Customer | I want to add products to a basket	 | So i can buy them later | [x] |
| Customer | I want to be able to browse by categories | To avoid seeing things i don't need | [x] |
| Customer | To be able to create an account | So i don't have to keep filling in my details | [x] |
| Customer | See past orders | Making it easier for me to do repeat purchases | [x] |
| Customer | Easily find important/Social Links | E.g. terms & conditions | [x] |
|||||
| Owner | Ability to add products through the store | So i can easily manage my store | [x] |
| Owner | Ability to easily edit/delete products | Providing me a simple way to run my business | [x] |
| Owner | Auto send Order confirmations to Customers | To provide them with invoices etc | [x] |
| Owner | Provide important & social links | To promote our social accounts and LinkedIn | [x] |
| Owner | Take card payments on website | Using an app like Stripe | [x] |


## Features
### Existing Features
Save checkout form - once the user add the items to their cart and clicks "Secure Checkout" they can fill in their Delivery info and if the save info box is selected then it'll save the info
for future use.

Accounts - This allows the user to see past orders and even save their info.

emails - Sending REAL emails about the store e.g. confirmation emails

management - Allows the owner to easily ADD, DELETE & EDIT products

### Features Left to Implement

In the future once the amount of products starts getting higher i would like to include:

- Pagination
- Back to top button

## Technologies UsedIn
Used in the project is:
- HTML
- CSS
- Javascript
- JQuery
- Django
- Bootstrap
- Gitpod
- Heroku
- AWS
- boto3
- botocore
- dj-database-url
- django-allauth
- django-countries
- django-crispy-forms
- django-storages
- gunicorn
- Pillow
- psycopg2-binary
- stripe

## Deployment

- LINK TO HEROKU APP - https://polar-ms4-hylia358.herokuapp.com/

Proces for deployment:
1) create a Heroku account
2) (on homescreen) Click "NEW" then click "CREATE NE APP" to start your project
3) Enter app name and region
4) Select Postgres as a free add on
5) Go to settings tab, click reaveal on CONFIG VARS and input the following values

|Keys|Value|
|----|-----|
|DATABASE_URL|Postgres Datbase URL|
|SECRET_KEY|Django Secret Key|
|STRIPE_PUBLIC_KEY|From Stripe|
|STRIPE_SECRET_KEY|from stripe|
|STRIPE_WH_SECRET|From Stripe|
|AWS_ACCESS_KEY_ID|AWS ACCESS KEY|
|AWS_SECRET_ACCESS_KEY|AWS|
|USE_AWS|True|
|EMAIL_HOST_PASS|email app password|
|EMAIL_HOST_USER|Email address|

6) create requirements.txt in your gitpod project
7) Create your Procfile with the following:  web: gunicorn Polar.wsgi:application
8) Set up database with Postgres
9) Create a superuser to work as an admin on the web
10) commit
11) log into Heroku
12) link your remote repo to Heroku using (heroku git:remote -a put name here)
13)push to heroku: GIT PUSH HEROKU MASTER
14) set up auto push to heroku so you can just use GIT PUSH to go to both GITHUB & HEROKU

## Credits
### Content

- All product content was collected from both Overclockers.com and ebuyer.com

### Media

- Most media was collected from both Overclockers.com and ebuyer.com

### Acknowledgements
Inspiration for this website came from a few sources:

- Code Institute - Boutique Ado = a few layout feathures were inspired from Boutique Ado aswell as the videos on the course were rewatched to assist me with understanding Django functionality
and how to make a few things work the way i wanted them to.

- Overclockers - Majority of the content was acquired from Overclockers such as images/title/content and prices, The reviews were random.

- Ebuyer - Bits of the content was acquired from Ebuyer such as images/title/content and prices, The reviews were random.
