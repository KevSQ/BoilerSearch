# BoilerSearch

BoilerSearch is a web application that provides CRUD functionality for Boiler Room YouTube videos, which are recorded DJ sets by the organization Boiler Room. It allows users to upload Boiler Room YouTube videos and save them to a database, enabling users to search for their favorite videos. Users can filter videos by genre, artist, and location.

## Features

- **Upload Videos**: Users can upload their favorite Boiler Room YouTube videos.
- **Search Videos**: Search functionality allows users to find videos by artist, location, genre, or year.
- **Filter Videos**: Users can filter videos by genre, artist, and location.
- **View and Edit Videos**: Users can view details of each video and edit the video information.

## Future Plans

1. **Database Implementation**: Persist the data through a database implementation to enhance data management and storage.
2. **Advanced Search Functionality**: Expand search functionality by implementing a vector database and vector search, bringing LLM (Large Language Model) functionality to the experience.

## Technologies Used

- **Frontend**: HTML, JavaScript, Bootstrap
- **Backend**: Flask with local data storage

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/boilersearch.git
    cd boilersearch
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies**
    ```bash
    pip install Flask
    ```

### Running the Application

1. **Navigate to the project directory**
    ```bash
    cd boilersearch
    ```

2. **Start the Flask server**
    ```bash
    python server.py
    ```

3. **Open your browser and navigate to**
    ```
    http://127.0.0.1:5000/
    ```

## Project Structure

