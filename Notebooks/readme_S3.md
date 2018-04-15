## Accessing data from the S3 bucket
bucket url: https://s3.console.aws.amazon.com/s3/buckets/*****
bucket name: ******

### Steps for accessing from local computer:

1. Install AWS command line tools via bash

`pip install awscli --upgrade --user`

2. Configure AWS credentials via bash

`aws configure`

This will prompt you to provide your AWS Access Key ID and AWS Secret Access Key.

If the above command throws an error, try:

`export PATH=~/.local/bin:$PATH`

`source ~/.bash_profile`

3. Install the `boto3` and `s3fs` python libraries

`pip install boto3`

`pip install s3fs`

4. Use the following functions from `S3_read_write.py` to read and write data to S3:

* `load_df_s3()` to load **csv** files from S3
* `load_feather_s3()` to load **feather** files from S3
* `save_feather2s3()` to save a dataframe to S3 in the **feather** format
