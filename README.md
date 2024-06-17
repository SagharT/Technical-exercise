Setting Up Automatic Weekly Execution

Make the script executable:
```bash
chmod +x /path/to/Technical_Evaluation.py
```
Open crontab for editing:

```bash
crontab -e
```
Add the following line to schedule the script to run every Monday at 3 AM:
```bash
MAILTO="your@email.com"
0 3 * * 1 /usr/bin/python3 /path/to/Technical_Evaluation.py /path/to/samples.txt 
```
Here:
0 3 * * 1: Runs at 3:00 AM every Monday.
/usr/bin/python3: Path to the Python executable.
/path/to/Technical_Evaluation.py: Path to this script.
/path/to/samples.txt: Path to the sample file.

Save and exit the crontab editor.

IF there is an error, the script will have an output which will be email to the address you write.