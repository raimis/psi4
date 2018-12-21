import pint
import pytest

from utils import *
from addons import *

pytestmark = pytest.mark.quick


_results = {
    "subject1":
    """
3 au

Co 0 0 0
H  2 0 0
h_OTher -2 0 0
""",
    "ans1_au":
    """3 au
CoH2
Co                    0.000000000000     0.000000000000     0.000000000000
H                     2.000000000000     0.000000000000     0.000000000000
H                    -2.000000000000    -0.000000000000     0.000000000000
""",
    "ans1_ang":
    """3
CoH2
Co                    0.000000000000     0.000000000000     0.000000000000
H                     1.058354421340     0.000000000000     0.000000000000
H                    -1.058354421340    -0.000000000000     0.000000000000
""",
    "ans1c_ang":
    """3
CoH2
59Co                      0.00000000         0.00000000         0.00000000
1H                        1.05835442         0.00000000         0.00000000
1H_other                 -1.05835442        -0.00000000         0.00000000
""",
    "ans1c_nm":
    """3 nm
CoH2
59Co                      0.00000000         0.00000000         0.00000000
1H                        0.10583544         0.00000000         0.00000000
1H_other                 -0.10583544        -0.00000000         0.00000000
""",
    "subject2":
    """
Co 0 0 0
no_reorient
--
@H  1.05835442134 0 0
h_OTher -1.05835442134 0 0
""",
    "ans2_au":
    """3 au
CoH2
Co                    0.000000000000     0.000000000000     0.000000000000
@H                    2.000000000000     0.000000000000     0.000000000000
H                    -2.000000000000     0.000000000000     0.000000000000
""",
    "ans2_ang":
    """3
CoH2
Co                    0.000000000000     0.000000000000     0.000000000000
Gh(1)                 1.058354421340     0.000000000000     0.000000000000
H                    -1.058354421340     0.000000000000     0.000000000000
""",
    "ans2c_ang":
    """2
CoH2
Co                    0.000000000000     0.000000000000     0.000000000000
H                    -1.058354421340     0.000000000000     0.000000000000
""",
    "ans2_cfour_ang":
    """auto-generated by qcelemental from molecule CoH2
Co                    0.000000000000     0.000000000000     0.000000000000
GH                    1.058354421340     0.000000000000     0.000000000000
H                    -1.058354421340     0.000000000000     0.000000000000
""",
    "ans2_nwchem_ang":
    """geometry units angstrom
Co                    0.000000000000     0.000000000000     0.000000000000
GH                    1.058354421340     0.000000000000     0.000000000000
H                    -1.058354421340     0.000000000000     0.000000000000

end
""",
    "subject3":
    """
# HSG-4
-1 1
C   17.05600       28.65300       6.834000
H   17.72900       28.22900       7.569000
H   16.32100       29.27500       7.342000
C   16.35100       27.45400       6.256000
O   16.17800       26.43900       6.902000
O   15.98200       27.55700       4.965000
H   15.73800       26.67800       4.650000
C   16.27300       25.57900       0.088000
H   16.75700       24.66100      -0.278000
H   15.39700       25.75100      -0.577000
C   15.87600       25.38300       1.569000
O   16.42900       26.07300       2.466000
O   14.98200       24.56700       1.861000
H   17.61665       29.26091       6.108662
H   16.97158       26.42544       0.013713047
--
0 1
C   14.25800       24.02900       5.093000
O   15.51000       24.53800       4.641000
H   15.42000       24.70300       3.667000
H   14.02700       23.02800       4.754000
H   13.45976       24.69373       4.731124
H   14.36576       23.85731       6.174161
units angstrom
""",
    "ans3_mol":
    """default
  Generated by xyz2mol

 21 18  0  0  0  0  0  0  0  0999 V2000
    1.1827    2.6495    2.7573 C   0  0  0  0  0
    1.8557    2.2255    3.4923 H   0  0  0  0  0
    0.4477    3.2715    3.2653 H   0  0  0  0  0
    0.4777    1.4505    2.1793 C   0  0  0  0  0
    0.3047    0.4355    2.8253 O   0  0  0  0  0
    0.1087    1.5535    0.8883 O   0  0  0  0  0
   -0.1353    0.6745    0.5733 H   0  0  0  0  0
    0.3997   -0.4245   -3.9887 C   0  0  0  0  0
    0.8837   -1.3425   -4.3547 H   0  0  0  0  0
   -0.4763   -0.2525   -4.6537 H   0  0  0  0  0
    0.0027   -0.6205   -2.5077 C   0  0  0  0  0
    0.5557    0.0695   -1.6107 O   0  0  0  0  0
   -0.8913   -1.4365   -2.2157 O   0  0  0  0  0
    1.7434    3.2574    2.0319 H   0  0  0  0  0
    1.0983    0.4219   -4.0630 H   0  0  0  0  0
   -1.6153   -1.9745    1.0163 C   0  0  0  0  0
   -0.3633   -1.4655    0.5643 O   0  0  0  0  0
   -0.4533   -1.3005   -0.4097 H   0  0  0  0  0
   -1.8463   -2.9755    0.6773 H   0  0  0  0  0
   -2.4135   -1.3098    0.6544 H   0  0  0  0  0
   -1.5075   -2.1462    2.0974 H   0  0  0  0  0
  1  2  1  0  0  0
  1  3  1  0  0  0
  1  4  1  0  0  0
  1 14  1  0  0  0
  4  5  2  0  0  0
  4  6  1  0  0  0
  6  7  1  0  0  0
  8  9  1  0  0  0
  8 10  1  0  0  0
  8 11  1  0  0  0
  8 15  1  0  0  0
 11 12  2  0  0  0
 11 13  1  0  0  0
 16 17  1  0  0  0
 16 19  1  0  0  0
 16 20  1  0  0  0
 16 21  1  0  0  0
 17 18  1  0  0  0
M  END
""",
}


