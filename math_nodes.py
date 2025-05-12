import torch
from comfy.model_management import get_torch_device

class AddNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "a": ("FLOAT", {"default": 0.0, "min": -1000000.0, "max": 1000000.0}),
                "b": ("FLOAT", {"default": 0.0, "min": -1000000.0, "max": 1000000.0}),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "add"
    CATEGORY = "math"

    def add(self, a, b):
        return (a + b,)

class SubtractNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "a": ("FLOAT", {"default": 0.0, "min": -1000000.0, "max": 1000000.0}),
                "b": ("FLOAT", {"default": 0.0, "min": -1000000.0, "max": 1000000.0}),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "subtract"
    CATEGORY = "math"

    def subtract(self, a, b):
        return (a - b,)

# Node class mappings
NODE_CLASS_MAPPINGS = {
    "Add": AddNode,
    "Subtract": SubtractNode
}

# Node display names
NODE_DISPLAY_NAME_MAPPINGS = {
    "Add": "Add Numbers",
    "Subtract": "Subtract Numbers"
}

# This is the main entry point for ComfyUI to load the nodes
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 