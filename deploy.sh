#!/bin/bash -e

if [ "$CODEBUILD_BUILD_SUCCEEDING" == "0" ]; then
 echo "Deploy exiting because build did not succeed";
 exit 1;
fi

R=`dirname $0`

aws s3 sync $R/build s3://${S3_DEPLOY_BUCKET} --cache-control max-age=900
aws cloudfront create-invalidation --distribution-id ${CLOUDFRONT_DISTRIBUTION_ID} --paths '/*'
