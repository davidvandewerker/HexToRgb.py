# HexToRgb.py
## Description
A simple python program for converting hexadecimal color values to rgb color values.

## Usage
Basic Usage:
```PowerShell
HexToRgb.py [-h] hex_color
```

Example:
*convert hex value #FFFFFF to rgb format.*
```PowerShell
PS> HexToRgb.py FFFFFF                                                                  
hex value:
 #FFFFFF

rgb value:
 rgb(255, 255, 255)
```

To view the the help menu, use the ```-h or --help``` argument:
```PowerShell
PS> HexToRgb.py -h
usage: HexToRgb.py [-h] hex_color

convert hexadecimal values to rgb values

positional arguments:
  hex_color   hexadecimal value to be converted to rgb

optional arguments:
  -h, --help  show this help message and exit

related programs: RgbToHex.py
```
