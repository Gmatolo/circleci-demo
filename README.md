# Anatomy of a circleci config.yml file

Pipelines have workflows that have jobs that have steps

version: specifies the circle-ci version, recent version mostly used

jobs: specifies the jobs that need to be performed in a workflow

commands: specifies commands that can be reused

orbs: prewritten functions

workflow: specifies the order of jobs, a pipeline can be made up of one or more jobs
