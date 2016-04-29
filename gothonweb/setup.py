try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Sophie Cowie',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'sophie_cowie@hotmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'gothonweb'
}

setup(**config)