@pytest.mark.parametrize("inp", [
    ("subject1", {'dtype': 'xyz', 'units': 'kg', 'prec': 8, 'atom_format': '{elea}{elem}{elbl}'}),
])  # yapf: disable
def test_to_string_error(inp):
    mol = qcdb.Molecule(_results[inp[0]])

    with pytest.raises(pint.errors.DimensionalityError):
        mol.to_string(**inp[1])


@pytest.mark.parametrize("inp,expected", [
    (("subject1", {'dtype': 'xyz', 'units': 'Bohr'}), "ans1_au"),
    (("subject1", {'dtype': 'xyz', 'units': 'Angstrom'}), "ans1_ang"),
    (("subject1", {'dtype': 'xyz', 'prec': 8, 'atom_format': '{elea}{elem}{elbl}'}), "ans1c_ang"),
    (("subject2", {'dtype': 'xyz', 'units': 'Bohr'}), "ans2_au"),
    (("subject2", {'dtype': 'xyz', 'units': 'Angstrom', 'ghost_format': 'Gh({elez})'}), "ans2_ang"),
    (("subject2", {'dtype': 'xyz', 'units': 'angstrom', 'ghost_format': ''}), "ans2c_ang"),
    (("subject2", {'dtype': 'cfour'}), "ans2_cfour_ang"),
    (("subject2", {'dtype': 'nwchem'}), "ans2_nwchem_ang"),
    (("subject1", {'dtype': 'xyz', 'units': 'nm', 'prec': 8, 'atom_format': '{elea}{elem}{elbl}'}), "ans1c_nm"),
])  # yapf: disable
def test_to_string_xyz_qmol(inp, expected):
    mol = qcdb.Molecule(_results[inp[0]])
    smol = mol.to_string(**inp[1])

    assert compare_strings(_results[expected], smol, tnm())


