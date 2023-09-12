""" This is the Committee model """
from typing import List
import pandas as pd
from . import base

class CommitteeCollection(base.BaseModel):
    """ A collection of committees """
    def __init__(self, data:List[dict]):
        super().__init__(data)
        self._dtypes = {
            'filer_nid': int,
            'Ballot_Measure_Election': 'string',
            'Filer_ID': 'string',
            'Filer_NamL': 'string',
            '_Status': 'string',
            '_Committee_Type': 'string',
            'Ballot_Measure': 'string',
            'Support_Or_Oppose': 'string',
            'candidate_controlled_id': 'string',
            'Start_Date': 'string',
            'End_Date': 'string',
            'data_warning': 'string',
            'Make_Active': 'string'
        }

    @classmethod
    def from_filers(cls, filer_records:List[dict], elections:pd.DataFrame):
        """ Reshape NetFile filer records """
        empty_election_influence = {
            'electionDate': None,
            'measure': None,
            'doesSupport': None,
            'startDate': None,
            'endDate': None
        }
        return cls([
            {
                'filer_nid': f['filerNid'],
                'Ballot_Measure_Election': [ *elections[elections['date'] == infl['electionDate']]['name'].array, None ][0],
                'Filer_ID': f['registrations'].get('CA SOS'),
                'Filer_NamL': infl.get('committeeName', f['filerName']),
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
            for infl in (
                f['electionInfluences']
                if f['electionInfluences']
                else [ empty_election_influence ]
            )
            if f['registrations'].get('CA SOS')
        ])
