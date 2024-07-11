# Meal Planner:


![Beige Brown Aesthetic Save The Date Editable Mockup Instagram Post (1)](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/43d06fb1-1dd1-4b75-8644-c8479f971614)


 meal planner is a management system used to organize and schedule meals in advance. It helps individuals or families decide what they will eat for a certain period, typically a week or a month, and plan accordingly. 

The live application can be viewed here : 

https://meal-plann-92f1402c6fab.herokuapp.com/


# Purpose and Target Audience:
 **Problem Statement:** Busy schedules can make it difficult to find time to prepare meals, leading to skipped meals or unhealthy choices, also the daily pressure of deciding what to cook and ensuring you have the right ingredients can be stressful.

**Purpose:** The Meal Planner will allow the user to add/track what they would like to eat also at what time and it also gives the user the ability to add the recipe of that specific dish if they would like to return to it at a later date.

**Target Audience:** The primary target include individuals who would like to track what they are eating and who cannot find time to prepare long meals as well as those who feel pressure in not being able to decide what to eat due to not having the correct ingredients.



# Persona and User Stories:

 Rachel is a extremley busy individual who works long hours and has limited time for meal planning and preparation. She finds it difficult to keep track of what she has already ate throughout the week. Rachel is looking for a solution to her difficulties and would like to try out a meal planner. 

## User Stories:
* As a busy individual I want to be able to plan my meals ahead of time.
* As a user I want to be able to add my own meals.
* As a user I want to be able to create an account so that I can view the meals I have added.
*  As a busy individual I want to be able adjust meal plans easily for unexpected changes in my schedule.
* As a user I want to be able to edit meals on my account.
* As a user i want to be bale to delete meals.
* As a user I want to be able to logout of my account.
* As a user I want to be able to download my meal plan as a PDF.
* As a user i want to be able to view when i created a certain meal when i go to edit it and when the last time i edited it was.
* As an admin i want to be able to set the date and time for each meal specific to me and the user.

## Wireframe & Initial Design:
### Home Page/Login
![1](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/a17458a2-fd0b-45cb-af44-387ed524fef6)

### Register
![1](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/a4c56a06-3692-467d-813a-ba3797d3087c)

### (Logged in) Add recipes/meals
![Add a book wireframe](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c0379553-0906-4d77-aca6-beb8fc6834d9)

### Gnerate the PDF page

![Book Details Wireframe](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/467fa65e-eb66-4b21-94af-f9090b6a54ab)

## Agile:
This project was created using Agile principles via a projectboard on Github. This is the first time I have implemented Agile as an individual developer. However, creating user stories and identifying accepterance criteria acted as a roadmap to target the various features and functionalities of the application. It helped me stay on track and reduced distractions.

![project board](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/98b7d24d-7234-4155-af15-df72403659f9)


# Design Choices:

## Colour scheme: white and on the generate PDF page #22e010 to make it stand out to the user this is your final product.

  Nav Bar light bg

Red - Button for Gnerating the PDF so it stands out


The colours were selected with the intention of being clear for the user as I wanted the site to be about functionality and not have any distractions, simplifying it for the user.

## Typography:
 The following fonts were standard and not changed as once again I wanted the site to be minimalistic as well as being clear for all to read and utilise.

## Priority Features:

### Home Page/Login

#### Navbar & Hero Image:
![home](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/4f033ade-4485-40c2-ac2d-5fc5641b5cb7)

The landing page provides the user with the login function as well as the create an account link directly underneath allowing the user to register if they don't already have an account. On the Home page their is also a navbar allowing the user to navigate to each page as well as the title of the site so the user knows what site they are on.


#### Registration:

Registration allows users to create an account and once an account has been created they will then be prompted to login.

![signup](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0b6b2b83-d426-4e63-805b-09a6dcdde550)



#### Sign In:

![sign-in](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/6a1d9a16-2211-4403-88a1-3ec1b506cef4)


####  Add Recipes:

![books](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/54c96d8e-6bc3-403f-a8ad-1c4188b60a6e)

Once logged in the user will then be faced with the add recipes page this is where the user can fill out the boxes provided with the information prompted and add the data by clicking the add data button, once this has been clicked directly below the user will be able to see the information they input in the table.

#### Generate Plan:

![add a book](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/8e15c1d9-193f-4032-b147-0969c3b45bab)


When the user is happy with th information they have input they can then click the Generate Plan button this will then take them to another page which will showcase them their information again.


#### Generate PDF:

![book detail](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e88f0274-670b-4a76-8ef8-7c44a5f440a7)

Users are able to click the red Generate PDF button once they are happy which will then save the document to their device as a PDF document to which they can then share or print.

# Future Features:

* Implement a review system so users can share their thoughts about how they feel about the site. 
* A search engine where users can search for previous meals they have added.
* Include an about page to inform others of how The Meal Planner site works and how to use it.


Database Design:

![ERD](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/6db92c85-0b4c-485c-b60d-709df3fb963e)


