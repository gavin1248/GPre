"""
Reads Calculix input file
Completed so far...
*NODE
*ELEMENT
*STEP
*MATERIAL
*ELASTIC
*PLASTIC
*CONDUCTIVITY
*CREEP
*CYCLIC HARDENING
*DEFORMATION PLASTICITY
*DENSITY
*DEPVAR
*ELECTRICAL CONDUCTIVITY
*EXPANSION
*FLUID CONSTANTS
*HYPERELASTIC
*HYPERFOAM
*MAGNETIC PERMEABILITY
*SPECIFIC GAS CONSTANT
*SPECIFIC HEAT
*STATIC
Working on...
*OUTPUT
Somewhat tested
*NODE
*ELEMENT
*STEP
"""

# Functions that interpret keywords are stored in separate files
import geometry_reader
import material_reader
import bc_reader
import output_reader
import section_reader
import step_reader
# import math_reader
# import other_reader

# Geometry related keywords
geom_rel = ['*ELEMENT', '*ELSET', '*NODE', "*NSET", '*RIGIDBODY', '*SURFACE',
            '*ORIENTATION']
# Material related keywords
mat_rel = ['*CONDUCTIVITY', '*CREEP', '*CYCLICHARDENING',
           '*DEFORMATIONPLASTICITY', '*DENSITY', '*DEPVAR',
           '*ELASTIC', '*ELECTRICALCONDUCTIVITY',
           '*EXPANSION', '*FLUIDCONSTANTS', '*HYPERELASTIC',
           '*HYPERFOAM', '*MAGNETICPERMEABILITY', '*MATERIAL',
           '*PLASTIC', '*SPECIFICGASCONSTANT', '*SPECIFICHEAT',
           '*USERMATERIAL']
# Section related keywords
# Nodal thickness is kind of a section
# Does pre-tension section belong here?
sec_rel = ['*BEAMGENERALSECTION', '*BEAMSECTION', '*FLUIDSECTION',
           '*NODALTHICKNESS', '*NORMAL', 'PRE-TENSIONSECTION',
           '*SHELLSECTION', '*SOLIDSECTION', '*DASHPOT', '*GAP', '*SPRING']
# Step related keywords
# Only includes changes and types of steps
step_rel = ['*BUCKLE', '*CFD', '*CHANGEFRICTION', '*CHANGEMATERIAL',
            '*CHANGEPLASTIC', '*CHANGESURFACEBEHAVIOR', '*CHANGESOLIDSECTION',
            '*COMPLEXFREQUENCY', '*CONTROLS',
            '*COUPLEDTEMPERATURE-DISPLACEMENT', '*DYNAMIC',
            '*ELECTROMAGNETICS', '*ENDSTEP', '*FREQUENCY', '*HEATTRANSFER'
            '*MODALDAMPING', '*MODALDYNAMIC', '*MODELCHANGE', '*NOANALYSIS',
            '*RADIATE', '*RETAINEDNODALDOF', '*SELECTCYCLICSYMMETRYMODES',
            '*SENSITIVITY', '*STATIC', '*STEADYSTATEDYNAMICS', '*STEP',
            '*SUBSTRUCTUREGENERATE', '*SUBSTRUCTUREMATRIXOUTPUT',
            '*UNCOUPLEDTEMPERATURE-DISPLACEMENT', '*VIEWFACTOR', '*VISCO']
# Load related or boundary condition related
# I thought films were interactions in Abaqus but it seems more of a load
bc_rel = ['*CFLUX', '*CLOAD', '*DFLUX', '*DLOAD', '*DSLOAD', '*FILM',
          '*MASSFLOW', '*BOUNDARY', '*BOUNDARYF', '*TEMPERATURE',
          '*INITIALCONDITIONS', '*DISTRIBUTINGCOUPLING', '*EQUATION',
          '*MPC', '*TIE', '*TRANSFORM', '*TRANSFORMF',
          '*CLEARANCE', '*CONTACTDAMPING', '*CONTACTPAIR', '*FRICTION',
          '*GAPCONDUCTANCE', '*SURFACEBEHAVIOR', '*SURFACEINTERATION']
