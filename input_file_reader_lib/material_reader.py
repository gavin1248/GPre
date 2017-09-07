"""
Contains functions to read material related keywords
"""
import reader_utils

# Material related keywords
mat_rel = ['*CONDUCTIVITY', '*CREEP', '*CYCLICHARDENING',
           '*DEFORMATIONPLASTICITY', '*DENSITY', '*DEPVAR',
           '*ELASTIC', '*ELECTRICALCONDUCTIVITY',
           '*EXPANSION', '*FLUIDCONSTANTS', '*HYPERELASTIC',
           '*HYPERFOAM', '*MAGNETICPERMEABILITY', '*MATERIAL',
           '*PLASTIC', '*SPECIFICGASCONSTANT', '*SPECIFICHEAT',
           '*USERMATERIAL']


def star_material_setup(keys, materials):
    """
    Sets up *MATERIAL
    Adds a material to materials
    keys -- String of line split by commas with spaces removed
    materials -- dictionary of materials (which are dictionaries)
    """
    # reader_utils.untested_warning(keys[0])
    name = keys[1].split('=')[1]
    # Adds entry for name in materials
    materials[name] = dict()
    return materials[name]


def star_material_receive():
    """
    *MATERIAL has no additional lines
    """
    return


def star_elastic_setup(keys, current_mat):
    """
    Sets up *ELASTIC
    Adds elastic property to last material
    keys -- String of line split by commas with spaces removed
    current_mat -- dictionary of current material
    """
    # reader_utils.untested_warning(keys[0])
    current_mat['ELASTIC'] = dict()
    if len(keys) > 1:
        # Grab elastic property type if present
        current_mat['ELASTIC']['TYPE'] = keys[1].split('=')[1]
    else:
        # Otherwise apply the default (ISO)
        current_mat['ELASTIC']['TYPE'] = 'ISO'
    # Create empty array for values
    current_mat['ELASTIC']['VALUES'] = []
    return


def star_elastic_receive(line, current_mat, num):
    """
    Adds properties to ELASTIC entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    num -- number denoting where property is in required lines
    """
    # Remove all whitespace
    temp = ''.join(line.split())
    # Split and convert to floats
    entries = [float(i) for i in temp.split(',')]
    elastic_type = current_mat['ELASTIC']['TYPE']
    if elastic_type == 'ISO':
        # reader_utils.untested_warning("*ELASTIC", elastic_type)
        # Add another row
        current_mat['ELASTIC']['VALUES'].append(entries)
        # Only one line per group so always 1
        return 1
    elif elastic_type == 'ORTHO' or elastic_type == 'ENGINEERINGCONSTANTS':
        reader_utils.untested_warning("*ELASTIC", elastic_type)
        if num == 1:
            # Add another row
            current_mat['ELASTIC']['VALUES'].append(entries)
            # Update to second row
            return 2
        elif num == 2:
            # Extend last row
            current_mat['ELASTIC']['VALUES'][-1].extend(entries)
            # Update to first row
            return 1
    elif elastic_type == 'ANISO':
        reader_utils.untested_warning("*ELASTIC", elastic_type)
        if num == 1:
            # Add another row
            current_mat['ELASTIC']['VALUES'].append(entries)
            # Update to second row
            return 2
        elif num == 2:
            # Extend last row
            current_mat['ELASTIC']['VALUES'][-1].extend(entries)
            # Update to first row
            return 3
        elif num == 3:
            # Extend last row
            current_mat['ELASTIC']['VALUES'][-1].extend(entries)
            # Update to first row
            return 1
    print("MISSED CASE!!!")
    return 1


def star_plastic_setup(keys, current_mat):
    """
    Sets up *PLASTIC
    Adds plastic property to last material
    keys -- String of line split by commas with spaces removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning(keys[0])
    current_mat['PLASTIC'] = dict()
    if len(keys) > 1:
        # Grab plastic property type if present
        current_mat['PLASTIC']['TYPE'] = keys[1].split('=')[1]
    else:
        # Otherwise apply the default (ISOTROPIC)
        current_mat['PLASTIC']['TYPE'] = 'ISOTROPIC'
    # Create empty array for values
    current_mat['PLASTIC']['VALUES'] = []
    return


def star_plastic_receive(line, current_mat):
    """
    Adds properties to ELASTIC entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    """
    # Remove all whitespace
    temp = ''.join(line.split())
    # Split and convert to floats
    entries = [float(i) for i in temp.split(',')]
    current_mat['PLASTIC']['VALUES'].append(entries)
    return


def star_conductivity_setup(keys, current_mat):
    """
    Sets up *CONDUCTIVITY
    Adds conductivity property to last material
    keys -- String of line split by commas with spaces removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning(keys[0])
    current_mat['CONDUCTIVITY'] = dict()
    if len(keys) > 1:
        # Grab conductivity property type if present
        current_mat['CONDUCTIVITY']['TYPE'] = keys[1].split('=')[1]
    else:
        # Otherwise apply the default (ISO)
        current_mat['CONDUCTIVITY']['TYPE'] = 'ISO'
    # Create empty array for values
    current_mat['CONDUCTIVITY']['VALUES'] = []
    return


