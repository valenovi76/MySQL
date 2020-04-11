# Covid19 Neighborhood Shopping Rota

Our lives have dramatically changed in the last few months.

We have been asked to step up and contribute to the safety of our communities. It’s incumbent on all of us – families, communities, neighbourhoods – to step up and think about what we can do to support people. Everyone needs to try and avoid large crowds, such as supermarkets, so I thought it would have been a good idea to create a simple, user-friendly website to submit a shopping list, to share the load of shopping thus decreasing the risk of exposure.

Hosted on GitHub Pages Repository on GitHub

## UX

**Users**
 Typical users of this site should be people in quarantine who cannot or wish not to go out shopping and people that are currently able/willing to shop for them.

**User Stories**
The user should be able to

-   Submit their shopping list,
-   Pick the date by when they would like to have it delivered
-   Select the shop where the food should be purchased.
-   Update their request or delete it
-   Check the requests list and filter it by either date or requestor's name
-   Email the requests list to their own account to use it while shopping
-   Mark the request as done

The site is simple and standard in its structure and navigation because the target audience would be of a certain age. It is also fully mobile responsive. The data is saved on a Collection database in MongoDB.

Here are the links to the wireframes and below you can see the database structure

## Design

![enter image description here](https://github.com/valenovi76/Neighborhood_Shopping_Rota/blob/ce0fa1f223470b8ac2f32c0a4923352751a8e9e0/static/img/responsive_site.JPG)


**Design** 
The background is very simple to be unobtrusive. The colour palette has been selected using the Extract theme option on  [https://color.adobe.com/](https://color.adobe.com/)  The links on the navbar are quite big to facilitate navigation since I presume the biggest users would be elderly people.

## Features

### Current features:

-   **Member sign up form**  - allows users to add their names and phone numbers to the site database. The main function at this stage is to have a list of names, phone numbers in case further contact is needed and to know who will use the site to have the food delivered ad who instead will take care of the shopping and will deliver the shopping
-   **Shopping list submit form**  - the form allows the user to enter their list, the date by which they would like the request delivered and the shop where to get the food. The form has a hidden field setting the status of the request to "open" on the Mongo DB, the field becomes visible and can be updatebale in the requests update form.
-   **All Requests list**  - the page presents a list of all the open requests (which haven't been delivered as of yet) and incorporates an update and delete buttons to access the Update Requests page/form
-   **Requests Update form**  - the page gives the users the option to review their orders and amend the date, food list and shop name
-   **Data**  - The data is stored and provided by a Cloud-hosted MongoDB (covid19_rota_DB) organised in 5 collections: 
- c_member_type: to store the values for the member type dropdown select input field 
- c_members: to store the member's data entered using the member input form 
- c_requests: to store the shopping requests from the users 
- c_shops: to store the values for the shops dropdown select input field 
- c_status: to store the values for the requests status dropdown select input field
Please see below the structure of the tables

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
-   [Heroku](https://www.heroku.com/)
    -   Website hosted on  **Github Pages**
-   [Mongo DB]([https://www.mongodb.com/](https://www.mongodb.com/))
    -   Database **covid19_rota_DB**
-   [Am I Responsive](http://ami.responsivedesign.is/)
    -   Testing responsiveness of the website


## Deployment

The project is deployed  on  [Heroku]([https://dashboard.heroku.com/apps/covid19-shop-rota](https://dashboard.heroku.com/apps/covid19-shop-rota)), the data is stored and processed on [MongoDB](https://cloud.mongodb.com/v2/5e626aa576cec5275ce0c8e8#clusters)

The process involved:

**Git**
-   Host a git repository on GitHub. Explained  [here](https://help.github.com/en/articles/create-a-repo).
-   The root folder contains README.md and index.html files
-   On GitHub, repository settings page move to GitHub Pages section
-   Change source to master branch. (Or any desired branch)
-   Provided link will be your projects home (index) page.

To deploy your version of the website:
-   Have git installed
-   Visit the repository
-   Click 'Clone or download' and copy the code for http
-   Open your chosen IDE (Cloud9, VS Code, etc.)
-   Open a terminal in your root directory
-   Type 'git clone ' followed by the code taken from GitHub repository
    -   `git clone  https://github.com/valenovi76/Neighborhood_Shopping_Rota `
-   When this completes you have your own version of the website
The site stores and processes its data on MongoDB.
You will need to

**MONGODB**

Create a DB on MONGO DB
Find various directions on how to create a DB [here](https://docs.mongodb.com/manual/tutorial/getting-started/)
The database name should be "Covid19_rota_DB".
The collections and their structure should be as per the above diagram

**Heroku**

This site is deployed on Heroku. You will need to 
1.  Create a new app with the name covid19-shop-rota.
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
    
    -   To check the validity of the CSS code.
-   [W3C Markup Validation](https://validator.w3.org/)
    
    -   To check the validity of the HTML code.

**User Testing:**

Manual tests were carried out and the testing process was as follows:

**Homepage**
Homepage appears correct at opening
Verify that new members form functions correctly

 1. Try to submit the form as empty to verify error message appears
 2. Try to submit the form with empty fields, in turn, to ensure error message appears
 3. verify that only one value can be selected on the dropdown option
 4. verify that Submit buttons does upload entries to the relevant collection and loads the correct new page
 5. Ensure that navbar links are redirecting to correct sites pages
 6. Ensure that navbar collapses when the screen size decreases

**New request Page**
New requests page loads both when navbar link is used or when the new member form is filled in and the submit button is clicked
The following tests have been performed on the form

 7. Try to submit the form as empty to verify error message appears
 8. Try to submit the form with empty fields, in turn, to ensure error message appears
 9. verify that the new member added in the previous form does now appear as a value in the Requestor drop down and that only one value can be selected
 10. verify that the shopping lists text area does contain several lines of text
 11. verify that the shops list works and that only one value can be selected
 12. verify that the calendar pops up correctly and that past dates are greyed out
 13. verify that no free text can be entered in the calendar picker field
 14. verify that the submit button uploads the new shopping request to the correct collection on mongo and that it loads the correct page
 
 
**View Requests Page**
The page appears correct at opening
All requests table

 1. verify that all the open requests are loading 
 2. verify that the date and name filters on the table are working correctly
 3. verify that the Reset button clears the filters correctly
 4. verify that the View button opens the correct ticket Edit page

**Update/Delete Page**
The page displays the correct requests at opening
Update/delete form

 1. The form displays all the correct values for each field
 2. verify that the Member drop-down can be edited, the name updated if needed and that the values offered on the dropdown are the ones in the corresponding collection
 3. verify that the Shopping list field can be edited and updated
 4. verify that the Shops drop-down can be edited, the shop name updated if needed and that the values offered on the dropdown are the ones in the corresponding collection
 5. verify that the Date picker can be edited and updated if needed and that no free text can be added
 6. verify that the Status drop downloads with value =" open", that it can be edited, that the values offered on the dropdown are the ones in the corresponding collection

**Issues Found & Fixes Implemented**

In building the database I initially created a list of food types, one for quantities and one for foods. The idea was to ensure there was no free text to avoid misspelling and the normal data issues that come from user interaction.
However, I quickly realised that it was virtually impossible to foresee all the shopping options both from food type, categories, brands and also units. 
I decided to have a fixed table with the most common foods and their category. I was going to leave the quantity field editable and offer the unit as a drop down and have a tick box to indicate that was the product to be added as a request.
The list displayed on the form was too long and I never managed to convert the multiple lines selection in different documents on the mongo collection.
I decided to have the actual shopping as free text. this made the management easier, and the form displayed on smaller screens user friendly.

##Credits

My Mentor Seun Owonikoko for the great advice and helping me fixing some issues along the way.
https://www.w3schools.com/howto/howto_js_filter_table.asp for how to creae a JS filter on a table.
Chris Youderian, https://formden.com/blog/date-picker
