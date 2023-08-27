""" Filings """
from .base import BaseModel

class FilingCollection(BaseModel):
    """ A collection of filings """
    def __init__(self, filings):
        super().__init__([
            {
                'filer_nid': f['filerMeta']['filerId'],
                'Rpt_Num': f['filingMeta']['amendmentSequence'],
                'Rpt_Date': f['filingMeta']['legalFilingDate'],
                'From_Date': f['filingMeta']['startDate'],
                'Thru_Date': f['filingMeta']['endDate'],
            } for f in filings
        ])

        self._dtypes = {
            'filer_nid': int,
            'Rpt_Num': int,
            'Rpt_Date': 'string',
            'From_Date': 'string',
            'Thru_Date': 'string'
        }
