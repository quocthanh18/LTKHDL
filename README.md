# Netflix Dataset
| ID       | Name                  |
|----------|-----------------------|
| 21127428 | Phạm Nguyễn Quốc Thanh|
| 21127627 | Cao Nguyễn Khánh      |
## Introduction

Netflix is one of the most popular media and video streaming platforms. They have over 8000 movies or tv shows available on their platform, as of mid-2021, they have over 200M Subscribers globally. This tabular dataset consists of listings of all the movies and tv shows available on Netflix, along with details such as - cast, directors, ratings, release year, duration, etc.
### License
CC0: Public Domain

### Source
[Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)



## Structure
```
+---data
|   +---processed
|   |       data.csv
|   |       
|   +---raw
|           data.csv
|           
+---notebooks
|       1.0-Introduction.ipynb
|       2.0-Preprocessing.ipynb
|       3.0-EDA.ipynb
|       4.0-Reflection-References.ipynb
|
+---scripts
        tmdb.py
```

## Dataset overview
| Column Name | Description |
| --- | --- |
| show_id | Unique ID for each movie/ tv show |
| type | Type of the movie/ tv show (Movie or TV Show) |
| title | Title of the movie/ tv show |
| director | Director of the movie/ tv show |
| cast | Cast of the movie/ tv show |
| country | Country where the movie/ tv show was produced |
| date_added | Date when the movie/ tv show was added to Netflix |
| release_year | Year when the movie/ tv show was released |
| rating | Rating of the movie/ tv show |
| duration | Duration of the movie/ tv show |
| listed_in | Genre of the movie/ tv show |
| description | Description of the movie/ tv show |

