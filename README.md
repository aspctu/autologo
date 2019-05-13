# AutoLogo
Automatically generate object detection networks via *one logo image*

# Usage

1) run gen_data.py with following arguments: 

    `python gen_data.py --logo (path to logo image) --label (class name)`

2) The above command will push 2 files into the csvFiles directory:

     `[label].csv` : Holds the CSVGenerator file needed to train the network in the next step.

     `label.csv` : Attaches label to key value, needed to train as well

3) The new synthetic dataset will be placed in `/syntheticImages`

3) CD into the `retinanet/keras_retinanet/bin` directory 

4) Run `train.py` with the following arguments:

     `python train.py <path/to/csvFiles/[label].csv> <path/to/csvFiles/label.csv>`

     Trianing will begin and snapshots will be saved to the snapshot folder


# Acknowledgements 

Creds to @fizyr for the keras-retinanet model definition. 





