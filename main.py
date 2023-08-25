""" main, to run everything """
import json
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
    with open('data/filers.json', encoding='utf8') as f:
        filers = json.loads(f.read())
    committees = CommitteeCollection.from_filers(filers)

    print('table fields:', [
        'Ballot_Measure_Election',
        'Filer_ID',
        'Filer_NamL',
        '_Status',
        '_Committee_Type',
        'Ballot_Measure',
        'Support_Or_Oppose',
        'candidate_controlled_id',
        'Start_Date',
        'End_Date',
        'data_warning',
        'Make_Active',
        'id'
    ])

    committees_df = committees.df
    fops_filers = committees_df.loc[committees_df['Filer_NamL'].str.contains('Friends of Oakland Public Schools')]
    print(fops_filers)

    with open('data/elections.json', encoding='utf8') as f:
        elections_json = json.loads(f.read())

    elections = ElectionCollection(elections_json)
    print(elections.data)

if __name__ == '__main__':
    main()
