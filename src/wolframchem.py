from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr, Global
import pandas as pd

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


#Pubchem-----------------------------------------------------------------------------------------------------
class Pubchem:
    def __init__(self):
        pass
    @classmethod
    def get_compound_description(cls,parameters, parametername="Name", as_dataframe=False, Method=False, InterpretEntities = False):
        if parametername == "Formula" and Method != "FormulaSearch":
            raise ValueError("Formula only vaild for \"FormulaSearch\" method.")

        if isinstance(parameters,str):
            parameters = [parameters]
        searchdict = {parametername:parameters}

        if isinstance(Method,str):
            searchdict["Method"] = Method


        result = pubchem("CompoundDescription" ,searchdict)
    @classmethod
    def get_compound_sids(cls,parameters, parametername="Name", as_dataframe=False, SIDType = False,  Method=False):
        
        if parametername == "Formula" and Method != "FormulaSearch":
            raise ValueError("Formula only vaild for \"FormulaSearch\" method.")
        
        if isinstance(parameters,str):
            parameters = [parameters]
        searchdict = {parametername:parameters}

        if isinstance(SIDType,str):
            searchdict["SIDType"] = SIDType
        if isinstance(Method,str):
            searchdict["Method"] = Method
        result = pubchem("CompoundDescription" ,searchdict)

    @classmethod
    def get_compound_aids(cls,parameters, parametername="Name", as_dataframe=False, AIDType = False, Method=False):
        
        if parametername == "Formula" and Method != "FormulaSearch":
            raise ValueError("Formula only vaild for \"FormulaSearch\" method.")
        if isinstance(parameters,str):
            parameters = [parameters]
        searchdict = {parametername:parameters}

        if isinstance(AIDType,str):
            searchdict["AIDType"] = AIDType
        if isinstance(Method,str):
            searchdict["Method"] = Method
        result = pubchem("CompoundDescription" ,searchdict)

    @classmethod
    def get_cids(cls,parameters, parametername="Name", as_dataframe=False, remainfirst=False, CIDType = False, Method=False):
        
        if parametername == "Formula" and Method != "FormulaSearch":
            raise ValueError("Formula only vaild for \"FormulaSearch\" method.")
        if isinstance(parameters,str):
            parameters = [parameters]
        searchdict = {parametername:parameters}
        
        if isinstance(CIDType,str):
            searchdict["CIDType"] = CIDType
        if isinstance(Method,str):
            searchdict["Method"] = Method
        
        result =pubchem("CompoundCID",searchdict)
        
        if as_dataframe:
            resultdf =pd.DataFrame([])
            for i,name in enumerate(parameters):
                if remainfirst:
                    resultdf=resultdf.append(pd.DataFrame({parametername:name,"CompoundID": [result[0][i]["CompoundID"][0]]})).reset_index(drop=True)
                else:
                    resultdf=resultdf.append(pd.DataFrame({parametername:name,"CompoundID": result[0][i]["CompoundID"]})).reset_index(drop=True)
                
            return resultdf

        if remainfirst:
            return [iter["CompoundID"][0] for iter in result[0]]
        else:
            return [iter["CompoundID"] for iter in result[0]]      
    @classmethod
    def get_compound_properties(cls,parameters, parametername="Name", as_dataframe=False, Property = False, Method=False):
        
        if parametername == "Formula" and Method != "FormulaSearch":
            raise ValueError("Formula only vaild for \"FormulaSearch\" method.")
        if isinstance(parameters,str):
            parameters = [parameters]
        searchdict = {parametername:parameters}

        if isinstance(Property, list):
            searchdict["Property"] = Property
        if isinstance(Method,str):
            searchdict["Method"] = Method
        result = pubchem("CompoundDescription" ,searchdict)
    @classmethod
    def get_compound_cross_references(cls,parameters, parametername="Name", as_dataframe=False, CrossReference=False, Method=False):
        if isinstance(parameters,str):
            parameters = [parameters]
        searchdict = {parametername:parameters}

        if isinstance(CrossReference, list):
            searchdict["CrossReference"] = CrossReference
        if isinstance(Method,str):
            searchdict["Method"] = Method
        result = pubchem("CompoundDescription" ,searchdict)
    @classmethod
    def get_compound_image(cls,parameters, parametername="Name", as_dataframe=False, ImageType="2D", ImageSize=, Method=False):
        if isinstance(parameters,str):
            parameters = [parameters]
        searchdict = {parametername:parameters}

        if isinstance(Method,str):
            searchdict["Method"] = Method
        result = pubchem("CompoundDescription" ,searchdict)
    @classmethod
    def get_compound_sdf(cls,parameters, parametername="Name", as_dataframe=False, Method=False):
        if isinstance(parameters,str):
            parameters = [parameters]
        searchdict = {parametername:parameters}

        if isinstance(Method,str):
            searchdict["Method"] = Method
        result = pubchem("CompoundDescription" ,searchdict)
    @classmethod
    def get_compounds(cls,parameters, parametername="Name", as_pcp_compound=False, as_dataframe=False, Method=False):
    
        if isinstance(parameters,str):
                parameters = [parameters]

        searchdict = {parametername:parameters}

        if isinstance(Method,str):
            searchdict["Method"] = Method

        fullrecord = pubchem("CompoundFullRecords")

        return [Compound(r) for r in fullrecord[0]]
    @classmethod
    def get_compound_assay_summary(cls,parameters, parametername="Name", as_dataframe=False, Method=False):
        if isinstance(parameters,str):
            parameters = [parameters]
        searchdict = {parametername:parameters}

        if isinstance(Method,str):
            searchdict["Method"] = Method
        result = pubchem("CompoundDescription" ,searchdict)

