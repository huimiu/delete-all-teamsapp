# Configuration file for Teams App Deletion Script

# API Configuration
API_ENDPOINT = "https://dev.teams.microsoft.com/api/appdefinitions/{teamsAppId}"
BEARER_TOKEN = ""

# File Configuration
JSON_FILE_PATH = "teams_apps.json"

# Request Configuration
REQUEST_DELAY_SECONDS = 1  # Delay between API calls to avoid overwhelming the server
REQUEST_TIMEOUT_SECONDS = 30  # Timeout for each API request
