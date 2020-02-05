import pytest
from dagster_aws.emr import EmrClusterState, EmrError, EmrJobRunner
from moto import mock_emr

from dagster.utils.test import create_test_pipeline_execution_context

REGION = 'us-west-1'


@mock_emr
def test_emr_create_cluster(emr_cluster_config):
    context = create_test_pipeline_execution_context()
    cluster = EmrJobRunner(region=REGION)
    cluster_id = cluster.run_job_flow(context, emr_cluster_config)
    assert cluster_id.startswith('j-')


@mock_emr
def test_emr_describe_cluster(emr_cluster_config):
    context = create_test_pipeline_execution_context()
    cluster = EmrJobRunner(region=REGION)
    cluster_id = cluster.run_job_flow(context, emr_cluster_config)
    cluster_info = cluster.describe_cluster(cluster_id)
    assert cluster_info['Name'] == 'test-emr'
    assert EmrClusterState(cluster_info['Status']['State']) == EmrClusterState.Waiting


@mock_emr
def test_emr_id_from_name(emr_cluster_config):
    context = create_test_pipeline_execution_context()
    cluster = EmrJobRunner(region=REGION)
    cluster_id = cluster.run_job_flow(context, emr_cluster_config)
    assert cluster.cluster_id_from_name('test-emr') == cluster_id

    with pytest.raises(EmrError) as exc_info:
        cluster.cluster_id_from_name('cluster-doesnt-exist')

    assert (
        'dagster_aws.emr.emr.EmrError: cluster cluster-doesnt-exist not found in region us-west-1'
        in str(exc_info)
    )


def test_emr_construct_step_dict():
    cmd = ['pip', 'install', 'dagster']

    assert EmrJobRunner.construct_step_dict_for_command('test_step', cmd) == {
        'Name': 'test_step',
        'ActionOnFailure': 'CONTINUE',
        'HadoopJarStep': {'Jar': 'command-runner.jar', 'Args': cmd},
    }

    assert EmrJobRunner.construct_step_dict_for_command(
        'test_second_step', cmd, action_on_failure='CANCEL_AND_WAIT'
    ) == {
        'Name': 'test_second_step',
        'ActionOnFailure': 'CANCEL_AND_WAIT',
        'HadoopJarStep': {'Jar': 'command-runner.jar', 'Args': cmd},
    }
