"""
Section related keywords and
definitions for special elements
"""
import reader_utils

# Section related keywords
# Nodal thickness is kind of a section
# Does pre-tension section belong here?
sec_rel = ['*BEAMGENERALSECTION', '*BEAMSECTION', '*FLUIDSECTION',
           '*NODALTHICKNESS', '*NORMAL', 'PRE-TENSIONSECTION',
           '*SHELLSECTION', '*SOLIDSECTION', '*DASHPOT', '*GAP', '*SPRING']


def star_beam_general_section_setup():
    print("SETUP NOT COMPLETED")
    return


def star_beam_general_section_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_beam_section_setup(keys, sections):
    """
    Sets up a beam section for a set of beam elements
    """
    # reader_utils.untested_warning(keys[0])
    # Checks for ELSET in keywords
    # Spaces were removed so can't be a space
    cur_sec = " "
    for i in keys[1:]:
        if i.startswith("ELSET"):
            # reader_utils.untested_warning(keys[0], i)
            cur_sec = i.split("=")[1]
            sections[cur_sec] = dict()
    # Make sure keyword was present
    if cur_sec == " ":
        raise ValueError("ELSET not specified")
    # Add type
    sections[cur_sec]["TYPE"] = "BEAMSECTION"
    for i in keys[1:]:
        # Orientation not included
        if i.startswith("MATERIAL"):
            # reader_utils.untested_warning(keys[0], i)
            sections[cur_sec]["MATERIAL"] = i.split("=")[1]
        elif i.startswith("SECTION"):
            # reader_utils.untested_warning(keys[0], i)
            sections[cur_sec]["SECTION"] = i.split("=")[1]
        elif i.startswith("OFFSET1"):
            reader_utils.untested_warning(keys[0], i)
            sections[cur_sec]["OFFSET1"] = i.split("=")[1]
        elif i.startswith("OFFSET2"):
            reader_utils.untested_warning(keys[0], i)
            sections[cur_sec]["OFFSET2"] = i.split("=")[1]
        elif i != keys[0] and not i.startswith("ELSET"):
            reader_utils.missed_option(keys[0], i)
    # There are no examples using ORIENTATION keyword
    # !! Orientation keyword not completed
    return sections[cur_sec]


def star_beam_section_receive(line, last_info):
    """
    Receives a beam section for a set of beam elements
    line -- unchanged line
    last_info -- list containing current section
    """
    # Eliminate whitespace
    up = ''.join(line.split())
    # Eliminate d0's that fortran likes
    up = ''.join(up.split('d0'))
    up = up.split(',')
    # Get cur_sec from last_info
    cur_sec = last_info
    # These lines don't repeat, so can assume if not
    # second line then it is the third
    if "THICKNESS" not in cur_sec.keys():
        # Should give both thickness directions
        if len(up) != 2:
            raise ValueError("Should have two thicknesses")
        cur_sec["THICKNESS"] = [float(i) for i in up]
    else:
        # Third line
        if len(up) != 3:
            raise ValueError("Should have three coordinates")
        cur_sec["D1"] = [float(i) for i in up]
    return


def star_fluid_section_setup():
    print("SETUP NOT COMPLETED")
    return


def star_fluid_section_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_nodal_thickness_setup():
    print("SETUP NOT COMPLETED")
    return


def star_nodal_thickness_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_normal_setup():
    print("SETUP NOT COMPLETED")
    return


def star_normal_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_pre_tension_section_setup():
    print("SETUP NOT COMPLETED")
    return


def star_pre_tension_section_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_shell_section_setup(keys, sections):
    """
    Sets up a shell section for a set of shell elements
    """
    # reader_utils.untested_warning(keys[0])
    # Checks for ELSET in keywords
    # Spaces were removed so can't be a space
    cur_sec = " "
    for i in keys[1:]:
        if i.startswith("ELSET"):
            # reader_utils.untested_warning(keys[0], i)
            cur_sec = i.split("=")[1]
            sections[cur_sec] = dict()
    # Make sure keyword was present
    if cur_sec == " ":
        raise ValueError("ELSET not specified")
    # Add type
    sections[cur_sec]["TYPE"] = "SHELLSECTION"
    for i in keys[1:]:
        if i.startswith("MATERIAL"):
            # reader_utils.untested_warning(keys[0], i)
            sections[cur_sec]["MATERIAL"] = i.split("=")[1]
        elif i.startswith("COMPOSITE"):
            reader_utils.untested_warning(keys[0], i)
            sections[cur_sec]["COMPOSITE"] = i.split("=")[1]
        elif i.startswith("ORIENTATION"):
            reader_utils.untested_warning(keys[0], i)
            sections[cur_sec]["ORIENTATION"] = i.split("=")[1]
        elif i.startswith("NODALTHICKNESS"):
            reader_utils.untested_warning(keys[0], i)
            sections[cur_sec]["NODALTHICKNESS"] = i.split("=")[1]
        elif i.startswith("OFFSET"):
            reader_utils.untested_warning(keys[0], i)
            sections[cur_sec]["OFFSET"] = i.split("=")[1]
        elif i != keys[0] and not i.startswith("ELSET"):
            reader_utils.missed_option(keys[0], i)
    return sections[cur_sec]


