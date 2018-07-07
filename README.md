# PW-Sat2-EGSE
Software for PW-Sat2 Flight Model EGSE: health check software, EGSE Box v1

# PW-Sat2 Flight Model Health Check Software

The aim of the Health check software is to assist an engineer in the process of investigating the spacecraft state and condition (later referred to as 'performing health check').

It's based on following assumptions:
* test environment takes care of OBC time (every 10 s time is set to 0)
* there is a general set of available tests
* each test returns a result, it can take parameters in its constructor (e.g. test ranges)
* user should define test scenario that comprises of pre-defined tests but provide proper ranges and parameters
* output can be written to report file

## Working principles

The very low layer for communication with on-board computer is its terminal. Technically, possibilities of communication/control/reading are limited by commands available in [OBC Terminal](https://github.com/PW-Sat2/PWSat2OBC/blob/master/src/terminal.cpp#L7). In higher layer, on PC-side, [Python wrapper for OBC Terminal](https://github.com/PW-Sat2/PWSat2OBC/tree/master/integration_tests/obc) commands and reponses is written. Health Check Software utilizes this wrapper in its tests.

## How to

The software uses following dependencies:

* [PW-Sat2 OBC Software repository](https://github.com/PW-Sat2/PWSat2OBC) (added as submodule)

### Run the environment

1. Start with config file, let's name it `config.py`. It must contain number/name of the COM port to be used:

```
config = dict(OBC_COM='COM_PORT')
```

2. Run the test environment iPython console:

```python .\main.py -c .\config.py```

3. At this point the test environment should take control over the spacecraft time.

### Create and load test scenario

Basically, test scenario is a list of test objects. Test scenarios can be composed from pre-defined tests that are available in `tests` folder (any class derived from `SingleTest` class is a test). Some tests takes additional parameters to be defined in test scenario.

1. Put test scenario file in `test_scenarios` folder. Let's name it: `all_tests.py`

2. Import needed tests e.g.: `from tests.test_ping import TestPing`

2. Create list of test objects in desired order:

```
my_tests_queue = [
# OBC communication test
TestPing()]
```

It's recommended to build your own test scenarion taking as a reference provided test scenarios in this repository.

3. Run the test environment and import created test scenario:
`from test_scenarios.all_tests import *`

4. Load tests into test list:
`executor.load_tests_list(my_tests_queue)`

5. You can check if tests are loaded correctly:
`executor.show_test_list()`

You should obtain something similar to this table:
```
PW-Sat2 Health Check> executor.show_test_list()
+---+-----------+------------------------------+
| # |    Name   |         Description          |
+---+-----------+------------------------------+
| 0 | Test Ping | Basic OBC test - ping - pong |
+---+-----------+------------------------------+
```

#### Data ranges

Some tests need value ranges to decide wheter obtained from satellite data are correct or not. Data range files are available in `ranges` folder.

Examples:
```
'BATC.TEMP': [15, 25], # allowed BATC.TEMP value is between <15, 20>
'BATC.STATE': [3, 3],  # allowed BATC.STATE value equals 3
```

#### Test descriptions
Tests have defined default titles and description that can be overwritten at the level of test scenario.

Examples:
* `TestPing()` - this test uses default values for title and description

```
+----------------------------------+
| You are about running a test #0. |
+----------------------------------+
| 0. Test Ping                     |
+----------------------------------+
```

* `TestPing("my title", "my description")` - this test uses values defined by user in test scenario

```
+----------------------------------+
| You are about running a test #0. |
+----------------------------------+
| 0. my title                      |
+----------------------------------+
```

### Running tests from test scenario

Once the test scenario is loaded into executor it's possible to run tests in a few modes:
* `executor.run_all` - all tests in the list, one by one
* `executor.run_range(first_test, last_test)` - define range of tests to be executed
* `executor.run_single(test_no)` - run single test

In all or range-based modes particular test can be aborted (skipped), run. When particular test is completed the result is shown and test can be repeated or user can proceed with next test in the queue.

### Outputs

1. At any time user can display results history: `executor.show_results()`
2. At any time `describe()` can be invoked to set some important info for report e.g.:
```
PW-Sat2 Health Check> describe()
Title: Title of the tests
Description: You can type in observations etc. here
Place: Place of health check
Members: People involved
```
3. To generate report type in: `generate_report(path, name)`, e.g.:
```
generate_report('D:/Documents', 'Health Check Flight Model')
```
Two files should be created - `.md` and `.pdf`.



# PW-Sat2 EGSE Box v1.0

![dsc_3927](https://user-images.githubusercontent.com/6267528/42413528-b9d6f1a8-8222-11e8-9e28-1fd7c849faef.JPG)

Electrical Ground Support Equipment Box is an ultimate solution created to test and maintain flight model of PW-Sat2 spacecraft via umbilical cable. Its main functions include:
* external kill-switch of the satellite
* current probe on kill-switch line
* communication with on-board computer (OBC) via UART
* I2C bus and payload and UART sniffing
* solar panels simulator (with external power supply)

![dsc_3904](https://user-images.githubusercontent.com/6267528/42413513-806ea3ca-8222-11e8-9bac-681745ecf1c2.JPG)



## Technical details

### Kill switch
As kill switch key switch is used. LED diode indicates the state (on/off).

### Current probe

Current probe is based on Allegro MicroSystems ACS712ELCTR-05B-T Hall effect linear current sensor. Output analog signal from the sensor is digitized by Digilent Analog Discovery 2 scope. Analog Discovery 2 also provides 5 V supply for current sensor IC. Resolution of single milliamps can be achieved.

![vlcsnap-2018-07-07-20h09m29s593](https://user-images.githubusercontent.com/6267528/42413502-26df1510-8222-11e8-968d-9449a5192b0c.png)

### I2C bus and payload sniffing

8 channel logic states analyzer is used to record all data transmissions on I2C buses and OBC UART.

### UART Communication with OBC

UART to USB converter based on FT232 chip is used to communicate with on-board computer.

### Solar panel simulator

Solar panel simulator in the box comprises solely of diodes strings - for each channel (X, Y+, Y-) thus Solar panel simulator needs external power supply (3 channels, in CC mode).

![img_20180302_192208](https://user-images.githubusercontent.com/6267528/42413545-16c678e8-8223-11e8-83e0-b5dc84e1e0ca.jpg)

## Repository contents

The repository contains WaveForms workspace file `(*.dwf3work)` with configured power supply for current probe and calibration formula apploed in WaveForms scope view (sensor's output voltage to current).

## Practical information
It's good idea to adjust actual offset voltage (at zero current) because it strongly depends on ambient temperature.
Offset voltage is highlighted in yellow:

![image](https://user-images.githubusercontent.com/6267528/42413646-b87bf036-8224-11e8-9ef0-7db59b9c4a27.png)

