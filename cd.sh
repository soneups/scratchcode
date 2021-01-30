#!/bin/bash -x
# this file -- enos.in/cd -- https://raw.githubusercontent.com/soneups/scratchcode/master/cd.sh
A="2021-30-1"; B="2021-10-5";
echo $(((`date -jf %Y-%d-%m $B +%s` - `date -jf %Y-%d-%m $A +%s`)/86400))
