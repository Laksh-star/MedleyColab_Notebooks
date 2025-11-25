# SynthID Detection: Text & Image AI Detection Guide

This notebook provides a comprehensive guide to understanding and implementing AI detection methods, focusing on Google's SynthID for text and images, and exploring alternative techniques for image detection. 

## Table of Contents

1.  [SynthID Text Detection (Open Source)](#synthid-text-detection-open-source)
2.  [SynthID Image Detection (Limited Availability)](#synthid-image-detection-limited-availability)
3.  [Alternative AI Image Detection Methods](#alternative-ai-image-detection-methods)

## SynthID Text Detection (Open Source)

SynthID Text is an open-source watermarking and detection tool available through Hugging Face Transformers. This section of the notebook demonstrates how to generate watermarked text and then attempt to detect that watermark.

### Current Status / Known Issues

During testing, the SynthID Text Detector **did not reliably identify watermarks**, even in text explicitly generated with SynthID watermarking. All tests (watermarked text, non-watermarked text, and human-written text) consistently resulted in an "unknown" prediction with 0% confidence. This indicates a potential issue with the current implementation, model compatibility, or detector configuration in the provided notebook environment.

### How to Use (SynthID Text)

1.  **Install necessary packages:**
    ```bash
    !pip install transformers>=4.46.0 torch -q
    ```
2.  **Generate Watermarked Text:** The notebook loads a causal language model (e.g., `facebook/opt-1.3b`) and configures `SynthIDTextWatermarkingConfig` with secret keys. It then generates text both with and without the watermark for comparison.
3.  **Detect Watermark:** The `SynthIDTextWatermarkDetector` is initialized with the tokenizer, the generative model (wrapped for detection), and a configured logits processor. A `detect_watermark` function is used to process texts and print detection results.
4.  **Test Robustness:** The notebook includes basic robustness tests by applying minor modifications and truncation to watermarked text.

## SynthID Image Detection (Limited Availability)

**IMPORTANT:** SynthID for images is NOT open-source. Its availability is restricted:

1.  **Google Cloud Vertex AI:** Primarily for images generated with Google's Imagen models, requiring a GCP account and Vertex AI API access.
2.  **SynthID Detector Portal:** A waitlist-only portal for journalists and researchers.

The notebook includes example Python code demonstrating how one would interact with SynthID via Google Cloud Vertex AI, but it is commented out as it requires specific GCP setup and credentials not available in a standard Colab environment.

## Alternative AI Image Detection Methods

Given the limited access to SynthID for images, the notebook explores several alternative, publicly available methods for detecting AI-generated images.

### 1. Check Image Metadata (EXIF/C2PA)

Examines image metadata (EXIF, C2PA) for indicators of AI generation (e.g., creator tools, software used). This method is quick but often unreliable, as many AI generators strip metadata or it can be easily altered.

**Packages:** `pillow`, `exifread`

### 2. Hugging Face AI Image Detector

Utilizes a pre-trained image classification model from Hugging Face (`umm-maybe/AI-image-detector`) to predict whether an image is artificial or human-created. This is a machine learning-based approach offering probabilistic estimates.

**Packages:** `transformers`, `pillow`, `torch`, `torchvision`

### 3. OpenAI's CLIP-based Detection

Leverages OpenAI's CLIP (Contrastive Language-Image Pre-training) model to compare an image against various text prompts describing AI-generated vs. real photographs. It provides a score indicating the likelihood of an image belonging to each category.

**Packages:** `transformers`, `pillow`, `torchvision`, `torch`

### 4. Statistical Analysis Method

Analyzes inherent statistical properties of images (noise levels, color distribution variance, edge density, compression artifacts) that can differ between AI-generated and real photos. AI images often exhibit characteristics like very low noise, overly smooth color distributions, and lack of typical compression artifacts. This method provides indicative, not definitive, insights.

**Packages:** `numpy`, `opencv-python`, `pillow`, `scipy`

## Summary & Recommendations

-   **For TEXT Detection:** Use **SynthID Text** (open-source via Hugging Face Transformers), but be aware of potential detection issues as observed in this notebook.
-   **For IMAGE Detection:**
    -   If you have Google Cloud access: **SynthID on Vertex AI** (most reliable for Imagen-generated images).
    -   If not: Combine **Hugging Face AI Detector**, **CLIP-based Detection**, **Metadata Check**, and **Statistical Analysis** for higher confidence. No single method is 100% accurate, and sophisticated manipulation can bypass detection.

**Best Practice:** Always combine multiple detection methods and contextual analysis for a more robust assessment of AI generation.
