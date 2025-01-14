import requests
from requests.auth import HTTPBasicAuth
# Elasticsearch connection details
ELASTICSEARCH_HOST = 'https://xxxxx-v.es.us-east-1.aws.found.io'
USERNAME = 'elastic'  # Replace with your Elasticsearch username
PASSWORD = 'xxxxxxx'  # Replace with your Elasticsearch password
def get_indices_with_zero_docs():
    # Get all indices and their document counts
    response = requests.get(f'{ELASTICSEARCH_HOST}/_cat/indices?v&format=json', auth=HTTPBasicAuth(USERNAME, PASSWORD))
    indices = response.json()
    # Filter indices with zero documents
    zero_doc_indices = [index['index'] for index in indices if int(index['docs.count']) == 0]
    return zero_doc_indices
def delete_indices(indices):
    for index in indices:
        print(f'Deleting index: {index}')
        response = requests.delete(f'{ELASTICSEARCH_HOST}/{index}', auth=HTTPBasicAuth(USERNAME, PASSWORD))
        if response.status_code == 200:
            print(f'Successfully deleted index: {index}')
        else:
            print(f'Failed to delete index: {index}. Status Code: {response.status_code}')
def main():
    zero_doc_indices = get_indices_with_zero_docs()
    if zero_doc_indices:
        delete_indices(zero_doc_indices)
    else:
        print('No indices with zero documents found.')
if __name__ == '__main__':
    main()