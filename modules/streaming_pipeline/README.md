# Streaming Pipeline

## Usage

### 3.1. Local

Run the streaming pipeline in real-time and production modes:

```bash
make run_real_time
'''

To populate the vector DB, you can ingest historical data from the latest 8 days by running the streaming pipeline in batch and production modes:

'''bash
make run_batch
'''

For debugging and testing, run the streaming pipeline in real-time and development modes:

'''bash
make run_real_time_dev
'''

For debugging and testing, run the streaming pipeline in batch and development modes:

'''bash
make run_batch_dev
'''

To query the Qdrant vector DB, run the following:

'''bash
make search PARAMS='--query_string "Should I invest in Tesla?"'
'''

we can replace the --query_string with any question.

### 3.2. Docker

First, build the Docker image:

'''bash
make build
'''

Then, run the streaming pipeline in real-time mode inside the Docker image

'''bash
make run_real_time_docker
'''

### 3.3. Deploy to AWS

First, ensure successfully configured your AWS CLI credentials.

After, run the following to deploy the streaming pipeline to a t2.small AWS EC2 machine:

'''bash
make deploy_aws
'''

can log in to the AWS console, go to the EC2 section, and see your machine running.

To check the state of the deployment, run:

'''bash

make info_aws
'''


To destroy the EC2 machine, run:

'''bash
make undeploy_aws
'''
