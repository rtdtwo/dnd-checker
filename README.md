# DND Checker
A tool that scrapes official TRAI NCCP registry (http://www.nccptrai.gov.in/nccpregistry/search.misc) to return DND status of a given number. Useful for telecalling applications.

# How to run?
 - Clone or download the repo.
 - Install `python` and `pip` in your machine if not installed already.
 - `cd` to the repo folder and run `pip install -r requirements.txt` to install dependent Python modules.
   - Note: You can also use `virtualenv` tool to create a Python virtual environemnt and install dependencies within it. I highly recommend this procedure as it keeps your system pip clean.
 - **Run the code:**
   - As a web app: Run `app.py` to start the Flask server. You can then check DND of the number using the endpoint `http://localhost:5000/dnd_status/9876543210`
   - As standalone code: Uncomment the print statement at the end of the `nccp_lib.py` file and run the file (`python nccp_lib.py`) directly from your console.
   
# Legal aspects
As of 14 July 2019, TRAI does not post any copyright message in the NCCP registry search website (http://www.nccptrai.gov.in/nccpregistry/search.misc). However, to avoid disputes, discuss the usage of this tool with your legal team if you wish to use it commercially.
