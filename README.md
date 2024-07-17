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
 <img src="readmeimages/wireframelogin.png">

### Register
<img src="readmeimages/wireframeregister.png">

### (Logged in) Add recipes/meals
<img src="readmeimages/wireframerecipe.png">

### Gnerate the PDF page
<img src="readmeimages/wireframepdf.png">

## Agile:
This project was created using Agile principles via a projectboard on Github. This is the first time I have implemented Agile as an individual developer. However, creating user stories and identifying accepterance criteria acted as a roadmap to target the various features and functionalities of the application. It helped me stay on track and reduced distractions.

<img src="readmeimages/kanbanboard.png">


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
<img src="readmeimages/loginhomepage.png">

The landing page provides the user with the login function as well as the create an account link directly underneath allowing the user to register if they don't already have an account. On the Home page their is also a navbar allowing the user to navigate to each page as well as the title of the site so the user knows what site they are on.


#### Registration:

Registration allows users to create an account and once an account has been created they will then be prompted to login.

<img src="readmeimages/registerpage.png">


####  Add Recipes:

<img src="readmeimages/addrecipepage.png">

Once logged in the user will then be faced with the add recipes page this is where the user can fill out the boxes provided with the information prompted and add the data by clicking the add data button, once this has been clicked directly below the user will be able to see the information they input in the table.

#### Generate Plan:

<img src="


When the user is happy with th information they have input they can then click the Generate Plan button this will then take them to another page which will showcase them their information again.


#### Generate PDF:

<img src="readmeimages/pdfpage.png">

Users are able to click the red Generate PDF button once they are happy which will then save the document to their device as a PDF document to which they can then share or print.

# Future Features:

* Implement a review system so users can share their thoughts about how they feel about the site. 
* A search engine where users can search for previous meals they have added.
* Include an about page to inform others of how The Meal Planner site works and how to use it.


Database Design:

<img src="readmeimages/databaseschema.png">


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
<img src="readmeimages/userflowchart.png">

The Flowchart served as an efficient way to make important decisions when creating the app. It helped me narrow down which decisions were important for the users and admin as well as establishing the appropriate authentication. It also helped me decide which features were the most important i.e adding a book and viewing a list of books that are available to borrow at The Book Booth Library.

# Validation
## HTML

| Page | W3C | Screenshot | Notes |
| --- | --- | --- | --- |
| Home/Login | [W3C]| ![home page validate]<img src="readmeimages/loginhtmlvalidation.png"> | Pass: |
| Update Recipe | [W3C] | <img src="readmeimages/updaterecipepagehtmlvalidation.png">| Pass: No Errors |
| Add a Recipe/Meal |  | <img src="readmeimages/recipepagehtmlvalidation.png"> | Pass: No Errors |
| Register| [W3C] | <img src="readmeimages/registervalidation.png"> | |

 ## CSS

 I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file.
 
| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw] | <img src="readmeimages/cssvalidation.png">| Pass: No Errors |

## Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| settings.py | [PEP8 CI] | <img src="readmeimages/settings.pyvalidation.png">
 | Pass: No Errors |
| views.py | [PEP8 CI]| <img src="readmeimages/views.pyvalidation.png">
 | Pass: No Errors |
| urls.py | [PEP8 CI] | <img src="readmeimages/urls.pyvalidation.png">
 | Pass: No Errors |
|  models.py | [PEP8 CI] | <img src="readmeimages/models.pyvalidation.png">
 | Pass: No Errors |

# Responsiveness:
Development tools were used to test responsiveness on varying sized devices including laptop, mobile and tablet size.

Full testing was performed on the following devices:

Laptops:

* Macbook Air 2018 13.3-inch screen
* Lenovo Thinkpad 14" screen

 Mobile Devices:
* Galaxy Note 20

 * Browser Compatibility:
 
 I have tested the site using the following browsers:

* Google Chrome

![chrome](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/545ba4e5-c7bc-4fd8-8660-1444dcb3be2a)


* Firefox

![microsoft edge]<img src-"readmeimages/firefox.png">


