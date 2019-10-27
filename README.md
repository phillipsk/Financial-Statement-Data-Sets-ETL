   # Financial Statement Data ETL
Analysis of SEC DERA data

## Overview

* Python 3 Scrapy spider to retrieve SEC data
* Scrapyd & scrapyd-client utilized for distributed crawling
    * resulting zip files uploaded to S3 bucket via scrapy feed export configuration
* AWS infrastructure
    * Lambda function deployed via Cloud Formation
    * Serverless s3-uncompressor SAM repo to unzip files from one S3 bucket into another
* Cloud Watch logging enabled 
* Scrapyd logging enabled

## TODO

* Incorporate Spark 
    * Calculate metrics
    * Year over year growth of SEC ledger balances
    * Quarter over quarter
    * 3 Year growth
    * 5 Year growth
    * Export calculated results
* Improve scalability
* Architecture diagram
* IAM authentication
 
    
## Resources
* Data Location: https://www.sec.gov/dera/data/financial-statement-data-sets.html
* Data Dictionary: https://www.sec.gov/files/aqfs.pdf

## Setup

#### Clone the repo

```bash
git clone https://github.com/phillipsk/Financial-Statement-Data-Sets-ETL.git
cd Financial-Statement-Data-Sets-ETL
```

#### Deploy Lambda Function

##### AWS CLI Deploy
```bash
git checkout fork-aws-lambda
```
* Follow README.md instructions (this is a copy of Piotr's forked repo)

#### OR
##### AWS Web Deploy

* From the AWS Lambda page
* Lambda > Create Function > Browse Serverless App Repository > Search: "s3-uncompressor"
* Configure Source & Destination buckets

##### Troubleshooting
* Adjust LambdaFunctionMemorySize and/or LambdaFunctionTimeout 

#### Revert back to master branch
```bash
git checkout master
```

#### Create Virtualenv:

```bash
virtualenv venv
source venv/bin/activate
```
#### Install dependencies

```bash
pip install -r requirements.txt
```

#### Set environment variables
```bash
export AWS_ACCESS_KEY_ID=[xxxxxxxxxxxxxxxxxxx]
export AWS_SECRET_ACCESS_KEY=[xxxxxxxxxxxxxxxxxxxxxxxx]
```

#### Run scrapy spider
##### Crawl all zip files in table
```bash
scrapy crawl sec_table
```
#### OR
##### Specify year as an argument
```bash
scrapy crawl args_spider -a year=2011
```

## Distributed crawling
### [Scrapyd](https://scrapyd.readthedocs.io/en/stable/overview.html)
* Launch a separate EC2 instance

##### Set environment variables
```bash
export AWS_ACCESS_KEY_ID=[xxxxxxxxxxxxxxxxxxx]
export AWS_SECRET_ACCESS_KEY=[xxxxxxxxxxxxxxxxxxxxxxxx]
```

##### Clone and install the dependencies
```bash
git clone https://github.com/phillipsk/Financial-Statement-Data-Sets-ETL.git
cd Financial-Statement-Data-Sets-ETL
pip install -r requirements.txt
```

##### Install scrapyd
```bash
pip install scrapyd
```

##### Run the scrapyd daemon
```bash
scrapyd
```

## Revert back to the original instance
##### Checkout the distributed branch
```bash
git checkout feature-aws-distributed
```

##### Configure scrapy.cfg
* Under the `[deploy]` property
    * Set the URL to the EC2 IP 
    * Note the project name
    * By default Scrapyd runs on port 6800
```
url = http://x.x.x.x:6800/
project = secScrap
```

### [scrapyd-client](https://github.com/scrapy/scrapyd-client#deploying-a-project)

##### Install scrapyd-client
```bash
pip install scrapyd-client
```
##### Deploy the project
```bash
scrapyd-deploy default -p secScrap
```
```bash
curl http://x.x.x.x:6800/schedule.json -d project=secScrap -d spider=sec_table
```

