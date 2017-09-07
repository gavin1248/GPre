"""
Contains output related keywords
Separated from steps although it goes into step object
"""
import reader_utils

# Output related keywords
op_rel = ['*CONTACTFILE', '*CONTACTOUTPUT', '*CONTACTPRINT',
          '*ELEMENTOUTPUT', '*ELFILE', '*ELPRINT',
          '*FACEPRINT', '*NODEFILE', '*NODEOUTPUT', '*NODEPRINT',
          '*OUTPUT']


# No receive since no additional lines
def star_output_setup(keys, step):
    """
    Sets up a dictionary for output in step
    keys -- cleaned keywords separated by commas
    step -- dictionary of current step
    """
    reader_utils.untested_warning(keys[0])
    # Add dictionary for output if not present
    if 'OUTPUT' not in step.keys():
        step['OUTPUT'] = []
    # Grab output
    output = step['OUTPUT']
    # Create entry for current output
    output.append(dict())
    # Grab newly created dictionary
    op = output[-1]
    # Add type of output
    op["TYPE"] = "OUTPUT"
    
    # Look for optional keywords
    if len(keys) > 1:
        for i in keys[1:]:
            if i.startswith('FREQUENCYF'):
                op['FREQUENCYF'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('FREQUENCY'):
                op['FREQUENCY'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i != keys[0]:
                reader_utils.missed_option(keys[0], i)
    return


def star_element_output_setup(keys, step):
    reader_utils.untested_warning(keys[0])
    # Add dictionary for output if not present
    if 'OUTPUT' not in step.keys():
        step['OUTPUT'] = []
    # Grab output
    output = step['OUTPUT']
    # Create entry for current output
    output.append(dict())
    # Grab newly created dictionary
    el_out = output[-1]
    # Add type of output
    el_out["TYPE"] = "ELEMENTOUTPUT"
    # Add set for variables
    # Dont care about order and dont want duplicates
    el_out["VARS"] = set()
    # Look for optional keywords
    if len(keys) > 1:
        for i in keys:
            if i.startswith('FREQUENCYF'):
                el_out['FREQUENCYF'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('FREQUENCY'):
                el_out['FREQUENCY'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('GLOBAL'):
                el_out['GLOBAL'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('OUTPUT'):
                el_out['OUTPUT'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('SECTIONFORCES'):
                el_out['SECTIONFORCES'] = True
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('TIMEPOINTS'):
                el_out['TIMEPOINTS'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('LASTITERATIONS'):
                el_out['LASTITERATIONS'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('CONTACTELEMENTS'):
                el_out['CONTACTELEMENTS'] = True
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('NSET'):
                el_out['NSET'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i != keys[0]:
                reader_utils.missed_option(keys[0], i)
    return


def star_element_output_receive(line, step):
    # Note that all receives are same, may want to condense
    # Grab set
    varset = step["OUTPUT"][-1]["VARS"]
    # Capitalize line
    up = line.upper()
    # Eliminate whitespace
    up = ''.join(up.split())
    # Split by comma
    spl = up.split(',')
    # Union the variables with the line in set form
    varset |= set(spl)
    return


def star_el_file_setup(keys, step):
    # reader_utils.untested_warning(keys[0])
    # Add dictionary for output if not present
    if 'OUTPUT' not in step.keys():
        step['OUTPUT'] = []
    # Grab output
    output = step['OUTPUT']
    # Create entry for current output
    output.append(dict())
    # Grab newly created dictionary
    el_out = output[-1]
    # Add type of output
    el_out["TYPE"] = "ELFILE"
    # Add set for variables
    # Dont care about order and dont want duplicates
    el_out["VARS"] = set()
    # Look for optional keywords
    if len(keys) > 1:
        for i in keys:
            if i.startswith('FREQUENCYF'):
                el_out['FREQUENCYF'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('FREQUENCY'):
                el_out['FREQUENCY'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('GLOBAL'):
                el_out['GLOBAL'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('OUTPUT'):
                el_out['OUTPUT'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('SECTIONFORCES'):
                el_out['SECTIONFORCES'] = True
                # reader_utils.untested_warning(keys[0], i)
            elif i.startswith('TIMEPOINTS'):
                el_out['TIMEPOINTS'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('LASTITERATIONS'):
                el_out['LASTITERATIONS'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('CONTACTELEMENTS'):
                el_out['CONTACTELEMENTS'] = True
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('NSET'):
                el_out['NSET'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i != keys[0]:
                reader_utils.missed_option(keys[0], i)
    return


def star_el_file_receive(line, step):
    # Note that all receives are same, may want to condense
    # Grab set
    varset = step["OUTPUT"][-1]["VARS"]
    # Capitalize line
    up = line.upper()
    # Eliminate whitespace
    up = ''.join(up.split())
    # Split by comma
    spl = up.split(',')
    # Union the variables with the line in set form
    varset |= set(spl)
    return


def star_el_print_setup(keys, step):
    # reader_utils.untested_warning(keys[0])
    # Add dictionary for output if not present
    if 'OUTPUT' not in step.keys():
        step['OUTPUT'] = []
    # Grab output
    output = step['OUTPUT']
    # Create entry for current output
    output.append(dict())
    # Grab newly created dictionary
    el_out = output[-1]
    # Add type of output
    el_out["TYPE"] = "ELPRINT"
    # Add set for variables
    # Dont care about order and dont want duplicates
    el_out["VARS"] = set()
    # Look for optional keywords
    if len(keys) > 1:
        for i in keys:
            if i.startswith('FREQUENCYF'):
                el_out['FREQUENCYF'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('FREQUENCY'):
                el_out['FREQUENCY'] = i.split('=')[1]
                # reader_utils.untested_warning(keys[0], i)
            elif i.startswith('GLOBAL'):
                el_out['GLOBAL'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('TIMEPOINTS'):
                el_out['TIMEPOINTS'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('ELSET'):
                el_out['ELSET'] = i.split('=')[1]
                # reader_utils.untested_warning(keys[0], i)
            elif i.startswith('TOTALS'):
                el_out['TOTALS'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i != keys[0]:
                reader_utils.missed_option(keys[0], i)
    return


def star_el_print_receive(line, step):
    # Note that all receives are same, may want to condense
    # Grab set
    varset = step["OUTPUT"][-1]["VARS"]
    # Capitalize line
    up = line.upper()
    # Eliminate whitespace
    up = ''.join(up.split())
    # Split by comma
    spl = up.split(',')
    # Union the variables with the line in set form
    varset |= set(spl)
    return


def star_contact_file_setup():
    print("SETUP NOT COMPLETED")
    return


def star_contact_file_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_contact_output_setup():
    print("SETUP NOT COMPLETED")
    return


def star_contact_output_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_contact_print_setup():
    print("SETUP NOT COMPLETED")
    return


def star_contact_print_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_face_print_setup():
    print("SETUP NOT COMPLETED")
    return


def star_face_print_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_node_file_setup(keys, step):
    # reader_utils.untested_warning(keys[0])
    # Add dictionary for output if not present
    if 'OUTPUT' not in step.keys():
        step['OUTPUT'] = []
    # Grab output
    output = step['OUTPUT']
    # Create entry for current output
    output.append(dict())
    # Grab newly created dictionary
    n_out = output[-1]
    # Add type of output
    n_out["TYPE"] = "NODEFILE"
    # Add set for variables
    # Dont care about order and dont want duplicates
    n_out["VARS"] = set()
    # Look for optional keywords
    if len(keys) > 1:
        for i in keys:
            if i.startswith('FREQUENCYF'):
                n_out['FREQUENCYF'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('FREQUENCY'):
                n_out['FREQUENCY'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('GLOBAL'):
                n_out['GLOBAL'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('OUTPUT'):
                n_out['OUTPUT'] = i.split('=')[1]
                # reader_utils.untested_warning(keys[0], i)
            elif i.startswith('TIMEPOINTS'):
                n_out['TIMEPOINTS'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('LASTITERATIONS'):
                n_out['LASTITERATIONS'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('CONTACTELEMENTS'):
                n_out['CONTACTELEMENTS'] = True
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('NSET'):
                n_out['NSET'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i != keys[0]:
                reader_utils.missed_option(keys[0], i)
    return


def star_node_file_receive(line, step):
    # Note that all receives are same, may want to condense
    # Grab set
    varset = step["OUTPUT"][-1]["VARS"]
    # Capitalize line
    up = line.upper()
    # Eliminate whitespace
    up = ''.join(up.split())
    # Split by comma
    spl = up.split(',')
    # Union the variables with the line in set form
    varset |= set(spl)
    return


def star_node_output_setup(keys, step):
    reader_utils.untested_warning(keys[0])
    # Add dictionary for output if not present
    if 'OUTPUT' not in step.keys():
        step['OUTPUT'] = []
    # Grab output
    output = step['OUTPUT']
    # Create entry for current output
    output.append(dict())
    # Grab newly created dictionary
    n_out = output[-1]
    # Add type of output
    n_out["TYPE"] = "NODEOUTPUT"
    # Add set for variables
    # Dont care about order and dont want duplicates
    n_out["VARS"] = set()
    # Look for optional keywords
    if len(keys) > 1:
        for i in keys:
            if i.startswith('FREQUENCYF'):
                n_out['FREQUENCYF'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('FREQUENCY'):
                n_out['FREQUENCY'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('GLOBAL'):
                n_out['GLOBAL'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('OUTPUT'):
                n_out['OUTPUT'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('TIMEPOINTS'):
                n_out['TIMEPOINTS'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('LASTITERATIONS'):
                n_out['LASTITERATIONS'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('CONTACTELEMENTS'):
                n_out['CONTACTELEMENTS'] = True
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('NSET'):
                n_out['NSET'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i != keys[0]:
                reader_utils.missed_option(keys[0], i)
    return


def star_node_output_receive(line, step):
    # Note that all receives are same, may want to condense
    # Grab set
    varset = step["OUTPUT"][-1]["VARS"]
    # Capitalize line
    up = line.upper()
    # Eliminate whitespace
    up = ''.join(up.split())
    # Split by comma
    spl = up.split(',')
    # Union the variables with the line in set form
    varset |= set(spl)
    return


def star_node_print_setup(keys,  step):
    # Add dictionary for output if not present
    if 'OUTPUT' not in step.keys():
        step['OUTPUT'] = []
    # Grab output
    output = step['OUTPUT']
    # Create entry for current output
    output.append(dict())
    # Grab newly created dictionary
    n_out = output[-1]
    # Add type of output
    n_out["TYPE"] = "NODEPRINT"
    # Add set for variables
    # Dont care about order and dont want duplicates
    n_out["VARS"] = set()
    # Look for optional keywords
    if len(keys) > 1:
        for i in keys:
            if i.startswith('FREQUENCYF'):
                n_out['FREQUENCYF'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('FREQUENCY'):
                n_out['FREQUENCY'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('GLOBAL'):
                n_out['GLOBAL'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('TIMEPOINTS'):
                n_out['TIMEPOINTS'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith('NSET'):
                n_out['NSET'] = i.split('=')[1]
                # reader_utils.untested_warning(keys[0], i)
            elif i.startswith('TOTALS'):
                n_out['TOTALS'] = i.split('=')[1]
                reader_utils.untested_warning(keys[0], i)
            elif i != keys[0]:
                reader_utils.missed_option(keys[0], i)
    return


def star_node_print_receive(line, step):
    # Note that all receives are same, may want to condense
    # Grab set
    varset = step["OUTPUT"][-1]["VARS"]
    # Capitalize line
    up = line.upper()
    # Eliminate whitespace
    up = ''.join(up.split())
    # Split by comma
    spl = up.split(',')
    # Union the variables with the line in set form
    varset |= set(spl)
    return


def op_rel_setup(keys, cur_step):
    """
    Completes necessary setup for
    output related keys
    """
    if keys[0] == "*OUTPUT":
        star_output_setup(keys, cur_step)
    elif keys[0] == "*ELEMENTOUTPUT":
        star_element_output_setup(keys, cur_step)
    elif keys[0] == "*ELFILE":
        star_el_file_setup(keys, cur_step)
    elif keys[0] == "*ELPRINT":
        star_el_print_setup(keys, cur_step)
    elif keys[0] == "*NODEOUTPUT":
        star_node_output_setup(keys, cur_step)
    elif keys[0] == "*NODEFILE":
        star_node_file_setup(keys, cur_step)
    elif keys[0] == "*NODEPRINT":
        star_node_print_setup(keys, cur_step)
    else:
        reader_utils.missed_option(keys[0])
    return


def op_rel_receive(last_key, line, cur_step):
    """
    Completes necessary commands for
    receiving output related keys
    """
    # Output does not have receive
    if last_key == "*ELEMENTOUTPUT":
        star_element_output_receive(line, cur_step)
    elif last_key == "*ELFILE":
        star_el_file_receive(line, cur_step)
    elif last_key == "*ELPRINT":
        star_el_print_receive(line, cur_step)
    elif last_key == "*NODEOUTPUT":
        star_node_output_receive(line, cur_step)
    elif last_key == "*NODEFILE":
        star_node_file_receive(line, cur_step)
    elif last_key == "*NODEPRINT":
        star_node_print_receive(line, cur_step)
    return
