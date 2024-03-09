from setuptools import setup, find_packages

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    reuirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements





setup(
    name = "Xray",
    version= "0.0.1",
    author = "DeependraVerma",
    author_email = "deependra.verma00@gmail.com",
    install_requires = get_requirements("requirements_dev.txt"),
    package = find_packages()
)