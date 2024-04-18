#!/bin/sh

fatal() {
	echo "error - $1"
	exit 1
}

error() {
	return 1
}

echo "first" || fatal "first failed"
echo "second" || fatal "second failed"
error || fatal "failed on error"
