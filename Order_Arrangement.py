"""
QGIS Python Script: Categorize Joined Layer by Geological Order
Applies categorized symbology to 'Joined layer' based on 'order' field (1-44)
while maintaining CGMW standard colors from 'color' field
"""

from qgis.core import (
    QgsProject,
    QgsSymbol,
    QgsCategorizedSymbolRenderer,
    QgsRendererCategory,
    QgsExpression,
    QgsFeatureRequest
)
from qgis.PyQt.QtGui import QColor
from qgis.utils import iface

def categorize_joined_geological_layer():
    """
    Categorizes the 'Joined layer' based on 'order' field (1-44) and applies colors from 'color' field.
    
    Requirements:
    - Layer must be named 'Joined layer'
    - Layer must have 'order' field (integer: 1-44)
    - Layer must have 'color' field (hex color string)
    - Optional: 'era' and period name field for better labels
    """
    
    # Get the layer named "Joined layer"
    layer = QgsProject.instance().mapLayersByName('Africa_Geological_Data')
    
    if not layer:
        iface.messageBar().pushMessage(
            "Error", 
            "Layer 'Joined layer' not found in project!", 
            level=Qgis.Critical
        )
        return
    
    layer = layer[0]  # Get first match
    
    if not layer:
        iface.messageBar().pushMessage(
            "Error", 
            "No active layer selected!", 
            level=Qgis.Critical
        )
        return
    
    # Check if required fields exist
    field_names = [field.name() for field in layer.fields()]
    
    if 'order' not in field_names:
        iface.messageBar().pushMessage(
            "Error", 
            "Layer must have 'order' field!", 
            level=Qgis.Critical
        )
        return
    
    if 'color' not in field_names:
        iface.messageBar().pushMessage(
            "Error", 
            "Layer must have 'color' field!", 
            level=Qgis.Critical
        )
        return
    
    # Find the period name field (common names)
    period_field = None
    possible_names = ['name', 'long_name', 'period', 'period_name', 'geo_period']
    for name in possible_names:
        if name in field_names:
            period_field = name
            break
    
    if not period_field:
        period_field = field_names[0]  # Use first field as fallback
    
    # Get unique combinations of order, color, and name
    categories_data = {}
    
    request = QgsFeatureRequest()
    for feature in layer.getFeatures(request):
        order = feature['order']
        color = feature['color']
        
        # Get the name field value
        name = feature[period_field] if period_field and period_field in field_names else f"Order {order}"
        
        if order not in categories_data:
            categories_data[order] = {
                'color': color,
                'name': name
            }
    
    # Sort by order
    sorted_orders = sorted(categories_data.keys())
    
    # Create categories
    categories = []
    geom_type = layer.geometryType()
    
    for order in sorted_orders:
        data = categories_data[order]
        color_hex = data['color']
        name = data['name']
        
        # Create symbol
        symbol = QgsSymbol.defaultSymbol(geom_type)
        
        # Set fill color
        qcolor = QColor(color_hex)
        symbol.setColor(qcolor)
        
        # Configure symbol based on geometry type
        if geom_type == 0:  # Point
            symbol.setSize(2.5)
            symbol.symbolLayer(0).setStrokeColor(QColor('#333333'))
            symbol.symbolLayer(0).setStrokeWidth(0.2)
        elif geom_type == 1:  # Line
            symbol.setWidth(0.5)
        elif geom_type == 2:  # Polygon
            symbol.symbolLayer(0).setStrokeColor(QColor('#444444'))
            symbol.symbolLayer(0).setStrokeWidth(0.26)
            symbol.setOpacity(0.9)
        
        # Create label - only the name
        label = str(name)
        
        # Create category
        category = QgsRendererCategory(
            order,
            symbol,
            label
        )
        categories.append(category)
    
    # Create and apply renderer
    renderer = QgsCategorizedSymbolRenderer('order', categories)
    layer.setRenderer(renderer)
    layer.triggerRepaint()
    
    # Refresh legend
    iface.layerTreeView().refreshLayerSymbology(layer.id())
    
    # Success message
    iface.messageBar().pushMessage(
        "Success", 
        f"Categorized {len(categories)} geological periods from oldest to youngest!", 
        level=Qgis.Success,
        duration=5
    )
    
    print(f"Applied categorized symbology to layer: {layer.name()}")
    print(f"Total categories: {len(categories)}")
    print(f"Order range: {sorted_orders[0]} to {sorted_orders[-1]}")


# Execute the function
categorize_joined_geological_layer()
