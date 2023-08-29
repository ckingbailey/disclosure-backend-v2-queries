""" main, to run everything """
import json
from sqlalchemy import create_engine
from model.a_contributions import A_Contributions
from model.committee import CommitteeCollection
from model.election import ElectionCollection
from model.filing import FilingCollection
from model.transaction import TransactionCollection

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

    committees = CommitteeCollection.from_filers(filers, elections).df

    # A-Contribs:
    # join filers + filings + elections + transactions
    # transactions.filing_nid -> filings.filing_nid
    #   filings.filer_nid -> committees.filer_nid
    #     committees.Ballot_Measure_Election -> elections.Ballot_Measure_Election
    # where trans['transaction']['calTransactionType'] == 'F460A'
    with open('data/filings.json', encoding='utf8') as f:
        filings = FilingCollection(json.loads(f.read())).df

    with open('data/transactions.json', encoding='utf8') as f:
        transactions = TransactionCollection(json.loads(f.read())).df

    a_contributions = A_Contributions(transactions, filings, committees, elections).df
    print(a_contributions.head())

    with engine.connect() as conn:
        common_opts = {
            'index_label': 'id',
            'if_exists': 'replace'
        }
        elections.to_sql('elections', conn, **common_opts)
        committees.drop(columns=['filer_nid']).to_sql('committees', conn, **common_opts)
        a_contributions.to_sql('A_Contributions', conn, **common_opts)

if __name__ == '__main__':
    main()
