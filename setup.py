from setuptools import setup, find_namespace_packages

setup(name='clean-folder',
      version='1',
      description='Сортуе файли, переносить та створюе папку під кожний тип файлу',
      url='https://github.com/3Seryoga/clean_folder',
      author='3Seryoga',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']})
