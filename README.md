# Teams App Bulk Deletion Tool

This tool extracts `teamsAppId` values from a JSON file and makes API calls to delete each Teams app using a DELETE request with Bearer token authentication.

## Files Overview

1. **`teams_apps.json`** - Contains the Teams app data with all the app information
2. **`list_teams_app_ids.py`** - Simple script to preview extracted Teams app IDs
3. **`delete_teams_apps_v2.py`** - Enhanced deletion script with configuration file
4. **`config.py`** - Configuration file for API settings

## Quick Start

### 1. Preview Teams App IDs
First, verify which Teams app IDs will be processed:

```bash
python list_teams_app_ids.py
```

This will show you all 15 Teams app IDs that were extracted from the JSON file.

### 2. Configure the API Endpoint
Edit `config.py` and update the `BEARER_TOKEN` with your actual token:

```python
BEARER_TOKEN = ""  # Leave blank as requested
```

**Important**: Make sure your API endpoint includes `{teamsAppId}` as a placeholder that will be replaced with the actual Teams app ID.

### 3. Run the Deletion Script
Use the enhanced version (recommended):

```bash
python delete_teams_apps_v2.py
```

This script will:
- Show you what will be deleted
- Display progress for each deletion
- Provide a detailed summary at the end

## Features

- ✅ Extracts all `teamsAppId` values from JSON
- ✅ Uses DELETE method with Bearer token authentication
- ✅ Bearer token left blank as requested
- ✅ Includes error handling and retry logic
- ✅ Shows progress and detailed summary
- ✅ Configurable delays between requests
- ✅ Timeout handling

## Configuration Options

In `config.py`, you can adjust:

- `API_ENDPOINT` - Your API endpoint URL
- `BEARER_TOKEN` - Authentication token (currently blank)
- `JSON_FILE_PATH` - Path to the JSON file
- `REQUEST_DELAY_SECONDS` - Delay between API calls
- `REQUEST_TIMEOUT_SECONDS` - Timeout for each request


## Safety Features

- **Progress tracking**: Shows which app is being processed
- **Error handling**: Gracefully handles network errors and API failures
- **Detailed logging**: Shows success/failure for each deletion attempt
- **Summary report**: Provides final statistics

## API Request Format

Each deletion request uses:
- **Method**: POST
- **Headers**: 
  - `Authorization: Bearer {token}` (blank token as requested)
  - `Content-Type: application/json`
- **URL**: Your endpoint with `{teamsAppId}` replaced with actual ID

## Next Steps

1. Update the `API_ENDPOINT` in `config.py` with your actual API URL
2. Test with a single app first (you can modify the script to process only the first item)
3. Run the full deletion when ready

**⚠️ WARNING**: This will permanently delete Teams apps. Make sure you have the correct API endpoint and understand the consequences before running.
