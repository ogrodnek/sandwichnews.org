#!/bin/bash

R=`dirname $0`

rm -rf $R/.build
cactus build && aws s3 sync $R/.build s3://sandwichnews.org --profile analog --cache-control max-age=900