def star_conductivity_receive(line, current_mat):
    """
    Adds properties to CONDUCTIVITY entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning(keys[0])
    # Remove all whitespace
    temp = ''.join(line.split())
    # Split and convert to floats
    entries = [float(i) for i in temp.split(',')]
    current_mat['CONDUCTIVITY']['VALUES'].append(entries)
    return


def star_creep_setup(keys, current_mat):
    """
    Sets up *CREEP
    Adds creep property to last material
    keys -- String of line split by commas with spaces removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning(keys[0])
    current_mat['CREEP'] = dict()
    if len(keys) > 1:
        # Grab creep property type if present
        current_mat['CREEP']['TYPE'] = keys[1].split('=')[1]
    else:
        # Otherwise apply the default (NORTON)
        current_mat['CREEP']['TYPE'] = 'NORTON'
    # Create empty array for values
    current_mat['CREEP']['VALUES'] = []
    return


def star_creep_receive(line, current_mat):
    """
    Adds properties to CREEP entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    """
    # Remove all whitespace
    temp = ''.join(line.split())
    # Split and convert to floats
    entries = [float(i) for i in temp.split(',')]
    current_mat['CREEP']['VALUES'].append(entries)
    return


def star_cyclic_hardening_setup(keys, current_mat):
    """
    Sets up *CYCLIC HARDENING
    Adds cyclic hardening property to last material
    keys -- String of line split by commas with spaces removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning(keys[0])
    # Create empty array for values
    current_mat['CYCLICHARDENING']['VALUES'] = []
    return


def star_cyclic_hardening_receive(line, current_mat):
    """
    Adds properties to CYCLICHARDENING entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    """
    # Remove all whitespace
    temp = ''.join(line.split())
    # Split and convert to floats
    entries = [float(i) for i in temp.split(',')]
    current_mat['CYCLICHARDENING']['VALUES'].append(entries)


def star_deformation_plasticity_setup(keys, current_mat):
    """
    Sets up *DEFORMATION PLASTICITY
    Adds deformation plasticity constants to last material
    keys -- String of line split by commas with spaces removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning(keys[0])
    # Create empty array for values
    current_mat['DEFORMATIONPLASTICITY']['VALUES'] = []
    return


def star_deformation_plasticity_receive(line, current_mat):
    """
    Adds properties to DEFORMATIONPLASTICITY entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    """
    # Remove all whitespace
    temp = ''.join(line.split())
    # Split and convert to floats
    entries = [float(i) for i in temp.split(',')]
    current_mat['DEFORMATIONPLASTICITY']['VALUES'].append(entries)
    return


def star_density_setup(keys, current_mat):
    """
    Sets up *DENSITY
    Adds density property to last material
    keys -- String of line split by commas with spaces removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning(keys[0])
    # Create empty array for values
    current_mat['DENSITY']['VALUES'] = []
    return


def star_density_receive(line, current_mat):
    """
    Adds properties to DENSITY entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    """
    # Remove all whitespace
    temp = ''.join(line.split())
    # Split and convert to floats
    entries = [float(i) for i in temp.split(',')]
    current_mat['DENSITY']['VALUES'].append(entries)
    return


def star_depvar_setup():
    """
    *DEPVAR has no additional keywords and requires no setup
    """
    return


def star_depvar_receive(line, current_mat):
    """
    Creates DEPVAR entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning("DEPVAR")
    # Remove all whitespace
    temp = ''.join(line.split())
    # Convert to int
    current_mat['DEPVAR']['VALUES'] = int(temp)
    return


