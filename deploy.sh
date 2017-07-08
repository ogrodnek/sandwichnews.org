#!/bin/bash

R=`dirname $0`

rm -rf $R/.build
cactus build
aws s3 sync $R/.build s3://sandwichnews.org --profile analog --cache-control max-age=900

#CF Invalidation
INVALIDATION_ID=$(date +"%s")
INVALIDATION_JSON="{
    \"DistributionId\": \"E12B42DU84I3C\",
    \"InvalidationBatch\": {
        \"Paths\": {
            \"Quantity\": 3,
            \"Items\": [
                \"/rss.xml\",
                \"/index.html\",
		\"/\"
            ]
        },
        \"CallerReference\": \"$INVALIDATION_ID\"
    }
}"

aws cloudfront create-invalidation --cli-input-json "$INVALIDATION_JSON" --profile analog
