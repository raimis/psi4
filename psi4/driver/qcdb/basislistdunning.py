#
# @BEGIN LICENSE
#
# Psi4: an open-source quantum chemistry software package
#
# Copyright (c) 2007-2019 The Psi4 Developers.
#
# The copyrights for code used from other parties are included in
# the corresponding files.
#
# This file is part of Psi4.
#
# Psi4 is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3.
#
# Psi4 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with Psi4; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# @END LICENSE
#

"""Module (auto-generated from make_dunning.pl script)
with commands building :py:class:`~basislist.BasisFamily` objects that
encode the Dunning basis set orbital definitions in
:source:`lib/basis/NOTES` and fitting bases designed for those
orbital bases.

"""

from .basislist import *


def load_basfam_dunning():

    basis_ccpvdz = BasisFamily('cc-pVDZ', zeta=2)
    basisfamily_list.append(basis_ccpvdz)
    basis_ccpv_dpd_z = BasisFamily('cc-pV(D+d)Z', zeta=2)
    basisfamily_list.append(basis_ccpv_dpd_z)
    basis_ccpcvdz = BasisFamily('cc-pCVDZ', zeta=2)
    basisfamily_list.append(basis_ccpcvdz)
    basis_ccpcv_dpd_z = BasisFamily('cc-pCV(D+d)Z', zeta=2)
    basisfamily_list.append(basis_ccpcv_dpd_z)
    basis_ccpwcvdz = BasisFamily('cc-pwCVDZ', zeta=2)
    basisfamily_list.append(basis_ccpwcvdz)
    basis_ccpwcv_dpd_z = BasisFamily('cc-pwCV(D+d)Z', zeta=2)
    basisfamily_list.append(basis_ccpwcv_dpd_z)
    basis_augccpvdz = BasisFamily('aug-cc-pVDZ', zeta=2)
    basisfamily_list.append(basis_augccpvdz)
    basis_augccpv_dpd_z = BasisFamily('aug-cc-pV(D+d)Z', zeta=2)
    basisfamily_list.append(basis_augccpv_dpd_z)
    basis_augccpcvdz = BasisFamily('aug-cc-pCVDZ', zeta=2)
    basisfamily_list.append(basis_augccpcvdz)
    basis_augccpcv_dpd_z = BasisFamily('aug-cc-pCV(D+d)Z', zeta=2)
    basisfamily_list.append(basis_augccpcv_dpd_z)
    basis_augccpwcvdz = BasisFamily('aug-cc-pwCVDZ', zeta=2)
    basisfamily_list.append(basis_augccpwcvdz)
    basis_augccpwcv_dpd_z = BasisFamily('aug-cc-pwCV(D+d)Z', zeta=2)
    basisfamily_list.append(basis_augccpwcv_dpd_z)
    basis_heavyaugccpvdz = BasisFamily('heavy-aug-cc-pVDZ', zeta=2)
    basisfamily_list.append(basis_heavyaugccpvdz)
    basis_heavyaugccpv_dpd_z = BasisFamily('heavy-aug-cc-pV(D+d)Z', zeta=2)
    basisfamily_list.append(basis_heavyaugccpv_dpd_z)
    basis_heavyaugccpcvdz = BasisFamily('heavy-aug-cc-pCVDZ', zeta=2)
    basisfamily_list.append(basis_heavyaugccpcvdz)
    basis_heavyaugccpcv_dpd_z = BasisFamily('heavy-aug-cc-pCV(D+d)Z', zeta=2)
    basisfamily_list.append(basis_heavyaugccpcv_dpd_z)
    basis_heavyaugccpwcvdz = BasisFamily('heavy-aug-cc-pwCVDZ', zeta=2)
    basisfamily_list.append(basis_heavyaugccpwcvdz)
    basis_heavyaugccpwcv_dpd_z = BasisFamily('heavy-aug-cc-pwCV(D+d)Z', zeta=2)
    basisfamily_list.append(basis_heavyaugccpwcv_dpd_z)
    basis_junccpvdz = BasisFamily('jun-cc-pVDZ', zeta=2)
    basisfamily_list.append(basis_junccpvdz)
    basis_junccpv_dpd_z = BasisFamily('jun-cc-pV(D+d)Z', zeta=2)
    basisfamily_list.append(basis_junccpv_dpd_z)
    basis_junccpcvdz = BasisFamily('jun-cc-pCVDZ', zeta=2)
    basisfamily_list.append(basis_junccpcvdz)
    basis_junccpcv_dpd_z = BasisFamily('jun-cc-pCV(D+d)Z', zeta=2)
    basisfamily_list.append(basis_junccpcv_dpd_z)
    basis_junccpwcvdz = BasisFamily('jun-cc-pwCVDZ', zeta=2)
    basisfamily_list.append(basis_junccpwcvdz)
    basis_junccpwcv_dpd_z = BasisFamily('jun-cc-pwCV(D+d)Z', zeta=2)
    basisfamily_list.append(basis_junccpwcv_dpd_z)
    basis_daugccpvdz = BasisFamily('d-aug-cc-pVDZ', zeta=2)
    basisfamily_list.append(basis_daugccpvdz)
    basis_daugccpcvdz = BasisFamily('d-aug-cc-pCVDZ', zeta=2)
    basisfamily_list.append(basis_daugccpcvdz)
    basis_daugccpwcvdz = BasisFamily('d-aug-cc-pwCVDZ', zeta=2)
    basisfamily_list.append(basis_daugccpwcvdz)
    basis_ccpvdz.add_rifit('cc-pVDZ-RI')
    basis_ccpv_dpd_z.add_rifit('cc-pVDZ-RI')
    basis_ccpwcvdz.add_rifit('cc-pwCVDZ-RI')
    basis_ccpwcv_dpd_z.add_rifit('cc-pwCVDZ-RI')
    basis_augccpvdz.add_rifit('aug-cc-pVDZ-RI')
    basis_augccpv_dpd_z.add_rifit('aug-cc-pVDZ-RI')
    basis_augccpwcvdz.add_rifit('aug-cc-pwCVDZ-RI')
    basis_augccpwcv_dpd_z.add_rifit('aug-cc-pwCVDZ-RI')
    basis_heavyaugccpvdz.add_rifit('heavy-aug-cc-pVDZ-RI')
    basis_heavyaugccpv_dpd_z.add_rifit('heavy-aug-cc-pVDZ-RI')
    basis_heavyaugccpwcvdz.add_rifit('heavy-aug-cc-pwCVDZ-RI')
    basis_heavyaugccpwcv_dpd_z.add_rifit('heavy-aug-cc-pwCVDZ-RI')
    basis_junccpvdz.add_rifit('jun-cc-pVDZ-RI')
    basis_junccpv_dpd_z.add_rifit('jun-cc-pVDZ-RI')
    basis_junccpwcvdz.add_rifit('jun-cc-pwCVDZ-RI')
    basis_junccpwcv_dpd_z.add_rifit('jun-cc-pwCVDZ-RI')
    basis_ccpvdz.add_jkfit('cc-pVDZ-JKFIT')
    basis_ccpv_dpd_z.add_jkfit('cc-pVDZ-JKFIT')
    basis_augccpvdz.add_jkfit('aug-cc-pVDZ-JKFIT')
    basis_augccpv_dpd_z.add_jkfit('aug-cc-pVDZ-JKFIT')
    basis_heavyaugccpvdz.add_jkfit('heavy-aug-cc-pVDZ-JKFIT')
    basis_heavyaugccpv_dpd_z.add_jkfit('heavy-aug-cc-pVDZ-JKFIT')
    basis_junccpvdz.add_jkfit('jun-cc-pVDZ-JKFIT')
    basis_junccpv_dpd_z.add_jkfit('jun-cc-pVDZ-JKFIT')
    basis_ccpvdzdk = BasisFamily('cc-pVDZ-DK', zeta=2)
    basisfamily_list.append(basis_ccpvdzdk)
    basis_ccpcvdzdk = BasisFamily('cc-pCVDZ-DK', zeta=2)
    basisfamily_list.append(basis_ccpcvdzdk)
    basis_augccpvdzdk = BasisFamily('aug-cc-pVDZ-DK', zeta=2)
    basisfamily_list.append(basis_augccpvdzdk)
    basis_augccpcvdzdk = BasisFamily('aug-cc-pCVDZ-DK', zeta=2)
    basisfamily_list.append(basis_augccpcvdzdk)
    basis_heavyaugccpvdzdk = BasisFamily('heavy-aug-cc-pVDZ-DK', zeta=2)
    basisfamily_list.append(basis_heavyaugccpvdzdk)
    basis_heavyaugccpcvdzdk = BasisFamily('heavy-aug-cc-pCVDZ-DK', zeta=2)
    basisfamily_list.append(basis_heavyaugccpcvdzdk)

    basis_ccpvtz = BasisFamily('cc-pVTZ', zeta=3)
    basisfamily_list.append(basis_ccpvtz)
    basis_ccpv_tpd_z = BasisFamily('cc-pV(T+d)Z', zeta=3)
    basisfamily_list.append(basis_ccpv_tpd_z)
    basis_ccpcvtz = BasisFamily('cc-pCVTZ', zeta=3)
    basisfamily_list.append(basis_ccpcvtz)
    basis_ccpcv_tpd_z = BasisFamily('cc-pCV(T+d)Z', zeta=3)
    basisfamily_list.append(basis_ccpcv_tpd_z)
    basis_ccpwcvtz = BasisFamily('cc-pwCVTZ', zeta=3)
    basisfamily_list.append(basis_ccpwcvtz)
    basis_ccpwcv_tpd_z = BasisFamily('cc-pwCV(T+d)Z', zeta=3)
    basisfamily_list.append(basis_ccpwcv_tpd_z)
    basis_augccpvtz = BasisFamily('aug-cc-pVTZ', zeta=3)
    basisfamily_list.append(basis_augccpvtz)
    basis_augccpv_tpd_z = BasisFamily('aug-cc-pV(T+d)Z', zeta=3)
    basisfamily_list.append(basis_augccpv_tpd_z)
    basis_augccpcvtz = BasisFamily('aug-cc-pCVTZ', zeta=3)
    basisfamily_list.append(basis_augccpcvtz)
    basis_augccpcv_tpd_z = BasisFamily('aug-cc-pCV(T+d)Z', zeta=3)
    basisfamily_list.append(basis_augccpcv_tpd_z)
    basis_augccpwcvtz = BasisFamily('aug-cc-pwCVTZ', zeta=3)
    basisfamily_list.append(basis_augccpwcvtz)
    basis_augccpwcv_tpd_z = BasisFamily('aug-cc-pwCV(T+d)Z', zeta=3)
    basisfamily_list.append(basis_augccpwcv_tpd_z)
    basis_heavyaugccpvtz = BasisFamily('heavy-aug-cc-pVTZ', zeta=3)
    basisfamily_list.append(basis_heavyaugccpvtz)
    basis_heavyaugccpv_tpd_z = BasisFamily('heavy-aug-cc-pV(T+d)Z', zeta=3)
    basisfamily_list.append(basis_heavyaugccpv_tpd_z)
    basis_heavyaugccpcvtz = BasisFamily('heavy-aug-cc-pCVTZ', zeta=3)
    basisfamily_list.append(basis_heavyaugccpcvtz)
    basis_heavyaugccpcv_tpd_z = BasisFamily('heavy-aug-cc-pCV(T+d)Z', zeta=3)
    basisfamily_list.append(basis_heavyaugccpcv_tpd_z)
    basis_heavyaugccpwcvtz = BasisFamily('heavy-aug-cc-pwCVTZ', zeta=3)
    basisfamily_list.append(basis_heavyaugccpwcvtz)
    basis_heavyaugccpwcv_tpd_z = BasisFamily('heavy-aug-cc-pwCV(T+d)Z', zeta=3)
    basisfamily_list.append(basis_heavyaugccpwcv_tpd_z)
    basis_junccpvtz = BasisFamily('jun-cc-pVTZ', zeta=3)
    basisfamily_list.append(basis_junccpvtz)
    basis_junccpv_tpd_z = BasisFamily('jun-cc-pV(T+d)Z', zeta=3)
    basisfamily_list.append(basis_junccpv_tpd_z)
    basis_junccpcvtz = BasisFamily('jun-cc-pCVTZ', zeta=3)
    basisfamily_list.append(basis_junccpcvtz)
    basis_junccpcv_tpd_z = BasisFamily('jun-cc-pCV(T+d)Z', zeta=3)
    basisfamily_list.append(basis_junccpcv_tpd_z)
    basis_junccpwcvtz = BasisFamily('jun-cc-pwCVTZ', zeta=3)
    basisfamily_list.append(basis_junccpwcvtz)
    basis_junccpwcv_tpd_z = BasisFamily('jun-cc-pwCV(T+d)Z', zeta=3)
    basisfamily_list.append(basis_junccpwcv_tpd_z)
    basis_mayccpvtz = BasisFamily('may-cc-pVTZ', zeta=3)
    basisfamily_list.append(basis_mayccpvtz)
    basis_mayccpv_tpd_z = BasisFamily('may-cc-pV(T+d)Z', zeta=3)
    basisfamily_list.append(basis_mayccpv_tpd_z)
    basis_mayccpcvtz = BasisFamily('may-cc-pCVTZ', zeta=3)
    basisfamily_list.append(basis_mayccpcvtz)
    basis_mayccpcv_tpd_z = BasisFamily('may-cc-pCV(T+d)Z', zeta=3)
    basisfamily_list.append(basis_mayccpcv_tpd_z)
    basis_mayccpwcvtz = BasisFamily('may-cc-pwCVTZ', zeta=3)
    basisfamily_list.append(basis_mayccpwcvtz)
    basis_mayccpwcv_tpd_z = BasisFamily('may-cc-pwCV(T+d)Z', zeta=3)
    basisfamily_list.append(basis_mayccpwcv_tpd_z)
    basis_daugccpvtz = BasisFamily('d-aug-cc-pVTZ', zeta=3)
    basisfamily_list.append(basis_daugccpvtz)
    basis_daugccpcvtz = BasisFamily('d-aug-cc-pCVTZ', zeta=3)
    basisfamily_list.append(basis_daugccpcvtz)
    basis_daugccpwcvtz = BasisFamily('d-aug-cc-pwCVTZ', zeta=3)
    basisfamily_list.append(basis_daugccpwcvtz)
    basis_ccpvtz.add_rifit('cc-pVTZ-RI')
    basis_ccpv_tpd_z.add_rifit('cc-pVTZ-RI')
    basis_ccpwcvtz.add_rifit('cc-pwCVTZ-RI')
    basis_ccpwcv_tpd_z.add_rifit('cc-pwCVTZ-RI')
    basis_augccpvtz.add_rifit('aug-cc-pVTZ-RI')
    basis_augccpv_tpd_z.add_rifit('aug-cc-pVTZ-RI')
    basis_augccpwcvtz.add_rifit('aug-cc-pwCVTZ-RI')
    basis_augccpwcv_tpd_z.add_rifit('aug-cc-pwCVTZ-RI')
    basis_heavyaugccpvtz.add_rifit('heavy-aug-cc-pVTZ-RI')
    basis_heavyaugccpv_tpd_z.add_rifit('heavy-aug-cc-pVTZ-RI')
    basis_heavyaugccpwcvtz.add_rifit('heavy-aug-cc-pwCVTZ-RI')
    basis_heavyaugccpwcv_tpd_z.add_rifit('heavy-aug-cc-pwCVTZ-RI')
    basis_junccpvtz.add_rifit('jun-cc-pVTZ-RI')
    basis_junccpv_tpd_z.add_rifit('jun-cc-pVTZ-RI')
    basis_junccpwcvtz.add_rifit('jun-cc-pwCVTZ-RI')
    basis_junccpwcv_tpd_z.add_rifit('jun-cc-pwCVTZ-RI')
    basis_mayccpvtz.add_rifit('may-cc-pVTZ-RI')
    basis_mayccpv_tpd_z.add_rifit('may-cc-pVTZ-RI')
    basis_mayccpwcvtz.add_rifit('may-cc-pwCVTZ-RI')
    basis_mayccpwcv_tpd_z.add_rifit('may-cc-pwCVTZ-RI')
    basis_ccpvtz.add_jkfit('cc-pVTZ-JKFIT')
    basis_ccpv_tpd_z.add_jkfit('cc-pVTZ-JKFIT')
    basis_augccpvtz.add_jkfit('aug-cc-pVTZ-JKFIT')
    basis_augccpv_tpd_z.add_jkfit('aug-cc-pVTZ-JKFIT')
    basis_heavyaugccpvtz.add_jkfit('heavy-aug-cc-pVTZ-JKFIT')
    basis_heavyaugccpv_tpd_z.add_jkfit('heavy-aug-cc-pVTZ-JKFIT')
    basis_junccpvtz.add_jkfit('jun-cc-pVTZ-JKFIT')
    basis_junccpv_tpd_z.add_jkfit('jun-cc-pVTZ-JKFIT')
    basis_mayccpvtz.add_jkfit('may-cc-pVTZ-JKFIT')
    basis_mayccpv_tpd_z.add_jkfit('may-cc-pVTZ-JKFIT')
    basis_ccpvtzdk = BasisFamily('cc-pVTZ-DK', zeta=3)
    basisfamily_list.append(basis_ccpvtzdk)
    basis_ccpcvtzdk = BasisFamily('cc-pCVTZ-DK', zeta=3)
    basisfamily_list.append(basis_ccpcvtzdk)
    basis_ccpwcvtzdk = BasisFamily('cc-pwCVTZ-DK', zeta=3)
    basisfamily_list.append(basis_ccpwcvtzdk)
    basis_augccpvtzdk = BasisFamily('aug-cc-pVTZ-DK', zeta=3)
    basisfamily_list.append(basis_augccpvtzdk)
    basis_augccpcvtzdk = BasisFamily('aug-cc-pCVTZ-DK', zeta=3)
    basisfamily_list.append(basis_augccpcvtzdk)
    basis_augccpwcvtzdk = BasisFamily('aug-cc-pwCVTZ-DK', zeta=3)
    basisfamily_list.append(basis_augccpwcvtzdk)
    basis_heavyaugccpvtzdk = BasisFamily('heavy-aug-cc-pVTZ-DK', zeta=3)
    basisfamily_list.append(basis_heavyaugccpvtzdk)
    basis_heavyaugccpcvtzdk = BasisFamily('heavy-aug-cc-pCVTZ-DK', zeta=3)
    basisfamily_list.append(basis_heavyaugccpcvtzdk)
    basis_heavyaugccpwcvtzdk = BasisFamily('heavy-aug-cc-pwCVTZ-DK', zeta=3)
    basisfamily_list.append(basis_heavyaugccpwcvtzdk)

    basis_ccpvqz = BasisFamily('cc-pVQZ', zeta=4)
    basisfamily_list.append(basis_ccpvqz)
    basis_ccpv_qpd_z = BasisFamily('cc-pV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_ccpv_qpd_z)
    basis_ccpcvqz = BasisFamily('cc-pCVQZ', zeta=4)
    basisfamily_list.append(basis_ccpcvqz)
    basis_ccpcv_qpd_z = BasisFamily('cc-pCV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_ccpcv_qpd_z)
    basis_ccpwcvqz = BasisFamily('cc-pwCVQZ', zeta=4)
    basisfamily_list.append(basis_ccpwcvqz)
    basis_ccpwcv_qpd_z = BasisFamily('cc-pwCV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_ccpwcv_qpd_z)
    basis_augccpvqz = BasisFamily('aug-cc-pVQZ', zeta=4)
    basisfamily_list.append(basis_augccpvqz)
    basis_augccpv_qpd_z = BasisFamily('aug-cc-pV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_augccpv_qpd_z)
    basis_augccpcvqz = BasisFamily('aug-cc-pCVQZ', zeta=4)
    basisfamily_list.append(basis_augccpcvqz)
    basis_augccpcv_qpd_z = BasisFamily('aug-cc-pCV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_augccpcv_qpd_z)
    basis_augccpwcvqz = BasisFamily('aug-cc-pwCVQZ', zeta=4)
    basisfamily_list.append(basis_augccpwcvqz)
    basis_augccpwcv_qpd_z = BasisFamily('aug-cc-pwCV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_augccpwcv_qpd_z)
    basis_heavyaugccpvqz = BasisFamily('heavy-aug-cc-pVQZ', zeta=4)
    basisfamily_list.append(basis_heavyaugccpvqz)
    basis_heavyaugccpv_qpd_z = BasisFamily('heavy-aug-cc-pV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_heavyaugccpv_qpd_z)
    basis_heavyaugccpcvqz = BasisFamily('heavy-aug-cc-pCVQZ', zeta=4)
    basisfamily_list.append(basis_heavyaugccpcvqz)
    basis_heavyaugccpcv_qpd_z = BasisFamily('heavy-aug-cc-pCV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_heavyaugccpcv_qpd_z)
    basis_heavyaugccpwcvqz = BasisFamily('heavy-aug-cc-pwCVQZ', zeta=4)
    basisfamily_list.append(basis_heavyaugccpwcvqz)
    basis_heavyaugccpwcv_qpd_z = BasisFamily('heavy-aug-cc-pwCV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_heavyaugccpwcv_qpd_z)
    basis_junccpvqz = BasisFamily('jun-cc-pVQZ', zeta=4)
    basisfamily_list.append(basis_junccpvqz)
    basis_junccpv_qpd_z = BasisFamily('jun-cc-pV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_junccpv_qpd_z)
    basis_junccpcvqz = BasisFamily('jun-cc-pCVQZ', zeta=4)
    basisfamily_list.append(basis_junccpcvqz)
    basis_junccpcv_qpd_z = BasisFamily('jun-cc-pCV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_junccpcv_qpd_z)
    basis_junccpwcvqz = BasisFamily('jun-cc-pwCVQZ', zeta=4)
    basisfamily_list.append(basis_junccpwcvqz)
    basis_junccpwcv_qpd_z = BasisFamily('jun-cc-pwCV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_junccpwcv_qpd_z)
    basis_mayccpvqz = BasisFamily('may-cc-pVQZ', zeta=4)
    basisfamily_list.append(basis_mayccpvqz)
    basis_mayccpv_qpd_z = BasisFamily('may-cc-pV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_mayccpv_qpd_z)
    basis_mayccpcvqz = BasisFamily('may-cc-pCVQZ', zeta=4)
    basisfamily_list.append(basis_mayccpcvqz)
    basis_mayccpcv_qpd_z = BasisFamily('may-cc-pCV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_mayccpcv_qpd_z)
    basis_mayccpwcvqz = BasisFamily('may-cc-pwCVQZ', zeta=4)
    basisfamily_list.append(basis_mayccpwcvqz)
    basis_mayccpwcv_qpd_z = BasisFamily('may-cc-pwCV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_mayccpwcv_qpd_z)
    basis_aprccpvqz = BasisFamily('apr-cc-pVQZ', zeta=4)
    basisfamily_list.append(basis_aprccpvqz)
    basis_aprccpv_qpd_z = BasisFamily('apr-cc-pV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_aprccpv_qpd_z)
    basis_aprccpcvqz = BasisFamily('apr-cc-pCVQZ', zeta=4)
    basisfamily_list.append(basis_aprccpcvqz)
    basis_aprccpcv_qpd_z = BasisFamily('apr-cc-pCV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_aprccpcv_qpd_z)
    basis_aprccpwcvqz = BasisFamily('apr-cc-pwCVQZ', zeta=4)
    basisfamily_list.append(basis_aprccpwcvqz)
    basis_aprccpwcv_qpd_z = BasisFamily('apr-cc-pwCV(Q+d)Z', zeta=4)
    basisfamily_list.append(basis_aprccpwcv_qpd_z)
    basis_daugccpvqz = BasisFamily('d-aug-cc-pVQZ', zeta=4)
    basisfamily_list.append(basis_daugccpvqz)
    basis_daugccpcvqz = BasisFamily('d-aug-cc-pCVQZ', zeta=4)
    basisfamily_list.append(basis_daugccpcvqz)
    basis_daugccpwcvqz = BasisFamily('d-aug-cc-pwCVQZ', zeta=4)
    basisfamily_list.append(basis_daugccpwcvqz)
    basis_ccpvqz.add_rifit('cc-pVQZ-RI')
    basis_ccpv_qpd_z.add_rifit('cc-pVQZ-RI')
    basis_ccpwcvqz.add_rifit('cc-pwCVQZ-RI')
    basis_ccpwcv_qpd_z.add_rifit('cc-pwCVQZ-RI')
    basis_augccpvqz.add_rifit('aug-cc-pVQZ-RI')
    basis_augccpv_qpd_z.add_rifit('aug-cc-pVQZ-RI')
    basis_augccpwcvqz.add_rifit('aug-cc-pwCVQZ-RI')
    basis_augccpwcv_qpd_z.add_rifit('aug-cc-pwCVQZ-RI')
    basis_heavyaugccpvqz.add_rifit('heavy-aug-cc-pVQZ-RI')
    basis_heavyaugccpv_qpd_z.add_rifit('heavy-aug-cc-pVQZ-RI')
    basis_heavyaugccpwcvqz.add_rifit('heavy-aug-cc-pwCVQZ-RI')
    basis_heavyaugccpwcv_qpd_z.add_rifit('heavy-aug-cc-pwCVQZ-RI')
    basis_junccpvqz.add_rifit('jun-cc-pVQZ-RI')
    basis_junccpv_qpd_z.add_rifit('jun-cc-pVQZ-RI')
    basis_junccpwcvqz.add_rifit('jun-cc-pwCVQZ-RI')
    basis_junccpwcv_qpd_z.add_rifit('jun-cc-pwCVQZ-RI')
    basis_mayccpvqz.add_rifit('may-cc-pVQZ-RI')
    basis_mayccpv_qpd_z.add_rifit('may-cc-pVQZ-RI')
    basis_mayccpwcvqz.add_rifit('may-cc-pwCVQZ-RI')
    basis_mayccpwcv_qpd_z.add_rifit('may-cc-pwCVQZ-RI')
    basis_aprccpvqz.add_rifit('apr-cc-pVQZ-RI')
    basis_aprccpv_qpd_z.add_rifit('apr-cc-pVQZ-RI')
    basis_aprccpwcvqz.add_rifit('apr-cc-pwCVQZ-RI')
    basis_aprccpwcv_qpd_z.add_rifit('apr-cc-pwCVQZ-RI')
    basis_ccpvqz.add_jkfit('cc-pVQZ-JKFIT')
    basis_ccpv_qpd_z.add_jkfit('cc-pVQZ-JKFIT')
    basis_augccpvqz.add_jkfit('aug-cc-pVQZ-JKFIT')
    basis_augccpv_qpd_z.add_jkfit('aug-cc-pVQZ-JKFIT')
    basis_heavyaugccpvqz.add_jkfit('heavy-aug-cc-pVQZ-JKFIT')
    basis_heavyaugccpv_qpd_z.add_jkfit('heavy-aug-cc-pVQZ-JKFIT')
    basis_junccpvqz.add_jkfit('jun-cc-pVQZ-JKFIT')
    basis_junccpv_qpd_z.add_jkfit('jun-cc-pVQZ-JKFIT')
    basis_mayccpvqz.add_jkfit('may-cc-pVQZ-JKFIT')
    basis_mayccpv_qpd_z.add_jkfit('may-cc-pVQZ-JKFIT')
    basis_aprccpvqz.add_jkfit('apr-cc-pVQZ-JKFIT')
    basis_aprccpv_qpd_z.add_jkfit('apr-cc-pVQZ-JKFIT')
    basis_ccpvqzdk = BasisFamily('cc-pVQZ-DK', zeta=4)
    basisfamily_list.append(basis_ccpvqzdk)
    basis_ccpcvqzdk = BasisFamily('cc-pCVQZ-DK', zeta=4)
    basisfamily_list.append(basis_ccpcvqzdk)
    basis_ccpwcvqzdk = BasisFamily('cc-pwCVQZ-DK', zeta=4)
    basisfamily_list.append(basis_ccpwcvqzdk)
    basis_augccpvqzdk = BasisFamily('aug-cc-pVQZ-DK', zeta=4)
    basisfamily_list.append(basis_augccpvqzdk)
    basis_augccpcvqzdk = BasisFamily('aug-cc-pCVQZ-DK', zeta=4)
    basisfamily_list.append(basis_augccpcvqzdk)
    basis_augccpwcvqzdk = BasisFamily('aug-cc-pwCVQZ-DK', zeta=4)
    basisfamily_list.append(basis_augccpwcvqzdk)
    basis_heavyaugccpvqzdk = BasisFamily('heavy-aug-cc-pVQZ-DK', zeta=4)
    basisfamily_list.append(basis_heavyaugccpvqzdk)
    basis_heavyaugccpcvqzdk = BasisFamily('heavy-aug-cc-pCVQZ-DK', zeta=4)
    basisfamily_list.append(basis_heavyaugccpcvqzdk)
    basis_heavyaugccpwcvqzdk = BasisFamily('heavy-aug-cc-pwCVQZ-DK', zeta=4)
    basisfamily_list.append(basis_heavyaugccpwcvqzdk)

    basis_ccpv5z = BasisFamily('cc-pV5Z', zeta=5)
    basisfamily_list.append(basis_ccpv5z)
    basis_ccpv_5pd_z = BasisFamily('cc-pV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_ccpv_5pd_z)
    basis_ccpcv5z = BasisFamily('cc-pCV5Z', zeta=5)
    basisfamily_list.append(basis_ccpcv5z)
    basis_ccpcv_5pd_z = BasisFamily('cc-pCV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_ccpcv_5pd_z)
    basis_ccpwcv5z = BasisFamily('cc-pwCV5Z', zeta=5)
    basisfamily_list.append(basis_ccpwcv5z)
    basis_ccpwcv_5pd_z = BasisFamily('cc-pwCV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_ccpwcv_5pd_z)
    basis_augccpv5z = BasisFamily('aug-cc-pV5Z', zeta=5)
    basisfamily_list.append(basis_augccpv5z)
    basis_augccpv_5pd_z = BasisFamily('aug-cc-pV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_augccpv_5pd_z)
    basis_augccpcv5z = BasisFamily('aug-cc-pCV5Z', zeta=5)
    basisfamily_list.append(basis_augccpcv5z)
    basis_augccpcv_5pd_z = BasisFamily('aug-cc-pCV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_augccpcv_5pd_z)
    basis_augccpwcv5z = BasisFamily('aug-cc-pwCV5Z', zeta=5)
    basisfamily_list.append(basis_augccpwcv5z)
    basis_augccpwcv_5pd_z = BasisFamily('aug-cc-pwCV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_augccpwcv_5pd_z)
    basis_heavyaugccpv5z = BasisFamily('heavy-aug-cc-pV5Z', zeta=5)
    basisfamily_list.append(basis_heavyaugccpv5z)
    basis_heavyaugccpv_5pd_z = BasisFamily('heavy-aug-cc-pV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_heavyaugccpv_5pd_z)
    basis_heavyaugccpcv5z = BasisFamily('heavy-aug-cc-pCV5Z', zeta=5)
    basisfamily_list.append(basis_heavyaugccpcv5z)
    basis_heavyaugccpcv_5pd_z = BasisFamily('heavy-aug-cc-pCV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_heavyaugccpcv_5pd_z)
    basis_heavyaugccpwcv5z = BasisFamily('heavy-aug-cc-pwCV5Z', zeta=5)
    basisfamily_list.append(basis_heavyaugccpwcv5z)
    basis_heavyaugccpwcv_5pd_z = BasisFamily('heavy-aug-cc-pwCV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_heavyaugccpwcv_5pd_z)
    basis_junccpv5z = BasisFamily('jun-cc-pV5Z', zeta=5)
    basisfamily_list.append(basis_junccpv5z)
    basis_junccpv_5pd_z = BasisFamily('jun-cc-pV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_junccpv_5pd_z)
    basis_junccpcv5z = BasisFamily('jun-cc-pCV5Z', zeta=5)
    basisfamily_list.append(basis_junccpcv5z)
    basis_junccpcv_5pd_z = BasisFamily('jun-cc-pCV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_junccpcv_5pd_z)
    basis_junccpwcv5z = BasisFamily('jun-cc-pwCV5Z', zeta=5)
    basisfamily_list.append(basis_junccpwcv5z)
    basis_junccpwcv_5pd_z = BasisFamily('jun-cc-pwCV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_junccpwcv_5pd_z)
    basis_mayccpv5z = BasisFamily('may-cc-pV5Z', zeta=5)
    basisfamily_list.append(basis_mayccpv5z)
    basis_mayccpv_5pd_z = BasisFamily('may-cc-pV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_mayccpv_5pd_z)
    basis_mayccpcv5z = BasisFamily('may-cc-pCV5Z', zeta=5)
    basisfamily_list.append(basis_mayccpcv5z)
    basis_mayccpcv_5pd_z = BasisFamily('may-cc-pCV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_mayccpcv_5pd_z)
    basis_mayccpwcv5z = BasisFamily('may-cc-pwCV5Z', zeta=5)
    basisfamily_list.append(basis_mayccpwcv5z)
    basis_mayccpwcv_5pd_z = BasisFamily('may-cc-pwCV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_mayccpwcv_5pd_z)
    basis_aprccpv5z = BasisFamily('apr-cc-pV5Z', zeta=5)
    basisfamily_list.append(basis_aprccpv5z)
    basis_aprccpv_5pd_z = BasisFamily('apr-cc-pV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_aprccpv_5pd_z)
    basis_aprccpcv5z = BasisFamily('apr-cc-pCV5Z', zeta=5)
    basisfamily_list.append(basis_aprccpcv5z)
    basis_aprccpcv_5pd_z = BasisFamily('apr-cc-pCV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_aprccpcv_5pd_z)
    basis_aprccpwcv5z = BasisFamily('apr-cc-pwCV5Z', zeta=5)
    basisfamily_list.append(basis_aprccpwcv5z)
    basis_aprccpwcv_5pd_z = BasisFamily('apr-cc-pwCV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_aprccpwcv_5pd_z)
    basis_marccpv5z = BasisFamily('mar-cc-pV5Z', zeta=5)
    basisfamily_list.append(basis_marccpv5z)
    basis_marccpv_5pd_z = BasisFamily('mar-cc-pV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_marccpv_5pd_z)
    basis_marccpcv5z = BasisFamily('mar-cc-pCV5Z', zeta=5)
    basisfamily_list.append(basis_marccpcv5z)
    basis_marccpcv_5pd_z = BasisFamily('mar-cc-pCV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_marccpcv_5pd_z)
    basis_marccpwcv5z = BasisFamily('mar-cc-pwCV5Z', zeta=5)
    basisfamily_list.append(basis_marccpwcv5z)
    basis_marccpwcv_5pd_z = BasisFamily('mar-cc-pwCV(5+d)Z', zeta=5)
    basisfamily_list.append(basis_marccpwcv_5pd_z)
    basis_daugccpv5z = BasisFamily('d-aug-cc-pV5Z', zeta=5)
    basisfamily_list.append(basis_daugccpv5z)
    basis_daugccpcv5z = BasisFamily('d-aug-cc-pCV5Z', zeta=5)
    basisfamily_list.append(basis_daugccpcv5z)
    basis_daugccpwcv5z = BasisFamily('d-aug-cc-pwCV5Z', zeta=5)
    basisfamily_list.append(basis_daugccpwcv5z)
    basis_ccpv5z.add_rifit('cc-pV5Z-RI')
    basis_ccpv_5pd_z.add_rifit('cc-pV5Z-RI')
    basis_ccpwcv5z.add_rifit('cc-pwCV5Z-RI')
    basis_ccpwcv_5pd_z.add_rifit('cc-pwCV5Z-RI')
    basis_augccpv5z.add_rifit('aug-cc-pV5Z-RI')
    basis_augccpv_5pd_z.add_rifit('aug-cc-pV5Z-RI')
    basis_augccpwcv5z.add_rifit('aug-cc-pwCV5Z-RI')
    basis_augccpwcv_5pd_z.add_rifit('aug-cc-pwCV5Z-RI')
    basis_heavyaugccpv5z.add_rifit('heavy-aug-cc-pV5Z-RI')
    basis_heavyaugccpv_5pd_z.add_rifit('heavy-aug-cc-pV5Z-RI')
    basis_heavyaugccpwcv5z.add_rifit('heavy-aug-cc-pwCV5Z-RI')
    basis_heavyaugccpwcv_5pd_z.add_rifit('heavy-aug-cc-pwCV5Z-RI')
    basis_junccpv5z.add_rifit('jun-cc-pV5Z-RI')
    basis_junccpv_5pd_z.add_rifit('jun-cc-pV5Z-RI')
    basis_junccpwcv5z.add_rifit('jun-cc-pwCV5Z-RI')
    basis_junccpwcv_5pd_z.add_rifit('jun-cc-pwCV5Z-RI')
    basis_mayccpv5z.add_rifit('may-cc-pV5Z-RI')
    basis_mayccpv_5pd_z.add_rifit('may-cc-pV5Z-RI')
    basis_mayccpwcv5z.add_rifit('may-cc-pwCV5Z-RI')
    basis_mayccpwcv_5pd_z.add_rifit('may-cc-pwCV5Z-RI')
    basis_aprccpv5z.add_rifit('apr-cc-pV5Z-RI')
    basis_aprccpv_5pd_z.add_rifit('apr-cc-pV5Z-RI')
    basis_aprccpwcv5z.add_rifit('apr-cc-pwCV5Z-RI')
    basis_aprccpwcv_5pd_z.add_rifit('apr-cc-pwCV5Z-RI')
    basis_marccpv5z.add_rifit('mar-cc-pV5Z-RI')
    basis_marccpv_5pd_z.add_rifit('mar-cc-pV5Z-RI')
    basis_marccpwcv5z.add_rifit('mar-cc-pwCV5Z-RI')
    basis_marccpwcv_5pd_z.add_rifit('mar-cc-pwCV5Z-RI')
    basis_ccpv5z.add_jkfit('cc-pV5Z-JKFIT')
    basis_ccpv_5pd_z.add_jkfit('cc-pV5Z-JKFIT')
    basis_augccpv5z.add_jkfit('aug-cc-pV5Z-JKFIT')
    basis_augccpv_5pd_z.add_jkfit('aug-cc-pV5Z-JKFIT')
    basis_heavyaugccpv5z.add_jkfit('heavy-aug-cc-pV5Z-JKFIT')
    basis_heavyaugccpv_5pd_z.add_jkfit('heavy-aug-cc-pV5Z-JKFIT')
    basis_junccpv5z.add_jkfit('jun-cc-pV5Z-JKFIT')
    basis_junccpv_5pd_z.add_jkfit('jun-cc-pV5Z-JKFIT')
    basis_mayccpv5z.add_jkfit('may-cc-pV5Z-JKFIT')
    basis_mayccpv_5pd_z.add_jkfit('may-cc-pV5Z-JKFIT')
    basis_aprccpv5z.add_jkfit('apr-cc-pV5Z-JKFIT')
    basis_aprccpv_5pd_z.add_jkfit('apr-cc-pV5Z-JKFIT')
    basis_marccpv5z.add_jkfit('mar-cc-pV5Z-JKFIT')
    basis_marccpv_5pd_z.add_jkfit('mar-cc-pV5Z-JKFIT')
    basis_ccpv5zdk = BasisFamily('cc-pV5Z-DK', zeta=5)
    basisfamily_list.append(basis_ccpv5zdk)
    basis_ccpcv5zdk = BasisFamily('cc-pCV5Z-DK', zeta=5)
    basisfamily_list.append(basis_ccpcv5zdk)
    basis_ccpwcv5zdk = BasisFamily('cc-pwCV5Z-DK', zeta=5)
    basisfamily_list.append(basis_ccpwcv5zdk)
    basis_augccpv5zdk = BasisFamily('aug-cc-pV5Z-DK', zeta=5)
    basisfamily_list.append(basis_augccpv5zdk)
    basis_augccpcv5zdk = BasisFamily('aug-cc-pCV5Z-DK', zeta=5)
    basisfamily_list.append(basis_augccpcv5zdk)
    basis_augccpwcv5zdk = BasisFamily('aug-cc-pwCV5Z-DK', zeta=5)
    basisfamily_list.append(basis_augccpwcv5zdk)
    basis_heavyaugccpv5zdk = BasisFamily('heavy-aug-cc-pV5Z-DK', zeta=5)
    basisfamily_list.append(basis_heavyaugccpv5zdk)
    basis_heavyaugccpcv5zdk = BasisFamily('heavy-aug-cc-pCV5Z-DK', zeta=5)
    basisfamily_list.append(basis_heavyaugccpcv5zdk)
    basis_heavyaugccpwcv5zdk = BasisFamily('heavy-aug-cc-pwCV5Z-DK', zeta=5)
    basisfamily_list.append(basis_heavyaugccpwcv5zdk)

    basis_ccpv6z = BasisFamily('cc-pV6Z', zeta=6)
    basisfamily_list.append(basis_ccpv6z)
    basis_ccpv_6pd_z = BasisFamily('cc-pV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_ccpv_6pd_z)
    basis_ccpcv6z = BasisFamily('cc-pCV6Z', zeta=6)
    basisfamily_list.append(basis_ccpcv6z)
    basis_ccpcv_6pd_z = BasisFamily('cc-pCV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_ccpcv_6pd_z)
    basis_augccpv6z = BasisFamily('aug-cc-pV6Z', zeta=6)
    basisfamily_list.append(basis_augccpv6z)
    basis_augccpv_6pd_z = BasisFamily('aug-cc-pV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_augccpv_6pd_z)
    basis_augccpcv6z = BasisFamily('aug-cc-pCV6Z', zeta=6)
    basisfamily_list.append(basis_augccpcv6z)
    basis_augccpcv_6pd_z = BasisFamily('aug-cc-pCV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_augccpcv_6pd_z)
    basis_heavyaugccpv6z = BasisFamily('heavy-aug-cc-pV6Z', zeta=6)
    basisfamily_list.append(basis_heavyaugccpv6z)
    basis_heavyaugccpv_6pd_z = BasisFamily('heavy-aug-cc-pV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_heavyaugccpv_6pd_z)
    basis_heavyaugccpcv6z = BasisFamily('heavy-aug-cc-pCV6Z', zeta=6)
    basisfamily_list.append(basis_heavyaugccpcv6z)
    basis_heavyaugccpcv_6pd_z = BasisFamily('heavy-aug-cc-pCV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_heavyaugccpcv_6pd_z)
    basis_junccpv6z = BasisFamily('jun-cc-pV6Z', zeta=6)
    basisfamily_list.append(basis_junccpv6z)
    basis_junccpv_6pd_z = BasisFamily('jun-cc-pV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_junccpv_6pd_z)
    basis_junccpcv6z = BasisFamily('jun-cc-pCV6Z', zeta=6)
    basisfamily_list.append(basis_junccpcv6z)
    basis_junccpcv_6pd_z = BasisFamily('jun-cc-pCV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_junccpcv_6pd_z)
    basis_mayccpv6z = BasisFamily('may-cc-pV6Z', zeta=6)
    basisfamily_list.append(basis_mayccpv6z)
    basis_mayccpv_6pd_z = BasisFamily('may-cc-pV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_mayccpv_6pd_z)
    basis_mayccpcv6z = BasisFamily('may-cc-pCV6Z', zeta=6)
    basisfamily_list.append(basis_mayccpcv6z)
    basis_mayccpcv_6pd_z = BasisFamily('may-cc-pCV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_mayccpcv_6pd_z)
    basis_aprccpv6z = BasisFamily('apr-cc-pV6Z', zeta=6)
    basisfamily_list.append(basis_aprccpv6z)
    basis_aprccpv_6pd_z = BasisFamily('apr-cc-pV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_aprccpv_6pd_z)
    basis_aprccpcv6z = BasisFamily('apr-cc-pCV6Z', zeta=6)
    basisfamily_list.append(basis_aprccpcv6z)
    basis_aprccpcv_6pd_z = BasisFamily('apr-cc-pCV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_aprccpcv_6pd_z)
    basis_marccpv6z = BasisFamily('mar-cc-pV6Z', zeta=6)
    basisfamily_list.append(basis_marccpv6z)
    basis_marccpv_6pd_z = BasisFamily('mar-cc-pV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_marccpv_6pd_z)
    basis_marccpcv6z = BasisFamily('mar-cc-pCV6Z', zeta=6)
    basisfamily_list.append(basis_marccpcv6z)
    basis_marccpcv_6pd_z = BasisFamily('mar-cc-pCV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_marccpcv_6pd_z)
    basis_febccpv6z = BasisFamily('feb-cc-pV6Z', zeta=6)
    basisfamily_list.append(basis_febccpv6z)
    basis_febccpv_6pd_z = BasisFamily('feb-cc-pV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_febccpv_6pd_z)
    basis_febccpcv6z = BasisFamily('feb-cc-pCV6Z', zeta=6)
    basisfamily_list.append(basis_febccpcv6z)
    basis_febccpcv_6pd_z = BasisFamily('feb-cc-pCV(6+d)Z', zeta=6)
    basisfamily_list.append(basis_febccpcv_6pd_z)
    basis_daugccpv6z = BasisFamily('d-aug-cc-pV6Z', zeta=6)
    basisfamily_list.append(basis_daugccpv6z)
    basis_daugccpcv6z = BasisFamily('d-aug-cc-pCV6Z', zeta=6)
    basisfamily_list.append(basis_daugccpcv6z)
    basis_ccpv6z.add_rifit('cc-pV6Z-RI')
    basis_ccpv_6pd_z.add_rifit('cc-pV6Z-RI')
    basis_augccpv6z.add_rifit('aug-cc-pV6Z-RI')
    basis_augccpv_6pd_z.add_rifit('aug-cc-pV6Z-RI')
    basis_heavyaugccpv6z.add_rifit('heavy-aug-cc-pV6Z-RI')
    basis_heavyaugccpv_6pd_z.add_rifit('heavy-aug-cc-pV6Z-RI')
    basis_junccpv6z.add_rifit('jun-cc-pV6Z-RI')
    basis_junccpv_6pd_z.add_rifit('jun-cc-pV6Z-RI')
    basis_mayccpv6z.add_rifit('may-cc-pV6Z-RI')
    basis_mayccpv_6pd_z.add_rifit('may-cc-pV6Z-RI')
    basis_aprccpv6z.add_rifit('apr-cc-pV6Z-RI')
    basis_aprccpv_6pd_z.add_rifit('apr-cc-pV6Z-RI')
    basis_marccpv6z.add_rifit('mar-cc-pV6Z-RI')
    basis_marccpv_6pd_z.add_rifit('mar-cc-pV6Z-RI')
    basis_febccpv6z.add_rifit('feb-cc-pV6Z-RI')
    basis_febccpv_6pd_z.add_rifit('feb-cc-pV6Z-RI')
    basis_ccpvtz.add_dualfit('cc-pvtz-dual')
    basis_ccpvqz.add_dualfit('cc-pvqz-dual')
    basis_augccpvdz.add_dualfit('aug-cc-pvdz-dual')
    basis_augccpvtz.add_dualfit('aug-cc-pvtz-dual')
    basis_augccpvqz.add_dualfit('aug-cc-pvqz-dual')
    basis_heavyaugccpvtz.add_dualfit('heavy-aug-cc-pvtz-dual')
    basis_heavyaugccpvqz.add_dualfit('heavy-aug-cc-pvqz-dual')
