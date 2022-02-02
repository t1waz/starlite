from os import environ
from pathlib import Path
from typing import List

from setuptools import Extension, Distribution

from Cython.Build import cythonize
from Cython.Distutils.build_ext import new_build_ext as cython_build_ext

SOURCE_DIR = Path("starlite")  # replace SRC with the root of your source
BUILD_DIR = Path("cython_build")

environ['CFLAGS'] = '-O3'

def get_extension_modules() -> List[Extension]:
    """Collect all .py files and construct Setuptools Extensions"""
    extension_modules: List[Extension] = []

    for py_file in SOURCE_DIR.rglob("*.py"):

        # Get path (not just name) without .py extension
        module_path = py_file.with_suffix("")

        # Convert path to module name
        module_path = str(module_path).replace("/", ".")

        extension_module = Extension(
            name=module_path,
            sources=[str(py_file)]
        )

        extension_modules.append(extension_module)

    return extension_modules


# Collect and cythonize all files
extension_modules = cythonize(
    module_list=get_extension_modules(),
    build_dir=BUILD_DIR,
    annotate=False,
    nthreads=0,
    compiler_directives={"language_level": "3"},
    force=True,
)

# Use Setuptools to collect files
distribution = Distribution({
    "ext_modules": extension_modules,
    "cmdclass": {
        "build_ext": cython_build_ext,
    },
})

# Grab the build_ext command and copy all files back to source dir.
# Done so Poetry grabs the files during the next step in its build.
distribution.run_command("build_ext")
build_ext_cmd = distribution.get_command_obj("build_ext")
build_ext_cmd.copy_extensions_to_source()