Entity Relationship Diagrams (ERD) help the developer to make connections between databases and information. Creating an ERD helped me understand how the tables relate to one another. I used LucidChart to create the diagram and the arrow represent how the data fields relate to one another.


## Data Models:


| Recipe   |            |   |
|----------|:-------------:|------:|
| User |  Interger |  | FK
| Day |  CharField   |    |
| Name | CharField |     |
| Description |  CharField |  |
| Created_at |  DateTimeField   |    |
| Updated_at | DateTimeField |     |


## User Flow Chart:
![The Book Booth Flowchart](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/7727f007-8e2e-45fc-b955-57e2d50d1e98)

The Flowchart served as an efficient way to make important decisions when creating the app. It helped me narrow down which decisions were important for the users and admin as well as establishing the appropriate authentication. It also helped me decide which features were the most important i.e adding a book and viewing a list of books that are available to borrow at The Book Booth Library.

# Validation
## HTML

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2F) | ![home page validate](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/2ba0ff6e-6159-47e9-ad4c-2fe954589ca8) | Pass: button is a descendant of a tag |
| Books | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Fbooks%2Fbooks%2F) | ![Validate Books page](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/b7c018c4-a68a-43ee-97c5-778658bbf705) | Pass: No Errors |
| Add a Book | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Fbooks%2Fadd_book%2F) | ![validate adda book page](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/95eb01b9-22fc-43c4-93de-0ebcd1263467) | Pass: No Errors |
| Sign In| [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Faccounts%2Flogin%2F) | ![validate sign in](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/872629ce-e50d-4870-845b-ed699f9178dc) | Pass: No Errors |
| Register| [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Faccounts%2Fsignup%2F) | ![validate sign up](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c5e042af-b3d5-4718-bc50-ef319ba1a1c3) | unclosed elements main and div |

 ## CSS

 I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file.
 
| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=enhttps://jigsaw.w3.org/css-validator/validator) | ![validate css](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/200fc160-1092-4cd0-bba4-2ab1a721eb72) | Pass: No Errors |

## Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/run.py) | ![screenshot]![forms py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/f299346f-bb44-43a2-a8a5-868373d753e3)
 | Pass: No Errors |
| settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/boutique-ado/settings.py) | ![screenshot]![settings py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/7951202c-2d55-4adb-90d6-8fef0707c82c)
 | Pass: No Errors |
| Book views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/blog/views.py) | ![screenshot]![views py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/4f545d53-b304-4600-b9fb-d4feb93b6c93)
 | Pass: No Errors |
| Book urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/checkout/urls.py) | ![screenshot]![urls py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e3f52187-1f65-4171-b1ba-e9096d1b5fc0)
 | Pass: No Errors |
|  models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/profiles/models.py) | ![screenshot]![models py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/f3438ec1-f275-44b6-847d-48a93c0466ed)
 | Pass: No Errors |

# Responsiveness:
Development tools were used to test responsiveness on varying sized devices including laptop, mobile and tablet size.

Full testing was performed on the following devices:

Laptops:

* Macbook Air 2018 13.3-inch screen
* Lenovo Thinkpad 14" screen

 Mobile Devices:
* Google Pixel 4a

 * Browser Compatibility:
 
 I have tested the site using the following browsers:

* Google Chrome

![chrome](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/545ba4e5-c7bc-4fd8-8660-1444dcb3be2a)


* Microsoft Edge

![microsoft edge](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/1570a9cd-6591-45db-840b-ecbe7f7aeb5b)


I can confirm that the site is responsive and looks as expected good on different screen sizes.


Mobile devices:

![Screenshot_20231207-234024](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0f0b0d7d-a72f-43a4-8a57-bc1cf02a1367)

![Screenshot_20231207-234033](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/4c3cc202-b8f6-4f9d-b1bd-cf57c911db65)

![Screenshot_20231207-234013](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/39989e07-4e8d-4faf-8b57-e11686792b38)


![0](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/211095bf-ffac-42ca-b1c8-2a45d8444038)

![Screenshot_20231207-234117 (1)](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e52d022b-d3fb-4f6c-8fcb-092386ce566b)

![Screenshot_20231208-000014](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0cd224f9-b46e-4db9-9260-999cc63fff90)





Tablet Devices:


![homepage](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/5e6eb5c7-4aba-434c-8ed8-8bfd56632f8a)

![signup tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c5f5a237-83ee-4ef3-b9b0-444f648ca225)

![sign in tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/9ac1d08b-d4b8-4aa5-a65b-e46040f3b60b)

![books tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/a9c42d34-a49a-48ed-97ba-660c02de3543)

![tabletadd](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/b516d61d-6e21-460a-b7f4-5b18abf41d00)

![bookdetails tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/17a0f099-ae15-4b8a-887b-254beac2dbb0)





# Testing:

## Lighthouse Audit:

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.


* On a laptop:

Home

