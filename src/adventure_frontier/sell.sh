#!/bin/bash

# Define a dictionary-like array with item names as keys and IDs as values
declare -A items=(
  ["leather"]="1964c0c3f09c6ea392a2dde"
  ["raw meat"]="19651674842b048100a1e5a"
  ["m stickweed"]="1964864f4d3cbe90c69927c"
  ["bloodberry"]="1964864f4d4eaabfeaf8397"
  ["deatnettle"]="1964af50474ff3945dc4243"
  # ["combat potion"]="196538bcb6aa42d12c4df71"
  # ["four leaf"]="1964d48483ced2aba81c7f8"
  # ["bandage"]="1965aec348bd1c7efef294c"
  # ["cooked meat"]="196587e1640d9a9b072a7a7"
  # ["leather bag"]="1965b0340738b16fc91a6a0"
  # ["explorer kit"]="1965af1daa1fbbd4be0bea8"

)

# Prompt the user for the amount of each item to sell
read -p "Enter the amount of each item to sell (default is 5): " amount
amount=${amount:-5}

# Extract the base URL
base_url="https://adventurefrontier.net/sell-item"

for item_name in "${!items[@]}"; do
  item_id=${items[$item_name]}
  echo "Selling $amount of $item_name (ID: $item_id)"
  
  for ((i = 1; i <= amount; i++)); do
    # Perform the curl request for each item
    curl "${base_url}?id=${item_id}" \
      -H 'Accept: */*' \
      -H 'Accept-Language: en-US,en;q=0.9,id;q=0.8' \
      -H 'Connection: keep-alive' \
      -b 'connect.sid=s%3Az8I3TUiqKgI-rJzGhgDNrhPP-4xBfUPF.q3HucgbL0Zee9clnWDCAhti%2BUABm5cwce%2BjxPuTIWpE' \
      -H 'If-None-Match: W/"7-U6VofLJtxB8qtAM+l+E63v03QNY"' \
      -H 'Referer: https://adventurefrontier.net/dashboard' \
      -H 'Sec-Fetch-Dest: empty' \
      -H 'Sec-Fetch-Mode: cors' \
      -H 'Sec-Fetch-Site: same-origin' \
      -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36' \
      -H 'X-Requested-With: XMLHttpRequest' \
      -H 'sec-ch-ua: "Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"' \
      -H 'sec-ch-ua-mobile: ?0' \
      -H 'sec-ch-ua-platform: "Windows"'
    echo "Sold $i/$amount of $item_name"
  done
done