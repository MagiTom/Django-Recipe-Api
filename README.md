Recipe App Mobile – A Mobile Application for Managing Culinary Recipes
Technology Stack:
Backend: Python - Django

Frontend: Ionic Vue

URL: https://recipe-ionic-app.netlify.app/

Frontend hosting: render.com

Backend hosting: https://supabase.com/

Application Overview:
The application is designed to store culinary recipes found online, organize them into categories, and allow the addition of links to source websites. Users can also add images directly from the camera or from local storage. If no image is added, a preview of the website from the provided URL will be displayed.

Registration Page:
Each user has their own recipe database. After registering, the user is redirected to the main page.

Login Page:
Simple user login form to access personalized recipe content.

Main Page:
The main screen displays a list of categories. By default, there's a category called “All Recipes.”
To add your own categories, click the category management button in the bottom right corner.

A modal window appears, where you can add a new category using a form, including assigning an image to it.
You can also edit or delete categories from the list shown in that same modal. Once a category is added, it becomes visible both in the edit list and on the main page.

Category View:
Clicking on a category redirects the user to a page displaying all recipes assigned to it.
You can filter the list by recipe name or by favorites.

Adding Recipes:
Click the plus icon in the bottom right corner. A form view appears for entering the recipe.
After saving, the recipe appears in the corresponding category. Recipes can be edited or deleted.

Additionally, each recipe can be marked as a "favorite" by clicking the heart icon.

Backend Project Structure:
Models for Category, Recipe, and User

URL paths for API views (e.g., registration, login, CRUD for categories and recipes)

API views handle authentication and user-specific recipe management

Frontend Functionality:
Global error handling via toasts with the backend’s error messages

Loading indicators are shown while data is being fetched from the backend