def star_electrical_conductivity_setup(keys, current_mat):
    """
    Sets up *ELECTRICAL CONDUCTIVITY
    Adds electrical conductivity propertiess to last material
    keys -- String of line split by commas with spaces removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning(keys[0])
    # Create empty array for values
    current_mat['ELECTRICALCONDUCTIVITY']['VALUES'] = []
    return


def star_electrical_conductivity_receive(line, current_mat):
    """
    Adds properties to ELECTRICALCONDUCTIVITY entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    """
    # Remove all whitespace
    temp = ''.join(line.split())
    # Split and convert to floats
    entries = [float(i) for i in temp.split(',')]
    current_mat['ELECTRICALCONDUCTIVITY']['VALUES'].append(entries)
    return


def star_expansion_setup(keys, current_mat):
    """
    Sets up *EXPANSION
    Adds thermal expansion property to last material
    keys -- String of line split by commas with spaces removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning(keys[0])
    # Set defaults and then overwrite if present
    current_mat['EXPANSION'] = dict()
    # Otherwise apply the default (ISO)
    current_mat['EXPANSION']['TYPE'] = 'ISO'
    # Default for zero is 0
    current_mat['EXPANSION']['ZERO'] = 0
    for i in keys:
        if i.startswith('TYPE'):
            current_mat['EXPANSION']['TYPE'] = keys[1].split('=')[1]
        elif i.startwith('ZERO'):
            current_mat['EXPANSION']['ZERO'] = float(keys[1].split('=')[1])
    # Create empty array for values
    current_mat['EXPANSION']['VALUES'] = []
    return


def star_expansion_receive(line, current_mat):
    """
    Adds properties to EXPANSION entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    """
    # Remove all whitespace
    temp = ''.join(line.split())
    # Split and convert to floats
    entries = [float(i) for i in temp.split(',')]
    current_mat['EXPANSION']['VALUES'].append(entries)
    return


def star_fluid_constants_setup(keys, current_mat):
    """
    Sets up *FLUID CONSTANTS
    Adds fluid constants to last material
    keys -- String of line split by commas with spaces removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning(keys[0])
    # Create empty array for values
    current_mat['FLUIDCONSTANTS']['VALUES'] = []
    return


def star_fluid_constants_receive(line, current_mat):
    """
    Adds properties to FLUIDCONSTANTS entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    """
    # Remove all whitespace
    temp = ''.join(line.split())
    # Split and convert to floats
    entries = [float(i) for i in temp.split(',')]
    current_mat['FLUIDCONSTANTS']['VALUES'].append(entries)
    return


def star_hyperelastic_setup(keys, current_mat):
    """
    Sets up *HYPERELASTIC
    Adds hyperelastic model and properties to last material
    keys -- String of line split by commas with spaces removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning(keys[0])
    # Set defaults and then overwrite if present
    current_mat['HYPERELASTIC'] = dict()
    l = len(keys)
    if l == 1:
        # Apply the default model (POLYNOMIAL)
        current_mat['HYPERELASTIC']['MODEL'] = 'POLYNOMIAL'
        # Default for N is 1
        current_mat['HYPERELASTIC']['N'] = 1
    elif l == 2:
        if keys[1].startswith('N='):
            # Apply the default model (POLYNOMIAL)
            current_mat['HYPERELASTIC']['MODEL'] = 'POLYNOMIAL'
            # Set N
            current_mat['HYPERELASTIC']['N'] = int(keys[1].split('=')[1])
        else:
            # Set model
            current_mat['HYPERELASTIC']['MODEL'] = keys[1].split('=')[1]
            # Set n even if unnecessary
            current_mat['HYPERELASTIC']['N'] = 1
    elif l == 3:
        # Assumes model is set first always
        # Set model
        current_mat['HYPERELASTIC']['MODEL'] = keys[1].split('=')[1]
        # Set N
        current_mat['HYPERELASTIC']['N'] = int(keys[2].split('=')[1])
    # Create empty array for values
    current_mat['HYPERELASTIC']['VALUES'] = []
    return


