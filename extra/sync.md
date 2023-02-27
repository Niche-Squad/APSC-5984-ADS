# Syncing the course repository

- [Syncing the course repository](#syncing-the-course-repository)
  - [First time syncing](#first-time-syncing)
  - [Syncing after configuring the upstream repository](#syncing-after-configuring-the-upstream-repository)

Remember to sync your forked repository with the course repository before you start working on the assignment. You can do this by running the following commands in the `terminal`.

## First time syncing

[Official Guide](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/configuring-a-remote-repository-for-a-fork)

Check the current upstream repository:

```bash
git remote -v
# origin git@github.com:Poissonfish/APSC-5984-ADS.git (fetch)
# origin git@github.com:Poissonfish/APSC-5984-ADS.git (push)
```

You won't see the course repository as the upstream repository. So let's add the course repository as the upstream:

```bash
git remote add upstream git@github.com:Niche-Squad/APSC-5984-ADS.git
```

Check again:

```bash
git remote -v
# origin git@github.com:Poissonfish/APSC-5984-ADS.git (fetch)
# origin git@github.com:Poissonfish/APSC-5984-ADS.git (push)
# upstream git@github.com:Niche-Squad/APSC-5984-ADS.git (fetch)
# upstream git@github.com:Niche-Squad/APSC-5984-ADS.git (push)
```

## Syncing after configuring the upstream repository

[Official Guide](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)

```bash
git fetch upstream
git merge -X ours upstream/main --no-edit --allow-unrelated-histories
git push
```
