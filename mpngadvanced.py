from pymol import cmd

'''
DESCRIPTION
    "mpng_status" produces a series of PNG files corresponding to
    states of the current structure.
    "mpng_objs" produces a series of PNG files corresponding to
    objects on pymol.

ARGUMENTS
    width = int: a PNG file width in pixels {default: 800}
    height = int: a PNG file height in pixels {default: 600}
    prefix = str: a PNG file name prefix {default: ""}
    output = str: a PNG file output directory {default: "."}
    '''

def mpng_states(width=800, height=600, prefix="", output="."):
    cmd.set("ray_opaque_background", 1)
    for state_num in range(cmd.count_frames()):
        cmd.frame(state_num + 1)
        cmd.ray(width, height)
        cmd.png("%s/%s%03d.png" % (output, prefix, state_num + 1), dpi=300)
    cmd.set("ray_opaque_background", 0)
cmd.extend("mpng_states", mpng_states)

def mpng_objs(width=800, height=600, prefix="", output="."):
    cmd.set("ray_opaque_background", 1)
    for obj in cmd.get_names():
        cmd.disable("(all)")
        cmd.enable(obj)
        cmd.ray(width=width, height=height)
        cmd.png("%s/%s.png" % (output, obj), dpi=300)
    cmd.set("ray_opaque_background", 0)
cmd.extend("mpng_objs", mpng_objs)
