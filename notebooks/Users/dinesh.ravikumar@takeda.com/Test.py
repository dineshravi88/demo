# Databricks notebook source
import pandas as pd
from tensorflow import keras
import boto3

s3 = boto3.client('s3')
obj = s3.get_object(Bucket='tpc-aws-ted-dev-edpp-alyt-mitd842-us-east-1', Key='Intermediate/EVOLVE_Canada_Chart_Review_SASdescription.csv')
df=pd.read_csv(obj['Body'])
df