# Robot Framework Page Object Model Demo

## Robot Framework Introduction
[Robot Framework](http://robotframework.org) is a generic open source
automation framework for acceptance testing, acceptance test driven
development (ATDD), and robotic process automation (RPA). It has simple plain
text syntax and it can be extended easily with libraries implemented using
Python or Java.

Robot Framework is operating system and application independent. The core
framework is implemented using [Python](http://python.org), supports both
Python 2 and Python 3, and runs also on [Jython](http://jython.org) (JVM),
[IronPython](http://ironpython.net) (.NET) and [PyPy](http://pypy.org).
The framework has a rich ecosystem around it consisting of various generic
libraries and tools that are developed as separate projects. For more
information about Robot Framework and the ecosystem, see
http://robotframework.org.

[GitHub](https://github.com/robotframework/robotframework)

[PyPI](https://pypi.python.org/pypi/robotframework)

[Maven central](http://search.maven.org/#search%7Cga%7C1%7Ca%3Arobotframework)

## Installation
1. Download and Install [Python](https://www.python.org/downloads/ "Python").
2. Check Python installation

    `python3 -V`

3. Install [pip](https://pip.pypa.io/ "pip").

    `pip3 -V`
    
4. Download and install Intellij [Intellij](https://www.jetbrains.com/pycharm/download/).
5. Install Plugin [Hyper Robot Code Support](https://plugins.jetbrains.com/plugin/16382-hyper-robotframework-support) extension from Intellij's Marketplace
6. Install Robot Framework.

    `pip3 install robotframework`
    
7. Install Selenium Library.

    `pip3 install robotframework-seleniumlibrary`

8. Install Browser Drivers 

    `pip3 install webdrivermanager`

## Example
Here, I have developed sample test cases for a sample web site [Demoblaze](https://demoblaze.com/).

This project is developed to demonstrate Web UI automation using Robot Framework and Selenium Library.

Here, there are 3 variables `${SMALL_RETRY_SCALE}`, `${MEDIUM_RETRY_SCALE}` and `${LARGE_RETRY_SCALE}` for retrying the keywords when they are failing. Each variable has assigned with the number of retries. Automation engineers are advised to use `${SMALL_RETRY_SCALE}` as the default number of retries for the keywords. If there are big delays in some scenarios, you can use other variables `${MEDIUM_RETRY_SCALE}` and `${LARGE_RETRY_SCALE}`. You can find the examples for this in `object-repository/page-objects` directory.

Test cases are in `test-cases` directory and covers login functionality.

## File organization
```
|- robot-framework-page-object-model-demo/                        // Home folder for robot selenium UI automation project
  |- configs/ApplicationVariables.robot                           // Application common variables file
  |- configs/BrowserDetails.robot                                 // Test execution browser configurations
  |- configs/EnvDetails.robot                                     // Test execution environment configurations
  |- configs/SeleniumConfigs.robot                                // Selenium configurations
  |- object-repository/locators/*.robot                           // UI locators of the application
  |- object-repository/page-objects/CommonPo.robot                // Common keywords for the application
  |- object-repository/page-objects/*.robot                       // Page object keywords of the application
  |- test-cases/..../*.robot                                      // Test cases of the application
|- results                                                        // Test results will be saving here
|- .gitignore                                                     // Excluded the unnecessary files in the repo
|- README.md                                                      // This file
```

## Usage
Starting from Robot Framework 3.0, tests are executed from the command line
using the ``robot`` script or by executing the ``robot`` module directly
like ``python -m robot`` or ``jython -m robot``.

The basic usage is giving a path to a test (or task) file or directory as an
argument with possible command line options before the path

    python3 -m robot -v ENV:DEMO -i Smoke -d path/to/results path/to/tests/
    python3 -m robot -v ENV:DEMO -i Smoke -d ui-automation/results ui-automation/test-cases/LoginTest.robot

"***-v***" refers to the variables. To replace a declared value within the code, you can specify a variable name and value.

"***-i***" refers to the tags. To run only a selected group of tests, you may specify a tag name.

"***-d***" refers to the test results. The location to save the test results can be specified here.

Additionally, there is ``rebot`` tool for combining results and otherwise
post-processing outputs

    rebot --name Example output1.xml output2.xml

Run ``robot --help`` and ``rebot --help`` for more information about the command
line usage. For a complete reference manual see [Robot Framework User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html "Robot Framework User Guide").

