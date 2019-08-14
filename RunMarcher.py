from Marcher import Marcher
from Map import Map
import tkinter as tk
from tkinter import filedialog
from Weight import *
import sys
from argparse import ArgumentParser
import os

OUTPUT_DIR = "./output"

def runMarcher(image, function, filename, file_path, output_dir):
    cost = 0
    try:
        print("Parsing", file_path)
        cost = Marcher.findPath(image, function)
        image.outputPath(output_dir)
        print("Output path generated in", output_dir+"/"+filename, 
                "\n    ---> Total cost of path: ", cost)
        print("...........")
    except Exception:
        print("A valid path could not be generated for this image...")

if __name__ == "__main__":
   
    parser = ArgumentParser()
    parser.add_argument("-d", "--directory", dest="dir", default=None,
                        help="Parses all JPG, PNG, and PPM images in DIRECTORY", metavar="DIRECTORY")
    parser.add_argument("-m", "--maze", dest="is_maze",
                        action="store_true", default=False,
                        help="Set this option if input image is a black and white maze. May not work for non-fullsized mazes")

    args = vars(parser.parse_args())

    # pase all files in selected directory
    if args["dir"]:
       for filename in os.listdir(args["dir"]):
           file_path = args["dir"] + "/" + filename
           if os.path.isfile(file_path):
                image = Map(file_path)
                runMarcher(image, similar_colour, filename, file_path, OUTPUT_DIR)

    # prompt GUI file selection    
    else:   
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        image = Map(file_path)
        if args["is_maze"]:
            runMarcher(image, how_white, file_path, file_path, OUTPUT_DIR)
        else:
            runMarcher(image, similar_colour, file_path, file_path, OUTPUT_DIR)
            

        # print("Generating path...")
        # cost = Marcher.findPath(image, similar_colour)

        # image.outputPath()

        # print("Path successfully generated, output image can be found in directory: ./output")
        # print("Total cost of path: ", cost)