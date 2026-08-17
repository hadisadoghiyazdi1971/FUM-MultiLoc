# Push FUM-MultiLoc to GitHub

Target local path:

```text
J:\SadoghiSite2\FUM-MultiLoc
```

## Recommended GitHub repository

Repository name:

```text
FUM-MultiLoc
```

Description:

```text
Multimodal, map-aware benchmark for indoor positioning using Wi-Fi, IMU, vision, cellular/BTS and semantic indoor maps at Ferdowsi University of Mashhad.
```

Suggested topics:

```text
indoor-positioning
indoor-localization
wifi-fingerprinting
imu
visual-localization
sensor-fusion
multimodal
benchmark
dataset
pedestrian-localization
mobile-sensing
```

## If the Git repository already exists locally

After extracting this package into the repository root:

```bat
cd /d J:\SadoghiSite2\FUM-MultiLoc
git status
git add .
git status
git commit -m "Initialize FUM-MultiLoc benchmark repository structure"
git push
```

Inspect the second `git status` carefully. No raw images, archives, sensor blobs, or private files should appear.

## If no remote is configured

```bat
git remote -v
git remote add origin https://github.com/YOUR-USERNAME/FUM-MultiLoc.git
git branch -M main
git push -u origin main
```

## Do not enable Git LFS yet

This skeleton does not need Git LFS. Large benchmark data should not be committed until the release/data-hosting strategy is finalized.
