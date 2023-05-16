from setuptools import setup

package_name = "{{ cookiecutter.project_name | snakecase }}"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="juruc",
    maintainer_email="jafar.uruc@gmail.com",
    description="{{ cookiecutter.project_short_description }}",
    license="BSD",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [],
    },
)