def star_shell_section_receive(line, last_info):
    """
    Receives a shell section for a set of shell elements
    line -- unchanged line
    last_info -- list containing current section
    """
    # Eliminate whitespace
    up = ''.join(line.split())
    # Eliminate d0's that fortran likes
    up = ''.join(up.split('d0'))
    up = up.split(',')
    # Get cur_sec from last_info
    cur_sec = last_info
    # Skip if includes *nodalthickness
    if "NODALTHICKNESS" in cur_sec.keys():
        return
    if "COMPOSITE" not in cur_sec.keys():
        cur_sec["THICKNESS"] = float(line)
    else:   
        # includes composite
        # Create layers if not already created
        if "LAYERS" not in cur_sec.keys():
            cur_sec["LAYERS"] = []
        cur_sec["LAYERS"].append(dict())
        layer = cur_sec["LAYERS"][-1]
        # first is thickness
        layer["THICKNESS"] = float(up[0])
        # the second is nothing
        # third is name of material
        layer["MATERIAL"] = up[2]
        # Fourth is orientation (optional)
        if len(up) > 3:
            layer["ORIENTATION"] = up[3]
    return


def star_solid_section_setup(keys,  sections):
    """
    Sets up a solid section for a set of solid elements
    """
    # reader_utils.untested_warning(keys[0])
    # Checks for ELSET in keywords
    # Spaces were removed so can't be a space
    cur_sec = " "
    for i in keys[1:]:
        if i.startswith("ELSET"):
            # reader_utils.untested_warning(keys[0], i)
            cur_sec = i.split("=")[1]
            sections[cur_sec] = dict()
    # Make sure keyword was present
    if cur_sec == " ":
        raise ValueError("ELSET not specified")
    # Add type
    sections[cur_sec]["TYPE"] = "SOLIDSECTION"
    for i in keys[1:]:
        if i.startswith("MATERIAL"):
            # reader_utils.untested_warning(keys[0], i)
            sections[cur_sec]["MATERIAL"] = i.split("=")[1]
        elif i.startswith("ORIENTATION"):
            reader_utils.untested_warning(keys[0], i)
            sections[cur_sec]["ORIENTATION"] = i.split("=")[1]
        elif i != keys[0] and not i.startswith("ELSET"):
            reader_utils.missed_option(keys[0], i)
    return sections[cur_sec]


def star_solid_section_receive(line, last_info):
    """
    Receives a solid section for a set of solid elements
    line -- unchanged line
    last_info -- list containing current section
    """
    # Eliminate whitespace
    up = ''.join(line.split())
    # Eliminate d0's that fortran likes
    up = ''.join(up.split('d0'))
    up = up.split(',')
    # Get cur_sec from last_info
    cur_sec = last_info
    # Could be thickness or cross sectional area so calling it value
    cur_sec["VALUE"] = float(line)
    return


def star_dashpot_setup():
    print("SETUP NOT COMPLETED")
    return


def star_dashpot_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_gap_setup():
    print("SETUP NOT COMPLETED")
    return


def star_gap_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_spring_setup():
    print("SETUP NOT COMPLETED")
    return


def star_spring_receive():
    print("RECEIVE NOT COMPLETED")
    return


def sec_rel_setup(keys, sections):
    """
    Completes necessary set up for
    section related keys
    """
    if keys[0] == "*BEAMSECTION":
        last_info = star_beam_section_setup(keys, sections)
    elif keys[0] == "*SOLIDSECTION":
        last_info = star_solid_section_setup(keys, sections)
    elif keys[0] == "*SHELLSECTION":
        last_info = star_shell_section_setup(keys, sections)
    else:
        reader_utils.missed_keyword(keys[0])
        # Just so last_info will be something
        last_info = []
    return last_info


def sec_rel_receive(last_key, line, last_info):
    """
    Completes necessary commands for
    receiving section related keys
    """
    if last_key == "*BEAMSECTION":
        star_beam_section_receive(line, last_info)
    elif last_key == "*SOLIDSECTION":
        last_info = star_solid_section_receive(line, last_info)
    elif last_key == "*SHELLSECTION":
        last_info = star_shell_section_receive(line, last_info)
    else:
        print(last_key)
        reader_utils.missed_keyword(last_key)
    return
