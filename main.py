""" main, to run everything """
import json
from sqlalchemy import create_engine
from model.committee import CommitteeCollection
from model.election import ElectionCollection

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
    engine = create_engine('postgresql+psycopg2://localhost/disclosure-backend-v2', echo=True)

    with open('data/elections.json', encoding='utf8') as f:
        elections_json = json.loads(f.read())

    elections = ElectionCollection(elections_json)

    with open('data/filers.json', encoding='utf8') as f:
        filers = json.loads(f.read())
    committees = CommitteeCollection.from_filers(filers)

    committees = committees

    with engine.connect() as conn:
        elections.df.to_sql('elections', conn)

if __name__ == '__main__':
    main()
