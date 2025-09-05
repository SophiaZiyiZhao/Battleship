#!/usr/bin/env python3
"""
Business Architecture Diagram Generator
Creates a visual representation of the Shopify ecosystem architecture
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

def create_business_architecture_diagram():
    # Create figure and axis
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Define colors
    colors = {
        'primary': '#3498db',      # Blue
        'secondary': '#2ecc71',    # Green  
        'accent': '#e74c3c',       # Red
        'neutral': '#95a5a6',      # Gray
        'warning': '#f39c12',      # Orange
        'info': '#9b59b6'          # Purple
    }
    
    # Define component positions and sizes
    components = {
        'shopify': {'pos': (2, 9), 'size': (3, 1.5), 'color': colors['primary']},
        'shokz_sdk': {'pos': (2, 6.5), 'size': (3, 1.5), 'color': colors['secondary']},
        'cdp': {'pos': (8, 8), 'size': (3.5, 2), 'color': colors['accent']},
        'data_warehouse': {'pos': (13, 8), 'size': (2.5, 1.5), 'color': colors['neutral']},
        'aftership': {'pos': (1, 3.5), 'size': (2.5, 1), 'color': colors['warning']},
        'loyalty': {'pos': (1, 2), 'size': (2.5, 1), 'color': colors['warning']},
        'tnpl': {'pos': (1, 0.5), 'size': (2.5, 1), 'color': colors['warning']},
        'klaviyo': {'pos': (8, 4.5), 'size': (3, 1.5), 'color': colors['info']},
        'bi_tools': {'pos': (13, 4.5), 'size': (2.5, 1.5), 'color': colors['neutral']}
    }
    
    # Draw components
    def draw_component(name, info, text):
        x, y = info['pos']
        w, h = info['size']
        color = info['color']
        
        # Create rounded rectangle
        box = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.1",
            facecolor=color,
            edgecolor='black',
            linewidth=2,
            alpha=0.8
        )
        ax.add_patch(box)
        
        # Add text
        ax.text(x + w/2, y + h/2, text, 
                ha='center', va='center', 
                fontsize=10, fontweight='bold',
                color='white', wrap=True)
    
    # Draw all components
    draw_component('shopify', components['shopify'], 'Shopify\nStorefront')
    draw_component('shokz_sdk', components['shokz_sdk'], 'Shokz App\nSDK')
    draw_component('cdp', components['cdp'], 'CDP:\nEvents/Profiles/\nIdentity')
    draw_component('data_warehouse', components['data_warehouse'], 'Data Warehouse\n(可选)')
    draw_component('aftership', components['aftership'], 'AfterShip\n(Trade-in)')
    draw_component('loyalty', components['loyalty'], 'Loyalty &\nReferrals')
    draw_component('tnpl', components['tnpl'], 'TNPL\nProvider')
    draw_component('klaviyo', components['klaviyo'], 'Klaviyo\nESP/SMS')
    draw_component('bi_tools', components['bi_tools'], 'BI/Looker/\nGA4')
    
    # Define connections
    connections = [
        # Main data flow to CDP
        {'from': 'shopify', 'to': 'cdp', 'style': 'solid', 'color': 'black', 'width': 2},
        {'from': 'shokz_sdk', 'to': 'cdp', 'style': 'solid', 'color': 'black', 'width': 2},
        
        # CDP to Data Warehouse (optional)
        {'from': 'cdp', 'to': 'data_warehouse', 'style': 'dashed', 'color': 'gray', 'width': 1.5},
        
        # Event/Status sync to CDP
        {'from': 'aftership', 'to': 'cdp', 'style': 'solid', 'color': 'orange', 'width': 1.5},
        {'from': 'loyalty', 'to': 'cdp', 'style': 'solid', 'color': 'orange', 'width': 1.5},
        {'from': 'tnpl', 'to': 'cdp', 'style': 'solid', 'color': 'orange', 'width': 1.5},
        
        # CDP to downstream systems
        {'from': 'cdp', 'to': 'klaviyo', 'style': 'solid', 'color': 'purple', 'width': 2},
        {'from': 'cdp', 'to': 'bi_tools', 'style': 'solid', 'color': 'blue', 'width': 2},
        
        # Optional: Data Warehouse to BI
        {'from': 'data_warehouse', 'to': 'bi_tools', 'style': 'dashed', 'color': 'gray', 'width': 1.5}
    ]
    
    # Draw connections
    def draw_connection(conn):
        from_comp = components[conn['from']]
        to_comp = components[conn['to']]
        
        # Calculate connection points
        from_x = from_comp['pos'][0] + from_comp['size'][0]
        from_y = from_comp['pos'][1] + from_comp['size'][1]/2
        
        to_x = to_comp['pos'][0]
        to_y = to_comp['pos'][1] + to_comp['size'][1]/2
        
        # Special handling for vertical connections
        if conn['from'] in ['aftership', 'loyalty', 'tnpl']:
            from_x = from_comp['pos'][0] + from_comp['size'][0]/2
            from_y = from_comp['pos'][1] + from_comp['size'][1]
            to_x = to_comp['pos'][0] + to_comp['size'][0]/2
            to_y = to_comp['pos'][1]
        
        # Draw arrow
        if conn['style'] == 'dashed':
            ax.annotate('', xy=(to_x, to_y), xytext=(from_x, from_y),
                       arrowprops=dict(arrowstyle='->', color=conn['color'], 
                                     lw=conn['width'], linestyle='--'))
        else:
            ax.annotate('', xy=(to_x, to_y), xytext=(from_x, from_y),
                       arrowprops=dict(arrowstyle='->', color=conn['color'], 
                                     lw=conn['width']))
    
    # Draw all connections
    for conn in connections:
        draw_connection(conn)
    
    # Add special annotations
    # Deep Link / QR annotation
    ax.text(3.5, 5.5, 'Deep Link / QR', ha='center', va='center',
            fontsize=9, style='italic', 
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.7))
    
    # Event/Status sync annotation
    ax.text(5, 2.5, '事件/状态同步', ha='center', va='center',
            fontsize=9, style='italic', rotation=45,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.7))
    
    # Downstream annotations
    ax.text(11, 5.5, '触达/分群', ha='center', va='center',
            fontsize=9, style='italic',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightpink', alpha=0.7))
    
    ax.text(14, 3, 'KPI 可视化', ha='center', va='center',
            fontsize=9, style='italic',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen', alpha=0.7))
    
    # Add title
    ax.text(8, 11.5, 'Business Architecture Diagram', 
            ha='center', va='center', fontsize=18, fontweight='bold')
    
    # Add legend
    legend_elements = [
        plt.Line2D([0], [0], color='black', lw=2, label='主要数据流'),
        plt.Line2D([0], [0], color='orange', lw=1.5, label='事件同步'),
        plt.Line2D([0], [0], color='purple', lw=2, label='营销触达'),
        plt.Line2D([0], [0], color='blue', lw=2, label='数据分析'),
        plt.Line2D([0], [0], color='gray', lw=1.5, linestyle='--', label='可选连接')
    ]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0, 1))
    
    plt.tight_layout()
    return fig

# Generate and save the diagram
if __name__ == "__main__":
    fig = create_business_architecture_diagram()
    
    # Save as high-quality PNG
    plt.savefig('/workspace/business_architecture_diagram.png', 
                dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    
    # Save as SVG for scalability
    plt.savefig('/workspace/business_architecture_diagram.svg', 
                format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    
    print("Business architecture diagram generated successfully!")
    print("Files created:")
    print("- business_architecture_diagram.png (high-resolution)")
    print("- business_architecture_diagram.svg (scalable vector)")
    
    plt.show()