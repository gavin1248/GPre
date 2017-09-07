"""
Functions that read in geometry related keywords
"""
import reader_utils

# Geometry related keywords
geom_rel = ['*ELEMENT', '*ELSET', '*NODE', "*NSET", '*RIGIDBODY', '*SURFACE',
            '*ORIENTATION']


def star_node_setup(keys, nsets):
    """
    Set up the input deck reader to collect nodes
    nsets is a dictionary that will be modified if
    the NSET option is included after *NODE
    Note that dictionaries are mutable
    keys -- String of line split by commas with spaces removed
    nsets -- dict of node sets
    Return True to start collecting nodes
    Return current_nset to tell what nset is or keep it as nothing
    """
    # reader_utils.untested_warning(keys[0])
    # print("Collecting Nodes")
    # Check if nodes are being put into node set
    if len(keys) > 1:
        for i in keys:
            if i.startswith("NSET"):
                # reader_utils.untested_warning(keys[0], i)
                # Grab part after =
                current_nset = keys[1].split('=')[1]
                # print("Grabbing "+current_nset)
                # Add node set
                nsets[current_nset] = []
            elif i != keys[0]:
                reader_utils.missed_option(keys[0], i)
    return current_nset


def star_node_receive(line, nsets, all_nodes, current_nset):
    """
    Receive nodes from input deck and place in proper data structures
    line -- String of line, will be split and whitespace removed
    nsets -- dict of node sets
    all_nodes -- dict of all nodes
    current_nset -- node set being added to, "" if none added
    """
    # print('Receiving Nodes')
    # Remove all whitespace
    temp = ''.join(line.split())
    # Split up line
    temp = temp.split(',')
    # Convert to proper line
    # int for node number, float for coordinates
    all_nodes[int(temp[0])] = [float(i) for i in temp[1:]]
    # Append to nset if requested
    if current_nset != "":
        nsets[current_nset].append(temp[0])
    return


def star_element_setup(keys, elsets):
    """
    Set up the input deck reader to collect elements
    elsets is a dictionary that will be modified if
    the ELSET option is included after *ELEMENT
    Note that dictionaries are mutable
    keys -- String of line split by commas with spaces removed
    elsets -- dictionary of element sets
    Return True to start collecting elements
    Return the current elset to tell what it is or keep it as nothing
    """
    # reader_utils.untested_warning(keys[0])
    # print('Collecting Elements')
    # Check for elset and type
    if len(keys) > 1:
        for i in keys:
            if i.startswith("ELSET"):
                # reader_utils.untested_warning(keys[0], i)
                # Grab part after =
                current_elset = i.split('=')[1]
                # print("Grabbing "+current_elset)
                elsets[current_elset] = []
            elif i.startswith("TYPE"):
                # reader_utils.untested_warning(keys[0], i)
                last_type = i.split('=')[1]
            elif i != keys[0]:
                reader_utils.missed_option(keys[0], i)
    return current_elset, last_type


def star_element_receive(line, elsets, all_elements, current_elset,
                         last_type, continued, last_label):
    """
    Receive elements from input deck and place in proper data structures
    line -- String of line, will be split and whitespace removed
    all_elements -- dict of elements with type and connectivity
    current_elset -- element set being added to, "" if none added
    last_type -- type of element for *ELEMENT block
    continued -- True if continued line
    last_label -- Last element label
    """
    # print('Receiving Elements')
    # Remove all whitespace
    temp = ''.join(line.split())
    # Check if last is blank and onvert to ints
    if temp.endswith(','):
        entries = [int(i) for i in temp.split(',')[0:-1]]
    else:
        entries = [int(i) for i in temp.split(',')]
    # print(entries)
    # print(current_elset)
    if continued:
        # reader_utils.untested_warning("*ELEMENT", "line continuation")
        if temp.endswith(','):
            # Add more nodes but not empty at end
            all_elements[last_label]['connectivity'].extend(entries)
        else:
            # Add nodes and remove continued flag
            all_elements[last_label]['connectivity'].extend(entries)
            continued = False
    else:
        # First line
        # Update last_label
        last_label = entries[0]
        # Create dict to add type and connectivity
        all_elements[entries[0]] = dict()
        all_elements[entries[0]]['type'] = last_type
        if temp.endswith(','):
            continued = True
            all_elements[entries[0]]['connectivity'] = entries[1:]
        else:
            all_elements[entries[0]]['connectivity'] = entries[1:]
        if current_elset != "":
            # Add element label if current elset exists
            elsets[current_elset].append(entries[0])
    return continued, last_label


