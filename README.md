# Foot Traffic Tracking Project

## Overview

The **Foot Traffic Tracking Project** is designed to analyze and monitor pedestrian movement using computer vision techniques. By leveraging YOLOv8 (You Only Look Once) models for object detection and custom tracking algorithms, this project provides valuable insights into foot traffic patterns from video footage.

## Features

- **Real-time Object Detection**: Utilizes YOLOv8 to detect and track individuals in video frames.
- **Custom Tracking Algorithm**: Maintains identities of tracked objects across multiple frames.
- **Area-specific Analysis**: Monitors foot traffic within defined regions of interest.
- **Visual Annotations**: Displays detected objects and movement patterns directly on video frames.
- **Processed Video Output**: Generates annotated video showcasing foot traffic analysis.

## Technical Details

### Libraries and Tools

- **OpenCV**: For video processing and annotations.
- **YOLOv8**: Object detection using Ultralytics' YOLOv8 model.
- **cvzone**: Provides additional visual enhancements.
- **Pandas**: For handling data and results.

### How It Works

1. **Video Processing**: Reads video frames, applies object detection, and updates object tracking.
2. **Detection and Tracking**: YOLOv8 model detects objects and a custom tracker maintains their identities.
3. **Annotations**: Draws bounding boxes, labels, and statistics on the video frames.
4. **Output**: Generates a processed video showing the analyzed foot traffic.

## Setup

### Prerequisites

- Python 3.x
- Required libraries listed in `requirements.txt`

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/foot-traffic-tracking-project.git
   cd foot-traffic-tracking-project

## Example

### Notebook
For a detailed analysis and additional information, you can view the Jupyter Notebook used in this project. It provides a comprehensive overview of the code, methods, and results.

### Contributing
Contributions are welcome! If you have suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.

### Acknowledgments
YOLOv8: For object detection capabilities.
OpenCV: For video processing functionalities.
cvzone: For additional visual enhancements.
