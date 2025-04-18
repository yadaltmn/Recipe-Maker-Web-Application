## Functional Requirements
1. The system shall allow a cistor to register by providing a username, email, and password.
2. The system shall allow a registered user log in usig email and password.
3. The system shall allow a logged-in user to securely log out of their account.
4. The system shall allow logged-in users to create new recipes with a title, description, ingredients, and instructions.
5. The system shall allow users to edit their own recipes.
6. The system shall allow users to delete their own recipes.
7. The system shall display full recipe details, including ingredients and instructions, to any visitor or user.
8. The system shall provide a search feature for users to find recipes by title or ingredient.
9. The system shall allow users to rate recipes from 1 to 5 stars.
10. The system shall allow users to post comments on recipes.
11. The system shall allow users to view their profile, including all submitted recipes.
12. The system shall allow users to update their display name, email, or password.
13. The system shall allow users to save or favorite recipes for future access.
14. The system shall display all available recipes on the homepage or main recipe list.
15. The system shall allow users to filter recipes based on tags such as 'vegan', 'dessert', and more.

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. The system shall securely store user passwords using encryption and follow standard authentication best practices.

2. The system shall respond to user actions such as login, recipe creation, and search within 2 seconds under normal usage.
<each of the 14 requirements will have a use case associated with it>

## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>
1. User Registration
Writer: Chloe Knott
Implementer: Chloe Knott

2. User Login
Writer: Jada-Lien Nguyen
Implementer: Jada-Lien Nguyen

3. User Logout
Writer: Chloe Knott
Implementer: Chloe Knott

4. Create Recipe
Writer: Jada-Lien Nguyen
Implementer: Jada-Lien Nguyen

5. Edit Recipe
Writer: Chloe Knott
Implementer: Chloe Knott

6. Delete Recipe
Writer: Jada-Lien Nguyen
Implementer: Jada-Lien Nguyen

7. View Recipe
Writer: Chloe Knott
Implementer: Chloe Knott

8. Search Recipe
Writer: Jada-Lien Nguyen
Implementer: Jada-Lien Nguyen

9. Rate Recipe
Writer: Chloe Knott
Implementer: Chloe Knott

10. Comment on Recipe
Writer: Jada-Lien Nguyen
Implementer: Jada-Lien Nguyen

11. View User Profile
Writer: Chloe Knott
Implementer: Chloe Knott

12. Edit User Profile
Writer: Jada-Lien Nguyen
Implementer: Jada-Lien Nguyen

13. Save Recipe (Favorites)
Writer: Chloe Knott
Implementer: Chloe Knott

14. View All Recipes
Writer: Jada-Lien Nguyen
Implementer: Jada-Lien Nguyen

15. Filter Recipes
Writer: Chloe Knott
Implementer: Chloe Knott


- **Pre-condition:** <can be a list or short description>
1. User RegistrationWriter: Chloe KnottImplementer: Chloe Knott
    Pre-condition: User is not logged in.
    Post-condition: A new account is created, and the user is stored in the system.
    Description: A visitor fills out a registration form with a username, email, and password. The system validates the inputs, encrypts the password, and stores the new user in the database. A confirmation message is shown or a login prompt is presented.

2. User LoginWriter: Jada-Lien NguyenImplementer: Jada-Lien Nguyen
    Pre-condition: User has a registered account and valid login credentials.
    Post-condition: User is logged in and redirected to the dashboard.
    Description: The user enters their email and password on the login page. The system verifies the credentials and creates a session if they are valid.

3. User LogoutWriter: Chloe KnottImplementer: Chloe Knott
   Pre-condition: User is currently logged in.
    Post-condition: User session is ended and they are logged out.
    Description: The user clicks the logout button. The system ends the session and redirects them to the homepage or login screen.

4. Create RecipeWriter: Jada-Lien NguyenImplementer: Jada-Lien Nguyen
    Pre-condition: User is logged in.
    Post-condition: New recipe is saved and displayed in the recipe list.
    Description: A logged-in user enters recipe information (title, ingredients, instructions) and submits the form. The recipe is saved and shown to all users.

5. Edit RecipeWriter: Chloe KnottImplementer: Chloe Knott
    Pre-condition: User is logged in and owns the recipe.
    Post-condition: Recipe details are updated and saved.
    Description: The user selects one of their recipes and modifies the content. The updated recipe is saved and replaces the old version.

