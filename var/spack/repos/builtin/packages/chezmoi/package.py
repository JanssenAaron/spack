# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install chezmoi
#
# You can edit this file again by typing:
#
#     spack edit chezmoi
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Chezmoi(MakefilePackage):
    """chezmoi helps you manage your personal configuration files (dotfiles, like ~/.gitconfig) across multiple machines."""

    homepage = "https://www.chezmoi.io/"
    url = "https://github.com/twpayne/chezmoi/releases/download/v2.52.1/chezmoi-2.52.1.tar.gz"

    maintainers("JanssenAaron")

    license("MIT", checked_by="JanssenAaron")

    version("2.52.1", sha256="a55eafaa3bc0cc38d97b9080490b6c68b84063e21ba7f378eab21d37e8dea6d5")
    version("2.52.0", sha256="2664f63968b08ba834f41104095e3f523f3a33c703f14f0ca77dfc3fd1583498")
    version("2.51.0", sha256="ad1ebc43df75204c770bab476735f50e2aa08377327cd8c34085c7e8c0380e9b")
    version("2.50.0", sha256="f4e24835525a10a61ba69362be1f313d1fd381f310496000815ff2823607c8d4")
    version("2.49.1", sha256="90db273b77821508ba7cb09c3d63c7793a4180dae36988c557a9a11f743a0861")
    version("2.49.0", sha256="0e8c035394e42513d725d60b0f6d6fd00dddf15cea7247a835bb79212bb29570")
    version("2.48.2", sha256="fcc0866c3bcdc994af2eb618c31e169bd2b1190f3ca49e40cca4c49d636d9db3")
    version("2.48.1", sha256="c3b8de8bfc9287f54e6f92744d29fb829c4ae0c577296083b84678b9285c46a0")
    version("2.48.0", sha256="aa4a609b2d0b4cc13d1a2d709ef38606c682356bf037661f02fd31d6bc44f650")
    version("2.47.4", sha256="ccf688cf50788a7d470d54e8ce29b512268df2cbd3bc313dc813c082258db695")

    depends_on("go", type="build")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("chezmoi", prefix.bin)
