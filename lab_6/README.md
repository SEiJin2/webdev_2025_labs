# Angular Album Project

This project is an Angular-based web application that demonstrates the use of the `Route` and `Http` modules. It includes CRUD operations for albums and navigation between multiple pages.

## Features

### Static Pages
- **Home Page** (`/home`): A static markup page.
- **About Page** (`/about`): A static markup page.

### Albums
- **Albums List Page** (`/albums`): Displays a list of albums fetched from an external API. Each album:
  - Has a delete button to remove the album.
  - Is clickable, opening a detail page for the selected album.

- **Album Detail Page** (`/albums/:id`): Displays details of the selected album. This page includes:
  - Information about the selected album.
  - An editable input field for changing the album title and a "Save" button.
  - A "Return" button to navigate back to the albums list.
  - A "Photos" link to navigate to the photos page of the selected album.

- **Album Photos Page** (`/albums/:id/photos`): Displays all photos of the selected album. This page includes:
  - A "Return" button to navigate back to the album detail page.

### Routing
- The root URL (`""`) redirects to `/home`.

### Data Fetching
- Albums and photos are fetched using the Angular `HttpClient` module.
- Data is managed through an `albums.service.ts` file and passed to components as `Observable`.

## Components

1. **Home Component**: Displays the static home page.
2. **About Component**: Displays the static about page.
3. **Albums Component**: Displays the list of albums with delete functionality.
4. **Album Detail Component**: Displays details of a selected album with edit functionality.
5. **Album Photos Component**: Displays photos of a selected album.

## API

- Albums and photos are fetched from [JSONPlaceholder](https://jsonplaceholder.typicode.com/).
  - Albums: `https://jsonplaceholder.typicode.com/albums`
  - Photos: `https://jsonplaceholder.typicode.com/photos`

> **Note**: If JSONPlaceholder links are unavailable, please use a VPN.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. Install dependencies:
    ```bash
    npm install
    ```

3. Run the dev server: 
    ```bash
    ng serve
    ```
