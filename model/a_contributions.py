"""
Schedule A, Contributions
Hopefully this can be joined with other Schedule classes into a single Transaction class
"""
import pandas as pd
from .base import BaseModel

class A_Contributions(BaseModel):
    """
    Each record represents Schedule A - Contributions from form 460
    """
    def __init__(
        self,
        transactions:pd.DataFrame,
        filings:pd.DataFrame,
        committees:pd.DataFrame,
        elections: pd.DataFrame
    ):
        f460a = transactions.loc[transactions['cal_tran_type'] == 'F460A'].drop(
            columns=['cal_tran_type']
        ).merge(filings, on='filing_nid', how='left').drop(
            columns=['filing_nid']
        ).rename(
            columns={'RptNum': 'Report_Num'}
        ).merge(committees, on='filer_nid', how='left').drop(
            columns=[
                'filer_nid',
                '_Status',
                'Ballot_Measure',
                'Support_Or_Oppose',
                'candidate_controlled_id',
                'Start_Date',
                'End_Date',
                'data_warning',
                'Make_Active'
            ]
        ).rename(
            columns={'_Committee_Type': 'Committee_Type'}
        ).merge(elections, left_on='Ballot_Measure_Election', right_on='name', how='left').drop(
            columns=[
                'Ballot_Measure_Election',
                'title',
                'name',
                'location'
            ]
        ).rename(columns={'date': 'Elect_Date'})

        f460a[['Form_Type','tblCover_Offic_Dscr','tblCover_Office_Cd']] = ['00:00:00', '', '']

        super().__init__(f460a)

        self._dtypes = 'string'
