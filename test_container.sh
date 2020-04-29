IMG_NAME=it4all_mongo

docker build -t ${IMG_NAME} .

docker run -it --rm \
  -e MONGO_INITDB_ROOT_USERNAME=root \
  -e MONGO_INITDB_ROOT_PASSWORD=1234 \
  ${IMG_NAME}
