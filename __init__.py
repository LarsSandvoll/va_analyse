# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VLAnalyse
                                 A QGIS plugin
 Grupperer vannledningsnettverket inn i grupper basert på analyser av nettverket
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-06-25
        copyright            : (C) 2019 by Norkart
        email                : larsan@norkart.no
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load VLAnalyse class from file VLAnalyse.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    
    from .va_analyse import VAAnalyse
    
    return VAAnalyse(iface)