def star_hyperelastic_receive(line, current_mat, num):
    """
    Adds properties to HYPERELASTIC entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    num -- int that gives which part of row of set it is on
    """
    # Remove all whitespace
    temp = ''.join(line.split())
    # Grab model
    model = current_mat['HYPERELASTIC']['MODEL']
    N = current_mat['HYPERELASTIC']['N']
    # Models that require multiple rows if N=3
    multi_line = ['OGDEN', 'POLYNOMIAL']
    # Split and convert to floats
    entries = [float(i) for i in temp.split(',')]
    if N == 3 and model in multi_line:
        if num == 1:
            current_mat['HYPERELASTIC']['VALUES'].append(entries)
            return 2
        elif num == 2:
            current_mat['HYPERELASTIC']['VALUES'][-1].extend(entries)
            return 1
    else:
        current_mat['HYPERELASTIC']['VALUES'].append(entries)
        return 1
    print('MISSED CASE!!!')
    return 1


def star_hyperfoam_setup(keys, current_mat):
    """
    Sets up *HYPERFOAM
    Adds hyperfoam properties to last material
    keys -- String of line split by commas with spaces removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning(keys[0])
    # Set defaults and then overwrite if present
    current_mat['HYPERFOAM'] = dict()
    l = len(keys)
    if l == 1:
        # Default for N is 1
        current_mat['HYPERFOAM']['N'] = 1
    elif l == 2:
        # Set N
        current_mat['HYPERFOAM']['N'] = int(keys[1].split('=')[1])
    # Create empty array for values
    current_mat['HYPERFOAM']['VALUES'] = []
    return


def star_hyperfoam_receive(line, current_mat, num):
    """
    Adds properties to HYPERFOAM entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    num -- int that gives which part of row of set it is on
    """
    # Remove all whitespace
    temp = ''.join(line.split())
    # Grab N
    N = current_mat['HYPERFOAM']['N']
    # Split and convert to floats
    entries = [float(i) for i in temp.split(',')]
    current_mat['HYPERFOAM']['VALUES'].append(entries)
    if N == 3:
        if num == 1:
            current_mat['HYPERFOAM']['VALUES'].append(entries)
            return 2
        elif num == 2:
            current_mat['HYPERFOAM']['VALUES'][-1].extend(entries)
            return 1
    else:
        current_mat['HYPERFOAM']['VALUES'].append(entries)
        return 1
    print('MISSED CASE!!!')
    return 1


def star_magnetic_permeability_setup(keys, current_mat):
    """
    Sets up *MAGNETIC PERMEABILITY
    Adds magnetic permeability to last material
    keys -- String of line split by commas with spaces removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning(keys[0])
    # Create empty array for values
    current_mat['MAGNETICPERMEABILITY']['VALUES'] = []


def star_magnetic_permeability_receive(line, current_mat):
    """
    Adds properties to MAGNETICPERMEABILITY entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    """
    # Remove all whitespace
    temp = ''.join(line.split())
    # Split and convert to floats
    entries = [float(i) for i in temp.split(',')]
    current_mat['MAGNETICPERMEABILITY']['VALUES'].append(entries)
    return


def star_specific_gas_constant_setup():
    """
    *SPECIFICGASCONSTANT has no additional keywords and requires
    no setup
    """
    return


def star_specific_gas_constant_receive(line, current_mat):
    """
    Creates SPECIFICGASCONSTANT entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning("SPECGASCONST")
    # Remove all whitespace
    temp = ''.join(line.split())
    # Convert to int
    current_mat['SPECIFICGASCONSTANT']['VALUES'] = float(temp)
    return


def star_specific_heat_setup(keys, current_mat):
    """
    Sets up *SPECIFIC HEAT
    Adds magnetic permeability to last material
    keys -- String of line split by commas with spaces removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning(keys[0])
    # Create empty array for values
    current_mat['SPECIFICHEAT']['VALUES'] = []
    return


def star_specific_heat_receive(line, current_mat):
    """
    Adds properties to SPECIFICHEAT entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    """
    # Remove all whitespace
    temp = ''.join(line.split())
    # Split and convert to floats
    entries = [float(i) for i in temp.split(',')]
    current_mat['SPECIFICHEAT']['VALUES'].append(entries)
    return


