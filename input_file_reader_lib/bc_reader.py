"""
Contains boundary condition related keywords
This includes loads
"""

# Boundary condition related keywords
# Constraint related keywords included
bc_rel = ['*CFLUX', '*CLOAD', '*DFLUX', '*DLOAD', '*DSLOAD', '*FILM',
          '*MASSFLOW', '*BOUNDARY', '*BOUNDARYF', '*TEMPERATURE',
          '*INITIALCONDITIONS', '*DISTRIBUTINGCOUPLING', '*EQUATION',
          '*MPC', '*TIE', '*TRANSFORM', '*TRANSFORMF',
          '*CLEARANCE', '*CONTACTDAMPING', '*CONTACTPAIR', '*FRICTION',
          '*GAPCONDUCTANCE', '*SURFACEBEHAVIOR', '*SURFACEINTERATION']
# Each keyword has a setup and receive method no matter whether it requires
# set or has additional lines
import reader_utils


def create_homo_step(steps):
    """
    Creates a blank step for homogeneous
    conditions prescribed before *step
    """
    # Add a blank dictionary to steps
    steps.append(dict())
    # Add flag to edit
    steps[0]["HOMOGENEOUS"] = True
    return


def star_cflux_setup():
    print("SETUP NOT COMPLETED")
    return


