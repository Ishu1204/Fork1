import argparse
import requests
import os
def trigger_workflow(owner, repo, workflow_id, ref='main'):
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise ValueError("GITHUB_TOKEN environment variable not set")
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"    headers = {        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'    }    data = {        'ref': ref
    }
    response = requests.post(url, json=data, headers=headers)    if response.status_code == 204:
        print("Workflow triggered successfully")
    else:
        print(f"Failed to trigger workflow: {response.status_code}")
        print(response.json())
def main():
    parser = argparse.ArgumentParser(description='Trigger a GitHub Action')
    parser.add_argument('owner', type=str, help='Owner of the repository')
    parser.add_argument('repo', type=str, help='Name of the repository')
    parser.add_argument('workflow_id', type=str, help='ID of the workflow')
    parser.add_argument('--ref', type=str, default='main', help='The git reference (branch or tag) to use')
    args = parser.parse_args()
    trigger_workflow(args.owner, args.repo, args.workflow_id, args.ref)
if __name__ == "__main__":
    main()
