from arcana2.data.sets.bids import BidsFormat
from arcana2.data.spaces.clinical import Clinical
from arcana2.data.types.general import directory
from arcana2.data.types.neuroimaging import nifti_gz
from ais.utils import docker_image_executable


WRAPPER_VERSION = '0.1.0'
MRIQC_VERSION = '0.16.1'

INPUTS = {'anat/T1w': nifti_gz}
OUTPUTS = {'mriqc': directory}
PARAMETERS = []

docker_image = f"poldracklab/mriqc:{MRIQC_VERSION}"

metadata = {
    'name': "mriqc",
    'description': (
        "MRIQC extracts no-reference IQMs (image quality metrics) from "
        "structural (T1w and T2w) and functional MRI (magnetic resonance "
        "imaging) data."),
    'inputs': INPUTS,
    'outputs': OUTPUTS,
    'parameters': PARAMETERS,
    'version': WRAPPER_VERSION,
    'pkg_version': MRIQC_VERSION,
    'requirements': [],
    'packages': [],
    'base_image': f'poldracklab/mriqc:{MRIQC_VERSION}',
    'maintainer': 'thomas.close@sydney.edu.au',
    'info_url': 'http://mriqc.readthedocs.io',
    'frequency': Clinical.session}


task = BidsFormat.wrap_app(
    'mriqc',
    'mriqc',  # Extracted using `docker_image_executable(docker_image)`
    inputs=INPUTS)


docker_task = BidsFormat.wrap_app(
    'mriqc_docker',
    docker_image,
    inputs=INPUTS,
    container_type='docker')