def star_elset_setup(keys, elsets):
    # reader_utils.untested_warning(keys[0])
    # Check for elset
    for i in keys:
        if i.startswith("ELSET"):
            # reader_utils.untested_warning(keys[0], i)
            # Grab part after =
            current_elset = i.split('=')[1]
            elsets[current_elset] = []
    for i in keys:
        if i.startswith("GENERATE"):
            # Place generate keyword at front of list
            reader_utils.untested_warning(keys[0], i)
            elsets[current_elset].append("GENERATE")
        elif i != keys[0] and not i.startswith("ELSET"):
            reader_utils.missed_option(keys[0], i)
    return current_elset


def star_elset_receive(line, elsets, current_elset):
    # Clean line
    # Eliminate whitespace
    up = ''.join(line.split())
    up = up.upper()
    # Split up line
    if line.endswith(','):
        up = up.split(',')[0, -1]
    else:
        up = up.split(',')
    # Grab current elset element label list
    c_el = elsets[current_elset]
    # Check that there is something in list
    if bool(c_el) and c_el[0] == "GENERATE":
        c_el.append(up)
    elif bool(c_el):
        # if no generate keyword and non-empty list
        c_el.extend(up)
    else:
        # no generate keyword and empty list
        # can't update only c_el have to update elsets directly
        elsets[current_elset] = up
    return current_elset


def star_nset_setup(keys, nsets):
    # reader_utils.untested_warning(keys[0])
    # Check for elset
    for i in keys:
        if i.startswith("NSET"):
            # reader_utils.untested_warning(keys[0], i)
            # Grab part after =
            current_nset = i.split('=')[1]
            nsets[current_nset] = []
    for i in keys:
        if i.startswith("GENERATE"):
            # Place generate keyword at front of list
            reader_utils.untested_warning(keys[0], i)
            nsets[current_nset].append("GENERATE")
        elif i != keys[0] and not i.startswith("NSET"):
            reader_utils.missed_option(keys[0], i)
    return current_nset


def star_nset_receive(line, nsets, current_nset):
    # Clean line
    # Eliminate whitespace
    up = ''.join(line.split())
    up = up.upper()
    # Split up line
    if line.endswith(','):
        up = up.split(',')[0, -1]
    else:
        up = up.split(',')
    # Grab current elset element label list
    c_n = nsets[current_nset]
    # Check that there is something in list
    if bool(c_n) and c_n[0] == "GENERATE":
        c_n.append(up)
    elif bool(c_n):
        # if no generate keyword and non-empty list
        c_n.extend(up)
    else:
        # no generate keyword and empty list
        # can't update only c_el have to update elsets directly
        nsets[current_nset] = up
    return current_nset


def star_rigid_body_setup():
    print("NOT STARTED")
    return


def star_rigid_body_receive():
    print("NOT STARTED")
    return


def star_surface_setup():
    print("NOT STARTED")
    return


def star_surface_receive():
    print("NOT STARTED")
    return


def star_orientation_setup():
    print("NOT STARTED")
    return


def star_orientation_receive():
    print("NOT STARTED")
    return


def geom_rel_setup(keys, nsets, elsets, last_info):
    """
    Completes necessary preparation for
    geometry related keys
    """
    if keys[0] == "*NODE":
        # Set up for *NODE handled in function
        # Collect nodes and update current nset if needed
        # last_info will contain current_nset
        temp = star_node_setup(keys, nsets)
        last_info = [temp]
    elif keys[0] == "*ELEMENT":
        # Set up for *ELEMENT handled in function
        # Collect elements and update current elset if needed
        # last_info will contain current elset, last type,
        # if continued, and last element label
        temp = star_element_setup(keys, elsets)
        last_info = list(temp)
        # Not continued, last element doesn't matter so is 0
        last_info.extend([False, 0])
    elif keys[0] == "*ELSET":
        last_info = star_elset_setup(keys, elsets)
    elif keys[0] == "*NSET":
        last_info = star_nset_setup(keys, nsets)
    return last_info


def geom_rel_receive(last_key, line, nsets, elsets,
                     all_elements, all_nodes, last_info):
    if last_key == "*NODE":
        # print('got here')
        # Expansion of last_info commented
        # current_nset = last_info[0]
        star_node_receive(line, nsets, all_nodes, last_info[0])
    elif last_key == "*ELEMENT":
        # Expansion of last_info commented
        # current_elset = last_info[0]
        # last_type = last_info[1]
        # continued = last_info[2]
        # last_label = last_info[3]
        temp = star_element_receive(line, elsets, all_elements,
                                    last_info[0], last_info[1],
                                    last_info[2], last_info[3])
        # Update last_info
        last_info[2:] = temp
    elif last_key == "*ELSET":
        last_info = star_elset_receive(line, elsets, last_info)
    elif last_key == "*NSET":
        last_info = star_nset_receive(line, nsets, last_info)
    return last_info
