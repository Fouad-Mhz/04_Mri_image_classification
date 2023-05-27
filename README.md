{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1036{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.19041}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang12 # README\par
\par
## Description\par
This project uses a deep learning model to classify MRI scans into different phases: 'EO', 'IO', 'IPTE', 'LO', and 'PTE'. The MRI scans should be in '.jpg' format.\par
\par
## Prerequisites\par
\par
You should have Docker installed on your machine to use this model.\par
\par
## Steps to Run\par
\par
1. **Extract the zip file**. This will place the project files into a directory on your local machine.\par
\par
2. **Navigate to the project directory**. This is the location where the project files are stored.\par
\par
3. Within this directory, you will find two Bash scripts. The first script, `build.sh`, builds a Docker image from the Dockerfile. The second script, `run.sh`, runs the Docker image.\par
\par
4. **Open a terminal window** and navigate to the project directory.\par
\par
5. **Run the following commands** to give execute permissions to your scripts:\par
\par
```bash\par
chmod +x build.sh\par
chmod +x run.sh\par
```\par
\par
6. **Execute the `build.sh` script** to build the Docker image:\par
\par
```bash\par
./build.sh\par
```\par
\par
7. Once the Docker image has been successfully built, **open the `run.sh` file**.\par
\par
8. Replace `TEST_DIR` with the path to your test data directory and `TEST_NAME` with the name of the test image (in '.jpg' format) you wish to classify.\par
\par
9. **Save and close the file**.\par
\par
10. **Execute the `run.sh` script** to run the Docker container and make the prediction:\par
\par
```bash\par
./run.sh\par
```\par
\par
11. The script will print a prediction for the test image, indicating the phase the MRI scan most likely belongs to along with the associated confidence percentage.\par
\par
## Important Notes\par
\par
- Your Dockerfile should be located in the same directory as your Bash scripts.\par
- The model file should be located in the directory specified by the `MODEL_DIR` environment variable.\par
- The test image should be located in the directory specified by `TEST_DIR`.\par
- The name of the test image should match `TEST_NAME` as defined in the `run.sh` script.\par
- The Docker image name (`IMAGE_NAME_MP`) should be the same in both Bash scripts.\par
- Always remember to grant execute permissions to your Bash scripts before running them.\par
- Ensure that Docker is installed and running on your system.\par
- To modify the `MODEL_DIR` and `MODEL_NAME` environment variables, adjust them in the operating system where Docker is running. These variables denote the location and name of the model used for prediction.\par
}
 