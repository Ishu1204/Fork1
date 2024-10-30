import json
import csv

def sarif_to_csv(sarif_file, csv_file):
    with open(sarif_file, 'r') as f:
        sarif_data = json.load(f)

    results = sarif_data['runs'][0]['results']

    with open(csv_file, 'w', newline='') as csvfile:
        fieldnames = ['ruleId', 'level', 'message', 'file', 'startLine', 'endLine', 'startColumn', 'endColumn']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for result in results:
            for location in result['locations']:
                physical_location = location['physicalLocation']
                region = physical_location['region']
                writer.writerow({
                    'ruleId': result['ruleId'],
                    'level': result['level'],
                    'message': result['message']['text'],
                    'file': physical_location['artifactLocation']['uri'],
                    'startLine': region['startLine'],
                    'endLine': region.get('endLine', ''),
                    'startColumn': region['startColumn'],
                    'endColumn': region.get('endColumn', '')
                })

if __name__ == "__main__":
    sarif_to_csv('snyk.sarif', 'snyk_output.csv')
