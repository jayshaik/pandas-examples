#!/bin/bash

set -e

if [ $# -ne 3 ]; then
  echo "Usage: $0 <cluster-name> <region> <account-id>"
  exit 1
fi

cluster_name=$1
region=$2
account_id=$3

echo "=== Uninstalling AWS Load Balancer Controller ==="
helm uninstall aws-load-balancer-controller -n kube-system || echo "Helm release not found"

echo "=== Deleting IAM service account role ==="
aws iam delete-role-policy \
  --role-name AmazonEKSLoadBalancerControllerRole \
  --policy-name AWSLoadBalancerControllerIAMPolicy || true

aws iam delete-role \
  --role-name AmazonEKSLoadBalancerControllerRole || true

echo "=== Deleting IAM policy ==="
aws iam delete-policy \
  --policy-arn arn:aws:iam::$account_id:policy/AWSLoadBalancerControllerIAMPolicy || true

echo "=== Checking for old OIDC providers ==="
oidc_list=$(aws iam list-open-id-connect-providers | grep oidc.eks || true)
echo "$oidc_list"

echo "If you want to delete an old OIDC provider, run:"
echo "aws iam delete-open-id-connect-provider --open-id-connect-provider-arn <arn>"

echo "=== ALB Controller cleanup complete ==="
