# Python library imports
import sys
import math
# PyQt5 imports
from PyQt5.QtCore import pyqtSignal, QPoint, QSize, Qt
from PyQt5.QtGui import (QColor, QStandardItemModel, QStandardItem)
from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QOpenGLWidget,
                             QWidget, QMenuBar, QHBoxLayout,
                             QTreeView)
# Pyopengl import
import OpenGL.GL as gl


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        # Create widget
        self.glWidget = GLWidget()

        # Create menu bar
        self.topMenu = self.createMenuBar()

        # Creates tree view
        self.treeView, self.treeModel = self.createTreeView()

        # Creates layout and adds widgets
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.topMenu)
        bulkLayout = QHBoxLayout()
        bulkLayout.addWidget(self.treeView)
        bulkLayout.addWidget(self.glWidget)
        mainLayout.addLayout(bulkLayout)
        self.setLayout(mainLayout)

        self.setWindowTitle("Hello GL")

    def createMenuBar(self):
        # Creates a menu bar
        # Adds pull down menus from menu bar
        # Nothing does anything though
        menu_bar = QMenuBar(self)
        # File pull down options
        file = menu_bar.addMenu("File")
        file.addAction("New")
        file.addAction("Open")
        file.addAction("Preferences")
        file.addAction("Exit")

        # Group pull down
        # Nset, elset, surface manipulation
        group = menu_bar.addMenu("Group")
        g_create = group.addMenu("Create")
        g_create.addAction("Node Set")
        g_create.addMenu("Element Set")
        g_create.addMenu("Surface")
        g_create.addMenu("Orientation")
        group.addAction("Manage Geometry")

        # Material pull down
        # Material related commands
        material = menu_bar.addMenu("Material")
        material.addAction("Create")
        material.addAction("Manage")

        # Section pull down
        # Section related commands
        section = menu_bar.addMenu("Section")
        section.addAction("Create")
        section.addAction("Manage")

        # Variable pull down
        # Variable related commands
        var = menu_bar.addMenu("Variable")
        v_create = var.addMenu("Create")
        v_create.addAction("Amplitude")
        v_create.addAction("Time Point")
        v_create.addAction("Constant")
        var.addAction("Manage")

        # Design pull down
        # Design related commands
        design = menu_bar.addMenu("Design")
        d_create = design.addMenu("Create")
        d_create.addAction("Variable")
        d_create.addAction("Objective")
        design.addAction("Manage")

        # Step pull down
        # Step related commands
        step = menu_bar.addMenu("Step")
        step.addAction("Create")
        step.addAction("Manage")

        # Load and Boundary Condition pull down
        # Load and boundary condition related commands
        loadbc = menu_bar.addMenu("Load/BC")
        loadbc.addAction("Create")
        loadbc.addAction("Manage")

        # Constraint pull down
        # Constraint related commands
        constraint = menu_bar.addMenu("Constraint")
        constraint.addAction("Create")
        constraint.addAction("Manage")

        # Interaction pull down
        # Interaction related commands
        interaction = menu_bar.addMenu("Interaction")
        interaction.addAction("Create")
        interaction.addAction("Manage")

        # Output pull down
        # Output related commands
        output = menu_bar.addMenu("Output")
        output.addAction("Create")
        output.addAction("Manage")

        # Help pull down
        help = menu_bar.addMenu("Help")
        help.addAction("Documentation")

        return menu_bar

    def createTreeView(self):
        # Creates tree view panel for left side
        tree_view = QTreeView()

        # Creates model for data that will be displayed
        tree_model = QStandardItemModel()
        tree_model.setHorizontalHeaderLabels(['Main View'])
        tree_view.setModel(tree_model)

        # Add data
        # parent1 = QStandardItem('Family'.format(0))
        # child1 = QStandardItem('C1'.format(1))
        # child2 = QStandardItem('C2'.format(2))
        # child3 = QStandardItem('C3'.format(3))
        # parent1.appendRow([child1, child2, child3])
        # tree_model.appendRow(parent1)
        # parent2 = QStandardItem('Family2'.format(1))
        # child4 = QStandardItem('C1'.format(1))
        # tree_model.appendRow(parent2)
        # parent2.appendRow([child4])

        # Nested tree
        # Model is the input deck
        model = QStandardItem('Model')

        # Groups includes Node and Element sets plus surfaces
        groups = QStandardItem('Groups')
        model.appendRow([groups])
        nsets = QStandardItem('Node Sets')
        groups.appendRow([nsets])
        elsets = QStandardItem('Element Sets')
        groups.appendRow([elsets])
        surfaces = QStandardItem('Surfaces')
        groups.appendRow([surfaces])

        # Materials contains model materials
        materials = QStandardItem('Materials')
        model.appendRow([materials])

        # Sections contains model sections
        sections = QStandardItem('Sections')
        model.appendRow([sections])

        # Variables is a catch all for constants, amplitudes, etc
        var = QStandardItem('Variables')
        model.appendRow([var])
        amp = QStandardItem('Amplitudes')
        var.appendRow([amp])
        tp = QStandardItem('Time Points')
        var.appendRow([tp])
        constants = QStandardItem('Constants')
        var.appendRow([constants])

        # Design variables
        # Doubt that I will get to this so commented
        design = QStandardItem('Design')
        model.appendRow([design])

        # Steps contains model steps
        steps = QStandardItem('Steps')
        model.appendRow([steps])

        # Boundary Conditions contains any kind of
        # load or boundary condition
        bcs = QStandardItem('Loads/BCs')
        model.appendRow([bcs])

        # Constraints contains MPCs, ties, etc
        constraints = QStandardItem('Constraints')
        model.appendRow([constraints])

        # Interactions contains interactions like
        # contact (seems to only be contact)
        interactions = QStandardItem('Interactions')
        model.appendRow([interactions])

        # Outputs contains any output
        # Outputs get inserted into a step
        outputs = QStandardItem('Outputs')
        model.appendRow([outputs])
        # Add model to tree

        tree_model.appendRow(model)

        return tree_view, tree_model


