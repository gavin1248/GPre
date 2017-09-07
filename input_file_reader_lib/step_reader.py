"""
Functions for step related keywords
"""
import reader_utils

# Step related keywords
# Only includes changes and types of steps
step_rel = ['*BUCKLE', '*CFD', '*CHANGEFRICTION', '*CHANGEMATERIAL',
            '*CHANGEPLASTIC', '*CHANGESURFACEBEHAVIOR', '*CHANGESOLIDSECTION',
            '*COMPLEXFREQUENCY', '*CONTROLS',
            '*COUPLEDTEMPERATURE-DISPLACEMENT', '*DYNAMIC',
            '*ELECTROMAGNETICS', '*ENDSTEP', '*FREQUENCY', '*HEATTRANSFER'
            '*MODALDAMPING', '*MODALDYNAMIC', '*MODELCHANGE', '*NOANALYSIS',
            '*RADIATE', '*RETAINEDNODALDOF', '*SELECTCYCLICSYMMETRYMODES',
            '*SENSITIVITY', '*STATIC', '*STEADYSTATEDYNAMICS', 'STEP',
            '*SUBSTRUCTUREGENERATE', '*SUBSTRUCTUREMATRIXOUTPUT',
            '*UNCOUPLEDTEMPERATURE-DISPLACEMENT', '*VIEWFACTOR', '*VISCO']

# Note there is no receive since there is only one line
def star_step_setup(keys, steps):
    """
    Sets up *STEP
    Adds a step to steps with optional keywords added
    keys -- String of line split by commas with spaces removed
    steps -- list of steps
    """
    # reader_utils.untested_warning(keys[0])
    # Check to see how many steps there are already
    step_num = len(steps)
    # Add step to steps
    steps.append(dict())
    # Add optional keyword information
    # I decided against setting the defaults automatically
    # steps[step_num]['INC'] = 100
    # steps[step_num]['INCF'] = 10000
    # steps[step_num]['TURBULENCEMODEL'] = 'NONE'
    # steps[step_num]['SHOCKSMOOTHING'] = 0
    
    # !! Can NLGEOM and perturbation be set to off or no?
    # The code assumes they are just flags

    # Changes optional keywords from defaults if present
    for i in keys:
        if i.startswith('PERTURBATION'):
            reader_utils.untested_warning(keys[0], i)
            steps[step_num]['PERTURBATION'] = True
        elif i.startswith('NLGEOM'):
            reader_utils.untested_warning(keys[0], i)
            steps[step_num]['NLGEOM'] = True
        elif i.startswith('INCF'):
            reader_utils.untested_warning(keys[0], i)
            steps[step_num]['INCF'] = int(i.split('=')[1])
        elif i.startswith('INC'):
            reader_utils.untested_warning(keys[0], i)
            steps[step_num]['INC'] = int(i.split('=')[1])
        elif i.startswith('TURBULENCEMODEL'):
            reader_utils.untested_warning(keys[0], i)
            steps[step_num]['TURBULENCEMODEL'] = i.split('=')[1]
        elif i.startswith('SHOCKSMOOTHING'):
            reader_utils.untested_warning(keys[0], i)
            steps[step_num]['SHOCKSMOOTHING'] = float(i.split('=')[1])
        elif i != keys[0]:
            reader_utils.missed_option(keys[0], i)
    return steps[step_num]


def star_buckle_setup():
    print("SETUP NOT COMPLETED")
    return


def star_buckle_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_cfd_setup():
    print("SETUP NOT COMPLETED")
    return


def star_cfd_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_change_friction_setup():
    print("SETUP NOT COMPLETED")
    return


def star_change_friction_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_change_material_setup():
    print("SETUP NOT COMPLETED")
    return


def star_change_material_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_change_plastic_setup():
    print("SETUP NOT COMPLETED")
    return


def star_change_plastic_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_change_surface_behavior_setup():
    print("SETUP NOT COMPLETED")
    return


def star_change_surface_behavior_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_change_solid_section_setup():
    print("SETUP NOT COMPLETED")
    return


def star_change_solid_section_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_complex_frequency_setup():
    print("SETUP NOT COMPLETED")
    return


def star_complex_frequency_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_controls_setup():
    print("SETUP NOT COMPLETED")
    return


def star_controls_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_coupled_temperature_displacement_setup():
    print("SETUP NOT COMPLETED")
    return


def star_coupled_temperature_displacement_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_dynamic_setup():
    print("SETUP NOT COMPLETED")
    return


def star_dynamic_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_electromagnetics_setup():
    print("SETUP NOT COMPLETED")
    return


def star_electromagnetics_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_end_step_setup():
    print("SETUP NOT COMPLETED")
    return


def star_end_step_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_frequency_setup():
    print("SETUP NOT COMPLETED")
    return


def star_frequency_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_heat_transfer_setup():
    print("SETUP NOT COMPLETED")
    return


def star_heat_transfer_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_modal_damping_setup():
    print("SETUP NOT COMPLETED")
    return


