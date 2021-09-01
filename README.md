# WolframChem
 Wolfram Chemical data base python warrper. This module provides chemical data searching function through Wolfram language service. It needs Wolfram engine and Wolfram Client Library for Python. 

 Avaliable(A) and Futher(F) supported data source

 * Pubchem(A)
 * Chemspider(F)
 * OpenPACTS(F)
 * Wolfram ChemicalData(A)

Using pandas, some functions provides option `as_datafram` for comfortable data processing. 

If you want to use those database directly with `REST API` they provide. I recommend `pubchempy`, `ChemSpipy` and `O

## Get Pubchem `cids` with `names`

use `cids_from_names.py`

```python
import cids_from_names as wch

wch.start_session("{wolframe engine path}",Pubchem=True)
```

```python
wch.Pubchem.get_compound_cids(["Ambroxol","CYANOCOBALAMIN"],as_dataframe=True,remainfirst=False)
```
output:

```
	Name	CompoundID
0	Ambroxol	2132
1	CYANOCOBALAMIN	5311498
2	CYANOCOBALAMIN	46853873
3	CYANOCOBALAMIN	70678590
4	CYANOCOBALAMIN	11970261
5	CYANOCOBALAMIN	24892734
6	CYANOCOBALAMIN	25102581
7	CYANOCOBALAMIN	54605677
8	CYANOCOBALAMIN	129627537
9	CYANOCOBALAMIN	139030973
10	CYANOCOBALAMIN	5460135
11	CYANOCOBALAMIN	6474318
12	CYANOCOBALAMIN	23806828
13	CYANOCOBALAMIN	25195380
14	CYANOCOBALAMIN	44176380
15	CYANOCOBALAMIN	91898871
16	CYANOCOBALAMIN	118701720
17	CYANOCOBALAMIN	129627679
18	CYANOCOBALAMIN	137332389
19	CYANOCOBALAMIN	152743321
```
remainfirst True (default = False)

```python
wch.Pubchem.get_compound_cids(["Ambroxol","CYANOCOBALAMIN"],as_dataframe=True,remainfirst=True)
```
output:

```
	Name	CompoundID
0	Ambroxol	2132
0	CYANOCOBALAMIN	5311498
```

as data frame False (default = False)

```python
wch.Pubchem.get_compound_cids(["Ambroxol","CYANOCOBALAMIN"],as_dataframe=False,remainfirst=False)
```
output:

```
[(2132,),
 (5311498,
  46853873,
  70678590,
  11970261,
  24892734,
  25102581,
  54605677,
  129627537,
  139030973,
  5460135,
  6474318,
  23806828,
  25195380,
  44176380,
  91898871,
  118701720,
  129627679,
  137332389,
  152743321)]
```

## Use Wolfram ChemicalData

See [Wolfram ChemicalData](https://reference.wolfram.com/language/ref/ChemicalData.html)

you can use same interface with `ChemicalData[]` use 
```python
wch.ChemicalData()
```
Example

```python
wch.ChemicalData("LTryptophan", "SMILES")
```
output
```
'C1=CC=C2C(=C1)C(=CN2)CC(C(=O)[O-])[NH3+]'
```
after finishing search, you must terminate session for wolfram engine

```python
wch.end_session()
```
