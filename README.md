# DeepCardiacMRI

Deep learning models for cardiac MRI segmentation and pathology classification from cine MRI, comparing U-Net, Attention U-Net, TransUNet, and CBAM-UNet, alongside a novel Diagnosis-Aware Cardiac Loss (DACL) incorporating temporal consistency specific to cine MRI sequences.

This repository was developed as part of an MSc dissertation project (University of Leeds, School of Computing).

**This repository is for academic/research purposes only.**

## Overview

Four segmentation architectures were implemented from scratch in PyTorch and evaluated on the ACDC dataset under both standard Cross Entropy and the proposed DACL loss function. Segmentation output was used to derive physiological parameters (EDV, ESV, Ejection Fraction, Myocardial Mass) and to perform pathology classification via both a two-step classical machine learning pipeline and an end-to-end multi-task deep learning approach.

## Dataset

This project uses the ACDC (Automated Cardiac Diagnosis Challenge) dataset, licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).

**The dataset itself is NOT included in this repository** and must be obtained separately from the official ACDC challenge source, in compliance with its licence terms.

**Citation:**
Bernard, O., Lalande, A., Zotti, C., Cervenansky, F., et al. (2018) 'Deep Learning Techniques for Automatic MRI Cardiac Multi-structures Segmentation and Diagnosis: Is the Problem Solved?', *IEEE Transactions on Medical Imaging*, 37(11), pp. 2514-2525. doi: 10.1109/TMI.2018.2837502.

## Repository Structure

```
DeepCardiacMRI/
├── unet.py                    # U-Net architecture definition
├── dataset.py                 # Data loading, preprocessing, augmentation
├── train_segmentation.py      # Training loop (Cross Entropy / DACL)
├── test_loader.py             # Held-out test set loader
├── checkpoints/                # Trained model weights (.pth)
├── results/                    # Test-set evaluation results (.csv)
├── figures/                    # Figure and chart generation scripts
└── videos/                     # Cardiac cycle prediction videos
```

## Models

| Model | Description |
|---|---|
| U-Net | CNN baseline, encoder-decoder with skip connections |
| Attention U-Net | CNN with decoder-guided local attention gates |
| TransUNet | CNN encoder with Transformer bottleneck (global self-attention) |
| CBAM-UNet | CNN with self-contained channel and spatial attention (CBAM) |

## Loss Functions

- **Cross Entropy** (baseline)
- **DACL (Diagnosis-Aware Cardiac Loss)** — combines Cross Entropy and Dice with a temporal consistency term penalising large frame-to-frame changes in predicted segmentation across consecutive cine MRI frames.

## Requirements

See `requirements.txt`. Core dependencies: PyTorch, NiBabel, scikit-learn, NumPy, Matplotlib, Pandas.

## Environment

All models were trained using Google Colaboratory's free-tier GPU (NVIDIA T4).

## Licence

Code in this repository is provided for academic and research purposes only. No commercial use is intended or permitted. Use of the ACDC dataset must comply with its original CC BY-NC-SA 4.0 licence terms, available at https://creativecommons.org/licenses/by-nc-sa/4.0/

## Author

Hamna Farooq — MSc Project, University of Leeds
