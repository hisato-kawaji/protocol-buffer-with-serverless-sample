## Setup (Mac)
docker-machine create --driver virtualbox default
eval $(docker-machine env default)

## Deploy
npx sls deploy -v -r {region} --aws-profile {dev} -s {stage}
