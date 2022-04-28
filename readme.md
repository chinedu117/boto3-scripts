## Dump all databases in all regions on your AWS

Create .env from .env_template and fill in your profile

 mkdir rds_region
 python3 -m venv venv
 source venv/bin/activate (linux) or source venv/scripts/activate (windows)
 pip install -r requirements.txt
 python3 rdsAllRegions.py