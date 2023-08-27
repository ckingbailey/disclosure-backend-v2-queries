""" This is the Committee model """
from typing import List
import pandas as pd
from . import base

class CommitteeCollection(base.BaseModel):
    """ A collection of committees """
    def __init__(self, data:List[dict]):
        super().__init__(data)
        self._dtypes = 'string'

    @classmethod
    def from_filers(cls, filer_records:List[dict], elections:pd.DataFrame):
        """ Reshape NetFile filer records """
        return cls([
            {
                'filer_nid': f['filerNid'],
                'Ballot_Measure_Election': elections[elections['date'] == infl['electionDate']]['name'].array[0],
                'Filer_ID': f['registrations'].get('CA SOS'),
                'Filer_NamL': infl['committeeName'],
                '_Status': 'INACTIVE' if f['isTerminated'] else 'ACTIVE',
                '_Committee_Type': (f['committeeTypes'][0]
                                    if len(f['committeeTypes']) == 1
                                    else 'Multiple Types'),
                'Ballot_Measure': infl['measure'].get('measureNumber') if infl['measure'] else None,
                'Support_Or_Oppose': infl['doesSupport'],
                'candidate_controlled_id': None, # TODO: link to candidates if candidate committee
                'Start_Date': infl['startDate'],
                'End_Date': infl['endDate'],
                'data_warning': None,
                'Make_Active': None
            } for f in filer_records
            for infl in f['electionInfluences']
        ])
