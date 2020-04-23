"""
This pipeline creates an object mesh from an existing segmentation.
"""
import os

from core.adapters.file_loader import read_input_path_as_np_array
from core.adapters.trimesh_converter import convert_meshes_trimesh
from core.client.viewer import view_mesh
from core.services.marching_cubes import generate_mesh
from core.services.np_image_manipulation import seperate_segmentation


def run(input_path: str, output_path: str, segment_type: list) -> None:
    segmented_array = read_input_path_as_np_array(input_path)

    meshes = [
        generate_mesh(segment, 0)
        for segment in seperate_segmentation(
            segmented_array, unique_values=segment_type
        )
    ]
    meshes = convert_meshes_trimesh(meshes)
    view_mesh(meshes, output_path)
