# Beginner GitHub Workflow

A simple workflow I use to keep project changes organized and reviewable.

## Steps

1. Pull the latest changes from `main`.
2. Create a branch with a clear name.
3. Make one focused change.
4. Commit with a short, descriptive message.
5. Push the branch and open a pull request.
6. Review the changed files and checks.
7. Merge only when the change is ready.

## Example

```bash
git checkout main
git pull
git checkout -b docs/update-project-notes
git add .
git commit -m "docs: update project notes"
git push -u origin docs/update-project-notes
```

## Why I Use It

This workflow keeps the main branch stable, makes changes easier to understand, and creates a clear record of my progress.
