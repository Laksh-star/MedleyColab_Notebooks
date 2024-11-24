# YouTube Advertisement Analysis System

## Overview
An automated system for analyzing bottom banner advertisements in YouTube videos. This project combines video processing, computer vision, and data analytics to extract and analyze advertisement content from YouTube videos.

## Features
- 🎥 YouTube video and playlist processing
- 🔍 Automatic bottom banner ad detection
- 📊 Ad content analysis using Claude Vision API
- 📈 Interactive analytics dashboard
- 📋 Comprehensive reporting system

## Prerequisites
```bash
pip install yt-dlp opencv-python pillow anthropic pandas matplotlib seaborn plotly
apt-get install tesseract-ocr  # For OCR capabilities
```

## Environment Setup
```python
# Set your Claude API key
import os
os.environ["ANTHROPIC_API_KEY"] = "your_api_key_here"
```

## Project Structure
```
youtube-ad-analysis/
├── ad_scan_results/        # Generated ad scan results
│   ├── frames/            # Captured ad frames
│   └── scan_results.json  # Structured scan data
├── ad_reports/            # Generated analytics reports
│   ├── visualizations/    # Interactive charts
│   └── ad_analysis_report.html  # Complete report
└── youtube_ad_scanner.ipynb    # Main notebook with all code
```

## Usage

### 1. Basic Usage
```python
from youtube_ad_scanner import YouTubeAdScanner
from ad_report_generator import AdReportGenerator

# Initialize and run scanner
scanner = YouTubeAdScanner(
    playlist_url="your_playlist_url",
    output_dir="ad_scan_results"
)
await scanner.process_playlist()

# Generate report
report_generator = AdReportGenerator(
    json_path="ad_scan_results/scan_results.json",
    output_dir="ad_reports"
)
report_generator.generate_report()
```

### 2. Sample Output
```json
{
  "scan_metadata": {
    "scan_date": "2024-11-24T15:30:45",
    "total_videos_processed": 4
  },
  "ad_detections": [
    {
      "video_id": "example_id",
      "company_name": "BIG C",
      "offers": ["CASH BACK", "0 DOWN PAYMENT"],
      "timestamp": 0.0
    }
  ]
}
```

## Key Components

### 1. YouTube Ad Scanner
- Video download and processing
- Frame extraction
- Ad region detection
- Vision API integration
- Structured data output

### 2. Analytics Report Generator
- Data processing and analysis
- Interactive visualizations
- HTML report generation
- Statistical summaries

## Features in Detail

### Ad Detection
- Automatic bottom banner recognition
- Text extraction using Claude Vision API
- Structured data output
- Error handling and retry mechanisms

### Analytics
- Company frequency analysis
- Offer distribution
- Temporal patterns
- Interactive visualizations

## Visualization Types
1. Company Distribution Pie Chart
2. Offer Types Distribution
3. Ad Timeline Analysis
4. Day/Hour Heatmap

## Development Time
Total Development: 2 hours
- Initial Setup & Issues: 40 mins
- Claude Vision Integration: 30 mins
- Analytics Development: 35 mins
- Bug Fixes & Improvements: 15 mins

## Technologies Used
- Python 3.10
- OpenCV for image processing
- Claude-3 Vision API
- yt-dlp for video handling
- Pandas & Plotly for analytics
- Asyncio for concurrent processing

## Limitations
- Currently only analyzes bottom banner ads
- Requires Claude API key
- Processing time depends on video length and quantity
- YouTube API limitations apply

## Future Enhancements
- Real-time processing capabilities
- Additional ad type detection
- Enhanced error recovery
- Performance optimizations
- Sentiment analysis integration

## Contributing
Feel free to open issues and pull requests for any improvements.

## License
MIT License - feel free to use and modify as needed.

## Acknowledgments
- Claude AI for vision capabilities
- YouTube-DLP for video processing
- OpenCV community for image processing tools

## Report Issues
For any issues or feature requests, please create an issue in the repository.

## Author
[Your Name]
[Your Contact Information]

---
**Note**: Replace placeholder API keys and URLs with actual values before using.
