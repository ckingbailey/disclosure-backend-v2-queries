""" This is the Committee model """
from .base import BaseModel
from . import base

print(dir(base))

class CommitteeCollection(BaseModel):
    """ A collection of committees """
    def __init__(self, data):
        super().__init__(data)
        self._dtypes = 'string'

    @classmethod
    def from_filers(cls, filer_records):
        """ Reshape NetFile filer records """
        return cls([
            {
                'Ballot_Measure_Election': f'oakland-{infl["electionDate"][:4]}',
                'Filer_ID': f['registrations'].get('CA SOS'),
                'Filer_NamL': infl['committeeName'],
                '_Status': 'INACTIVE' if f['isTerminated'] else 'ACTIVE',
                '_Committee_Type': f['committeeTypes'][0] if len(f['committeeTypes']) == 1 else 'Multiple Types',
                'Ballot_Measure': infl['measure'].get('measureNumber') if infl['measure'] else None,
                'Support_Or_Oppose': infl['doesSupport'],
                'Start_Date': infl['startDate'],
                'End_Date': infl['endDate'],
                'data_warning': None,
                'Make_Active': None
            } for f in filer_records
            for infl in f['electionInfluences']
        ])
