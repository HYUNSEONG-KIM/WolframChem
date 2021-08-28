from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr, Global
import pandas as pd
import pubchempy as pcp

session = None
pubchem = None
chemspider = None
openphacts = None
ChemicalData = None

def start_session(wolframpath=None, Pubchem=False, ChemSpider=False, OpenPHACTS= False ):
    global session, pubchem, chemspider, openphacts,ChemicalData
    
    if wolframpath == None:
        session = WolframLanguageSession()
    else:
        session = WolframLanguageSession(wolframpath)
    
    if Pubchem:
        session.evaluate(wlexpr("pubchem= ServiceConnect[\"PubChem\"]"))
        pubchem = session.function(wlexpr("pubchem"))
    if ChemSpider:
        session.evaluate(wlexpr("chemspider= ServiceConnect[\"ChemSpider\"]"))
        chemspider = session.function(wlexpr("chemspider"))
    if OpenPHACTS :
        session.evaluate(wlexpr("openphacts= ServiceConnect[\"OpenPHACTS\"]"))
        openphacts = session.function(wlexpr("openphacts"))
    ChemicalData = session.function(wlexpr("ChemicalData"))
    return 0

def end_session():
    session.terminate()
    
#Pubchem====================================================================================================================
def pub_get_compound_description():
    pass
def pub_get_compound_sids():
    pass
def pub_get_compound_aids():
    pass

def pub_get_cids(parameters, parametername="Name", as_dataframe=False, remainfirst=False, CIDType = False, Method=False):
    
        if isinstance(parameters,str):
            parameters = [parameters]
        searchdict = {parametername:parameters}
        
        if isinstance(CIDType,str):
            searchdict["CIDType"]=CIDType
        if isinstance(Method,str):
            searchdict["Method"] = Method
        
        result =pubchem("CompoundCID",searchdict)
        
        if as_dataframe:
            resultdf =pd.DataFrame([])
            for i,name in enumerate(parameters):
                if remainfirst:
                    resultdf=resultdf.append(pd.DataFrame({parametername:name,"CompoundID": [result[0][i]["CompoundID"][0]]}))
                else:
                    resultdf=resultdf.append(pd.DataFrame({parametername:name,"CompoundID": result[0][i]["CompoundID"]}))
                
            return resultdf

        if remainfirst:
            return [iter["CompoundID"][0] for iter in result[0]]
        else:
            return [iter["CompoundID"] for iter in result[0]]
        
def pub_get_compound_description():
    pass
def pub_get_compound_description():
    pass
def pub_get_compound_description():
    pass
def pub_get_compound_description():
    pass
def pub_get_compound_description():
    pass
def pub_get_compound_description():
    pass

def pub_get_compounds_full_records(parameters, parametername="Name", as_pcp_compound=False, as_dataframe=False, Method=False):
    
    if isinstance(parameters,str):
            parameters = [parameters]
        
    searchdict = {parametername:parameters}
        
    if isinstance(Method,str):
        searchdict["Method"] = Method
            
    fullrecord = pubchem("CompoundFullRecords")

    return [Compound(r) for r in fullrecord[0]]


class Compound:
    def __init__(self, record):
        """Initialize with a record dict from the PubChem PUG REST service.

        For most users, the ``from_cid()`` class method is probably a better way of creating Compounds.

        :param dict record: A compound record returned by the PubChem PUG REST service.
        """
        self._record = None
        self._atoms = {}
        self._bonds = {}
        self.record = record


#ChemSpider====================================================================================================================




#OpenPHACTS====================================================================================================================