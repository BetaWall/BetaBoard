```diff
- Not currently deployable. Under active development.
```

<img src="https://cloud.githubusercontent.com/assets/1482941/22535019/0a8bcc9a-e8f0-11e6-8714-77324c347f00.png" alt="BetaBoard" height="80px" />

A multiplexed APA102 LED driver board for the BetaWall system.

## Features

- Runs off a single RS485 input
- Outputs SPI to APA102 LEDs
- Support up to 32 strips of 256 LEDs
- Supports daisychaining of up to 256 BetaBoards to drive a total of over 2 Million LEDs
- Board supports up to 40A continous current loads, but higher current can be achived with auxilery power supplies

## Block Diagram
![Block Diagram](https://cloud.githubusercontent.com/assets/1482941/22465406/7421d5a2-e7b3-11e6-8ee8-47d6ec707862.png)

## Additional Information for Implimentation

Further information about the BetaBoard can be found in the `datasheet` directory in the root of the repository.

![AGPLv3](https://www.gnu.org/graphics/agplv3-155x51.png)
