from setuptools import setup

setup(name='palidroms',
      version='0.1',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      author='Peter Kirov',
      author_email='p.kirov@gmail.com',
      license='MIT',
      packages=['palidroms'],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['palidroms=palidroms.__main__:main'],
      },
      include_package_data=True,
      zip_safe=False)
