# Oscilloscope_Plot_Data_Decoder
[![Maintainability](https://api.codeclimate.com/v1/badges/1971e445184b69a5452a/maintainability)](https://codeclimate.com/github/UnleashMe69/TDS694C/maintainability)

Oscilloscope_Plot_Data_Decoder is a Python script to decode the plot data transferred by the oscilloscope TDS694C.

When you transfer signal plotted on the oscilloscope using LabView, the data are encoded. This Python script decodes the data and writes in a csv file so you can freely plot the data on your favorite software and add it to your articles, for example.

For more information about the encoded data of the TDS694C, the user can refer to  _TDS Family Oscilloscope Programmer Manual "Command Descriptions"_

The corresponding page (355) can be found in this repository with an example file (file named _fft.txt_) of encoded plot data exported by the TDS694C.
## Installation

You can either download the Python script or clone this repository
[git](https://github.com/UnleashMe69/TDS694C) and run the script.

```bash
git clone https://github.com/UnleashMe69/TDS694C
```

## Usage

```bash
chmod +x oscilloscope_plot_data_decoder.py.py
./oscilloscope_plot_data_decoder.py -f exported_data.txt -o decoded_data.csv
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
If you would like to do the same for other oscilloscopes, let's discuss it and we can do it.


## License
[MIT](https://choosealicense.com/licenses/mit/)
