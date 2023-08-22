import pandas as pd

class CommitteeCollection:
    """ A collection of committees """
    def __init__(self, data):
        self._data = data
        self._df = None

    @property
    def data(self):
        return self._data
    
    @property
    def df(self):
        if self._df is None:
            self._df = pd.DataFrame(self._data).astype('string')

        return self._df

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
