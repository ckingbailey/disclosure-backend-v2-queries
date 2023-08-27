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

    elections = ElectionCollection(elections_json).df

    with open('data/filers.json', encoding='utf8') as f:
        filers = json.loads(f.read())

    committees = CommitteeCollection.from_filers(filers, elections)

    # A-Contribs:
    # join filers + filings + elections + transactions
    # transactions.filing_nid -> filings.filing_nid
    #   filings.filer_nid -> committees.filer_nid
    #     committees.Ballot_Measure_Election -> elections.Ballot_Measure_Election
    # where trans['transaction']['calTransactionType'] == 'F460A'

    with engine.connect() as conn:
        common_opts = {
            'index_label': 'id',
            'if_exists': 'replace'
        }
        elections.to_sql('elections', conn, **common_opts)
        committees.df.to_sql('committees', conn, **common_opts)

if __name__ == '__main__':
    main()
