# My gadgets

## docker-compose.secret.yml Decryption

```
$ gcloud --project=$GCP_PROJECT kms decrypt --location $LOCATION --keyring $KEYRING --key $KEY --plaintext-file docker-compose.secret.yml --ciphertext-file docker-compose.secret.yml.enc
```

## Setup Instance Template

Image: Container-Optimized OS

Startup Script:

```bash
mkdir -p /run/startup \
&& cd /run/startup \
&& git clone https://github.com/acomagu/gadgets \
&& cd gadgets \
&& docker run -i google/cloud-sdk gcloud kms decrypt --location global --keyring gadgets --key docker-compose_secret_yml --ciphertext-file - --plaintext-file - <docker-compose.secret.yml.enc >docker-compose.secret.yml \
&& docker run -v /var/run/docker.sock:/var/run/docker.sock -v $PWD:$PWD -w $PWD docker/compose:1.23.2 -fdocker-compose.{yml,secret.yml,gce.yml} up -d
```
