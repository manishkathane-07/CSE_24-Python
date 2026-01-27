# Installation Guide - Personal Expense Tracker

## System Requirements
- Python 3.7 or higher
- Linux/macOS/Windows operating system

## Installation Steps

### Option 1: Using pip (Recommended)

If you have pip installed:

```bash
pip install matplotlib seaborn pandas
```

Or using pip3:

```bash
pip3 install matplotlib seaborn pandas
```

Or using Python module:

```bash
python3 -m pip install matplotlib seaborn pandas
```

### Option 2: Using System Package Manager

#### For Amazon Linux 2023 / RHEL / Fedora:
```bash
sudo dnf install -y python3-pip
python3 -m pip install --user matplotlib seaborn pandas
```

#### For Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install -y python3-pip python3-matplotlib python3-seaborn python3-pandas
```

#### For macOS (using Homebrew):
```bash
brew install python3
pip3 install matplotlib seaborn pandas
```

### Option 3: Using Virtual Environment (Best Practice)

```bash
# Create virtual environment
python3 -m venv expense_env

# Activate virtual environment
# On Linux/macOS:
source expense_env/bin/activate
# On Windows:
expense_env\Scripts\activate

# Install dependencies
pip install matplotlib seaborn pandas
```

### Option 4: Manual Installation

If pip is not available, you can install pip first:

```bash
# Download get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Install pip
python3 get-pip.py --user

# Install dependencies
python3 -m pip install --user matplotlib seaborn pandas
```

## Verification

After installation, verify the packages:

```bash
python3 -c "import matplotlib; import seaborn; import pandas; print('All packages installed successfully!')"
```

## Running the Application

### Full Version (with visualizations):
```bash
python3 expense_tracker.py
```

### Text-Only Version (no visualization dependencies):
```bash
python3 expense_tracker_simple.py
```

### Generate Demo Data:
```bash
python3 demo_data_generator.py
```

### Run Tests:
```bash
python3 test_basic.py
```

## Troubleshooting

### Issue: "No module named pip"
**Solution**: Install pip using your system package manager or download get-pip.py

### Issue: "Permission denied"
**Solution**: Use `--user` flag or virtual environment:
```bash
python3 -m pip install --user matplotlib seaborn pandas
```

### Issue: "Command not found: python3"
**Solution**: Try `python` instead of `python3`, or install Python 3

### Issue: Matplotlib backend errors
**Solution**: Set the backend to non-GUI mode by adding to your script:
```python
import matplotlib
matplotlib.use('Agg')
```

### Issue: Cannot display plots in headless environment
**Solution**: Use the text-only version or save plots to files without displaying

## Alternative: Text-Only Version

If you cannot install visualization libraries, use the simplified version:
- `expense_tracker_simple.py` - Works without matplotlib/seaborn
- Provides all core functionality
- Generates text-based reports instead of visual charts

## Support

For issues or questions:
1. Check Python version: `python3 --version`
2. Check pip version: `python3 -m pip --version`
3. Verify package installation: `python3 -m pip list`
