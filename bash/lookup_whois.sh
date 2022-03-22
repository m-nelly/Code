#!/bin/bash

touch temp2.txt #create temp2 file to avoid file doesn't exist error

for domain in `cat $1` #sets up iteration through the list of IP addresses in a file passed as an argument
do
  whois $domain | grep -E "NetRange|Organization|NetType|Country|OrgAbuseEmail" > temp1.txt #whois lookup, filter output, and store in temp1 overwriting previous values

  head -n1 temp1.txt | grep -q -x -f temp2.txt #match on entire first line of temp1

  if [ $? -ne 0 ] #if the previous command had a match the status code will be 0
  then
    cat temp1.txt >> temp2.txt #if there was no match, read and append temp1 into temp2
  else
    : #do nothing
  fi
done

sed '/OrgAbuseEmail/G' temp2.txt > lookup_whois.txt #break up results in temp2 with a new line and write to lookup_whois.txt

rm temp1.txt #remove temp files
rm temp2.txt
