# My gadgets

## docker-compose.secret.yml Decryption

```
$ gcloud --project=$GCP_PROJECT kms decrypt --location $LOCATION --keyring $KEYRING --key $KEY --plaintext-file docker-compose.secret.yml --ciphertext-file docker-compose.secret.yml.enc
```

## Test locally

```
$ docker-compose -fdocker-compose.{,secret.}yml up
```

## Setup Instance Template

Image: CoreOS(Container Linux)

Use `clconfig.yml` as the Container Linux Configuration.
