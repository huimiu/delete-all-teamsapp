import json
import time
from typing import List

import requests

from config import (
    API_ENDPOINT,
    BEARER_TOKEN,
    JSON_FILE_PATH,
    REQUEST_DELAY_SECONDS,
    REQUEST_TIMEOUT_SECONDS,
)


def extract_teams_app_ids(json_file_path: str) -> List[str]:
    """
    Extract all teamsAppId values from the JSON file.
    
    Args:
        json_file_path (str): Path to the JSON file containing Teams app data
        
    Returns:
        List[str]: List of teamsAppId values
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            teams_apps_data = json.load(file)
        
        teams_app_ids = []
        for app in teams_apps_data:
            if 'teamsAppId' in app:
                teams_app_ids.append(app['teamsAppId'])
        
        return teams_app_ids
    
    except FileNotFoundError:
        print(f"❌ Error: File '{json_file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"❌ Error: Invalid JSON in file '{json_file_path}'.")
        return []
    except Exception as e:
        print(f"❌ Error reading file: {str(e)}")
        return []

def delete_teams_app(teams_app_id: str, api_endpoint: str, bearer_token: str = "") -> tuple[bool, str]:
    """
    Delete a Teams app using the provided API endpoint.
    
    Args:
        teams_app_id (str): The Teams app ID to delete
        api_endpoint (str): The API endpoint URL (should include placeholder for app ID)
        bearer_token (str): Bearer token for authentication
        
    Returns:
        tuple[bool, str]: (Success status, Response message)
    """
    try:
        # Replace {teamsAppId} placeholder in the API endpoint with actual ID
        url = api_endpoint.replace('{teamsAppId}', teams_app_id)
        
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Content-Type': 'application/json'
        }
        
        # Make DELETE request to delete the Teams app
        response = requests.delete(url, headers=headers, timeout=REQUEST_TIMEOUT_SECONDS)
        
        if response.status_code in [200, 202, 204]:
            return True, f"Success (Status: {response.status_code})"
        else:
            return False, f"HTTP {response.status_code}: {response.text[:200]}"
            
    except requests.exceptions.Timeout:
        return False, "Request timed out"
    except requests.exceptions.RequestException as e:
        return False, f"Network error: {str(e)}"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

def main():
    """
    Main function to extract Teams app IDs and delete them via API calls.
    """
    print("🚀 Teams App Bulk Deletion Tool")
    print("=" * 50)
    
    # Validate configuration
    if "{teamsAppId}" not in API_ENDPOINT:
        print("❌ Error: API_ENDPOINT must contain '{teamsAppId}' placeholder")
        return
    
    print(f"📁 Reading from: {JSON_FILE_PATH}")
    print(f"🌐 API Endpoint: {API_ENDPOINT}")
    print(f"🔑 Bearer Token: {'[SET]' if BEARER_TOKEN else '[BLANK]'}")
    
    # Extract Teams app IDs from JSON file
    teams_app_ids = extract_teams_app_ids(JSON_FILE_PATH)
    
    if not teams_app_ids:
        print("❌ No Teams app IDs found or error reading file.")
        return
    
    print(f"\n📋 Found {len(teams_app_ids)} Teams apps to delete:")
    for i, app_id in enumerate(teams_app_ids, 1):
        print(f"   {i:2d}. {app_id}")
    
    print("\n🗑️  Starting deletion process...")
    print("=" * 50)
    
    # Track results
    successful_deletions = []
    failed_deletions = []
    
    # Loop through each Teams app ID and delete it
    for i, teams_app_id in enumerate(teams_app_ids, 1):
        print(f"\n[{i:2d}/{len(teams_app_ids)}] Processing: {teams_app_id}")
        
        success, message = delete_teams_app(teams_app_id, API_ENDPOINT, BEARER_TOKEN)
        
        if success:
            print(f"✅ {message}")
            successful_deletions.append(teams_app_id)
        else:
            print(f"❌ {message}")
            failed_deletions.append((teams_app_id, message))
        
        # Add delay between requests (except for the last one)
        if i < len(teams_app_ids):
            time.sleep(REQUEST_DELAY_SECONDS)
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 DELETION SUMMARY")
    print("=" * 50)
    print(f"✅ Successful deletions: {len(successful_deletions)}")
    print(f"❌ Failed deletions: {len(failed_deletions)}")
    print(f"📈 Total processed: {len(teams_app_ids)}")
    
    if successful_deletions:
        print(f"\n✅ Successfully deleted:")
        for app_id in successful_deletions:
            print(f"   • {app_id}")
    
    if failed_deletions:
        print(f"\n❌ Failed to delete:")
        for app_id, error in failed_deletions:
            print(f"   • {app_id}: {error}")
    
    if len(failed_deletions) == 0:
        print("\n🎉 All Teams apps were successfully deleted!")
    else:
        print(f"\n⚠️  {len(failed_deletions)} deletions failed. Please review the errors above.")

if __name__ == "__main__":
    main()
