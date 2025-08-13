import json


def extract_and_display_teams_app_ids():
    """Extract and display all Teams app IDs from the JSON file."""
    
    try:
        with open('teams_apps.json', 'r', encoding='utf-8') as file:
            teams_apps_data = json.load(file)
        
        print("📋 Extracted Teams App IDs:")
        print("=" * 50)
        
        teams_app_ids = []
        for i, app in enumerate(teams_apps_data, 1):
            if 'teamsAppId' in app:
                teams_app_id = app['teamsAppId']
                app_name = app.get('appName', 'Unknown')
                teams_app_ids.append(teams_app_id)
                print(f"{i:2d}. {teams_app_id} ({app_name})")
        
        print(f"\n📊 Total: {len(teams_app_ids)} Teams apps found")
        
        return teams_app_ids
        
    except FileNotFoundError:
        print("❌ Error: 'teams_apps.json' file not found.")
        return []
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON in file.")
        return []
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return []

if __name__ == "__main__":
    extract_and_display_teams_app_ids()
