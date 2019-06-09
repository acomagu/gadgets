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

To generate Ignition:

```
cat clconfig.yml | ct --strict --platform=gce
```

## Notes

### On updating Container Linux Configuration

Discard the old VM/Instance-Template and create new one with updated user-data metadata.

### On updating Docker Image in docker-compose

Run `docker pull` on a VM and restart.