# Output related keywords
op_rel = ['*CONTACTFILE', '*CONTACTOUTPUT', '*CONTACTPRINT',
          '*ELEMENTOUTPUT', '*ELFILE', '*ELPRINT',
          '*FACEPRINT', '*NODEFILE', '*NODEOUTPUT', '*NODEPRINT',
          '*OUTPUT']
# Mathematical constants and signals keywords
math_rel = ['*AMPLITUDE', '*DAMPING', '*PHYSICALCONSTANTS', '*TIMEPOINTS',
            '*VALUESATINFINITY', '*CYCLICSYMMETRYMODEL']
# Constraint related keywords
# Included in boundary condition related keywords
const_rel = ['*DISTRIBUTINGCOUPLING', '*EQUATION', '*MPC',
             '*TIE', '*TRANSFORM', '*TRANSFORMF']
# Interatction related keywords
# Included in boundary condition related keywords
int_rel = ['*CLEARANCE', '*CONTACTDAMPING', '*CONTACTPAIR', '*FRICTION',
           '*GAPCONDUCTANCE', '*SURFACEBEHAVIOR', '*SURFACEINTERATION']
# Design variable related keywords
# Included with other
design_rel = ['*DESIGNVARIABLES', '*OBJECTIVE']
# Other
other = ['*HEADING', '*INCLUDE', '*RESTART', '*SUBMODEL'
         '*DESIGNVARIABLES', '*OBJECTIVE']
# Keywords that have not been started
not_started = ['*AMPLITUDE', '*BEAMGENERALSECTION',
               '*BOUNDARYF', '*BUCKLE', '*CFD', '*CFLUX',
               '*CHANGEFRICTION', '*CHANGEMATERIAL', '*CHANGEPLASTIC',
               '*CHANGESURFACEBEHAVIOR', '*CHANGESOLIDSECTION',
               '*CLEARANCE', '*COMPLEXFREQUENCY',
               '*CONTACTDAMPING', '*CONTACTFILE', '*CONTACTOUTPUT',
               '*CONTACTPAIR', '*CONTACTPRINT', '*CONTROLS'
               '*COUPLEDTEMPERATURE-DISPLACEMENT',
               '*CYCLICSYMMETRYMODEL', '*DAMPING', '*DASHPOT',
               '*DESIGNVARIABLES', '*DFLUX',
               '*DISTRIBUTINGCOUPLING', '*DLOAD', '*DSLOAD',
               '*DYNAMIC', '*ELECTROMAGNETICS',
               '*EQUATION', '*FACEPRINT', '*FILM', '*FLUIDSECTION',
               '*FREQUENCY', '*FRICTION', '*GAP', '*GAPCONDUCTANCE',
               '*HEADING', '*HEATTRANSFER', '*INCLUDE',
               '*INITIALCONDITIONS', '*MASSFLOW', '*MODALDAMPING',
               '*MODALDYNAMIC', '*MODELCHANGE', '*MPC',
               '*NOANALYSIS', '*NODALTHICKNESS',
               '*NORMAL',
               '*OBJECTIVE', '*ORIENTATION', '*PHYSICALCONSTANTS',
               'PRE-TENSIONSECTION', '*RADIATE', '*RESTART',
               '*RETAINEDNODALDOF', '*RIGIDBODY', '*SELECTCYCLICSYMMETRYMODES',
               '*SENSITIVITY',
               '*SPECIFICGASCONSTANT', '*SPECIFICHEAT', '*SPRING',
               '*STEADYSTATEDYNAMICS', '*SUBSTRUCTUREGENERATE',
               '*SUBSTRUCTUREMATRIXOUTPUT', '*SURFACE', '*SURFACEBEHAVIOR',
               '*SURFACEINTERATION', '*TEMPERATURE', '*TIE', '*TIMEPOINTS',
               '*TRANSFORM', '*TRANSFORMF',
               '*UNCOUPLEDTEMPERATURE-DISPLACEMENT',
               '*VALUESATINFINITY', '*VIEWFACTOR', '*VISCO']