6. Delete RecipeWriter: Jada-Lien NguyenImplementer: Jada-Lien Nguyen
    Pre-condition: User is logged in and owns the recipe.
    Post-condition: Recipe is removed from the system.
    Description: The user selects one of their recipes and confirms deletion. The system removes it permanently.

7. View RecipeWriter: Chloe KnottImplementer: Chloe Knott
    Pre-condition: Recipe exists in the system.
    Post-condition: Recipe details are displayed to the user.
    Description: A user clicks on a recipe title to view it. The system displays the title, ingredients, and instructions.

8. Search RecipeWriter: Jada-Lien NguyenImplementer: Jada-Lien Nguyen
    Pre-condition: User has entered search input.
    Post-condition: Relevant recipe search results are displayed.
    Description: The user types a keyword into the search bar. The system shows matching recipes by title or ingredient.

9. Rate RecipeWriter: Chloe KnottImplementer: Chloe Knott
    Pre-condition: User is logged in.
    Post-condition: Rating is saved and reflected in the recipe average rating.
    Description: A user selects a star rating for a recipe. The system saves the rating and updates the average rating.

10. Comment on RecipeWriter: Jada-Lien NguyenImplementer: Jada-Lien Nguyen
    Pre-condition: User is logged in.
    Post-condition: Comment is saved and displayed under the recipe.
    Description: A user writes a comment on a recipe. The comment is stored and appears below the recipe details.

11. View User ProfileWriter: Chloe KnottImplementer: Chloe Knott
    Pre-condition: User is logged in.
    Post-condition: User profile with submitted recipes is displayed.
    Description: A logged-in user clicks on their profile. The system shows their name, email, and posted recipes.

12. Edit User ProfileWriter: Jada-Lien NguyenImplementer: Jada-Lien Nguyen
    Pre-condition: User is logged in.
    Post-condition: Profile details are updated and saved.
    Description: The user edits their profile information like display name or password. The changes are saved to the database.

13. Save Recipe (Favorites)Writer: Chloe KnottImplementer: Chloe Knott
    Pre-condition: User is logged in.
    Post-condition: Recipe is added to user’s favorites list.
    Description: A user clicks a 'save' or 'favorite' button on a recipe. The recipe is added to their personal saved list.

14. View All RecipesWriter: Jada-Lien NguyenImplementer: Jada-Lien Nguyen
    Pre-condition: Recipes exist in the database.
    Post-condition: All recipes are displayed on the homepage.
    Description: The homepage displays a list of all available recipes from the database, visible to any user.

15. Filter RecipesWriter: Chloe KnottImplementer: Chloe Knott
    Pre-condition: User is viewing the recipe list.
    Post-condition: Recipes matching the selected filter are displayed.
    Description: The user selects a filter (e.g., vegan, dessert). The system refreshes the list to show only matching recipes.

- **Trigger:** <can be a list or short description>
1. User Registration – A visitor clicks on the 'Sign Up' or 'Register' button.
2. User Login – A user navigates to the login page and submits the login form.
3. User Logout – The user clicks the 'Logout' button.
4. Create Recipe – The user clicks the 'Create Recipe' button and fills out the recipe form.
5. Edit Recipe – The user selects a recipe they own and clicks 'Edit'.
6. Delete Recipe – The user clicks the 'Delete' button on one of their recipes.
7. View Recipe – A user clicks on a recipe title.
8. Search Recipe – A user enters keywords into the search bar and submits.
9. Rate Recipe – A user clicks on a star rating for a recipe.
10. Comment on Recipe – A user writes a comment and clicks 'Post Comment'.
11. View User Profile – A logged-in user clicks on the 'Profile' button or menu item.
12. Edit User Profile – A user clicks on the 'Edit Profile' button.
13. Save Recipe (Favorites) – A user clicks the 'Save' or 'Favorite' icon on a recipe.
14. View All Recipes – A user visits the homepage or recipe listing page.
15. Filter Recipes – A user selects a filter option (e.g., 'vegan') from the filter menu.

- **Primary Sequence:**
1. Ut enim ad minim veniam, quis nostrum e
2. Et sequi incidunt
3. Quis aute iure reprehenderit
4. ...
5. ...
6. ...
7. ...
8. ...
9. ...
10. <Try to stick to a max of 12 steps>


- **Primary Postconditions:** <can be a list or short description>
1. 


- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise and their outcomes>
1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...


- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...

