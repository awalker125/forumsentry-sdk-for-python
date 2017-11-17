#!/bin/bash


export SWAGGER_CODEGEN_VERSION=2.2.1


export WHEREAMI=$(dirname $0)

if [ -z "${REST_API_HOST}" ]
then
	echo "REST_API_HOST is not set"
	exit 1
fi

if [ -z "${REST_API_PORT}" ]
then
	export REST_API_PORT=80
fi

if [ -z "${REST_API_PROTOCOL}" ]
then
	export REST_API_PROTOCOL=http
fi

if [ -z "${REST_API_USER}" ]
then
	echo "REST_API_USER is not set"
	exit 1
fi

if [ -z "${REST_API_PASSWORD}" ]
then
	echo "REST_API_PASSWORD is not set"
	exit 1
fi

export AUTH=$(echo -n "${REST_API_USER}:${REST_API_PASSWORD}" |base64)

if [ -f ${WHEREAMI}/swagger-codegen-cli-${SWAGGER_CODEGEN_VERSION}.jar ]
then
	echo "using cached swagger-codegen-cli-${SWAGGER_CODEGEN_VERSION}.jar"
else
	wget --no-check-certificate https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/${SWAGGER_CODEGEN_VERSION}/swagger-codegen-cli-${SWAGGER_CODEGEN_VERSION}.jar
	echo "/swagger-codegen-cli-${SWAGGER_CODEGEN_VERSION}.jar" >> ${WHEREAMI}/.gitignore 
fi

#clean and make build dir
rm -rf ${WHEREAMI}/_build

mkdir ${WHEREAMI}/_build

java -jar swagger-codegen-cli-2.2.1.jar generate \
	--output ${WHEREAMI}/_build \
	--config ${WHEREAMI}/config.json \
	-i ${REST_API_PROTOCOL}://${REST_API_HOST}:${REST_API_PORT}/restApi/v1.0/api-docs/ \
	-l python --auth "Authorization: Basic ${AUTH}"