from ..hubs_component import HubsComponent
from bpy.props import StringProperty
from ..types import PanelType, NodeType
import uuid
from ..utils import add_component, has_component
import bpy


class Networked(HubsComponent):
    _definition = {
        'name': 'networked',
        'display_name': 'Networked',
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE]
    }

    def gather(self, export_settings, object):
        return {
            'id': str(uuid.uuid4()).upper()
        }


def migrate_networked(component_name):
    def migrate_data(ob):
        if component_name in ob.hubs_component_list.items:
            if Networked.get_name() not in ob.hubs_component_list.items:
                add_component(ob, Networked.get_name())

    for ob in bpy.data.objects:
        migrate_data(ob)

        if ob.type == 'ARMATURE':
            for bone in ob.data.bones:
                migrate_data(bone)
