#!/bin/bash

t1=""
t2=""

for domain in `cat $1` #sets up iteration through the list of IP addresses in a file passed as an argument
do
  whois $domain | grep -E "NetRange|Organization|NetType|Country|OrgAbuseEmail" > t1 #whois lookup, filter output, and store in temp1 overwriting previous values

  head -n1 t1 | grep -q -x -f t2 #match on entire first line of temp1

  if [ $? -ne 0 ] #if the previous command had a match the status code will be 0
  then
    cat t1 >> t2 #if there was no match, read and append temp1 into temp2
  else
    : #do nothing
  fi
done

sed '/OrgAbuseEmail/G' t2 > lookup_whois.txt #break up results in temp2 with a new line and write to lookup_whois.txt
