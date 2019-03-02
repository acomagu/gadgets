# My gadgets

## docker-compose.secret.yml Decryption

```
$ gcloud --project=$GCP_PROJECT kms decrypt --location $LOCATION --keyring $KEYRING --key $KEY --plaintext-file docker-compose.secret.yml --ciphertext-file docker-compose.secret.yml.enc
```

## Setup Instance Template

Image: Container-Optimized OS

Startup Script:

```bash
git clone https://github.com/acomagu/gadgets . \
&& docker run google/cloud-sdk gcloud kms decrypt --location global --keyring gadgets --key docker-compose_secret_yml --ciphertext-file - --plaintext-file - <docker-compose.secret.yml.enc >docker-compose.secret.yml \
&& docker run -v /var/run/docker.sock:/var/run/docker.sock -v $PWD:/tmp/home docker/compose:1.23.2 -f/tmp/home/docker-compose.{yml,secret.yml} up
```
