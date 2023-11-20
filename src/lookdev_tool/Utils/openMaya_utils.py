from shiboken2 import wrapInstance
import maya.OpenMaya


def maya_main_window(widget):
    """
        Return the Maya main window widget as a Python object
    """
    main_window_ptr = maya.OpenMayaUI.MQtUtil.mainWindow()

    return wrapInstance(int(main_window_ptr), widget)