def star_user_material_setup(keys, current_mat):
    """
    Sets up *USER MATERIAL
    Adds user material variables to last material
    keys -- String of line split by commas with spaces removed
    current_mat -- dictionary of current material
    """
    reader_utils.untested_warning(keys[0])
    # Set defaults and then overwrite if present
    current_mat['USERMATERIAL'] = dict()
    l = len(keys)
    if l == 2:
        # Apply the default type (MECHANICAL)
        current_mat['USERMATERIAL']['TYPE'] = 'MECHANICAL'
        # Set number of constants
        current_mat['USERMATERIAL']['CONSTANTS'] = int(keys[1].split('=')[1])
    elif l == 3:
        if keys[1].startswith('TYPE='):
            # Set variables
            current_mat['USERMATERIAL']['TYPE'] = keys[1].split('=')[1]
            current_mat['USERMATERIAL']['CONSTANTS'] = \
                int(keys[2].split('=')[1])
        elif keys[1].startswith('CONSTANTS='):
            # Set variables
            current_mat['USERMATERIAL']['TYPE'] = keys[2].split('=')[1]
            current_mat['USERMATERIAL']['CONSTANTS'] = \
                int(keys[1].split('=')[1])
    # Create empty array for values
    current_mat['USERMATERIAL']['VALUES'] = []
    return


def star_user_material_receive(line, current_mat, num):
    """
    Adds properties to USERMATERIAL entry in current_mat dict
    line -- String of line, will be split and whitespace removed
    current_mat -- dictionary of current material
    num -- number denoting where property is in required lines
    """
    reader_utils.untested_warning(keys[0])
    # Remove all whitespace
    temp = ''.join(line.split())
    # Split and convert to floats
    will_continue = 1
    if line.split(',')[-1] == '':
        will_continue = 2
        # Eliminate last comma
        line = line[0:-1]
    entries = [float(i) for i in temp.split(',')]
    if num == 1:
        # Add another row
        current_mat['USERMATERIAL']['VALUES'].append(entries)
        # Only one line per group so always 1
    elif num == 2:
        # Extend last row
        current_mat['ELASTIC']['VALUES'][-1].extend(entries)
        # Update to first row
    print("MISSED CASE!!!")
    return will_continue


def mat_rel_setup(keys, materials, last_info):
    """
    Completes necessary preparation for
    setting up material related keys
    """
    # print("this is last info",last_info)
    if keys[0] == "*MATERIAL":
        # Set up material
        # Last info contains current material dict
        temp = star_material_setup(keys, materials)
        last_info = [temp, 1]
    elif keys[0] == "*ELASTIC":
        # Set up elastic properties of material
        # current_mat = last_info[0]
        star_elastic_setup(keys, last_info[0])
        # Last info contains current material dict
        # and number of pair
        # Make sure on first in set
        last_info[1] = 1
    elif keys[0] == "*PLASTIC":
        # Set up plastic properties of material
        # Elastic properties must have already been defined
        star_plastic_setup(keys, last_info[0])
        # No changes to last_info since
        # last material dict is all that is needed
    elif keys[0] == "*CONDUCTIVITY":
        # Set up thermal conductivity of material
        star_conductivity_setup(keys, last_info[0])
        # No changes to last_info since
        # last material dict is all that is needed
    elif keys[0] == "*CREEP":
        # Set up creep properties of material
        # *ELASTIC and *PLASTIC should be defined
        # Or else zero yield surface with no hardening
        # is assumed
        star_creep_setup(keys, last_info[0])
        # No changes to last_info since
        # last material dict is all that is needed
    elif keys[0] == "*CYCLICHARDENING":
        # Set up cyclic hardening properties of material
        star_cyclic_hardening_setup(keys, last_info[0])
        # No changes to last_info since
        # last material dict is all that is needed
    elif keys[0] == "*DEFORMATIONPLASTICITY":
        # Set up deformation plasticity constants of material
        star_deformation_plasticity_setup(keys, last_info[0])
        # No changes to last_info since
        # last material dict is all that is needed
    elif keys[0] == "*DENSITY":
        # Set up density constants of material
        star_density_setup(keys, last_info[0])
        # No changes to last_info since
        # last material dict is all that is needed
    elif keys[0] == "*DEPVAR":
        # No setup required since just one line and
        # no optional variables
        pass
    elif keys[0] == "*ELECTRICALCONDUCTIVITY":
        # Set up electrical conductivity properties of material
        star_electrical_conductivity_setup(keys, last_info[0])
        # No changes to last_info since
        # last material dict is all that is needed
    elif keys[0] == "*EXPANSION":
        # Set up thermal expansion constants of material
        star_expansion_setup(keys, last_info[0])
        # No changes to last_info since
        # last material dict is all that is needed
    elif keys[0] == "*FLUIDCONSTANTS":
        # Set up fluid constants of material
        star_fluid_constants_setup(keys, last_info[0])
        # No changes to last_info since
        # last material dict is all that is needed
    elif keys[0] == "*HYPERELASTIC":
        # Set up hyperelastic model and properties of material
        star_hyperelastic_setup(keys, last_info[0])
        # last_info is updated
        last_info[1] = 1
    elif keys[0] == "*HYPERFOAM":
        # Set up hyperfoam properties of material
        star_hyperfoam_setup(keys, last_info[0])
        # last_info is updated
        last_info[1] = 1
    elif keys[0] == "*MAGNETICPERMEABILITY":
        # Set up magnetic permeability properties of material
        star_magnetic_permeability_setup(keys, last_info[0])
        # No changes to last_info since
        # last material dict is all that is needed
    elif keys[0] == "*SPECIFICGASCONSTANT":
        # No setup required since just one line and
        # no optional variables
        pass
    elif keys[0] == "*SPECIFICHEAT":
        # Set up specific heat of material
        star_specific_heat_setup(keys, last_info[0])
        # No changes to last_info since
        # last material dict is all that is needed
    elif keys[0] == "*USERMATERIAL":
        # Set up hyperfoam properties of material
        star_user_material_setup(keys, last_info[0])
        # last_info is updated
        last_info[1] = 1

    return last_info


