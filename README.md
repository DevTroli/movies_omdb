# 🎬 OMDB Explorer MVP

**Discover Movies & Series**  
*A Django MVP integrated with OMDB API for movie exploration*

## ✨ Features

- 🔍 Search movies by title
- 🎥 View detailed movie information
- 🍿 Discover similar movies (genre-based)
- 📖 Paginated popular movies list
- 📱 Responsive Tailwind CSS design
- 🔒 Environment variables configuration

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- OMDB API Key (free tier)

### Installation
```bash
# Clone repository
git clone https://github.com/DevTroli/movies_omdb.git
cd omdb-explorer

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
# ou .venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
echo "OMDB_API_KEY=sua_chave_aqui" > .env

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## 🛠️ Technologies
- Django 4.2
- Tailwind CSS (CDN)
- OMDB API
- Python 3.10+

## 🌐 Usage
1. Access `http://localhost:8000`
2. Use the navbar to:
   - Browse popular movies (paginated)
   - Search any movie title
3. Click movie cards for detailed view
4. Explore similar movies in detail page

## ⚙️ Configuration
- `.env` File:
  ```env
  OMDB_API_KEY=your_api_key_here
  ```
  
- API Limitations (Free Tier):
  - 1,000 requests/day
  - Popular movies list is manually curated

## 🚧 Possible Improvements
- [ ] Add caching layer for API responses
- [ ] Implement user authentication
- [ ] Create watchlist/favorites system
- [ ] Add movie rating functionality
- [ ] Implement proper error handling
