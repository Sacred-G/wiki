# Wiki Clone

## Overview

This Wiki Clone is a web application that allows users to create, edit, and view wiki pages using Markdown or HTML. The pages are rendered into HTML upon saving, providing a seamless reading experience. The application includes a search function that allows users to search the entire site for specific content. This project was developed as part of the CS50W course at Harvard University.

## Features

- **Create New Pages**: Users can create new wiki pages using Markdown or HTML.
- **Edit Existing Pages**: Users can edit existing pages to update content.
- **Search Functionality**: Users can search for content across the entire site.
- **Random Page**: Users can navigate to a random page.
- **Responsive Design**: The application is built using Bootstrap for a responsive and visually appealing design.

## Technology Stack

- **Backend**: Django
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Markdown Rendering**: Python-Markdown



Project Structure
 
   - encyclopedia/: Contains the main application code.
   - templates/encyclopedia/: Contains HTML templates.
   - static/encyclopedia/: Contains static files (CSS, images).
   - urls.py: URL routing for the application.
   - views.py: Contains view functions for handling requests and rendering templates.
   - layout.html: Base template for the application.

Usage

-   **Home Page**: Lists all available wiki pages.
-   **Create New Page**: Navigate to "Create New Page" to add a new wiki page.
-   **Edit Page**: Edit existing pages by navigating to the page and clicking "Edit".
-   **Search**: Use the search bar to find content across the site.
-   **Random Page**: Click "Random Page" to be taken to a randomly selected page.