def star_cflux_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_cload_setup(keys, steps):
    # reader_utils.untested_warning(keys[0])
    # Create an empty list for concentrated loads
    # in last step if not present
    if "CLOAD" not in steps[-1].keys():
        steps[-1]["CLOAD"] = []
    # Add a concentrated load
    steps[-1]["CLOAD"].append(dict())
    temp_cl = steps[-1]["CLOAD"][-1]
    # Set up node number/set, DOFs, and magnitude
    # Strings
    temp_cl["NODES"] = []
    # Ints
    temp_cl["DOFS"] = []
    # Floats
    temp_cl["MAGNITUDES"] = []
    # Look for optional keywords
    if len(keys) > 1:
        for i in keys:
            if i.startswith("OP"):
                # Grab NEW or MOD of OP=NEW/MOD
                temp_cl["OP"] = i.split("=")[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith("AMPLITUDE"):
                temp_cl["AMPLITUDE"] = i.split("=")[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith("TIMEDELAY"):
                temp_cl["TIMEDELAY"] = float(i.split("=")[1])
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith("USER"):
                temp_cl["USER"] = True
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith("LOADCASE"):
                temp_cl["LOADCASE"] = int(i.split("=")[1])
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith("SECTOR"):
                # !! I don't really understand what sector is
                temp_cl["SECTOR"] = i.split("=")[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith("AMPLITUDE"):
                temp_cl["AMPLITUDE"] = i.split("=")[1]
                reader_utils.untested_warning(keys[0], i)
            elif i.startswith("SUBMODEL"):
                # !! I don't really understand what submodel keyword wants
                temp_cl["SUBMODEL"] = i.split("=")[1]
                reader_utils.untested_warning(keys[0], i)
            else:
                reader_utils.missed_option(keys[0], i)
    return


def star_cload_receive(line, steps):
    # Capitalize line
    up = line.upper()
    # Eliminate whitespace
    up = ''.join(up.split())
    # Grab last step last concentrated load set
    temp_cl = steps[-1]["CLOAD"][-1]
    # Split by comma
    spl = up.split(',')
    # Keep as string
    temp_cl["NODES"].append(spl[0])
    # Convert to int
    temp_cl["DOFS"].append(int(spl[1])) 
    # Convert to float
    temp_cl["MAGNITUDES"].append(float(spl[2]))
    return


def star_dflux_setup():
    print("SETUP NOT COMPLETED")
    return


def star_dflux_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_dload_setup():
    print("SETUP NOT COMPLETED")
    return


def star_dload_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_dsload_setup():
    print("SETUP NOT COMPLETED")
    return


def star_dsload_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_film_setup():
    print("SETUP NOT COMPLETED")
    return


def star_film_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_massflow_setup():
    print("SETUP NOT COMPLETED")
    return


def star_massflow_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_boundary_setup(keys, steps):
    # reader_utils.untested_warning(keys[0])
    # Can check if steps is empty by checking if false
    # Must create a place holder step if steps is empty
    if not steps:
        create_homo_step(steps)
    # Create an empty list for boundary conditions
    # in last step if not present
    if "BOUNDARY" not in steps[-1].keys():
        steps[-1]["BOUNDARY"] = []
    # Add a boundary condition
    steps[-1]["BOUNDARY"].append(dict())
    temp_bc = steps[-1]["BOUNDARY"][-1]
    # Nodes are left as strings
    # Node number or node set can be entered
    temp_bc["NODES"] = []
    # DOFs are ints
    temp_bc["DOFS"] = []
    # Magnitudes are floats
    # Only used if Inhomogeneous
    # !! submodels case not handled
    if "HOMOGENEOUS" not in steps[-1].keys():
        temp_bc["MAGNITUDES"] = []
    # Search through keys for optional keywords
    # Note that only OP has been completed
    # !! still need other keywords
    if len(keys) > 1:
        for i in keys:
            if i.startswith("OP"):
                # Grab NEW or MOD of OP=NEW/MOD
                temp_bc["OP"] = i.split("=")[1]
                reader_utils.untested_warning(keys[0], i)
            else:
                reader_utils.missed_option(keys[0], i)
    return


def star_boundary_receive(line, steps):
    # Capitalize line
    up = line.upper()
    # Eliminate whitespace
    up = ''.join(up.split())
    # Grab last step boundary conditions
    temp_bc = steps[-1]["BOUNDARY"][-1]
    # Split by comma
    spl = up.split(',')
    # Leave as string
    temp_bc["NODES"].append(spl[0])
    # Convert DOFS to int
    temp_bc["DOFS"].append([int(spl[1])])
    # Second DOF can be left blank so check
    # !! Not sure if comma has to be at end, should test
    if spl[2] == "":
        # If blank it means only one DOF is constrained
        temp_bc["DOFS"][-1].append(int(spl[1]))
    else:
        temp_bc["DOFS"][-1].append(int(spl[2]))
    # Convert magnitudes to floats
    # Magnitudes is only created for inhomogeneous conditions
    if "MAGNITUDES" in temp_bc.keys():
        temp_bc["MAGNITUDES"].append(float(spl[3]))
    return


def star_boundaryf_setup():
    print("SETUP NOT COMPLETED")
    return


def star_boundaryf_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_temperature_setup():
    print("SETUP NOT COMPLETED")
    return


def star_temperature_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_initial_conditions_setup():
    print("SETUP NOT COMPLETED")
    return


def star_initial_conditions_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_distributing_coupling_setup():
    print("SETUP NOT COMPLETED")
    return


def star_distributing_coupling_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_equation_setup():
    print("SETUP NOT COMPLETED")
    return


def star_equation_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_mpc_setup():
    print("SETUP NOT COMPLETED")
    return


def star_mpc_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_tie_setup():
    print("SETUP NOT COMPLETED")
    return


def star_tie_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_transform_setup():
    print("SETUP NOT COMPLETED")
    return


def star_transformf_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_clearance_setup():
    print("SETUP NOT COMPLETED")
    return


def star_clearance_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_contact_damping_setup():
    print("SETUP NOT COMPLETED")
    return


def star_contact_damping_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_contact_pair_setup():
    print("SETUP NOT COMPLETED")
    return


def star_contact_pair_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_friction_setup():
    print("SETUP NOT COMPLETED")
    return


def star_friction_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_gap_conductance_setup():
    print("SETUP NOT COMPLETED")
    return


def star_gap_conductance_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_surface_behavior_setup():
    print("SETUP NOT COMPLETED")
    return


def star_surface_behavior_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_surface_interaction_setup():
    print("SETUP NOT COMPLETED")
    return


def star_surface_interaction_receive():
    print("RECEIVE NOT COMPLETED")
    return


def bc_rel_setup(keys, steps):
    """
    Completes necessary preparation for setting up boundary
    condition related keys
    """
    if keys[0] == "*BOUNDARY":
        star_boundary_setup(keys, steps)
    elif keys[0] == "*CLOAD":
        star_cload_setup(keys, steps)
    return


def bc_rel_receive(last_key, line, steps):
    """
    Completes necessary preparation for receiving boundary
    condition related keys
    """
    if last_key == "*BOUNDARY":
        star_boundary_receive(line, steps)
    elif last_key == "*CLOAD":
        star_cload_receive(line, steps)
    return
