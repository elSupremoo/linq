# Data Ingestion
This script generates mock data for visualization. I am a big fan of the video game Counter Strike so I figured
why not base this script on that.

## Mock Data Fields
- `rank`: One of ["Silver", "Gold Nova", "Master Guardian", "Global Elite"]
- `fav_pewpew`: One of ["AWP", "AK-47", "M4A4", "Deagle"]
- `kdr`: Float between 0.0–1.0

## How It Works
The script generates 100 player entries with randomized stats and inserts them into a MongoDB collection.

## To Run:
```bash
docker-compose exec app python data_ingest.py