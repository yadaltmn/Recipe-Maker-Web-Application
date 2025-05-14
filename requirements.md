## Functional Requirements
1. The system shall allow a visitor to register by providing a username, email, and password.
2. The system shall allow a registered user log in using email and password.
3. The system shall allow a logged-in user to securely log out of their account.
4. The system shall allow logged-in users to create new recipes with a title, description, ingredients, and instructions.
5. The system shall allow users to post comments on recipes.
6. The system shall allow users to delete their own recipes.
7. The system shall display full recipe details, including ingredients and instructions, to any visitor or user.
8. The system shall provide a search feature for users to find recipes by title or ingredient.
9. The system shall allow users to rate recipes from 1 to 5 stars.
10. The system shall allow users to edit their own recipes.
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

- **Trigger:** 
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
1. User Registration:

    1. Visitor navigates to the registration page.

    2.  Visitor enters a username, email, and password.

    3. System validates the input fields.

    4. System checks if the email/username is unique.

    5. System encrypts the password.

    6. System creates a new user record in the database.

    7. System displays a success message or redirects to the login page.

2. User Login: 

    1. User navigates to the login page.

    2. User enters email and password.

    3. System validates credentials.

    4. If valid, system creates a session for the user.

    5. System redirects the user to the dashboard or homepage.2.

3. User Logout: 

    1.  User clicks the logout button.

    2. System terminates the user's session.

    3. System redirects user to the homepage or login screen

4. Create Recipe: 

    1. User navigates to the create recipe page.

    2. User enters recipe details (title, description, ingredients, instructions).

    3. System validates the input.

    4. System saves the new recipe in the database.

    5. System displays the new recipe or a success message.

5. Edit Recipe:

    1. User navigates to their list of recipes.

    2. User selects a recipe to edit.

    3. System loads the current recipe details into an editable form.

    4. User updates one or more fields (title, description, ingredients, instructions).

    5. User submits the changes.

    6. System validates the updated input.

    7. System updates the recipe in the database.

    8. System displays the updated recipe or a success message.

6. Delete Recipe:

    1. User navigates to their list of recipes.

    2. User selects a recipe to delete.

    3. System prompts the user to confirm the deletion.

    4. User confirms the deletion.

    5. System deletes the recipe from the database.

    6. System updates the recipe list and displays a success message.

7. View Recipe:

    1. User browses or searches for recipes.

    2. User selects a recipe to view.

    3. System retrieves the recipe details from the database.

    4. System displays the recipe details, including ingredients and instructions.

8. Search Recipe:

    1. User navigates to the search bar.

    2. User enters a keyword or phrase (e.g., title or ingredient).

    3. User submits the search query.

    4. System searches the database for matching recipes.

    5. System displays a list of recipes that match the search criteria.

9. Rate Recipe:

    1. User views a specific recipe.

    2. User selects a star rating (1 to 5 stars).

    3. System records the user’s rating for the recipe.

    4. System updates the recipe’s average rating.

    5. System displays the updated average rating.

10. Comment on Recipe:

    1. User views a specific recipe.

    2. User enters a comment in the comment field.

    3. User submits the comment.

    4. System validates and saves the comment, associating it with the recipe and user.

    5. System displays the new comment below the recipe.

11. View User Profile:

    1. User navigates to their profile page.

    2. System retrieves the user’s profile information and submitted recipes from the database.

    3. System displays the profile information and a list of the user’s recipes.

12. Edit User Profile:

    1. User navigates to the profile edit page.

    2. System loads the current profile information into an editable form.

    3. User updates their display name, email, or password.

    4. User submits the changes.

    5. System validates the input and updates the user’s information in the database.

    6. System displays a success message or the updated profile.

13. Save Recipe (Favorites):

    1. User views a recipe they want to save.

    2. User clicks the ‘Save’ or ‘Favorite’ button.

    3. System adds the recipe to the user’s list of saved recipes in the database.

    4. System provides visual feedback (e.g., highlighted icon).

    5. User can access saved recipes from their profile or favorites page.

14. View All Recipes:

    1. User navigates to the homepage or main recipe list.

    2. System retrieves all recipes from the database.

    3. System displays a list or grid of all available recipes, possibly with pagination.

