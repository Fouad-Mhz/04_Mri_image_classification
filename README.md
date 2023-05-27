# README

## Description
This project uses a deep learning model to classify MRI scans into different phases: 'EO', 'IO', 'IPTE', 'LO', and 'PTE'. The MRI scans should be in '.jpg' format.

## Prerequisites

- You should have Docker installed on your machine to use this model.
- You will need to download the model: https://drive.google.com/file/d/1-77OVZFZwxeh-JkJZGC9VLxZx1eamBa1/view?usp=sharing

## Steps to Run

1. **Extract the zip file**. This will place the project files into a directory on your local machine.

2. **Navigate to the project directory**. This is the location where the project files are stored.

3. Within this directory, you will find two Bash scripts. The first script, `build.sh`, builds a Docker image from the Dockerfile. The second script, `run.sh`, runs the Docker image.

4. **Open a terminal window** and navigate to the project directory.

5. **Run the following commands** to give execute permissions to your scripts:

6. **Execute the `build.sh` script** to build the Docker image:

7. Once the Docker image has been successfully built, **open the `run.sh` file**.

8. Replace `TEST_DIR` with the path to your test data directory and `TEST_NAME` with the name of the test image (in '.jpg' format) you wish to classify.

9. **Save and close the file**.

10. **Execute the `run.sh` script** to run the Docker container and make the prediction:

11. The script will print a prediction for the test image, indicating the phase the MRI scan most likely belongs to along with the associated confidence percentage.

## Important Notes

- Your Dockerfile should be located in the same directory as your Bash scripts.
- The model file should be located in the directory specified by the `MODEL_DIR` environment variable.
- download the model: https://drive.google.com/file/d/1-77OVZFZwxeh-JkJZGC9VLxZx1eamBa1/view?usp=sharing
- The test image should be located in the directory specified by `TEST_DIR`.
- The name of the test image should match `TEST_NAME` as defined in the `run.sh` script.
- Always remember to grant execute permissions to your Bash scripts before running them.
- Ensure that Docker is installed and running on your system.
- To modify the `MODEL_DIR` and `MODEL_NAME` environment variables, adjust them in the operating system where Docker is running. These variables denote the location and name of the model used for prediction.
