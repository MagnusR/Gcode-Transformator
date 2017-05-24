# Gcode-Transformator
A command line tool to transform Gcode using any arbitrary transformation function

![Alt text](/images/Sphere-Transformation.jpg?raw=true "The Original toolpath and a transformed one")
	
~~~~
Transformer.py [-h] -i INPUT -t TRANSFORMATION -o OUTPUT
                      [-f FACTIONIZE] [-fl FACTIONIZE_LENGTH]
                      [-init_mpos INIT_MPOS INIT_MPOS INIT_MPOS]
                      [-init_cs INIT_CS]

A Script to transform a gcode file by a supplied transformation
function

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        An input gcode file to read
  -t TRANSFORMATION, --transformation TRANSFORMATION
                        Transfomration function, must be a .py module with
                        Transform function That accepts a 3-tuple of postion
                        and returns a transformed 3-tuple
  -o OUTPUT, --output OUTPUT
                        output gcode file, must be writable location
  -f FACTIONIZE, --factionize FACTIONIZE
                        to break into smaller movments, recommended for
                        accuracy
  -fl FACTIONIZE_LENGTH, --factionize_length FACTIONIZE_LENGTH
                        factionize interval, 0.5 by default
  -init_mpos INIT_MPOS INIT_MPOS INIT_MPOS
                        initial XYZ position, 0,0,0 by default
  -init_cs INIT_CS      initial cos, G54 by default	
~~~~
## Usage
The script takes an input gcode file, a transformation function (see examples in transformations), and produces an output file

                      
-FACTIONIZE flag breaks G1 moves longer the FACTIONIZE_LENGTH into smalle moves, this is needed for proper transformation onto curved surfaces etc, but increases file length.
#### Transformation functions accepted
The transformation function should be .py file with a Transform() function in it, that accepts a 3-tuple and produces a transformed 3-tuple

# License
MIT License

Copyright (c) 2017 Michael zlatin
gcode_machine - Copyright (c) 2016 Michael Franzl

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Please attrubite any academic publications as 
IEEE `M. Zlatin, “Gcode-Transformator.” 23-May-2017.`

MLA `Zlatin, Michael. Gcode-Transformator. Computer software. Vers. V1. N.p., 23 May 2017. Web. <https://github.com/MagnusR/Gcode-Transformator>.`

APA `Zlatin, M. (2017, May 23). Gcode-Transformator (Version V1) [Computer software]. Retrieved from https://github.com/MagnusR/Gcode-Transformator`
