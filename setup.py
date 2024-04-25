from setuptools import setup, find_packages

setup_args = {
    "name": "ocp_vscode",
    "version": "2.3.1",
    "description": "OCP CAD Viewer for VSCode",
    "long_description": "An extension to show OCP cad CAD objects (CadQuery, build123d) in VS Code via threejs",
    "include_package_data": True,
    "python_requires": ">=3.9",
    "install_requires": [
        "ocp-tessellate>=2.3.2,<2.4.0",
        "requests",
        "ipykernel",
        "orjson",
        "websockets @ git+https://github.com/python-websockets/websockets.git@f0398141d2efd28f64d8e1d6d9adc179a9e5e334",
    ],
    "packages": find_packages(),
    "zip_safe": False,
    "author": "Bernhard Walter",
    "author_email": "b_walter@arcor.de",
    "url": "https://github.com/bernhard-42/vscode-ocp-cad-viewer",
    "keywords": ["vscode", "widgets", "CAD", "cadquery"],
    "classifiers": [
        "Development Status :: 5 - Production/Stable",
        "Framework :: IPython",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Multimedia :: Graphics",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
}

setup(**setup_args)
