string="abhishekghosh:x:100000:abhishekghoshSEPARATORprototyping-groups:x:1000000:abhishekghoshSEPARATORprototyping-groups/mini-src:x:1000001:abhishekghoshSEPARATORprototyping-groups/mini-src/platform-users:x:1000002:abhishekghoshSEPARATORprototyping-groups/purple:x:1000003:abhishekghoshSEPARATORprototyping-groups/purple/gms-test:x:1000004:abhishekghoshSEPARATORprototyping-groups/purple/gms-test/developer:x:1000005:abhishekghosh"

separator="SEPARATOR"

# Using cut
echo "$string" | cut -d "$separator" -f 1-