15. Filter Recipes:

    1. User navigates to the recipe list or homepage.

    2. User selects one or more filter options (e.g., tags like 'vegan', 'dessert').

    3.  System filters the recipes based on the selected tags.

    4. System displays only the recipes that match the selected filters


- **Primary Postconditions:** 

1. User Registration:

    New user account is created and securely stored in the database.

    User is either logged in or redirected to the login page.

2. User Login:

    User is authenticated and has an active session.

3. User Logout:

    User session is terminated and user is logged out.

4. Create Recipe:

    New recipe is saved and displayed in the recipe list.

5. Edit Recipe:

    Recipe details are updated and saved in the database.

6. Delete Recipe:

     removed from the system and no longer visible in user lists.

7. View Recipe:

    Recipe details are displayed to the user.

8. Search Recipe:

    List of recipes matching the search criteria is displayed.

9. Rate Recipe:

    User’s rating is saved and recipe’s average rating is updated.

10. Comment on Recipe:

    Comment is saved and displayed under the recipe.

11. View User Profile:

    User’s profile information and submitted recipes are displayed.

12. Edit User Profile:

    User’s profile information is updated and saved.

13. Save Recipe (Favorites):

    Recipe is added to the user’s list of saved/favorite recipes.

14. View All Recipes:

    All available recipes are displayed to the user.

15. Filter Recipes:

    Only recipes matching the selected filters are displayed.



- **Alternate Sequence:** 
1. User Registration:

    User enters invalid email or weak password.

    System displays an error and prompts for correction.

    User attempts to register with an existing email/username.

    System displays a duplicate account error.

- **Alternate Sequence:** 
2. User Login:

    User enters incorrect credentials.

    System displays an error message and prompts to retry.

    User account is locked after repeated failed attempts (if applicable).

- **Alternate Sequence:** 
3. User Logout:

    Session termination fails due to server error.

    System displays an error message; user remains logged in.

 **Alternate Sequence:** 
4. Create Recipe:

    User submits incomplete or invalid data.

    System displays validation errors and prompts for correction.

    Database error occurs; system displays a failure message.

 **Alternate Sequence:** 
5. Edit Recipe:

    User tries to edit a recipe they do not own.

    System denies access and displays an error.

    User submits invalid data; system prompts for correction.

 **Alternate Sequence:** 
6. Delete Recipe:

    User cancels the deletion; recipe remains unchanged.

    User tries to delete a recipe they do not own; system denies access.

    Database error occurs; system displays a failure message.

 **Alternate Sequence:** 
7. View Recipe:

    Recipe does not exist (deleted or broken link).

    System shows a "Recipe not found" error.
 
 **Alternate Sequence:** 
8. Search Recipe:

    No recipes match the search criteria; system displays a "No results found" message.

    User enters invalid search input; system prompts for correction.

 **Alternate Sequence:** 
9. Rate Recipe:

    User tries to rate the same recipe multiple times; system prevents duplicate ratings.

    Database error occurs; system displays a failure message.

 **Alternate Sequence:** 
10. Comment on Recipe:

    User submits an empty or invalid comment; system prompts for correction.

    Comment fails to save due to a system error; system displays a failure message.

 **Alternate Sequence:** 
11. View User Profile:

    User profile does not exist; system shows an error message.

    Database error occurs; system displays a failure message.

**Alternate Sequence:** 
12. Edit User Profile:

    User submits invalid data (e.g., email already in use); system prompts for correction.

    Database error occurs; system displays a failure message.

 **Alternate Sequence:** 
13. Save Recipe (Favorites):

    User tries to save a recipe already in favorites; system prevents duplicate saves.

    Database error occurs; system displays a failure message.
 
 **Alternate Sequence:** 
14. View All Recipes:

    No recipes exist in the database; system displays a "No recipes available" message.

    Database error occurs; system displays a failure message.
 
 **Alternate Sequence:** 
15. Filter Recipes:

    No recipes match the selected filters; system displays a "No results found" message.

    User selects invalid or conflicting filters; system prompts for correction.



