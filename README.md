# CS50 E-commerce Project

#### Video Demo: https://youtu.be/t1-M-Jinh2A?si=uU-8-35aeBNTEYIq

#### Description:

This project, CS50 E-commerce, is a Flask-based e-commerce web application developed as the final project for CS50's Introduction to Computer Science course. The platform provides a comprehensive online shopping experience, allowing users to browse through a variety of products, add them to a cart, and proceed to purchase. Users can register, log in, and manage their shopping carts. This project demonstrates a strong understanding of web development using Python, Flask, and SQLite.

### Features:
- **Home Page:** A welcoming homepage introducing users to the e-commerce platform and its offerings. It showcases featured products and highlights ongoing promotions.
- **User Authentication:** Users can securely register, log in, and log out. The authentication system ensures that user data is protected and only accessible to authorized users.
- **Product Listings:** Products are displayed with detailed information such as name, price, and images. This feature enables users to browse through available products easily.
- **Shopping Cart:** Users can add products to a shopping cart, manage quantities and sizes, and proceed to checkout. The cart provides a summary of the selected items and the total cost.
- **Order Management:** Users have the ability to add items to their cart, view the cart's contents, update item quantities, and delete items from the cart.
- **FAQ Section:** An informational section providing answers to frequently asked questions about the platform, helping users to navigate and utilize the site effectively.
- **Contact Page:** A dedicated page for users to get in touch with customer support for any inquiries or issues they may encounter.
- **About Us Page:** This page provides information about the company, its mission, and its values, helping to build trust with users.
- **Beautiful Design:** The platform features a modern and visually appealing interface with intuitive navigation, ensuring a pleasant user experience.
- **Responsive Design:** While designed to work on desktops and laptops, the platform may need further adjustments to display correctly on all mobile devices.
- **Active Page Highlight:** The navigation bar clearly indicates the current page, enhancing user experience by providing context on their location within the site.
- **Custom JavaScript:** Custom JavaScript is used to enhance interactivity and functionality, providing a more dynamic user experience.

## Technologies Used

- **Python:** Used for backend logic and server-side scripting.
- **Flask:** A web framework for routing, templating, and session management.
- **SQLite:** A database management system for storing user data and product information.
- **HTML/CSS:** Used for frontend structure and styling.
- **Jinja Templating:** A template engine for generating HTML pages with Flask.
- **Bootstrap:** A frontend framework for responsive design and UI components.
- **JavaScript:** Used for frontend interactions and dynamic content.

### Project Structure:
- **app.py:** Contains the backend logic using Flask, including routes, SQL queries, and session management.
- **helper.py:** Utility functions for backend operations.
- **static/:** Contains CSS styles and images used in the project.
- **templates/:** Jinja templates for various pages like index.html, shop.html, cart.html, etc.
- **layout.html:** The main HTML template with navigation bar, footer, and flash message handling, included in the templates folder.
- **user.db:** An SQLite database storing user information and shopping cart details.
- **requirements.txt:** A list of Python packages required for the project. Install dependencies using `pip install -r requirements.txt`.
- **Flask session folder:** A folder for storing session data used by Flask.
- **README.md:** This file, explaining the project, its features, and current limitations.

### Current Limitations:
- **Responsive Design Issues:** The project is designed primarily for desktops/laptops and may not display correctly on all mobile devices. Further adjustments are needed to ensure responsiveness across all screen sizes.

### Future Improvements:
- **User Profile Section:** Implement a user profile section for managing user details and order history.
- **Enhanced Responsive Design:** Improve responsive design to ensure compatibility with various mobile devices.
- **Expanded Product Categories:** Expand product categories and filtering options for a richer shopping experience.
- **Additional Features:** Consider adding features like product reviews and wish lists to enhance user engagement and satisfaction.

This project was developed as part of the CS50 Introduction to Computer Science Course, aiming to demonstrate proficiency in web development using Python, Flask, and SQLite. It serves as a testament to the skills acquired during the course and showcases the ability to build functional, user-centric web applications. For any questions or feedback, please contact sarthakkhanna797@gmail.com.
