/*
 * @BEGIN LICENSE
 *
 * Psi4: an open-source quantum chemistry software package
 *
 * Copyright (c) 2007-2019 The Psi4 Developers.
 *
 * The copyrights for code used from other parties are included in
 * the corresponding files.
 *
 * This file is part of Psi4.
 *
 * Psi4 is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, version 3.
 *
 * Psi4 is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License along
 * with Psi4; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * @END LICENSE
 */

/*! \file
    \ingroup DPD
    \brief Enter brief description of file here
*/
#include "dpd.h"

namespace psi {

int DPD::file2_mat_close(dpdfile2 *File) {
    int h, my_irrep;

    my_irrep = File->my_irrep;

    if (File->incore) return 0; /* We need to keep the memory */

    for (h = 0; h < File->params->nirreps; h++)
        if (File->params->rowtot[h] && File->params->coltot[h ^ my_irrep])
            free_dpd_block(File->matrix[h], File->params->rowtot[h], File->params->coltot[h ^ my_irrep]);

    return 0;
}

}  // namespace psi
