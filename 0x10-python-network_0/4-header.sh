#!/bin/bash
# send a GET request with a custom header, and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
