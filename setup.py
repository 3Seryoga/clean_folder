from setuptools import setup

setup(name='clean_folder',
      version='1',
      description='Сортуе файли, переносить та створюе папку під кожний тип файлу',
      url='http://github.com/dummy_user/useful',
      author='3Seryoga',
      license='MIT',
      packages=['useful'],
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:def main:']})
