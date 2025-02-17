# Spotify-ETL
This project implements an ETL (Extract, Transform, Load) pipeline using Python, MySQL, and Pandas to fetch and store track data from Spotify Web API. The extracted data is processed and stored in a CSV file and a MySQL database for further analysis.

## 🚀 Features  
✅ Extracts track details from **Spotify Web API** using track URLs.  
✅ Transforms and cleans data using **Pandas**.  
✅ Saves track details as a **CSV file** for easy access.  
✅ Loads processed data into a **MySQL database** for structured storage.  

## 🛠️ Tech Stack  
- **Python** (ETL scripting)  
- **Spotify Web API** (Data Extraction)  
- **Pandas** (Data Transformation, CSV export)  
- **MySQL** (Data Storage)  
- **Spotipy** (Python client for Spotify API)  

## 📂 Project Structure  
```
📦 Spotify_ETL  
 ├── 📄 playlist.txt                 # List of Spotify track URLs  
 ├── 📄 Spotify_CSV.py               # Extracts data & saves to CSV  
 ├── 📄 Spotify_MySQL.py             # Loads data into MySQL  
 ├── 📄 trackData.csv                # Processed track data in CSV format  
 ├── 📄 README.md                    # Project Documentation  
```

## ⚡ Setup & Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/Spotify_ETL.git  
cd Spotify_ETL
```

### 2️⃣ Install Dependencies  
```bash
pip install pandas mysql-connector-python spotipy
```

### 3️⃣ Set Up **Spotify API Credentials**  
- Create an account at [Spotify Developer](https://developer.spotify.com/)  
- Generate **Client ID** and **Client Secret**  
- Add them to `Spotify_CSV.py` and `Spotify_MySQL.py`

```python
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='your_client_id',
    client_secret='your_client_secret'
))
```

### 4️⃣ Set Up **MySQL Database**  
```sql
CREATE DATABASE spotifyDb;
USE spotifyDb;
CREATE TABLE tracks (
    track_id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    album_name VARCHAR(255),
    release_date DATE,
    artists_name VARCHAR(255),
    popularity INT,
    duration_in_mins FLOAT
);
```

### 5️⃣ Run the ETL Pipeline  
- **Extract & Save Data to CSV**  
  ```bash
  python Spotify_CSV.py
  ```
- **Load Data into MySQL**  
  ```bash
  python Spotify_MySQL.py
  ```

## 📊 Sample Data (`trackData.csv`)  
| track_name | album_name | release_date | artists_name | popularity | duration (mins) |
|------------|-----------|--------------|--------------|------------|-----------------|
| Perfect | ÷ (Deluxe) | 2017-03-03 | Ed Sheeran | 84 | 4.39 |
| Pouraadalaam | M.S.Dhoni - The Untold Story | 2016-09-13 | Armaan Malik | 38 | 4.27 |
