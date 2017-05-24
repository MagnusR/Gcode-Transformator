# Gcode-Transformator
A command line tool to transform Gcode using any arbitrary transformation function

	
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
# Usage
The script takes an input gcode file, a transformation function (see examples in transformations), and produces an output file

                      
-FACTIONIZE flag breaks G1 moves longer the FACTIONIZE_LENGTH into smalle moves, this is needed for proper transformation onto curved surfaces etc, but increases file length.
# Transformation functions accepted
The transformation function should be .py file with a Transform() function in it, that accepts a 3-tuple and produces a transformed 3-tuple
