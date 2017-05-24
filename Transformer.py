
import argparse
import imp
import sys

from gcode_machine import gcode_machine


class GcodeTransformator:

    def main(self):
        self.parse_args()


        gcode=self.args.input.readlines()

        try:
            transform_src = imp.load_source('', self.args.transformation)
            if  len(transform_src.Transform([1,1,1]))!=3:
                raise ImportError, "Transform function didnt pass test"
        except:
            print("Transformation import not successfull")
            sys.exit(1)

        if self.args.factionize:
            factionized_gcode=list(self.factioniziation_pass(gcode))
            gcode=factionized_gcode

        #make the actual transformation
        transformed_gcode=list(self.transformation_pass(gcode,transform_src.Transform))
        gcode=transformed_gcode

        try:
            self.args.output.writelines(gcode)
        except:
            print("Output not writeable")
            sys.exit(1)

    def parse_args(self):
        parser = argparse.ArgumentParser(description="A Script to transform a planar gcode file by a supplied transformation function")
        parser.add_argument('-i','--input', type=argparse.FileType('r'),required=True,help="An input gcode file to read")
        parser.add_argument('-t','--transformation', required=True,help="Transfomration function, must be a .py module with Transform function"
                                                                                                            "\nThat accepts a 3-tuple of postion and returns a transformed 3-tuple")
        parser.add_argument('-o','--output', type=argparse.FileType('w'),required=True,help="output gcode file, must be writable location")
        parser.add_argument('-f','--factionize', action="store", type=bool, default=True,help="to break into smaller movments, recommended for accuracy" )
        parser.add_argument('-fl', '--factionize_length', action="store", type=float, default=0.5,
                            help="factionize interval, 0.5 by default")
        # initial conditions
        parser.add_argument('-init_mpos', action="store", nargs=3, default=(0, 0, 0),help="initial XYZ position, 0,0,0 by default")
        parser.add_argument('-init_cs', action="store", nargs=1, default="G54",
                            help="initial cos, G54 by default")
        self.args = parser.parse_args()
        self.coordinate_system_offsets = cs_offsets = {"G54": (0, 0, 0)}

    def factioniziation_pass(self,gcode):
        gcm = gcode_machine.GcodeMachine(self.args.init_mpos, self.args.init_cs, self.coordinate_system_offsets)
        gcm.do_fractionize_lines = True
        gcm.do_fractionize_arcs = True
        gcm.fract_linear_segment_len = self.args.factionize_length
        gcm.fract_linear_threshold = self.args.factionize_length

        for line in gcode:
            gcm.set_line(line)  # feed the line into the machine
            gcm.find_vars()  # parse variable usages
            gcm.substitute_vars()  # substitute variables
            gcm.parse_state()  # parse positions etc. and update the machine state

            gcm.transform_comments()  # transform parentheses to semicolon comments
            for x in gcm.fractionize():
                yield x
            gcm.done()  # update the machine position

    def transformation_pass(self,gcode,transform):
        gcm = gcode_machine.GcodeMachine(self.args.init_mpos, self.args.init_cs, self.coordinate_system_offsets)
        for line in gcode:
            gcm.set_line(line)  # feed the line into the machine

            gcm.find_vars()  # parse variable usages
            gcm.substitute_vars()  # substitute variables
            gcm.parse_state()  # parse positions etc. and update the machine state
            # detect if line is position line
            gcm.transform_comments()  # transform parentheses to semicolon comments
            if gcm.dist == 0:
                transformed_line = gcm.line
            else:
                new_position = transform(gcm.position_w)
                new_target = transform(gcm.target_w)
                # update the machine position
                feed = ("F" + '%.2f' % (gcm.feed_in_current_line)) if gcm.contains_feed else ""
                spindle = ("S" + '%.2f' % gcm.current_spindle_speed) if gcm.contains_spindle else ""
                # add movement mode
                transformed_line = "G%d " % gcm.current_motion_mode
                # if absolute mode, change target
                if gcm.current_distance_mode == "G90":
                    transformed_line = transformed_line + "X" + str(new_target[0]) + "Y" + str(new_target[1]) + "Z" + str(
                        new_target[2]) + feed + spindle
                # if relative mode, change target as displacment
                if gcm.current_distance_mode == "G91":
                    transformed_line = transformed_line + "X" + str(new_target[0] - new_position[0]) + "Y" + str(
                        new_target[1] - new_position[1]) + "Z" + str(new_target[2] - new_position[2]) + feed + spindle
                transformed_line = transformed_line + "\n"
            yield transformed_line
            gcm.done()

if __name__ == "__main__":
    t=GcodeTransformator()
    t.main()