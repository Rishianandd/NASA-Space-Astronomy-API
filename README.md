# 🚀 NASA Space & Astronomy – APOD

A Python-based application that integrates with NASA's Astronomy Picture of the Day (APOD) service to retrieve and explore astronomy images and their descriptions.

The project aims to make astronomy content accessible through a simple application, allowing users to explore daily, historical and random astronomy pictures.

## 🌌 Project Overview

NASA's Astronomy Picture of the Day (APOD) features a different astronomy-related image or photograph every day, accompanied by an explanation written by a professional astronomer.

This project uses NASA's APOD service to retrieve:

- Astronomy picture of the day
- Image title and publication date
- Detailed astronomical explanations
- Image URLs and high-resolution image URLs
- Image credits and copyright information

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| NASA APOD API | Astronomy data retrieval |
| Requests | HTTP communication |
| Python-dotenv | Environment variable management |
| Streamlit | User interface development |
| Git & GitHub | Version control and collaboration |

## 📡 NASA API Integration

**API Endpoint:**

`https://science.nasa.gov/wp-json/wp/v2/apod-basic/`

The application communicates with NASA using HTTP GET requests and retrieves astronomy data in JSON format.

### Implemented Backend Functions

The backend currently includes the following functions in `nasa_api.py`:

| Function | Description |
|---|---|
| `fetch_apod()` | Sends requests to the NASA APOD endpoint |
| `get_today_picture()` | Retrieves today's astronomy picture |
| `get_picture_by_date(date)` | Retrieves a picture for a specified date |
| `get_random_pictures(count)` | Retrieves multiple random astronomy pictures |

The backend also includes basic request error handling and response processing.

## 📂 Project Structure

```text
NASA-Space-Astronomy-API/
│
├── main.py              # Main application entry point
├── nasa_api.py          # NASA API integration
├── requirements.txt     # Python dependencies
├── .env                 # NASA API key (not committed)
├── .gitignore           # Ignored files configuration
└── README.md            # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Rishianandd/NASA-Space-Astronomy-API.git
```

### 2. Navigate to the project directory

```bash
cd NASA-Space-Astronomy-API
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Obtain a NASA API key

Register for an API key through:

https://api.nasa.gov/

### 5. Configure environment variables

Create a `.env` file in the project root directory.

Add:

```env
NASA_API_KEY=your_nasa_api_key
```

Never upload your API key to GitHub.

### 6. Run the application

```bash
python main.py
```

## 🔐 API Key Security

The NASA API key is stored in a local `.env` file and accessed using Python-dotenv.

The `.gitignore` file excludes:

- `.env`
- `__pycache__/`
- `*.pyc`
- `venv/`

This prevents sensitive credentials and unnecessary files from being committed.

## 🤝 Team Collaboration

This project is developed collaboratively by two team members using Git and GitHub.

| Team Member | Responsibility | Branch |
|---|---|---|
| Rishi Anand | Backend development and NASA API integration | `feature/api-backend` |
| Teammate | Frontend development and Streamlit interface | `feature/streamlit-ui` |

### Git Workflow

The team follows a feature-branch workflow:

1. Clone the shared GitHub repository.
2. Create separate feature branches.
3. Develop features independently.
4. Commit and push changes to the respective branches.
5. Create Pull Requests.
6. Review and merge approved changes into `main`.

## 🚀 Future Enhancements

- Interactive Streamlit dashboard.
- Display astronomy images directly in the application.
- Historical image search using date selection.
- Random astronomy picture generator.
- Improved API error handling.
- Responsive and user-friendly interface.

## 🔗 Project Repository

GitHub: https://github.com/Rishianandd/NASA-Space-Astronomy-API

NASA Open APIs: https://api.nasa.gov/

## 📄 Acknowledgements

Data and astronomy images are retrieved from NASA's Astronomy Picture of the Day service.

NASA APOD: https://science.nasa.gov/astrophysics/programs/astrophysics-data-system/

---

**Project:** NASA Space & Astronomy API  
**Category:** Space & Astronomy  
**Language:** Python  
**API:** NASA Astronomy Picture of the Day
