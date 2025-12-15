REGISTRY_URL=${1:-""}
IMAGE_NAME=${2:-"api-preprod"}
TAG_BASE=${3:-"0.2"}
VERSION_FILE=${4:-"version.txt"}

if [ ! -f "$VERSION_FILE" ]; then

    echo "0" > "$VERSION_FILE"

fi

VERSION=$(cat "$VERSION_FILE")

NEW_VERSION=$((VERSION+1))

docker build -t tobsss/${IMAGE_NAME}:${TAG_BASE}.$NEW_VERSION .

docker tag tobsss/${IMAGE_NAME}:${TAG_BASE}.$NEW_VERSION tobsss/${IMAGE_NAME}:${TAG_BASE}.$NEW_VERSION

docker push tobsss/${IMAGE_NAME}:${TAG_BASE}.$NEW_VERSION

echo $NEW_VERSION > "$VERSION_FILE"

echo "Docker build, tag, and push for ${IMAGE_NAME} version ${TAG_BASE}.$NEW_VERSION complete."