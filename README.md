# Djikstra Pixel Marcher
Finds and generates shortest path and/or path of minimal total pixel gradient (difference of adjacent RGB value) across image (JPG, PNG, PPM).

## Installation
cd into directory where repo was cloned
```shell
    pip install -r requirements.txt
```

## How To Run

### Steps
- `git clone` repo, `cd` into directory
- `python RunMarcher.py`

For details on more command line options such as bulk parsing, run:
```shell
    python RunMarcher.py --help
```

## Samples
![alt text](https://raw.githubusercontent.com/RylandWang/Djikstra-Pixel-Marcher/master/output/examples/Path-maze.jpg)

![alt text](https://raw.githubusercontent.com/RylandWang/Djikstra-Pixel-Marcher/master/output/examples/Path-bigmaze.jpg)

![alt text](https://raw.githubusercontent.com/RylandWang/Djikstra-Pixel-Marcher/master/output/examples/Path-wallpaper.jpg)

![alt text](https://raw.githubusercontent.com/RylandWang/Djikstra-Pixel-Marcher/master/output/examples/Path-water.jpg)

![alt text](https://raw.githubusercontent.com/RylandWang/Djikstra-Pixel-Marcher/master/output/examples/Path-scream.png)

## Implementation
* Algorithms: Djikstra's path finding algorithm, Min heapify
* Data Stuctures: Priority queue (min heap implementation)
* Libraries/API: PIL (image parsing), tKinter (GUI), argparse (command line arugment parsing)

## Authors
* **Ryland Wang** 


