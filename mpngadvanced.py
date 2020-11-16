from pymol import cmd


def mpngAdvanced(width=800, height=600, prefix=""):
    '''
DESCRIPTION
    "mpngAdvanced" produces a series of PNG files corresponding to
    states of the current structure.
ARGUMENTS

    width = int: a PNG file width in pixels {default: 800}
    height = int: a PNG file height in pixels {default: 600}
    prefix = str: a PNG file name prefix {default: ""}
    '''
    for state_num in xrange(cmd.count_frames()):
        cmd.frame(state_num + 1)
        # cmd.ray(width, height)
        cmd.png("%s%03d.png" % (prefix, state_num + 1))
