# Djikstra Pixel Marcher
Finds and generates shortest path and/or path of minimal total pixel gradient across image (JPG, PNG, PPM).

## Installation
cd into directory where repo was cloned
```shell
    pip install -r requirements.txt
```

## How To Run
```shell
    python RunMarcher.py
```
For details on more command line options such as bulk parsing, run:
```shell
    python RunMarcher.py --help
```

![alt text](https://raw.githubusercontent.com/RylandWang/Djikstra-Pixel-Marcher/master/output/examples/Path-bigmaze.jpg)

![alt text](https://raw.githubusercontent.com/RylandWang/Djikstra-Pixel-Marcher/master/output/examples/Path-maze.jpg)

![alt text](https://raw.githubusercontent.com/RylandWang/Djikstra-Pixel-Marcher/master/output/examples/Path-wallpaper.jpg)

![alt text](https://raw.githubusercontent.com/RylandWang/Djikstra-Pixel-Marcher/master/output/examples/Path-water.jpg)

![alt text](https://raw.githubusercontent.com/RylandWang/Djikstra-Pixel-Marcher/master/output/examples/Path-scream.png)

## Implementation
Implemented using Djikstra's algorithm and priority queue (min heap implementation)

## Authors
* **Ryland Wang** 


