#!/bin/bash

set -x 

#export SWAGGER_CODEGEN_VERSION=2.2.3
#export SWAGGER_CODEGEN_VERSION=3.0.0-20170924.102354-5
export SWAGGER_CODEGEN_VERSION=2.3.0-20171129.164117-307

export WHEREAMI=$(dirname $0)

if [ -z "${FORUM_REST_API_HOST}" ]
then
	echo "FORUM_REST_API_HOST is not set"
	exit 1
fi

if [ -z "${FORUM_REST_API_PORT}" ]
then
	export FORUM_REST_API_PORT=80
fi

if [ -z "${FORUM_REST_API_PROTOCOL}" ]
then
	export FORUM_REST_API_PROTOCOL=http
fi

if [ -z "${FORUM_REST_API_USER}" ]
then
	echo "FORUM_REST_API_USER is not set"
	exit 1
fi

if [ -z "${FORUM_REST_API_PASSWORD}" ]
then
	echo "FORUM_REST_API_PASSWORD is not set"
	exit 1
fi

export AUTH=$(echo -n "${FORUM_REST_API_USER}:${FORUM_REST_API_PASSWORD}" |base64)

if [ -f ${WHEREAMI}/swagger-codegen-cli-${SWAGGER_CODEGEN_VERSION}.jar ]
then
	echo "using cached swagger-codegen-cli-${SWAGGER_CODEGEN_VERSION}.jar"
else

	wget --no-check-certificate https://oss.sonatype.org/content/repositories/snapshots/io/swagger/swagger-codegen-cli/2.3.0-SNAPSHOT/swagger-codegen-cli-${SWAGGER_CODEGEN_VERSION}.jar
	#wget --no-check-certificate https://oss.sonatype.org/content/repositories/snapshots/io/swagger/swagger-codegen-cli/3.0.0-SNAPSHOT/swagger-codegen-cli-${SWAGGER_CODEGEN_VERSION}.jar
	#wget --no-check-certificate https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/${SWAGGER_CODEGEN_VERSION}/swagger-codegen-cli-${SWAGGER_CODEGEN_VERSION}.jar
	echo "/swagger-codegen-cli-${SWAGGER_CODEGEN_VERSION}.jar" >> ${WHEREAMI}/.gitignore 
fi

#clean and make build dir
rm -rf ${WHEREAMI}/_build

mkdir ${WHEREAMI}/_build


#uncomment for all. Fails due to problems with api
java -jar \
	swagger-codegen-cli-${SWAGGER_CODEGEN_VERSION}.jar generate \
	--output ${WHEREAMI}/_build \
	--config ${WHEREAMI}/config.json \
	-i ${FORUM_REST_API_PROTOCOL}://${FORUM_REST_API_HOST}:${FORUM_REST_API_PORT}/restApi/v1.0/api-docs \
	-l python --auth "Authorization: Basic ${AUTH}" \
	--template-dir ${WHEREAMI}/templates/python	
	
	
#uncomment for only models.	
# java -jar \
	# -Dmodels -DmodelDocs=false \
	# -DsupportingFiles=configuration.py,__init__.py,rest.py,api_client.py \
	# swagger-codegen-cli-${SWAGGER_CODEGEN_VERSION}.jar generate \
	# --output ${WHEREAMI}/_build \
	# --config ${WHEREAMI}/config.json \
	# -i ${FORUM_REST_API_PROTOCOL}://${FORUM_REST_API_HOST}:${FORUM_REST_API_PORT}/restApi/v1.0/api-docs \
	# -l python --auth "Authorization: Basic ${AUTH}" \
	# --template-dir ${WHEREAMI}/templates/python	




	
# if [ "$1" == "update" ]
# then
	# set -x
	# rm -rf ${WHEREAMI}/../forumsentry_api/
	# rm -rf ${WHEREAMI}/../tests/forumsentry_api/
	# cp -R -p ${WHEREAMI}/_build/forumsentry_api ../
	# cp -R -p ${WHEREAMI}/_build/test/ ../tests/forumsentry_api
# fi