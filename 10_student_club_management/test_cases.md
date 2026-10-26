# Test Cases — Student Club Management

Club membership uses space-separated roll numbers. Sets automatically remove duplicates.

| # | Coding club input | Sports club input | Search roll | Expected result |
|---|---|---|---|---|
| 1 | `101 102 103` | `102 104` | `102` | Union {101,102,103,104}; intersection {102}; coding-only {101,103}; member found |
| 2 | `101 102` | `103 104` | `999` | Intersection empty; coding-only {101,102}; not a member |
| 3 | `101 101 102` | `102 102` | `101` | Duplicate roll numbers are stored once; member found |
| 4 | empty input | `201 202` | `202` | Coding set empty; member found through sports club |
| 5 | empty input | empty input | `500` | Both sets empty; not a member |

Set display order can vary between Python runs. Compare membership and set contents, not the printed order.