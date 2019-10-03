from abc import ABCMeta, abstractmethod

import six


class RunStorage(six.with_metaclass(ABCMeta)):
    def __init__(self, *args, **kwargs):
        '''EventLogStorage.__init__ should idempotently ensure that any necessary one-time setup
        for the RunStorage is performed, or raise if this setup has not been performed and
        cannot be performed withim the context of this function.'''

    @abstractmethod
    def add_run(self, pipeline_run):
        '''Add a run to storage.

        Args:
            pipeline_run (PipelineRun): The run to add. If this is not a PipelineRun,
        '''

    @abstractmethod
    def handle_run_event(self, run_id, event):
        '''Update run storage in accordance to a pipeline run related DagsterEvent

        Args:
            event (DagsterEvent)

        '''

    @abstractmethod
    def all_runs(self, cursor=None, limit=None):
        '''Return all the runs present in the storage.

        Returns:
            List[PipelineRun]
        '''

    @abstractmethod
    def get_runs_with_pipeline_name(self, pipeline_name, cursor=None, limit=None):
        '''Return all the runs present in the storage for a given pipeline.

        Args:
            pipeline_name (str): The pipeline to index on
            cursor (Optional[str]): Starting cursor (run_id) of range of runs
            limit (Optional[int]): Number of results to get. Defaults to infinite.
        Returns:
            List[PipelineRun]
        '''

    @abstractmethod
    def get_runs_with_matching_tag(self, key, value, cursor=None, limit=None):
        '''Return all the runs present in the storage that have a tag with key, value

        Args:
            key (str): The key to index on
            value (str): The value to match
            cursor (Optional[str]): Starting cursor (run_id) of range of runs
            limit (Optional[int]): Number of results to get. Defaults to infinite.

        Returns:
            List[PipelineRun]
        '''

    @abstractmethod
    def get_runs_with_status(self, run_status, cursor=None, limit=None):
        '''Run all the runs matching a particular status

        Args:
            run_status (PipelineRunStatus)
            cursor (Optional[str]): Starting cursor (run_id) of range of runs
            limit (Optional[int]): Number of results to get. Defaults to infinite.

        Returns:
            List[PipelineRun]:
        '''

    @abstractmethod
    def get_run_by_id(self, run_id):
        '''Get a run by its id.

        Args:
            run_id (str): The id of the run

        Returns:
            Optional[PipelineRun]
        '''

    @abstractmethod
    def get_run_tags(self):
        '''Get a list of tag keys and the values that have been associated with them.

        Returns:
            List[Tuple[string, List[string]]]
        '''

    @abstractmethod
    def has_run(self, run_id):
        pass

    @abstractmethod
    def wipe(self):
        '''Clears the run storage.'''

    @abstractmethod
    def delete_run(self, run_id):
        '''Remove a run from storage'''