![homeaudit](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/5fa9bac2-d4bf-47fe-bb4a-50b3b0c4938b)

Books 

![auditbooks](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/d6401b01-e4d5-4ed1-b8e9-ff6d5eeb4bd9)

Add a book 
![audit add book](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e429ee62-ecbe-4b2f-8521-28da15773a46)

On a mobile device:

Home 
![audit home mobile ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/348889e3-8c4e-41d4-b1c6-2c974780e23b)

Books
![auditbooks](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/fad662af-54da-45d0-b381-c0d70955e4e4)

Add a book 
![audit addbookmobile](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/634965ca-1b9d-4aa1-bd17-bda89f9fbafe)


## Links

| Link | Expected Outcome | Grade |
| ------- | ---------------- | ----- |
| Logo | Navigates to the home page when clicked | Fail |
| Home | Navigates to the home page when clicked | Pass |
| Books | Navigates to a book list  page when clicked | Pass |
| Add a Book | Navigates to a form to add a book when clicked | Pass |
| Register | Navigates to a registration form when clicked | Pass |
| Log in | Navigates to a screen where users can log in when clicked | Pass |
| Logout | Navigates to a page confirming for the user to log out | Pass |

## Testing 


| Feature | Expected Outcome | Grade | Screenshots |
| ------- | ---------------- | ----- | --------- |
| Modal | A message will appear informing the user of a successful action | Pass | ![modal sign out ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/9e8658e8-f751-4cdf-be3d-ca19ad6c47b2)
| User logged in | Text displays the user logged in | Pass | ![modal sign in name](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/cc4a71db-9962-49c1-b4b6-563000687ad7)
| View books | Users can see available books which have been added | Pass | ![testing books](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/01cc3a5b-db46-4742-a8e1-cf715d78c89b)
| Add a book | Add a book to the book collection that will be available to borrow | Pass | ![addbook](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/82133f44-d43a-4f40-863a-f4e8970057aa)
| Admin has access to crud functionality of all additions | Admin can edit or delete any book addition | Pass | ![admin testing](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/72df0b87-6d4f-4659-9d4f-5e986f88e16c)
| Edit a book | A user can edit the details on the book that they have addded. It will update their addition on the books page | Pass | ![edit book ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/79f6de7e-fd14-4c34-a474-483b7cd5285f)
| Delete a book | A user who added a book OR an admin can delete a book. It will then be deleted from the DB | Pass | ![delete book](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/88275723-e875-404a-b96f-58bac0a4907a)
| Registration | New users can access a registration form from the "Register" link | Pass | ![testing sign up](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e9e6c4e1-c90a-4854-a11c-014a8fc80043)
| Log in | Users can log in using a form after clicking "Log in" | Pass | ![sign in testing ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/3fafee34-e6d6-4162-8989-faa78e1bf355)
| Log out | Users get logged out after clicking "Log out" | Pass | ![testing sign out](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/d7d377aa-fc2d-4025-a73e-22d2d81c622a)
| Grid display | A CSS grid will display the books in a clear, responsive format | Pass | N/A
| Functional buttons | Edit, delete, create buttons will be functional throughout the site | Pass | ![edit delete buttons](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/67cfb78d-7d5b-4072-8aa8-812b9c444b67)


# Tools and Technologies Used:
The technologies implemented in this application included HTML5, CSS, Bootstrap, Python and Django.

* Python used as the back-end programming language.
* Git used for version control. (git add, git commit, git push)
* GitHub used for secure online code storage.
* GitHub Pages used for hosting the deployed front-end site.
* Gitpod used as a cloud-based IDE for development.
* Bootstrap used as the front-end CSS framework for modern responsiveness and pre-built components.
* CI used as the Postgres database.
* Heroku used for hosting the deployed site.
* Balsamiq Utilized for collaborative design and prototyping(wireframes).

* Google and Stack Overflow utilized for general research or solving a bug, information gathering, and various online tools.


# Languages Used:
* HTML
* CSS
* Python

# Deployment :

I used the steps used when deploying our django blog to deploy this application. The instructions for this mainly came from the follow along videos and text-steps provided on the code institute LMS.

# Bugs

All the bugs that occured during the creation of this application have been resolved. There is a section of the application which allows you to reset your password that needs to be implemented, however they were not within the scope of this particular project and will be addressed in the near future along with the other future features.


# Credit: 

* Although I used the django blog resources provided on the LMS, I also received alot of additional clarification by following along with django projects on YouTube. One of the vidoes I found especially helpful was : https://youtu.be/JzDBCZTgVyw?si=w3BBwJswUjBTm1xw

* Stack Overflow was used to solve any smaller bugs and further clarification on errors I was receiving in the terminal.

* I used this site to generate a persona and created user stories: https://founderpal.ai/user-persona-generator

* Font Awesome was used for icons and the fonts used were derived from Google Fonts.

* Wireframes, logo and flowcharts were created using Canva. 

