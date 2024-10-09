## Introduction
This project aims at helping developers to create CLI tools and distribute it.

## Pre-requisites
1. You have installed Python  (At the time of writing this, I have 3.12.4 installed)
2. IDE - Visual Studio Code 
3. Clone the GIT project in your directory/workspace
3. Create a python virtual environment in your directory

## Steps to create your first CLI automation tool and distribute it

1. Install dependencies using pip. Refer requirements.txt

2. Run command - This is to create a command line tool and --editable is to get real time changes. No need to install again for any new changes.
```
pip3 install --editable .
```

3. Run command - This will run the agent_automation and command to upload the sample json and print it. I have provided a sample.json as part of GIT repo.
```
agent_automation read-json --file /path/of/the/json/file/sample.json
```

4. Now next step is to package your cli tool 

5. Ensure you have wheel installed
```
pip3 install setuptools wheel
```

6. You can create wheel file directly from setup.py **python3 setup.py bdist_wheel** but this is a deprecated approach. We will create wheel file using pypa/build. First let's install pypa/build
```
pip3 install build
```

7. Run the below command to create wheel package
```
python3 -m build
```

8. You will get the below message if the wheel file is generated successfully
```
Successfully built agent_automation-0.1.0.tar.gz and agent_automation-0.1.0-py3-none-any.whl
```

7. You will see a dist folder created with a .whl file - **agent_automation-0.1.0-py3-none-any.whl**
    * agent_automation - This is the package name
    * 0.1.0 - This is the package version
    * py3 - This package supports python3
    * none - This is the ABI tag, meaning the ABI isn’t a factor. ABI - Application Binary Interface
    * any - This is for platform indicating that this wheel will run on any platform

8. To install wheel locally, open a new terminal window
```
pip3 install <path/of/your/dist/folder>/agent_automation-0.1.0-py3-none-any.whl
```

9. Once installed successfully, you can simple call your command line tool as
```
agent_automation --help
```

10. You can then run any of the click commands
```
agent_automation read-json --file /path/of/the/json/file/sample.json
``` 

11. <span style="color:Orange">[OPTIONAL]</span> To distribute the wheel package to PyPi, you have to install twine
```
pip3 install twine
```

12. <span style="color:Orange">[OPTIONAL]</span> Upload to Pypi. You will need Pypi account and api token.
```
twine upload dist/*
```

## References

1. https://click.palletsprojects.com/en/8.1.x/
2. https://realpython.com/python-wheels/
3. https://opensource.org/license/mit