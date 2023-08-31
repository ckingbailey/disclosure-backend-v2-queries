""" Transcations """
from .base import BaseModel

class TransactionCollection(BaseModel):
    """ A collection of transactions """
    def __init__(self, transactions):
        super().__init__([
            {
                'filing_nid': t['filingNid'], # This will be used to join to filings
                'Rec_Type': (tran := t['transaction'])['recType'],
                'Tran_ID': tran['tranId'],
                'cal_tran_type': tran['calTransactionType'],
                'Entity_Cd': tran['entityCd'],
                'Tran_NamL': tran['tranNamL'],
                'Tran_NamF': tran['tranNamF'],
                'Tran_NamT': tran['tranNamT'],
                'Tran_NamS': tran['tranNamS'],
                'Tran_Adr1': tran['tranAdr1'],
                'Tran_Adr2': tran['tranAdr2'],
                'Tran_City': tran['tranCity'],
                'Tran_State': tran['tranST'],
                'Tran_Zip4': tran['tranZip4'],
                'Tran_Emp': tran['tranEmp'],
                'Tran_Occ': tran['tranOcc'],
                'Tran_Self': tran['tranSelf'],
                'Tran_Type': tran['tranType'],
                'Tran_Date': tran['tranDate'],
                'Tran_Date1': tran['tranDate1'],
                'Tran_Amt1': tran['tranAmt1'],
                'Tran_Amt2': tran['tranAmt2'],
                'Tran_Dscr': tran['tranDscr'],
                'Cmte_ID': tran['cmteId'],
                'Tres_NamL': tran['tresNamL'],
                'Tres_NamF': tran['tresNamF'],
                'Tres_NamT': tran['tresNamT'],
                'Tres_NamS': tran['tresNamS'],
                'Tres_Adr1': tran['tresAdr1'],
                'Tres_Adr2': tran['tresAdr2'],
                'Tres_City': tran['tresCity'],
                'Tres_State': tran['tresST'],
                'Tres_Zip': tran['tresZip4'],
                'Intr_NamL': tran['intrNamL'],
                'Intr_NamF': tran['intrNamF'],
                'Intr_NamT': tran['intrNamT'],
                'Intr_NamS': tran['intrNamS'],
                'Intr_Adr1': tran['intrAdr1'],
                'Intr_Adr2': tran['intrAdr2'],
                'Intr_City': tran['intrCity'],
                'Intr_State': tran['intrST'],
                'Intr_Zip4': tran['intrZip4'],
                'Intr_Emp': tran['intrEmp'],
                'Intr_Occ': tran['intrOcc'],
                'Intr_Self': tran['intrSelf'],
                'Cand_NamL': tran['candNamL'],
                'Cand_NamF': tran['candNamF'],
                'Cand_NamT': tran['candNamT'],
                'Cand_NamS': tran['candNamS'],
                'tblDetlTran_Office_Cd': tran['officeCd'],
                'tblDetlTran_Offic_Dscr': tran['officeDscr'],
                'Juris_Cd': tran['jurisCd'],
                'Juris_Dscr': tran['jurisDscr'],
                'Dist_No': tran['distNo'],
                'Off_S_H_Cd': tran['offSHCd'],
                'Bal_Name': tran['balName'],
                'Bal_Num': tran['balNum'],
                'Bal_Juris': tran['balJuris'],
                'Sup_Opp_Cd': tran['supOppCd'],
                'Memo_Code': tran['memoCode'],
                'Memo_RefNo': tran['memoRefNo'],
                'BakRef_TID': tran['bakRefTID'],
                'XRef_SchNm': tran['xrefSchNum'],
                'XRef_Match': tran['xrefMatch'],
                'Loan_Rate': tran['loanRate'],
                'Int_CmteId': tran['intCmteId']
            } for t in transactions
        ])

        self._dtypes = {
            'filing_nid': 'string',
            'Rec_Type': 'string',
            'Tran_ID': 'string',
            'cal_tran_type': 'string',
            'Entity_Cd': 'string',
            'Tran_NamL': 'string',
            'Tran_NamF': 'string',
            'Tran_NamT': 'string',
            'Tran_NamS': 'string',
            'Tran_Adr1': 'string',
            'Tran_Adr2': 'string',
            'Tran_City': 'string',
            'Tran_State': 'string',
            'Tran_Zip4': 'string',
            'Tran_Emp': 'string',
            'Tran_Occ': 'string',
            'Tran_Self': bool,
            'Tran_Type': 'string',
            'Tran_Date': 'string',
            'Tran_Date1': 'string',
            'Tran_Amt1': float,
            'Tran_Amt2': float,
            'Tran_Dscr': 'string',
            'Cmte_ID': 'string',
            'Tres_NamL': 'string',
            'Tres_NamF': 'string',
            'Tres_NamT': 'string',
            'Tres_NamS': 'string',
            'Tres_Adr1': 'string',
            'Tres_Adr2': 'string',
            'Tres_City': 'string',
            'Tres_State': 'string',
            'Tres_Zip': 'string',
            'Intr_NamL': 'string',
            'Intr_NamF': 'string',
            'Intr_NamT': 'string',
            'Intr_NamS': 'string',
            'Intr_Adr1': 'string',
            'Intr_Adr2': 'string',
            'Intr_City': 'string',
            'Intr_State': 'string',
            'Intr_Zip4': 'string',
            'Intr_Emp': 'string',
            'Intr_Occ': 'string',
            'Intr_Self': bool,
            'Cand_NamL': 'string',
            'Cand_NamF': 'string',
            'Cand_NamT': 'string',
            'Cand_NamS': 'string',
            'tblDetlTran_Office_Cd': 'string',
            'tblDetlTran_Offic_Dscr': 'string',
            'Juris_Cd': 'string',
            'Juris_Dscr': 'string',
            'Dist_No': 'string',
            'Off_S_H_Cd': 'string',
            'Bal_Name': 'string',
            'Bal_Num': 'string',
            'Bal_Juris': 'string',
            'Sup_Opp_Cd': 'string',
            'Memo_Code': 'string',
            'Memo_RefNo': 'string',
            'BakRef_TID': 'string',
            'XRef_SchNm': 'string',
            'XRef_Match': 'string',
            'Loan_Rate': 'string',
            'Int_CmteId': 'Int64'
        }