def mat_rel_receive(last_key, line, last_info):
    """
    Completes necessary preparation for
    receiving material related keys
    """
    if last_key == "*ELASTIC":
        # Expansion of last_info commented
        # current_mat = last_info[0]
        # num = last_info[1]
        temp = star_elastic_receive(line, last_info[0],
                                    last_info[1])
        # Update last_info
        last_info[1] = temp
    elif last_key == "*PLASTIC":
        # Expansion of last_info is same as *ELASTIC
        star_plastic_receive(line, last_info[0])
    elif last_key == "*CONDUCTIVITY":
        # Expansion of last_info is same as *ELASTIC
        star_conductivity_receive(line, last_info[0])
    elif last_key == "*CREEP":
        # Expansion of last_info is same as *ELASTIC
        star_creep_receive(line, last_info[0])
    elif last_key == "*CYCLICHARDENING":
        # Expansion of last_info is same as *ELASTIC
        star_cyclic_hardening_receive(line, last_info[0])
    elif last_key == "*DEFORMATIONPLASTICITY":
        # Expansion of last_info is same as *ELASTIC
        star_deformation_plasticity_receive(line, last_info[0])
    elif last_key == "*DENSITY":
        # Expansion of last_info is same as *ELASTIC
        star_density_receive(line, last_info[0])
    elif last_key == "*DEPVAR":
        # Expansion of last_info is same as *ELASTIC
        star_depvar_receive(line, last_info[0])
    elif last_key == "*ELECTRICALCONDUCTIVITY":
        # Expansion of last_info is same as *ELASTIC
        star_electrical_conductivity_receive(line, last_info[0])
    elif last_key == "*EXPANSION":
        # Expansion of last_info is same as *ELASTIC
        star_expansion_receive(line, last_info[0])
    elif last_key == "*FLUIDCONSTANTS":
        # Expansion of last_info is same as *ELASTIC
        star_fluid_constants_receive(line, last_info[0])
    elif last_key == "*HYPERELASTIC":
        # Expansion of last_info is same as *ELASTIC
        last_info[1] = star_hyperelastic_receive(line,
                                                 last_info[0],
                                                 last_info[1])
    elif last_key == "*HYPERFOAM":
        # Expansion of last_info is same as *ELASTIC
        last_info[1] = star_hyperfoam_receive(line,
                                              last_info[0],
                                              last_info[1])
    elif last_key == "*MAGNETICPERMEABILITY":
        # Expansion of last_info is same as *ELASTIC
        star_magnetic_permeability_receive(line, last_info[0])
    elif last_key == "*SPECIFICGASCONSTANT":
        # Expansion of last_info is same as *ELASTIC
        star_specific_gas_constant_receive(line, last_info[0])
    elif last_key == "*SPECIFICHEAT":
        # Expansion of last_info is same as *ELASTIC
        star_specific_heat_receive(line, last_info[0])
    elif last_key == "*USERMATERIAL":
        # Expansion of last_info is same as *ELASTIC
        last_info[1] = \
                star_user_material_receive(line,
                                           last_info[0],
                                           last_info[1])
    return last_info
