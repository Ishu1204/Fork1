import argparse
import requests
import os
def trigger_workflow(owner, repo, workflow_id, ref='main'):
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise ValueError("GITHUB_TOKEN environment variable not set")
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"    
    headers = {        'Authorization': f'token {token}',
                       'Accept': 'application/vnd.github.v3+json' 
              }   
    data = {        
            'ref': ref
           }
    response = requests.post(url, json=data, headers=headers)   
    if response.status_code == 204:
        print("Workflow triggered successfully")
    else:
        print(f"Failed to trigger workflow: {response.status_code}")
        print(response.json())
def main():
    repo_owner = input("Enter the repository owner: ")
    repo_name = input("Enter the repository name: ")
    workflow_id = input("Enter the workflow ID or filename: ")
    trigger_workflow(repo_owner, repo_name, workflow_id)
if __name__ == "__main__":
    main()
