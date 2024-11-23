# coding=utf-8
from setuptools import setup

####################################################################################################
plugin_identifier = "costestimation"
plugin_package = "octoprint_costestimation"
plugin_name = "OctoPrint-CostEstimation"
plugin_description = "Displays the estimated print cost for the loaded model"
plugin_author = "Sven Lohrmann, Olli, Hilton Shumway"
plugin_author_email = "hillshum@gmail.com, ollisgit@gmail.com, malnvenshorn@mailbox.org"
plugin_url = "https://github.com/Hillshum/OctoPrint-CostEstimation"
plugin_license = "AGPLv3"
plugin_requires = []
plugin_additional_data = []
plugin_additional_packages = []
plugin_ignored_packages = []
additional_setup_parameters = {}
####################################################################################################

try:
    import octoprint_setuptools
except ImportError:
    print("Could not import OctoPrint's setuptools, are you sure you are running that under "
          "the same python installation that OctoPrint is installed under?")
    import sys
    sys.exit(-1)

def get_version_and_cmdclass(pkg_path):
    import os
    from importlib.util import module_from_spec, spec_from_file_location
    spec = spec_from_file_location("version", os.path.join(pkg_path, "_version.py"))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    data = module.get_data()
    return data["version"], module.get_cmdclass(pkg_path)

setup_parameters = octoprint_setuptools.create_plugin_setup_parameters(
    identifier=plugin_identifier,
    package=plugin_package,
    name=plugin_name,
    description=plugin_description,
    author=plugin_author,
    mail=plugin_author_email,
    url=plugin_url,
    license=plugin_license,
    requires=plugin_requires,
    additional_packages=plugin_additional_packages,
    ignored_packages=plugin_ignored_packages,
    additional_data=plugin_additional_data
)

if len(additional_setup_parameters):
    from octoprint.util import dict_merge
    setup_parameters = dict_merge(setup_parameters, additional_setup_parameters)

if __name__ == "__main__":
    version, cmdclass = get_version_and_cmdclass(plugin_package)
    setup_parameters["version"] = version
    setup(**setup_parameters)
