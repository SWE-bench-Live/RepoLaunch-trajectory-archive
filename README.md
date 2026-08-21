# RepoLaunch Trajectory Archive

This repo includes some trajectory samples of [RepoLaunch](https://github.com/microsoft/RepoLaunch) aross 9 programming languages and 2 operating systems (linux, windows).

The trajectory demos could potentially benefit analysis for agentic workflow improvement and agentic training.

## Contents

- [`linux_tasks/`](./linux_tasks/) — RepoLaunch trajectories for eight
  programming languages on Linux. Generated with `launch <config_path>`.
- [`windows_tasks/`](./windows_tasks/) — RepoLaunch trajectories for nine
  programming languages on Windows. Generated with `launch <config_path>`.
- [`adjacent_commit_run_examples/`](./adjacent_commit_run_examples/) —
  Memory-aware RepoLaunch trajectories on Linux. Generated with:

  ```sh
  python -m launch.scripts.adjacent_commit_run --config_path <config_path>
  ```

  This command launches one commit per repository, then checks out to other
  commits of the same repo from the launch result. Each language directory contains:

  - `.cache/`: Commit relationships between the commit RepoLaunch ran and
    the commits to be checked out directly -- is-descendant or not.
  - `playground/`: Logs of the instances RepoLaunch actually ran (one commit per
    repository).
  - `adjacent_commit_run_log/`: Logs of git-checking out commits from the
    RepoLaunch results, including examples of failed direct checkouts.