I can confirm that the site is responsive and looks as expected good on different screen sizes.


Mobile devices:

<img src="readmeimages/loginpagemobile.png">

<img src="readmeimages/addrecipepagemobile.png">

<img src="readmeimages/updaterecipepagemobile.png">


<img src="readmeimages/generatepdfpagemobile.png">

<img src="readmeimages/registerpagemobile.png">

Tablet Devices:


![homepage/Login] <img src="readmeimages/loginpageipad.png">

![Register] <img src="readmeimages/registerpageipad.png">


![Add Recipe] <img src="readmeimages/recipepageipad.png">

![Update Recipe] <img src="readmeimages/updaterecipepageipad.png">

![Generate PDF] <img src="readmeimages/generatepdfpageipad.png">





# Testing:

## Lighthouse Audit:

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.


* On a laptop:

Home

![home/Login] <img src="readmeimages/loginpagelighthousedesktop.png">

Books 

![Update Recipe] <img src="readmeimages/updaterecipepagelighthousedesktop.png">

Add a book 
!add a recipe] <img src="readmeimages/recipepagelighthousedesktop.png">

Generate PDF Page
[PDF Page] <img src="readmeimages/generatepdfpagelighthousedesktop.png">

Register Page
[Register Page] <img src="readmeimages/registerpagelighthousedesktop.png">

On a mobile device:

Home/Login 
![audit home mobile ] <img src="readmeimages/homelighthouse.png">

Update Recipe
![Update Recipe Page] <img src="

Add a Recipe 
![Add recipe/meals] <img src="readmeimages/recipelighthouse.png">

Generate PDF Page
[PDF Page] <img src="readmeimages/generatepdfpagelighthouse.png">

Register Page
[Register Page] <img src="readmeimages/registerpagelighthouse.png">


## Links

| Link | Expected Outcome | Grade |
| ------- | ---------------- | ----- |
| Logo | Navigates to the home page when clicked | Pass |
| Home/Login | Navigates to the home page when clicked | Pass |
| Update | Navigates to a update page when clicked | Pass |
| Recipes/Meals | Navigates to a form to add a book when clicked | Pass |
| Register | Navigates to a registration form when clicked | Pass |
| Log in | Navigates to a screen where users can log in when clicked | Pass |
| Logout | Navigates to a page confirming for the user to log out | Pass |

## Testing 


| Feature | Expected Outcome | Grade | Screenshots |
| ------- | ---------------- | ----- | --------- |
| Modal | A message will appear informing the user of a successful action | Pass | ![Logged in ]<img src="readmeimages/addrecipepage.png">
| User logged in | Text displays the user login successful | Pass | ![modal Logged in]<img src="readmeimages/addrecipepage.png">
| View Recipes/Meals they added | Users can see recipes/meals which they have added | Pass | ![Recipes/Meals] <img src="readmeimages/addrecipepage.png">
| Add a book | Add a book to the book collection that will be available to borrow | Pass | ![add a recipe/meal]<img src="readmeimages/addrecipepage.png">
| Admin has access to crud functionality of all additions | Admin can edit or delete any book addition | Pass | ![admin testing](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/72df0b87-6d4f-4659-9d4f-5e986f88e16c)
| Edit a recipe/meal | A user can edit the details on the recipe/meal that they have addded. It will update their addition on the recipe page | Pass | ![edit recipe/meal ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/79f6de7e-fd14-4c34-a474-483b7cd5285f)
| Delete a recipe/meal | A user who added a recipe/meal OR an admin can delete. It will then be deleted from the DB | Pass | ![delete book](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/88275723-e875-404a-b96f-58bac0a4907a)
| Registration | New users can access a registration form from the "Register" link | Pass | ![testing sign up] <img src="readmeimages/registerpage.png">
| Log in | Users can log in using a form after clicking "Log in" | Pass | ![sign in testing ]<img src="readmeimages/loginhomepage.png">
| Log out | Users get logged out after clicking "Log out" | Pass | ![testing sign out](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/d7d377aa-fc2d-4025-a73e-22d2d81c622a)
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

