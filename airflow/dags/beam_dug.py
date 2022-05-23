from airflow import models
from airflow.providers.apache.beam.operators.beam import (
    BeamRunJavaPipelineOperator,
)
from datetime import datetime

with models.DAG(
        "example_beam_native_java_direct_runner",
        schedule_interval=None,  # Override to match your needs
        start_date=datetime(2022, 1, 1),
        catchup=False,
        tags=['example'],
) as dag_native_java_direct_runner:

    start_java_pipeline_direct_runner = BeamRunJavaPipelineOperator(
        task_id="start_java_pipeline_direct_runner",
        jar="/opt/airflow/pipelines/word_count_beam_bundled_0.1.jar",
        pipeline_options={
            'output': '/tmp/start_java_pipeline_direct_runner',
        },
        job_class='org.apache.beam.examples.WordCount',
    )

    start_java_pipeline_direct_runner