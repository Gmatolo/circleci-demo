# Anatomy of a circleci config.yml file

Pipelines have workflows that have jobs that have steps

version: specifies the circle-ci version, recent version mostly used

jobs: specifies the jobs that need to be performed in a workflow

commands: specifies commands that can be reused

orbs: prewritten functions

workflow: specifies the order of jobs, a pipeline can be made up of one or more jobs
workflow-name: The names needs to be as descriptive and relevant as possible
jobs
-1
-2
requires: job no. 1 is carried out before job no.2
1
-3
filters: excludes a job no.1 during its execution, the command uses the tag or branch to filter
-1