@using_psi4
@pytest.mark.parametrize("inp,expected", [
    (("subject1", {'dtype': 'xyz', 'units': 'Bohr'}), "ans1_au"),
    (("subject1", {'dtype': 'xyz', 'units': 'Angstrom'}), "ans1_ang"),
    (("subject1", {'dtype': 'xyz', 'prec': 8, 'atom_format': '{elea}{elem}{elbl}'}), "ans1c_ang"),
    (("subject2", {'dtype': 'xyz', 'units': 'Bohr'}), "ans2_au"),
    (("subject2", {'dtype': 'xyz', 'units': 'Angstrom', 'ghost_format': 'Gh({elez})'}), "ans2_ang"),
    (("subject2", {'dtype': 'xyz', 'units': 'angstrom', 'ghost_format': ''}), "ans2c_ang"),
    (("subject2", {'dtype': 'cfour'}), "ans2_cfour_ang"),
    (("subject2", {'dtype': 'nwchem'}), "ans2_nwchem_ang"),
    (("subject1", {'dtype': 'xyz', 'units': 'nm', 'prec': 8, 'atom_format': '{elea}{elem}{elbl}'}), "ans1c_nm"),
])  # yapf: disable
def test_to_string_xyz_pmol(inp, expected):
    import psi4

    mol = psi4.core.Molecule.from_string(_results[inp[0]])
    smol = mol.to_string(**inp[1])

    assert compare_strings(_results[expected], smol, tnm())

@pytest.mark.parametrize("inp,expected", [
    (("subject3", {}), "ans3_mol"),
])  # yapf: disable
def test_to_string_mol_qmol(inp, expected):
    mol = qcdb.Molecule(_results[inp[0]])
    smol = mol.format_molecule_for_mol(**inp[1])

    assert compare_strings(_results[expected], smol, tnm())


@using_psi4
@pytest.mark.parametrize("inp,expected", [
    (("subject3", {}), "ans3_mol"),
])  # yapf: disable
def test_to_string_mol_pmol(inp, expected):
    mol = psi4.core.Molecule.from_string(_results[inp[0]])
    smol = mol.format_molecule_for_mol(**inp[1])

    assert compare_strings(_results[expected], smol, tnm())


def test_provenance_connectivity_setting():
    he3 = psi4.geometry("""
    He
    He 1 3.
    He 1 3. 2 120.
    units au
    """)
    dhe3 = he3.to_dict()

    conn1 = [(0, 1, 2.0), (0, 2, 1.0)]
    prov1 = {'creator': 'hello!', 'version': '33', 'routine': 'hello.main'}
    dhe3['connectivity'] = conn1
    dhe3['provenance'] = prov1

    phe3 = psi4.core.Molecule.from_dict(dhe3)
    qhe3 = qcdb.Molecule.from_dict(dhe3)

    p2he3 = phe3.clone()
    q2he3 = qhe3.clone()

    conn2 = [(0, 1, 2.0), (0, 2, 3.0)]
    prov2 = {'creator': 'goodbye!', 'version': '44', 'routine': 'goodbye.main'}

    assert phe3.to_dict()['connectivity'] == conn1
    assert qhe3.to_dict()['connectivity'] == conn1
    assert phe3.to_dict()['provenance'] == prov1
    assert qhe3.to_dict()['provenance'] == prov1

    phe3.set_connectivity(conn2)
    qhe3.set_connectivity(conn2)
    phe3.set_provenance(prov2)
    qhe3.set_provenance(prov2)

    assert phe3.connectivity() == conn2
    assert qhe3.connectivity() == conn2
    assert phe3.provenance() == prov2
    assert qhe3.provenance() == prov2

    assert phe3.to_dict()['connectivity'] == conn2
    assert qhe3.to_dict()['connectivity'] == conn2
    assert phe3.to_dict()['provenance'] == prov2
    assert qhe3.to_dict()['provenance'] == prov2

    assert p2he3.to_dict()['connectivity'] == conn1
    assert q2he3.to_dict()['connectivity'] == conn1
    assert p2he3.to_dict()['provenance'] == prov1
    assert q2he3.to_dict()['provenance'] == prov1

