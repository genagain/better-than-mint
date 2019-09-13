# Better Than Mint

This software helps users stick to a budget. This uses Mint on the backend, so it assumes that you have a Mint account. It also assumes that you have some kind of budget. This software is better than Mint because it allows users to categorize their transactions automatically.

## Quickstart

### Setting up dependencies

Create a virtual environment
```
$ python3.6 -m venv venv
```

Source virtual environment
```
$ source venv/bin/activate
```

Install dependencies
```
$ pip3 install -r requirements.txt
```
### Connecting to your Mint account

Create a file called `.credentials`
```
$ touch .credentials
```

Open the `.credentials` file, enter your Mint username and password in the file and save the file
```
export EMAIL="YOUR_EMAIL"
export PASSWORD="YOUR_PASSWORD"
```

The `.credentials` file is in the `.gitignore` so your credentials will never be on the internet.

Source your credentials
```
$ source .credentials
```

### Configuring your budget

Next the software needs to know how to categorize your transactions. It uses the following categories to categorize your transactions.

* Fixed Costs - Any fixed costs you incur like rent, groceries, utilities etc.
* Investments - Any investments that you have like a Roth IRA
* Savings - Any money you save
* Spending Money - Any costs that don't fit in the above categories like eating out

In the `budget.json` file, type in the categories, their corresponding substrings and the expected amounts. The substrings are substrings that occur in the description of the transaction. For example if you spent money at Whole Foods, it's corresponding substring would be `wholefds`. You can use the `budget.json` in the repository as a reference.


### Running a report

To run a report you must specify an start date as a command line argument like so
```
$ python generate_report.py --start-date 2019-04-21
```

If you don't specify and end date, the report will set the end date to yesterday. 

Optionally you can specify an end date like so
```
$ python generate_report.py --start-date 2019-04-21 --end-date 2019-04-29
```

Running the either of the commands above will generate the files `summary_report.csv` and `maintaince.csv`