class GLWidget(QOpenGLWidget):
    xRotationChanged = pyqtSignal(int)
    yRotationChanged = pyqtSignal(int)
    zRotationChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)

        self.object = 0
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0

        self.lastPos = QPoint()

        self.trolltechGreen = QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)

    def minimumSizeHint(self):
        return QSize(50, 50)

    def sizeHint(self):
        return QSize(400, 400)

    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle
            self.xRotationChanged.emit(angle)
            self.update()

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.yRotationChanged.emit(angle)
            self.update()

    def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.zRot:
            self.zRot = angle
            self.zRotationChanged.emit(angle)
            self.update()

    def initializeGL(self):
        self.setClearColor(self.trolltechPurple.darker())
        self.object = self.make_rectangle()
        gl.glShadeModel(gl.GL_FLAT)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glEnable(gl.GL_CULL_FACE)

    def paintGL(self):
        gl.glClear(
            gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()
        gl.glTranslated(0.0, 0.0, -10.0)
        gl.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        gl.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        gl.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)
        gl.glCallList(self.object)

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return

        gl.glViewport((width - side) // 2, (height - side) // 2, side,
                      side)

        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)

    def mousePressEvent(self, event):
        self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)
        elif event.buttons() & Qt.RightButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setZRotation(self.zRot + 8 * dx)

        self.lastPos = event.pos()

    def make_rectangle(self):
        # This makes a rectangle

        # Creates one contiguous set of empty display lists
        genList = gl.glGenLists(1)
        # Creates a display list in compile mode
        gl.glNewList(genList, gl.GL_COMPILE)

        # Delimits vertices of a primitive or group of like primitives
        # In this case, the primitives are quads
        gl.glBegin(gl.GL_QUADS)

        # Actually drawing stuff
        x1 = +0.06
        y1 = -0.14
        x2 = +0.14
        y2 = -0.06

        # Creates two quads
        # You can only see one at a time since
        # the other will be invisible when facing away
        self.quad(x1, y1, x2, y2, y2, x2, y1, x1)

        # Connects created quads
        self.extrude(x1, y1, x2, y2)
        self.extrude(x2, y2, y2, x2)
        self.extrude(y2, x2, y1, x1)
        self.extrude(y1, x1, x1, y1)

        gl.glEnd()
        gl.glEndList()

        return genList

    def make_arrow(x1, y1, z1, x2, y2, z2, D):
        # Creates an arrow
        x = x2 - x1
        y = y2 - y1
        z = z2 - z1
        L = math.sqrt(x*x+y*y+z*z)

        # gl.glPushMatrix()
        # Translate to start point
        gl.glTranslated(x1, y1, z1)

        return L

    def makeObject(self):
        # This makes the Qt Q symbol
        genList = gl.glGenLists(1)
        gl.glNewList(genList, gl.GL_COMPILE)

        gl.glBegin(gl.GL_QUADS)

        x1 = +0.06
        y1 = -0.14
        x2 = +0.14
        y2 = -0.06
        x3 = +0.08
        y3 = +0.00
        x4 = +0.30
        y4 = +0.22

        self.quad(x1, y1, x2, y2, y2, x2, y1, x1)
        self.quad(x3, y3, x4, y4, y4, x4, y3, x3)

        self.extrude(x1, y1, x2, y2)
        self.extrude(x2, y2, y2, x2)
        self.extrude(y2, x2, y1, x1)
        self.extrude(y1, x1, x1, y1)
        self.extrude(x3, y3, x4, y4)
        self.extrude(x4, y4, y4, x4)
        self.extrude(y4, x4, y3, x3)

        NumSectors = 200

        for i in range(NumSectors):
            angle1 = (i * 2 * math.pi) / NumSectors
            x5 = 0.30 * math.sin(angle1)
            y5 = 0.30 * math.cos(angle1)
            x6 = 0.20 * math.sin(angle1)
            y6 = 0.20 * math.cos(angle1)

            angle2 = ((i + 1) * 2 * math.pi) / NumSectors
            x7 = 0.20 * math.sin(angle2)
            y7 = 0.20 * math.cos(angle2)
            x8 = 0.30 * math.sin(angle2)
            y8 = 0.30 * math.cos(angle2)

            self.quad(x5, y5, x6, y6, x7, y7, x8, y8)

            self.extrude(x6, y6, x7, y7)
            self.extrude(x8, y8, x5, y5)

        gl.glEnd()
        gl.glEndList()

        return genList

    def quad(self, x1, y1, x2, y2, x3, y3, x4, y4):
        # Creates two green quads
        # Flipping it creates a discontinuity
        self.setColor(self.trolltechGreen)

        gl.glVertex3d(x1, y1, -0.05)
        gl.glVertex3d(x2, y2, -0.05)
        gl.glVertex3d(x3, y3, -0.05)
        gl.glVertex3d(x4, y4, -0.05)

        gl.glVertex3d(x4, y4, +0.05)
        gl.glVertex3d(x3, y3, +0.05)
        gl.glVertex3d(x2, y2, +0.05)
        gl.glVertex3d(x1, y1, +0.05)

    def extrude(self, x1, y1, x2, y2):
        # Thickens quad on both sides
        # Connects the quads drawn with quad()
        # Uses slightly darker green
        self.setColor(self.trolltechGreen.darker(250 + int(100 * x1)))

        gl.glVertex3d(x1, y1, +0.05)
        gl.glVertex3d(x2, y2, +0.05)
        gl.glVertex3d(x2, y2, -0.05)
        gl.glVertex3d(x1, y1, -0.05)

    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle

    def setClearColor(self, c):
        gl.glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())

    def setColor(self, c):
        gl.glColor4f(c.redF(), c.greenF(), c.blueF(), c.alphaF())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
