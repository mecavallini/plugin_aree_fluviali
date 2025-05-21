# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BankFullDetection
                                 A QGIS plugin
 Automatic bankfull width detection
                              -------------------
        begin                : 2014-01-20
        copyright            : (C) 2014 by Pierluigi De Rosa
        email                : pierluigi.derosa@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt5.QtCore import QSettings, QTranslator, QCoreApplication, QLocale, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMessageBox
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from bankfulldetectiondialog import BankFullDetectionDialog
import os.path


class BankFullDetection:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
	locale = QLocale.system().name()[0:2]
       # locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'bankfulldetection_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/bankfulldetection/icon.png"),
            u"Automatic bankfull width detection", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Bankfull width detection", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Bankfull width detection", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        try:
            import shapely
        except ImportError:
            QMessageBox.warning(self.iface.mainWindow(),
                                "BankFullDetection",
                                'Library "shapely" not found. Please install!')
            return
        
        # Create the dialog (after translation) and keep reference
        self.dlg = BankFullDetectionDialog(self.iface)
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        #~ self.dlg.exec_()
        # See if OK was pressed
        #~ if result == 1:
            #~ pass
	self.dlg.exec_()

