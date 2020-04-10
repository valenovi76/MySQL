## Covid19 Neighborhood Shopping Rota

Our lives have drammatically changed in the last few months.

We have been asked to step up and contribute with our behaviour to the safety of our communities. It’s incumbent on all of us – families, communities, neighbourhoods – to step up and think about what we can do to support people. Everyone need to try and avoid large crowds, such as supermarkets, so I thought it would have been a good idea to creat a simple, user friendly website to submit a shopping list, to share the load of shopping thus decreasing the risk of exposure.

Hosted on GitHub Pages Repository on GitHub

## UX

**Users**
 Typical users of this site should be people in quarantine who cannot or whish not to go out shopping and people that are currently able/willing to shop for them.

**User Stories**
The user should be able to

-   Submit their shopping list,
-   Pick the date by when they would like to have it delivered
-   Select the lthe shop where the food should be purchased.
-   Update their request or delete it
-   Check the requests list and filter it by either date or requestor's name
-   Email the requests list to their own account to use it while shopping
-   Mark the request as done

The site is simple and standard in its structure and navigation because the target audience would be of a certain age. It is also fully mobile responsive. The data is saved on a Collection database in Mongodb.

Here are the links to the wireframes and the database structure

## Design

![enter image description here](https://github.com/valenovi76/Neighborhood_Shopping_Rota/blob/ce0fa1f223470b8ac2f32c0a4923352751a8e9e0/static/img/responsive_site.JPG)


**Design** 
The background is minimalist in its approach to be unobstrusive. The image represnts cooperation. The colour palette has been selected using the Extract theme option on  [https://color.adobe.com/](https://color.adobe.com/)  to armonize with the background picture (credit to Kelly Sikkema [Unsplash -Hands](https://unsplash.com/s/photos/hands%3E)) The links on the navbar are quite big to facilitate navigation.

## Features

### Current features:

-   **Memeber sign up form**  - allows users to add their names and phone numbers to the site database. The main function at this stage is to have a list of names , phone numbers in case further contact is needed and to know who will use the site to have the food delivered ad who instead will take care of the shopping and will deliver the shopping
-   **Shopping list submit form**  - the form allows the user to enter their list, the date by which they would like the request delivered and the shop where to get the food. The form has an hiddent field setting the status of the request to "open" on the Mongo db, the field becomes visible and updatebale in the requests update form.
-   **All Requests list**  - the page presentes a list of all the open requests (which haven't been delivered as of yet) and incorporates an update and delete buttons to access the Update Requests page/form
-   **Requests Update form**  - the page gives the users the option to review their orders and amend date, food list and shop name
-   **Data**  - The data is stored and provided by a Cloud-hosted MongoDB (covid19_rota_DB) organised in 5 collections: 
- c_member_type : to store the valuesfor the member type dropdown select input field 
- c_members : to store the members data entered using the member input form 
- c_requests : to store the shopping requests from the users 
- c_shops : to store the values for the shops dropdown select input field 
- c_status : to store the values for the requests status dropdown select input field
Please see below the tables structure
### Features Left to Implement

I would like to create a proper login form, capturing the users' credentials and recognising an existing member. 
I also would like to create an email service on the Requests page to send the filtered table to an address.

## Technologies Used

-   [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
    -   HTML for the site strucutre
-   [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
    -   CSS for the site style
-   [JavaScript](https://www.w3schools.com/jsref/)
    -   **JavaScript**  for application controller
-   [JQuery](https://jquery.com/)
    -   The project uses  **JQuery**  to simplify DOM manipulation.
-   [Bootstrap](https://getbootstrap.com/)
    -   HTML and CSS Framework from  **Bootstrap**
-   [Git](https://git-scm.com/)
    -   **Git**  used for Version Control
-   [GitHub](https://github.com/)
    -   Repository hosted on  **GitHub**
-   [Github Pages](https://pattern-projects.github.io/oireachtas-ifd-project/)
    -   Website hosted on  **Github Pages**
-   [Mongo DB]([https://www.mongodb.com/](https://www.mongodb.com/))
    -   Database **covid19_rota_DB**
-   [Am I Responsive](http://ami.responsivedesign.is/)
    -   Testing responsiveness of the website


## Deployment

The project is hosted on  [GitHub Pages](https://pattern-projects.github.io/oireachtas-ifd-project/), the data is stored and processed on [MongoDB](https://cloud.mongodb.com/v2/5e626aa576cec5275ce0c8e8#clusters)

The process involved:

**Git**
-   Host a git repository on GitHub. Explained  [here](https://help.github.com/en/articles/create-a-repo).
-   The root folder contains README.md and index.html files
-   On GitHub repository settings page move to GitHub Pages section
-   Change source to master branch. (Or any desired branch)
-   Provided link will be your projects home (index) page.

To deploy your own version of the website:
-   Have git installed
-   Visit the repository
-   Click 'Clone or download' and copy the code for http
-   Open your chosen IDE (Cloud9, VS Code, etc.)
-   Open a terminal in your root directory
-   Type 'git clone ' followed by the code taken from github repository
    -   `git clone  https://github.com/valenovi76/Neighborhood_Shopping_Rota `
-   When this completes you have your own version of the website
The site stores and processes its data on MongoDB.
You will need to

**MONGODB**

Create a db on MONGO DB
Find various directions on how to create a db [here](https://docs.mongodb.com/manual/tutorial/getting-started/)
The database name should be "Covid19_rota_DB".
The collections and their structure should be as per above diagram

**Heroku**

This site is deployed on Heroku. You will need to 
1.  Create a new app app with the name covid19-shop-rota.
2.  Linked the covid19-shop-rota app to its Github repository.
3.  Verify that the project has an up to date Procfile and requirements.txt
4.  Push the project to the Heroku remote.
6.  Set the IP to 0.0.0.0 and the PORT to 5000 in the Heroku config vars.
7.  Set the MONGO_URI environmental variable in the Heroku config vars.
8.  Restart all dynos.
9.  Open the app on Heroku and check to ensure that it's working correctly.

## [](https://github.com/valenovi76/Neighborhood_Shopping_Rota#testing)Testing

** Testing Tools**

-   [W3C CSS validation](https://jigsaw.w3.org/css-validator/)
    
    -   To check the the validity of the CSS code.
-   [W3C Markup Validation](https://validator.w3.org/)
    
    -   To check the the validity of the HTML code.

**User Testing:**

Manual tests were carried out and the testing process was as follows:
**Homepage**
**New request Page**
**Update/Delete Page**

**Issues Found & Fixes Implemented**

##Credits
