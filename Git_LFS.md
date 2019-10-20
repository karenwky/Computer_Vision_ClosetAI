# How to use Git LFS

1. `brew install git-lfs` or download from [official website](https://git-lfs.github.com)

1. `git lfs install`

2. clone your own repository into local machine

3. place the large file into your repository (sub)folder on local machine

5. `cd path-to-repo-dir`

5. `git lfs track "your-file-name-with-extension"`

6. `git lfs track` to see whether the file is being tracked
   ```
   Listing tracked patterns
       out-11.mp4 (.gitattributes)
   Listing excluded patterns
   ```

7. `git add .gitattributes`

1. `git add (path-to-repo-subfolder/)file-name-with-extension`

1. `git commit -m "your-summary-comment"`, you will see something like this:
   ```
   2 files changed, 4 insertions(+)
   create mode 100644 capstone/TRAIN_ALL_v1/out-11.mp4
   ```

1. `git push`
   ```
   Uploading LFS objects: 100% (1/1), 96 MB | 2.4 MB/s, done                       
   Enumerating objects: 10, done.
   Counting objects: 100% (10/10), done.
   Delta compression using up to 8 threads
   Compressing objects: 100% (6/6), done.
   Writing objects: 100% (6/6), 589 bytes | 589.00 KiB/s, done.
   Total 6 (delta 3), reused 0 (delta 0)
   remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
   To https://github.com/yyzz1010/project_drafts.git
   98e267e..06e2a5a  master -> master
   ```
   
1. Your large file is being successfully uploaded! =D
