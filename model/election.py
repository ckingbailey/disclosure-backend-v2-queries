"""
This is the Election model
"""
from datetime import datetime
from .base import BaseModel

class ElectionCollection(BaseModel):
    """ A collection of elections """
    def __init__(self, election_records):
        election_years = {}
        elections = []
        for el in election_records:
            caption = el['electionCaption'].split(' - ')
            election_date = datetime.strptime(caption[0], '%m/%d/%Y')
            election_year = caption[0][-4:]
            ordinal_day = self.ordinal(int(election_date.strftime('%-d')))
            long_date = datetime.strftime(election_date, f'%B {ordinal_day}, %Y')

            if election_year in election_years:
                election_years[election_year] += 1
            else:
                election_years[election_year] = 1

            elections.append({
                'location': 'Oakland',
                'date': el['electionDate'],
            })

        for el in elections:
            namef = f'oakland-%s{election_year}'
            titlef = f'Oakland {long_date} %sElection'

            if election_years[el['date'][:4]] > 1:
                name = (namef % (f'{datetime.strftime(election_date, "%B")}-')).lower()
                title = titlef % (f'{caption[1]} ')
            else:
                name = namef % ''
                title = titlef % ''

            el['name'] = name
            el['title'] = title

        super().__init__(elections)

    @staticmethod
    def ordinal(n):
        """
        Swiped from SO
        https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement#20007730
        """
        suffixes = 'tsnrhtdd'
        return f'{n}{suffixes[(n/10%10!=1)*(n%10<4)*n%10::4]}'