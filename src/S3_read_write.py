import pandas as pd
from io import BytesIO
import boto3
from pyarrow.feather import write_feather, read_feather
import s3fs


def load_df_s3(bucket_name, filepath, filetype, sep=','):
    """Load a text/feather file located at on S3 and return it in a dataframe

    Parameters:
        bucket_name: name of the S3 bucket
        filepath: path of the file on S3 (relative to the S3 bucket's home dir)
        filetype: one of 'text' or 'feather'
        sep: delimiter; applicable to reading text files
    Example: 
    df = load_df_s3(bucket_name='bucketymcbucket', filepath='data/topsecret', 
                    filetype='text', sep='|')
    """
    if filetype == 'text':
        filepath = 's3://{}/{}'.format(bucket_name, filepath)
        return pd.read_csv(filepath, sep=sep)

    elif filetype == 'feather':
    	# assuming the file is a feather file, if not a csv
	    fs = s3fs.S3FileSystem()
	    with fs.open('s3://{}/{}'.format(bucket_name, filepath)) as f:
	        return read_feather(f)


def save_df_s3(df, bucket_name, filepath):
    """ Save df to filepath on the S3 bucket in the feather format

    Parameters:
        df: pandas dataframe to be saved
        bucket_name: name of the S3 bucket
        filepath: path of the saved location on S3, including the filename
                  (relative to the S3 bucket's home dir)
    Example: Save the df 'allmysecrets' as a feather file 'topsecret.feather'
    save_df_s3(df=allmysecrets, bucket_name='bucketymcbucket', 
              'data/topsecret.feather')
    """
    s3_resource = boto3.resource('s3')
    with BytesIO() as f:
        write_feather(df, f)
        s3_resource.Object(bucket_name, filepath).put(Body=f.getvalue())