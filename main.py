""" main, to run everything """
from collections import Counter
from datetime import datetime
import json
import pandas as pd
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
    print('unique values of Support_Or_Oppose:', committees['Support_Or_Oppose'].unique().tolist())

    # A-Contribs:
    # join filers + filings + elections + transactions
    # transactions.filing_nid -> filings.filing_nid
    #   filings.filer_nid -> committees.filer_nid
    #     committees.Ballot_Measure_Election -> elections.Ballot_Measure_Election
    # where trans['transaction']['calTransactionType'] == 'F460A'
    with open('data/filings.json', encoding='utf8') as f:
        filings = FilingCollection(json.loads(f.read())).df

    with open('data/transactions.json', encoding='utf8') as f:
        records = json.loads(f.read())
        transactions = TransactionCollection(records)

        sup_opp_cd = [ t['Sup_Opp_Cd'] for t in transactions.data ]
        print('sup_opp_cd in records', len(sup_opp_cd), set(sup_opp_cd))
        print('ct of sup_opp_cd in records', Counter(sup_opp_cd))

        transactions = transactions.df
        print('sup_opp_cd in df', transactions['Sup_Opp_Cd'].unique().tolist())
        print('ct of sup_opp_cd in df', transactions.groupby(by=['Sup_Opp_Cd'], dropna=False).size())

    a_contributions = A_Contributions(transactions, filings, committees)
    a_contribs_df = a_contributions.df
    print(a_contribs_df.drop(columns=[
        'Form_Type',
        'tblCover_Offic_Dscr',
        'tblCover_Office_Cd',
        'XRef_SchNm',
        'XRef_Match',
        'Loan_Rate',
        'Int_CmteId',
        'Memo_Code',
        'Memo_RefNo',
        'BakRef_TID',
        'Bal_Juris',
        'Bal_Num',
        'Juris_Cd',
        'Juris_Dscr',
        'Dist_No',
        'Off_S_H_Cd',
        'Bal_Name',
        'tblDetlTran_Office_Cd',
        'tblDetlTran_Offic_Dscr'
    ]).sample(n=20))

    with engine.connect() as conn:
        common_opts = {
            'index_label': 'id',
            'if_exists': 'replace'
        }
        elections.to_sql('elections', conn, **common_opts)
        committees.drop(columns=['filer_nid']).to_sql('committees', conn, **common_opts)
        a_contributions.to_sql(conn, **common_opts)

if __name__ == '__main__':
    main()
