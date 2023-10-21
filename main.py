""" main, to run everything """
import os
import json
from sqlalchemy import create_engine
from model.committee import CommitteeCollection
from model.election import ElectionCollection

from gdrive_datastore.gdrive import test_data_pull

def get_last_status(status_list):
    """
    Return a tuple of index, status_item
    for max value of status_item['startDate']
    """

def unique_statuses(filers):
    """ What are the unique values for status? """
    return set(
        s['status'] for f in filers
        for s in f['statusList']
    )

def main():
    """ Do everyting """
    data_dir_path = '.local/downloads'

    # pull data from gdrive and put it in .local/downloads
    test_data_pull(default_folder='OpenDisclosure')

    #engine = create_engine('postgresql+psycopg2://localhost/disclosure-backend-v2', echo=True)

    with open(f'{data_dir_path}/elections.json', encoding='utf8') as f:
        elections_json = json.loads(f.read())

    elections = ElectionCollection(elections_json).df

    with open(f'{data_dir_path}/filers.json', encoding='utf8') as f:
        filers = json.loads(f.read())

    committees = CommitteeCollection.from_filers(filers, elections)

    elections.to_csv('.local/elections.csv', index=False)
    committees.df.to_csv('.local/committees.csv', index=False)

    '''
    with engine.connect() as conn:
        common_opts = {
            'index_label': 'id',
            'if_exists': 'replace'
        }
        elections.to_sql('elections', conn, **common_opts)
        committees.df.to_sql('committees', conn, **common_opts)
    '''

if __name__ == '__main__':
    main()