def read_input(path):
    """
    Reads in input file at path
    path - string
    """
    # Create dictionaries for each group
    nsets = dict()
    elsets = dict()
    # surfaces = dict()
    materials = dict()
    sections = dict()
    # Create lists for each group
    steps = []
    # Create dictionary for nodes and elements
    # Contains label and coordinates
    all_nodes = dict()
    # Contains type, label, and connectivity
    all_elements = dict()
    # Flag for identifying if any cards were unsupported
    unsupported_cards = False
    with open(path) as fp:
        # Last keyword
        last_key = ""
        # Information from earlier in deck
        # Check each keyword if statement for what this contains
        # Always an array (should I keep it that way?)
        last_info = []
        for line in fp:
            if line.startswith("**"):
                # Skip lines starting with **
                # These are comment lines
                continue
            elif line.startswith("*"):
                # Capitalize line
                up = line.upper()
                # Eliminate whitespace
                up = ''.join(up.split())
                # Grab first keyword
                keys = up.split(',')
                last_key = keys[0]
                # ifs for moving to more modular program
                if last_key in geom_rel:
                    last_info = geometry_reader.geom_rel_setup(keys, nsets, elsets, last_info)
                elif last_key in mat_rel:
                    last_info = material_reader.mat_rel_setup(keys, materials, last_info)
                elif last_key in sec_rel:
                    last_info = section_reader.sec_rel_setup(keys, sections)
                    # last_info is current section
                elif last_key in step_rel:
                    last_info = step_reader.step_rel_setup(keys, steps, last_info)
                    # last_info is current step
                elif last_key in op_rel:
                    output_reader.op_rel_setup(keys, steps[-1])
                elif last_key in bc_rel:
                    # print('Placeholder for load and bc cards')
                    bc_reader.bc_rel_setup(keys, steps)
                elif last_key in math_rel:
                    print('Placeholder for math cards')
                elif last_key in other:
                    print('Placeholder for other cards')
                # Check if supported
                if last_key in not_started:
                    print(last_key+' is not supported')
                    unsupported_cards = True
            else:
                if last_key in geom_rel:
                    last_info = geometry_reader.geom_rel_receive(last_key, line, nsets, elsets,
                                                     all_elements, all_nodes, last_info)
                elif last_key in mat_rel:
                    last_info = material_reader.mat_rel_receive(last_key, line, last_info)
                elif last_key in sec_rel:
                    section_reader.sec_rel_receive(last_key, line, last_info)
                elif last_key in step_rel:
                    step_reader.step_rel_receive(last_key, line, last_info)
                elif last_key in op_rel:
                    output_reader.op_rel_receive(last_key, line, steps[-1])
                elif last_key in bc_rel:
                    # print('Placeholder for load and bc cards')
                    bc_reader.bc_rel_receive(last_key, line, steps)
                elif last_key in math_rel:
                    print('Placeholder for math cards')
                elif last_key in other:
                    print('Placeholder for other cards')
                # Check if supported
                if last_key in not_started:
                    print(last_key+' is not supported')
                    unsupported_cards = True
    # print("Node Sets", nsets)
    # print("Element Sets", elsets)
    # print("All node set", all_nodes)
    # print("All element set", all_elements)
    print("Steps", steps)
    print("Materials", materials)
    print("Sections", sections)
    if unsupported_cards:
        print("SOME CARDS WERE NOT SUPPORTED")


# read_input("/home/gavin/OpenSourceFEA/GPre/CCX_test_files/test/simplebeam.inp")
# read_input("/home/gavin/OpenSourceFEA/GPre/CCX_test_files/test/solidshell1.inp")
read_input("/home/gavin/CCX_test_files/test/solidshell1.inp")
