# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Xplsprinters(AutotoolsPackage):
    """List Xprint printers."""

    homepage = "http://cgit.freedesktop.org/xorg/app/xplsprinters"
    url      = "https://www.x.org/archive/individual/app/xplsprinters-1.0.1.tar.gz"

    version('1.0.1', sha256='33377e499429ce3e100fbd7b59153c87ad79bf55872561db08419f69cac4fbfd')

    depends_on('libxp')
    depends_on('libxprintutil')
    depends_on('libx11')

    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