def star_modal_damping_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_modal_dynamic_setup():
    print("SETUP NOT COMPLETED")
    return


def star_modal_dynamic_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_model_change_setup():
    print("SETUP NOT COMPLETED")
    return


def star_model_change_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_no_analysis_setup():
    print("SETUP NOT COMPLETED")
    return


def star_no_analysis_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_radiate_setup():
    print("SETUP NOT COMPLETED")
    return


def star_radiate_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_retained_nodal_dof_setup():
    print("SETUP NOT COMPLETED")
    return


def star_retained_nodal_dof_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_select_cyclic_symmetry_modes_setup():
    print("SETUP NOT COMPLETED")
    return


def star_select_cyclic_symmetry_modes_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_sensitivity_setup():
    print("SETUP NOT COMPLETED")
    return


def star_sensitivity_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_static_setup(keys, step):
    """
    Sets up step for a static solve
    keys -- keywords split and with whitespace removed
    step -- dictionary of current step
    """
    # reader_utils.untested_warning(keys[0])
    step['TYPE'] = 'STATIC'
    for i in keys:
        if i.startswith('SOLVER'):
            reader_utils.untested_warning(keys[0], i)
            # Add solver if included
            step['SOLVER'] = i.split('=')[1]
        elif i.startswith('DIRECT'):
            reader_utils.untested_warning(keys[0], i)
            # Turns off autoincrementation
            step['DIRECT'] = True
        elif i.startswith('EXPLICIT'):
            reader_utils.untested_warning(keys[0], i)
            # Tells that CFD calcs should be explicit
            step['EXPLICIT'] = True
        elif i.startswith('TIMERESET'):
            reader_utils.untested_warning(keys[0], i)
            # Makes step not count in total time
            step['TIMERESET'] = True
        elif i.startswith('TOTALTIMEATSTART'):
            reader_utils.untested_warning(keys[0], i)
            # Sets the total time at the start of the step
            step['TOTALTIMEATSTART'] = i.split('=')[1]
    return


def star_static_receive(line, step):
    """
    line -- line as read in by python
    step -- dictionary of current step
    """
    # Remove all whitespace
    temp = ''.join(line.split())
    # Split and convert to floats
    entries = [float(i) for i in temp.split(',')]
    # Add entries to step
    step['VALUES'] = entries
    return


def star_steady_state_dynamics_setup():
    print("SETUP NOT COMPLETED")
    return


def star_steady_state_dynamics_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_substructure_generate_setup():
    print("SETUP NOT COMPLETED")
    return


def star_substructure_generate_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_substructure_matrix_output_setup():
    print("SETUP NOT COMPLETED")
    return


def star_substructure_matrix_output_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_uncoupled_temperature_displacement_setup():
    print("SETUP NOT COMPLETED")
    return


def star_uncoupled_temperature_displacement_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_viewfactor_setup():
    print("SETUP NOT COMPLETED")
    return


def star_viewfactor_receive():
    print("RECEIVE NOT COMPLETED")
    return


def star_visco_setup():
    print("SETUP NOT COMPLETED")
    return


def star_visco_receive():
    print("RECEIVE NOT COMPLETED")
    return


step_rel = ['*BUCKLE', '*CFD', '*CHANGEFRICTION', '*CHANGEMATERIAL',
            '*CHANGEPLASTIC', '*CHANGESURFACEBEHAVIOR', '*CHANGESOLIDSECTION',
            '*COMPLEXFREQUENCY', '*CONTROLS',
            '*COUPLEDTEMPERATURE-DISPLACEMENT', '*DYNAMIC',
            '*ELECTROMAGNETICS', '*ENDSTEP', '*FREQUENCY', '*HEATTRANSFER'
            '*MODALDAMPING', '*MODALDYNAMIC', '*MODELCHANGE', '*NOANALYSIS',
            '*RADIATE', '*RETAINEDNODALDOF', '*SELECTCYCLICSYMMETRYMODES',
            '*SENSITIVITY', '*STATIC', '*STEADYSTATEDYNAMICS', 'STEP',
            '*SUBSTRUCTUREGENERATE', '*SUBSTRUCTUREMATRIXOUTPUT',
            '*UNCOUPLEDTEMPERATURE-DISPLACEMENT', '*VIEWFACTOR', '*VISCO']


def step_rel_setup(keys, steps, last_info):
    """
    Completes necessary setup for
    step related keys
    """
    if keys[0] == "*STEP":
        # Set up steps
        # last_info contains dict of current step
        temp = star_step_setup(keys, steps)
        last_info = [temp]
    elif keys[0] == "*STATIC":
        # Set up static step
        star_static_setup(keys, last_info[0])
        # No update to last_info
    elif keys[0] == "*ENDSTEP":
        # Nothing to be done
        pass
    else:
        reader_utils.missed_option(keys[0])
    return last_info


def step_rel_receive(last_key, line, last_info):
    """
    Completes necessary commands for receiving
    step related keys
    """
    if last_key == "*STATIC":
        # last_info = current step
        star_static_receive(line, last_info)
    return