#ChemSpider-----------------------------------------------------------------------------------------------------

class ChemSpider:
    def __init__(self):
        pass
#OpenPHACTS-----------------------------------------------------------------------------------------------------

class OpenPHACTS:
    def __init__(self):
        pass


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

    def cid(self):
        pass
    def elements(self):
        pass
    def bonds(self):
        pass
    def synonyms(self):
        pass
    def sids(self):
        pass
    def aids(self):
        pass
    def coordinate_type(self):
        pass
    def charge(self):
        pass
    def molecular_formula(self):
        pass
    def molecular_weight(self):
        pass
    def canonical_smiles(self):
        pass
    def isomeric_smiles(self):
        pass
    def inchi(self):
        pass
    def inchikey(self):
        pass
    def iupac_name(self):
        pass
    def xlogp(self):
        pass
    def exact_mass(self):
        pass
    def monoisotopic_mass(self):
        pass
    def tpsa(self):
        pass
    def complexity(self):
        pass
    def h_bond_donor_count(self):
        pass
    def h_bond_acceptor_count(self):
        pass
    def rotatable_bond_count(self):
        pass
    def fingerprint(self):
        pass
    def cactvs_fingerprint(self):
        pass
    def heavy_atom_count(self):
        pass
    def isotope_atom_count(self):
        pass
    def atom_stereo_count(self):
        pass
    def defined_atom_stereo_count(self):
        pass
    def undefined_atom_stereo_count(self):
        pass
    def bond_stereo_count(self):
        pass
    def defined_bond_stereo_count(self):
        pass
    def undefined_bond_stereo_count(self):
        pass
    def covalent_unit_count(self):
        pass
    def volume_3d(self):
        pass
    def multipoles_3d(self):
        pass
    def conformer_rmsd_3d(self):
        pass
    def effective_rotor_count_3d(self):
        pass
    def pharmacophore_features_3d(self):
        pass
    def mmff94_partial_charges_3d(self):
        pass
    def mmff94_energy_3d(self):
        pass
    def conformer_id_3d(self):
        pass
    def shape_selfoverlap_3d(self):
        pass
    def feature_selfoverlap_3d(self):
        pass
    def shape_fingerprint_3d(self):
        pass

class Substance:
    def __init__(self):
        pass

    def sid(self):
        pass
    def synonyms(self):
        pass
    def source_name(self):
        pass
    def source_id(self):
        pass
    def standardized_cid(self):
        pass
    def standardized_compound(self):
        pass
    def deposited_compound(self):
        pass
    def cids(self):
        pass
    def aids(self):
        pass

class Assay:
    def __init__(self):
        pass
    def aid(self):
        pass
    def name(self):
        pass
    def description(self):
        pass
    def project_category(self):
        pass
    def comments(self):
        pass
    def results(self):
        pass
    def target(self):
        pass
    def revision(self):
        pass
    def aid_version(self):
        pass



#ChemSpider====================================================================================================================




#OpenPHACTS====================================================================================================================