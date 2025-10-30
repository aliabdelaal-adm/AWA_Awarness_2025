FROM gitpod/workspace-python-3.11

# Install FFmpeg for video processing
RUN sudo apt-get update && \
    sudo apt-get install -y ffmpeg && \
    sudo apt-get clean && \
    sudo rm -rf /var/lib/apt/lists/*

# Verify FFmpeg installation
RUN ffmpeg -version
